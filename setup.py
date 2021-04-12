#!/usr/bin/env python3
import os
from setuptools import setup

def read(fname):
	"""
	Utility function to read the README file.
	Used for the long_description.  It's nice, because now 1) we have a top level
	README file and 2) it's easier to type in the README file than to put a raw
	string in below ...
	"""
	return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
	name = "HyperTextStim",
	version = "0.1",
	install_requires = "pyppeteer",
	python_requires = ">=3",
	author = "Wilbert van Ham",
	author_email = "w.vanham@socsci.ru.nl",
	description = "The HyperTextStim stimulus allows you to use ʜᴛᴍʟ markup in a Psychopy-like stimulus "\
		"that otherwise works much the same as the TextStim stimulus. HyperTextStim uses pyppeteer to "\
		"generate the stimulus.",
	license = "GPLv3+",
	keywords = "psychopy",
	url = "https://www.socsci.ru.nl/wilberth/python/hypertextstim.html",
	packages = ['hypertextstim'],
	long_description = read('README.md'),
	classifiers=[
		"Development Status :: 4 - Beta",
		"License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
	],
)
