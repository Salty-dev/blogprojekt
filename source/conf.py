# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Saltyblog - matematika és informatika kedvelőknek'
copyright = '2026, Salty'
author = 'Salty'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx_math_dollar',
    'sphinx.ext.mathjax',
    'ablog',
]

blog_baseurl = 'https://salty-dev.github.io/blogprojekt/'
blog_path = 'archivum'

post_auto_excerpt = 0
blog_title = project
html_title = project

post_date_format = '%Y. %B %-d.'

templates_path = ['_templates']
exclude_patterns = []

language = 'hu'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_book_theme'
html_static_path = ['_static']

# -- Math ---------------------------------------------------------------------
mathjax3_config = {
    "tex": {
        "inlineMath": [["\\(", "\\)"]],
        "displayMath": [["\\[", "\\]"]],
        "macros": {
            "R": r"\mathbb{R}",
            "N": r"\mathbb{N}",
        },
    },
}
