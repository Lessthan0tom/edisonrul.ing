# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'edisonrul.ing'
author = 'vivaria'
copyright = 'vivaria'
version = '0.0.2'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'myst_parser',
    'sphinx_last_updated_by_git',
]
myst_enable_extensions = [
    "amsmath",
    "attrs_inline",
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
    # "linkify",
    "replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    "tasklist",
]
templates_path = ['_templates']
exclude_patterns = []
suppress_warnings = ['epub.unknown_project_files']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "pydata_sphinx_theme"
html_theme_options = {
    # Show search results while typing, like the original theme
    "search_as_you_type": True,
    # The top bar is brown in both modes, so the same white logo works for both
    "logo": {
        "text": "Edison Rulings",
        "image_light": "_static/img/cards-playing.svg",
        "image_dark": "_static/img/cards-playing.svg",
    },
    # Put all the letter pages in one "Cards" menu in the top bar
    "header_links_before_dropdown": 0,
    "header_dropdown_text": "Cards",
    # Only list the current letter's cards in the sidebar. Listing more on
    # every page makes pages much larger and the build very slow.
    "collapse_navigation": True,
    "github_url": "https://github.com/vivaria/edisonrul.ing",
    "use_edit_page_button": True,
}
# Rank cards whose name matches the search first. Sphinx opens this path
# from the folder the build is run in, so give it the full path.
html_search_scorer = os.path.join(os.path.dirname(__file__), 'search_scorer.js')
html_title = 'Edison Rulings'
html_favicon = '_static/img/favicon.ico'
html_static_path = ['_static']
html_css_files = [
    # The fonts the site used with sphinx-immaterial
    'https://fonts.googleapis.com/css2?family=Funnel+Sans:ital,wght@0,300;0,400;0,700;1,400'
    '&family=Roboto+Mono:ital,wght@0,400;0,700;1,400&display=swap',
    'css/custom.css',
]
html_context = {
    # Used by PyData for "Edit on GitHub" links
    'github_user': 'vivaria',
    'github_repo': 'edisonrul.ing',
    'github_version': 'main',
    'doc_path': 'docs/source',
    'downloads': [
        ('pdf', 'https://edisonrul.ing/_/downloads/en/latest/pdf/'),
        ('epub', 'https://edisonrul.ing/_/downloads/en/latest/epub/'),
    ],
}
html_last_updated_fmt = '%Y-%m-%d'
html_show_copyright = False
html_copy_source = False
html_show_sourcelink = True