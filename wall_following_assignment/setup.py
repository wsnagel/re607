#!/usr/bin/env python

##from distutils.core import setup
from setuptools import setup

setup(
	packages=['wall_following_assignment'],
	package_dir={'': 'python'},
	scripts=['python/wall_follower.py'], 
	install_requires=['setuptools'],
	zip_safe=True,
	)

