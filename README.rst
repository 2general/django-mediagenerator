Improve your user experience with fast page loads by combining,
compressing, and versioning your JavaScript & CSS files and images.
django-mediagenerator_ eliminates unnecessary HTTP requests
and maximizes cache usage.

Supports App Engine, Sass_, HTML5 offline manifests,  Jinja2_,
Python/pyjs_, CoffeeScript_, and much more. Visit the
`project site`_ for more information.

Most important changes after version 1.11
=============================================================

* Added Dust.js_ support (requires `a version with dustc`_)
* Added Hogan.js_ support
* Added UglifyJS_ as a JavaScript compressor option
* Added yUglify_ (a Yahoo wrapper around UglifyJS and cssmin) as
  a JavaScript and CSS compressor option
* Improved the performance of development mode with caching
* Always delimit JavaScript files with semicolons in bundles before running
  compression. This fixes e.g. bundling underscore.js 1.4 after
  jquery.history.js 1.7.
* ``{% get_media_urls %}`` assignment tag for getting bundle URLs as a list
  in a template variable. Requires Django 1.4 or newer. Usage:

    ..  code-block:: html+django
        
        {% get_media_urls "my_bundle.js" as bundle_urls %}
        {% for url in bundle_urls %}...{% endfor %}
    

Most important changes in version 1.11
=============================================================

* Added LESS_ support
* Fixed an incompatibility with App Engine 1.6.0 on Python 2.7

See `CHANGELOG.rst`_ for the complete changelog.

.. _django-mediagenerator: http://www.allbuttonspressed.com/projects/django-mediagenerator
.. _project site: django-mediagenerator_
.. _Sass: http://sass-lang.com/
.. _pyjs: http://pyjs.org/
.. _CoffeeScript: http://coffeescript.org/
.. _Jinja2: http://jinja.pocoo.org/
.. _Dust.js: http://akdubya.github.com/dustjs/
.. _Hogan.js: http://twitter.github.com/hogan.js/
.. _`a version with dustc`: https://github.com/linkedin/dustjs
.. _LESS: http://lesscss.org/
.. _CHANGELOG.rst: https://bitbucket.org/wkornewald/django-mediagenerator/src/tip/CHANGELOG.rst
.. _UglifyJS: https://github.com/mishoo/UglifyJS/
.. _yUglify: https://github.com/yui/yuglify
