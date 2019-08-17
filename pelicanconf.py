#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Jorge Garcia'
SITENAME = 'jorgegarcia.io'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'en'

THEME = "minimalxy"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('twitter', 'http://twitter.com/yorickgarcia'),
          ('linkedin', 'http://linkedin.com/yorickgarcia'),
          ('instagram', 'http://instagram.com/yorickgarcia'),
          ('github', 'http://github.com/yorickgarcia'),)

DEFAULT_PAGINATION = 42

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# HTML metadata
SITEDESCRIPTION = 'This is where Jorge lives.'

# all defaults to True.
DISPLAY_HEADER = True
DISPLAY_FOOTER = True
DISPLAY_HOME   = False
DISPLAY_MENU   = True
DISPLAY_PAGES_ON_MENU = False
STATIC_PATHS = ['images', 'pdfs',]

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
# MENU_INTERNAL_PAGES = (
#     ('Tags', TAGS_URL, TAGS_SAVE_AS),
#     ('Authors', AUTHORS_URL, AUTHORS_SAVE_AS),
#     ('Categories', CATEGORIES_URL, CATEGORIES_SAVE_AS),
#     ('Archives', ARCHIVES_URL, ARCHIVES_SAVE_AS),
# )
# additional menu items
MENUITEMS = (
    ('projects', '/pages/projects.html'),
    ('gallery', '/pages/gallery.html'),
    ('library', '/pages/library.html'),
    ('me', '/pages/me.html'),
)
