import docs_italia_theme

# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'test-docs-italia'
release = '1.0.0'
copyright = 'to be set'
author = u'INGV'

copyright = "2020 Istituto Nazionale di Geofisica e Vulcanologia"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.ifconfig',
    'docs_italia_theme',
    #'sphinx_sitemap'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['../docs-italia-ingv-theme-template/']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
    ('index', 'test-docs-italia.tex', project, author, 'manual'),
]


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'docs_italia_theme'
html_theme_path = [docs_italia_theme.get_html_theme_path()]
html_title = "test-docs-italia"
html_show_sourcelink = False
html_favicon = "../docs-italia-ingv-theme-template/static/images/favicon.ico"
html_logo = "../docs-italia-ingv-theme-template/static/images/logo_75_transp.png"
latex_logo = '../docs-italia-ingv-theme-template/static/images/logo_75_transp.png'
html_baseurl = 'docs'
smartquotes = False
language = "it"
html_context = {"languages": ["it", "en"]}

numfig = True
# The master toctree document.
master_doc = 'index'
source_suffix = '.rst'

sitemap_filename = "sitemap.xml"
sitemap_locales = ['it', 'en']


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['../docs-italia-ingv-theme-template/static']
