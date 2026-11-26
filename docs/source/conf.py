# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
project = 'miblab-dl'
copyright = '2026, miblab.org'
author = 'miblab.org'
release = '0.0.17'

# -- Path setup --------------------------------------------------------------
# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here
import os
import re
import sys
sys.path.insert(0, os.path.abspath('../../src'))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Execute new or changed examples locally. On CI the committed
# notebooks are used as they are (GitHub sets CI=true).
if not os.environ.get("CI") and not os.environ.get("SKIP_EXAMPLES"):
    import build_examples
    build_examples.build()


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom ones
extensions = [
    'sphinx.ext.napoleon',      # parsing of NumPy and Google style docstrings
    'sphinx.ext.autodoc',       # sphinx autodocumentation generation
    'sphinx.ext.autosummary',   # generates function/method/attribute summary lists
    'sphinx.ext.viewcode',      # viewing source code
    'sphinx.ext.intersphinx',   # generate links to the documentation of objects in external projects
    'sphinx_copybutton',        # copy button for code blocks
    'sphinx_design',            # sphinx web design components
    'sphinx_remove_toctrees',   # selectively remove toctree objects from pages
    'myst_nb',                  # renders both .md and .ipynb files
]

autosummary_generate = True

# Settings for sphinx-gallery, see
# https://sphinx-gallery.github.io/stable/getting_started.html#create-simple-gallery
sphinx_gallery_conf = {
    # path to the example scripts relative to conf.py
    'examples_dirs': '../examples',   

    # path to where to save gallery generated output
    'gallery_dirs': 'generated/examples',  
    
    # directory where function/class granular galleries are stored
    'backreferences_dir': 'generated/backreferences',

    # Modules for which function/class level galleries are created. 
    'doc_module': ('miblab_dl', ),

    # objects to exclude from implicit backreferences. The default option
    # is an empty set, i.e. exclude nothing.
    'exclude_implicit_doc': {},

    # thumbnail for examples that do not generate any plot
    'default_thumb_file': '_static/miblab-gemini.png',

    # Disabling download button of all scripts
    'download_all_examples': False,

    # Settings for use of binder
    "binder": {
        "org": "miblab",
        "repo": "docs-miblab-dl",
        "binderhub_url": "https://mybinder.org",
        "branch": "main",
        "dependencies": "./binder/requirements.txt",
        "use_jupyter_lab": True,
    },

}

# This way a link to other methods, classes, or modules can be made with back ticks so that you don't have to use qualifiers like :class:, :func:, :meth: and the likes
default_role = 'obj'

# Add any paths that contain templates here, relative to this directory
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path
exclude_patterns = []

# -- Extension configuration -------------------------------------------------
# Map intersphinx to pre-existing documentation from other projects used in this project
intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'numpy': ('https://numpy.org/doc/stable/', None),
    # 'matplotlib': ('https://matplotlib.org/stable/', None),
    'pydicom': ('https://pydicom.github.io/pydicom/stable/', None),
#    'nibabel': ('https://nipy.org/nibabel/', None),
    'pandas': ('https://pandas.pydata.org/docs/', None),
}

# generate autosummary even if no references
autosummary_generate = True 

# Tell sphinx-autodoc-typehints to generate stub parameter annotations including types, even if the parameters aren't explicitly documented.
always_document_param_types = True

# Remove auto-generated API docs from sidebars.
remove_from_toctrees = ["_autosummary/*"]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# The theme to use for HTML and HTML Help pages.  See the documentation for a list of builtin themes
html_theme = 'pydata_sphinx_theme'

html_theme_options = {
    "github_url": "https://github.com/openmiblab/docs-miblab-dl",
    "collapse_navigation": True,
    # "analytics": {
    #     "google_analytics_id": "G-DV3VWS9FBN",
    # },
    }

# Add any paths that contain custom static files (such as style sheets) here, relative to this directory. They are copied after the builtin static files, so a file named "default.css" will overwrite the builtin "default.css"
html_static_path = ['_static']

# Add any CSS files placed in _static here so they can be found when building the documentation
html_css_files = [
    'teams.css', # templates for the teams mosaic in About
]

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = '_static/miblab-gemini.jpg'

# Do not execute notebooks
nb_execution_mode = "off"  # nbsphinx: nbsphinx_execute = "never"


# Remove emoji's for the pdf build
_emoji = re.compile(
    "["
    "\U0001F000-\U0001FAFF"   # emoji, symbols, pictographs, flags
    "\u2190-\u21FF"           # arrows (↔, ↩, ...)
    "\u2300-\u23FF"           # misc technical (⏳, ⌚, ⏰, ...)
    "\u25A0-\u25FF"           # geometric shapes (▶, ◀, ...)
    "\u2600-\u27BF"           # misc symbols and dingbats (✅, ⚠, ✔, ...)
    "\u2900-\u297F"           # supplemental arrows
    "\u2B00-\u2BFF"           # misc symbols and arrows (⭐, ⬆, ...)
    "\u200D\u20E3\uFE0E\uFE0F"  # joiner, keycap, variation selectors
    "]"
)

def strip_emoji(app, docname, source):
    if app.builder.name == "latex":
        source[0] = _emoji.sub("", source[0])

from docutils import nodes

def strip_emoji_doctree(app, doctree, docname):
    if app.builder.name != "latex":
        return
    for node in list(doctree.findall(nodes.Text)):
        text = node.astext()
        cleaned = _emoji.sub("", text)
        if cleaned != text:
            node.parent.replace(node, nodes.Text(cleaned))

