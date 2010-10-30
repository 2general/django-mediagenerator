from setuptools import setup, find_packages

DESCRIPTION = 'Total asset management for Django. Combine and compress your JavaScript and CSS.'
LONG_DESCRIPTION = None
try:
    LONG_DESCRIPTION = open('README.rst').read()
except:
    pass

setup(name='django-mediagenerator',
      version='1.5',
      packages=find_packages(exclude=('tests', 'tests.*',
                                      'base_project', 'base_project.*')),
      package_data={'mediagenerator.filters': ['pyjslibs/*.py']},
      author='Waldemar Kornewald',
      author_email='wkornewald@gmail.com',
      url='http://www.allbuttonspressed.com/projects/django-mediagenerator',
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      platforms=['any'],
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Environment :: Web Environment',
          'Framework :: Django',
          'Intended Audience :: Developers',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Topic :: Software Development :: Libraries :: Application Frameworks',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'License :: OSI Approved :: BSD License',
      ],
)
