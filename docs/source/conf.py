# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'geomaps'
author = "ECMWF"
import datetime
import os
import sys

year = datetime.datetime.now().year
if year == 2020:
    years = "2020"
else:
    years = "2020-%s" % (year,)

copyright = "%s, ECMWF" % (years,)


release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.napoleon",
    "sphinx.ext.todo",
    "nbsphinx",
    "IPython.sphinxext.ipython_directive",
    "IPython.sphinxext.ipython_console_highlighting",
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'
