#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import date

AUTHOR = 'Jorge Garcia'
SITENAME = 'jorgegarcia.io'
SITEURL = ''
AUTHOR_INTRO = 'I make, break, and fix things to learn– teaching and consulting on technology along the way.'
CURRENTYEAR = date.today().year

PATH = 'content'

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'en'

THEME = "pelican/delphic"


PLUGIN_PATHS = "pelican/"
PLUGINS = "gallery"
GALLERY_PATH ="./content/images/gallery/"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Social widget
SOCIAL = (('twitter', 'http://twitter.com/yorickgarcia'),
          ('github', 'http://github.com/yorickgarcia'),
          ('instagram', 'http://instagram.com/yorickgarcia'),)

DEFAULT_PAGINATION = 42

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# HTML metadata
SITEDESCRIPTION = 'This is where Jorge lives.'

# all defaults to True.
DISPLAY_HEADER = True
DISPLAY_FOOTER = False
DISPLAY_HOME = False
DISPLAY_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False
STATIC_PATHS = ['images', 'pdfs', 'jpg']

# provided as examples, they make ‘clean’ urls. used by MENU_INTERNAL_PAGES.
TAGS_URL           = 'tags'
TAGS_SAVE_AS       = 'tags/index.html'
AUTHORS_URL        = 'authors'
AUTHORS_SAVE_AS    = 'authors/index.html'
CATEGORIES_URL     = 'categories'
CATEGORIES_SAVE_AS = 'categories/index.html'
ARCHIVES_URL       = 'archives'
ARCHIVES_SAVE_AS   = 'archives/index.html'

# use those if you want pelican standard pages to appear in your menu
#MENU_INTERNAL_PAGES = (
#     ('Tags', TAGS_URL, TAGS_SAVE_AS),
#     ('Authors', AUTHORS_URL, AUTHORS_SAVE_AS),
#    ('Categories', CATEGORIES_URL, CATEGORIES_SAVE_AS),
#     ('Archives', ARCHIVES_URL, ARCHIVES_SAVE_AS),
#)
# additional menu items

# ('Blog','/category/blog/'),
#     ('Library','/pages/library'),
    
LINKS = (
    ('Home', '/'),
    ('Projects', '/pages/projects'),
    ('Gallery', '/pages/gallery'),
    ('About', '/pages/about'),
)

SITES = (
    ('MakersinChicago.org','https://makersinchicago.org'),
    ('⋛⋋[±0dB]⋌⋚','https://thegrosbeak.com'),
    ('CyberNavigator.info','https://cybernavigator.info'),
)
