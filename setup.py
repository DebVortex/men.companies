from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='men.companies',
      version=version,
      description="",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='',
      author='Benjamin Tessmar',
      author_email='benjamin.tessmar@it2009.ba-leipzig.de',
      url='https://github.com/DebVortex/men.companies',
      license='Free BSD',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['nimc'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'plone.app.dexterity',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
