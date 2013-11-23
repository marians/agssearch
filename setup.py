# encoding: utf-8

from setuptools import setup

setup(name='agssearch',
      version='0.4',
      description='Python client for the German Destatis Gemeindeverzeichnis',
      long_description=open('README.md').read(),
      author='Marian Steinbach',
      author_email='marian@sendung.de',
      url='https://github.com/marians/agssearch',
      packages=['agssearch'],
      install_requires=[
          'lxml',
          'mechanize'
      ],
      entry_points={
        'console_scripts': [
            'agssearch = agssearch.agssearch:main'
        ]
      })
