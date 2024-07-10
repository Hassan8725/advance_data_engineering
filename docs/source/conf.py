import sys
from pathlib import Path

src_path = Path(__file__).resolve().parent.parent.parent / "project"
sys.path.insert(0, str(src_path))

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Data Engineering Toolkit'
copyright = '2024, Hassan Ahmed'
author = 'Hassan Ahmed'
release = '1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["sphinx.ext.autodoc", "sphinx.ext.napoleon", "nbsphinx"]

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "classic"
html_static_path = ["_static"]
html_css_files = ["custom.css"]
html_theme_options = {
    "collapsiblesidebar": "false",
    "stickysidebar": "true",
    "globaltoc_collapse": "true",
    "body_min_width": "70%",
    "sidebarwidth": 450,
    "relbarbgcolor": "#009899",
    "bodyfont": "Courier New",
}
html_short_title = "Data Engineering Toolkit"
