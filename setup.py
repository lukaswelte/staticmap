from distutils.core import setup
setup(
  name = 'staticmap',
  packages = ['staticmap'],
  version = '0.1',
  description = 'A small, python-based library for creating map images with lines and markers.',
  author = 'Christoph Lingg',
  author_email = 'christoph@komoot.de',
  url = 'https://github.com/komoot/staticmap',
  download_url = 'https://github.com/komoot/staticmap/tarball/0.1',
  keywords = 'static map image osm',
  classifiers = [
      'Programming Language :: Python :: 3',
  ],
  install_requires=[
      'Pillow',
      'requests'
  ]
)