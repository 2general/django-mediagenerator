from django.conf import settings
from django.utils.encoding import smart_str

from mediagenerator.generators.bundles.base import Filter
from mediagenerator.utils import get_media_dirs, find_file

import os
import sys
from hashlib import sha1
from subprocess import Popen, PIPE


class DustFilter(Filter):
    """
    Requires Dust.js compiler (dustc) which is available in LinkedIn's Dust.js fork:

        https://github.com/linkedin/dustjs/

        npm install dustjs-linkedin

    Filter looks for the Dust.js templates in both the app template directories
    and in your static file directories defined by GLOBAL_MEDIA_DIRS and
    IGNORE_APP_MEDIA_DIRS settings.

    USAGE:

    settings.py:
    (
        'my_bundle.js',
        {
            'filter': 'mediagenerator.filters.dust.DustFilter',
            'name': 'my_dust_template.html',
            'template_name': 'my_template_key',
        },
        'scripts/my_app.js',
    )

    Django template:
    {% include_media "my_bundle.js" %}
    <script type="text/javascript">
    dust.render("my_template_key", context, function(err, out) {
        // process result
    });
    </script>
    """
    def __init__(self, **kwargs):
        self.config(kwargs, name=kwargs["name"], path=(), template_name=kwargs.get("template_name"))
        if isinstance(self.path, basestring):
            self.path = (self.path,)

        # we need to be able to mutate self.path
        self.path = list(self.path)

        super(DustFilter, self).__init__(**kwargs)

        # dustc can't cope with nonexistent directories, so filter them
        media_dirs = [directory for directory in get_media_dirs()
                      if os.path.exists(directory)]
        self.path += tuple(media_dirs)

        # search from template directories first
        from django.template.loaders.app_directories import app_template_dirs
        self.path = list(app_template_dirs) + self.path

        self._compiled = None
        self._compiled_hash = None
        self._dependencies = {}

    def get_output(self, variation):
        self._regenerate(debug=False)
        yield self._compiled

    def get_dev_output(self, name, variation):
        self._regenerate(debug=True)
        return self._compiled

    def get_dev_output_names(self, variation):
        self._regenerate(debug=True)
        yield self.name + '.js', self._compiled_hash

    def _regenerate(self, debug=False):
        file_path = self._find_file(self.name)
        self._compiled = self._compile(file_path, debug=debug)
        self._compiled_hash = sha1(smart_str(self._compiled)).hexdigest()

    def _compile(self, path, debug=False):
        # check if already compiled
        if hasattr(self, "mtime") and self.mtime == os.path.getmtime(path):
            return self._compiled

        # compile with dustc
        try:
            shell = sys.platform == 'win32'

            relative_path = self._get_relative_path(path)

            cmd = Popen(['dustc', relative_path,
                        "--name=%s" % (self.template_name or relative_path)],
                        stdin=PIPE, stdout=PIPE, stderr=PIPE,
                        shell=shell, universal_newlines=True,
                        cwd=settings.PROJECT_ROOT)
            output, error = cmd.communicate()

            self.mtime = os.path.getmtime(path)

            # some dustc errors output to stdout, so we put both in the assertion message
            assert cmd.wait() == 0, ('dustc returned errors:\n%s\n%s' % (error, output))
            return output.decode('utf-8')
        except Exception, e:
            raise ValueError("Failed to run Dust.js compiler for this "
                "file. Please confirm that the \"dustc\" application is "
                "on your path and that you can run it from your own command "
                "line.\n"
                "Error was: %s" % e)

    def _find_file(self, name):
        return find_file(name, media_dirs=self.path)

    def _get_relative_path(self, abs_path):
        """Given an absolute path, return a path relative to the
        project root.

        >>> self._get_relative_path('/home/bob/bobs_project/subdir/foo')
        'subdir/foo'

        """
        relative_path = os.path.relpath(abs_path, settings.PROJECT_ROOT)
        return relative_path
