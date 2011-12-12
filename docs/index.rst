.. Django Mediagenerator documentation master file, created by
   sphinx-quickstart on Mon Dec 12 11:47:17 2011.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

django-mediagenerator: asset management for Django
==================================================

Improve your user experience with amazingly fast page loads by combining, compressing, and versioning your JavaScript & CSS files and images. django-mediagenerator eliminates unnecessary HTTP requests and maximizes cache usage. Also, it provides lots of advanced features required for building HTML5 web applications (e.g. HTML5 offline manifests, Sass support, etc.).

Take a look at the `feature comparison`_ for a quick overview and if you like django-mediagenerator please click the ``I use this!`` button on that page. Thank you!

Django mediagenerator lives on GitHub (`downloads`_, `source code`_ and `bug tracking`_).

.. _downloads: https://github.com/potatolondon/django-mediagenerator/downloads
.. _source code: https://github.com/potatolondon/django-mediagenerator
.. _bug tracking: https://github.com/potatolondon/django-mediagenerator/issues

.. toctree::
   :maxdepth: 2

   reference


Tutorials
-----------------------------
* Getting started: `django-mediagenerator: total asset management`_
* `Using Sass with django-mediagenerator`_
* `Offline HTML5 canvas app in Python with django-mediagenerator, Part 1: pyjs`_
* `Offline HTML5 canvas app in Python with django-mediagenerator, Part 2: Drawing`_
* `HTML5 offline manifests with django-mediagenerator`_

FAQ
----------------------------------------

Q: How does it relate to django-staticfiles / django.contrib.staticfiles?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
django-mediagenerator is a complete standalone asset manager which replaces django-staticfiles. You can still use both in the same project if you really need to, but that's very rarely the case (e.g. during a gradual transition from django-staticfiles to django-mediagenerator).

Q: What are the perfect caching headers?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* Disable ETags because they cause unnecessary ``If-modified-since`` requests.
* Use ``Cache-Control: public, max-age=31536000``

Tip: How to include IE-specific stylesheets
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Imagine you have several stylesheets combined into ``main.css`` bundle. Now imagine you also have an extra stylesheet for Internet Explorer called ``ie.css``. Most websites include their IE-specific stylesheet with an additional ``<link />`` tag using conditional HTML. The problem with this solution is that IE users have to wait for two requests: one for ``main.css`` and another one for ``ie.css``. Can this be done more efficiently?

Yes! Create two CSS bundles (``main-ie.css`` with ``ie.css`` and ``main.css`` without ``ie.css``) in your settings. For example:

.. sourcecode:: python

    _base_main_bundle = (
        'css/reset.css',
        'css/design.css',
    )

    MEDIA_BUNDLES = (
        ('main.css',)
            + _base_main_bundle,
        ('main-ie.css',)
            + _base_main_bundle
            + ('ie.css',),
    )

Then, use this conditional comment sequence to include the bundles:

.. sourcecode:: django

    <!--[if (!IE)|(gte IE 8)]><!--> {% include_media 'main.css' %} <!--<![endif]-->
    <!--[if lt IE 8]> {% include_media 'main-ie.css' %} <![endif]-->

Now every browser will only make one single request. Cool, isn't it?

In the example above only IE6 and IE7 get special treatment. IE8 loads the same stylesheet as all other browsers. Of course you can extend the example to serve different stylesheets for all the different IE versions.


.. _django-mediagenerator\: total asset management: http://www.allbuttonspressed.com/blog/django/2010/08/django-mediagenerator-total-asset-management
.. _Using Sass with django-mediagenerator: http://www.allbuttonspressed.com/blog/django/2010/08/Using-Sass-with-django-mediagenerator
.. _feature comparison: http://djangopackages.com/grids/g/asset-managers/
.. _Offline HTML5 canvas app in Python with django-mediagenerator, Part 1\: pyjs: http://www.allbuttonspressed.com/blog/django/2010/11/Offline-HTML5-canvas-app-in-Python-with-django-mediagenerator-Part-1-pyjs
.. _Offline HTML5 canvas app in Python with django-mediagenerator, Part 2\: Drawing: http://www.allbuttonspressed.com/blog/django/2010/11/Offline-HTML5-canvas-app-in-Python-with-django-mediagenerator-Part-2-Drawing
.. _HTML5 offline manifests with django-mediagenerator: http://www.allbuttonspressed.com/blog/django/2010/11/HTML5-offline-manifests-with-django-mediagenerator
