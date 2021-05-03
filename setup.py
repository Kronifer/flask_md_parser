from setuptools import setup

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_des = f.read()
setup(
  name = 'flask_md_parser',
  packages = ['flask_md_parser'],
  version = '0.1.0',
  description = 'Static content generation for Flask.',
  long_description=long_des,
  long_description_content_type='text/markdown',
  license='MIT',        
  author = 'Dillon Runke',                   
  author_email = 'dillonr5@live.wsd1.org',      
  url = 'https://github.com/Kronifer/flask_md_parser', 
  download_url = 'https://github.com/Kronifer/flask_md_parser/archive/v0.1.0.tar.gz',
  keywords = ['Markdown', 'Flask', 'Static Content Generation'],
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Web Development',
    'License :: OSI Approved :: MIT License', 
    'Programming Language :: Python :: 3.8.5',
  ],
)
