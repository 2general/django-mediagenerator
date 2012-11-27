from django.conf import settings
from django.utils.encoding import smart_str
from mediagenerator.generators.bundles.base import Filter


class YUglify(Filter):
    """
    yUglify is a Yahoo wrapper around UglifyJS and cssmin.

    https://github.com/yui/yuglify

    Install with npm:
    $ npm -g install yuglify
    """

    def __init__(self, **kwargs):
        super(YUglify, self).__init__(**kwargs)
        assert self.filetype in ('js', 'css'), (
            'yUglify only supports JS and CSS. '
            'The parent filter expects "%s".' % self.filetype)

    def get_output(self, variation):
        from subprocess import Popen, PIPE
        for input in self.get_input(variation):
            args = ['yuglify', '--type', self.filetype, '--terminal']
            try:
                args = args + settings.YUGLIFY_OPTIONS
            except AttributeError:
                pass
            try:
                cmd = Popen(args,
                            stdin=PIPE, stdout=PIPE, stderr=PIPE,
                            universal_newlines=True)
                output, error = cmd.communicate(smart_str(input))
                assert cmd.wait() == 0, 'Command returned bad result:\n%s' % error
                yield output.decode('utf-8')
            except Exception, e:
                raise ValueError("Failed to run yUglify. "
                    "Please make sure you have Node.js and yUglify installed "
                    "and that it's in your PATH .\n"
                    "Error was: %s" % e)
