import os
import sys
sys.path.insert(0, os.path.abspath('../osifinanceAPI'))

# -- Project information -----------------------------------------------------

project = 'osifinanceAPI'
copyright = '2023, OSI Finance Inc.'
author = 'OSI Finance Inc.'

# The short X.Y version
version = '0.1'
# The full version, including alpha/beta/rc tags
release = '0.1.0'

# -- General configuration ---------------------------------------------------

extensions = ['sphinx.ext.autodoc']


templates_path = ['_templates']

exclude_patterns = []

# -- Options for HTML output -------------------------------------------------

html_theme = 'alabaster'  # You can change the theme for something else.

html_static_path = ['_static']
