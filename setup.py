from setuptools import setup, find_packages

setup(
  name='dfir-unfurl',
  packages=find_packages(),
  include_package_data=True,
  scripts=['unfurl_app.py', 'unfurl_cli.py'],
  version='20221000',
  description='Unfurl takes a URL and expands ("unfurls") it into a directed graph',
  url='https://github.com/obsidianforensics/unfurl',
  author='Ryan Benson',
  author_email='ryan@dfir.blog',
  license='Apache',
  keywords=['unfurl', 'forensics', 'dfir', 'reverse-engineering', 'security'],
  classifiers=[],
  install_requires=[
    'flask>=2.2.0',
    'flask_cors',
    'flask-restx>=1.0.1',
    'maclookup',
    'networkx',
    'protobuf==3.*',
    'publicsuffix2',
    'pycountry',
    'pymispwarninglists>=1.3',
    'Requests',
    'torf',
    'ulid-py',
    'Werkzeug>=2.2.0'
  ]
)
