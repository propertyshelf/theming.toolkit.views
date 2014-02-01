# -*- coding: utf-8 -*-
"""Various useful browser views"""

# zope imports
from Products.Five import BrowserView
from plone.memoize.view import memoize
from zope.component import queryMultiAdapter
from zope.interface import implementer

# local imports
from plone.mls.listing.api import listing_details
from theming.toolkit.views.browser.interfaces import IToolkitViews



@implementer(IToolkitViews)
class ListingDetails(BrowserView):

    _error = {}
    _data = None
    listing_id = None

    def __init__(self, context, request):
        super(ListingDetails, self).__init__(context, request)
        self.update()

    def update(self):
        self.portal_state = queryMultiAdapter((self.context, self.request),
                                              name='plone_portal_state')
        self._get_data()

    @memoize
    def _get_data(self):
        """Get the remote listing data from the MLS."""
        lang = self.portal_state.language()
        if getattr(self.request, 'listing_id', None) is not None:
            self.listing_id = self.request.listing_id
        else:
            self.listing_id = getattr(self.context, 'listing_id', None)
        if self.listing_id:
            self._data = listing_details(self.listing_id, lang)

    @property
    def data(self):
        return self._data

    @property
    def error(self):
        return self._error 

    @property
    def lead_image(self):
        if self.data is not None:
            image = self.data.get('images', None)[:1]
            if len(image) > 0:
                return image[0]
        return None
    
    def base_url(self):
        if getattr(self.request, 'listing_id', None) is not None:
            return '/'.join([self.context.absolute_url(), self.listing_id])
        else:
            return self.context.absolute_url()