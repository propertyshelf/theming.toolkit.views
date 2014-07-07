# -*- coding: utf-8 -*-

from collective.cover.tiles.collection import CollectionTile
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class CollectionTile(CollectionTile):
    """Class for custom template"""
    index = ViewPageTemplateFile('templates/tiles_collection.pt')
