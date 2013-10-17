import unittest2 as unittest

from Products.CMFCore.utils import getToolByName

from theming.toolkit.views.testing import\
    THEMING_TOOLKIT_VIEWS_INTEGRATION


class TestExample(unittest.TestCase):

    layer = THEMING_TOOLKIT_VIEWS_INTEGRATION
    
    def setUp(self):
        self.app = self.layer['app']
        self.portal = self.layer['portal']
        self.qi_tool = getToolByName(self.portal, 'portal_quickinstaller')
    
    def test_product_is_installed(self):
        """ Validate that our products GS profile has been run and the product 
            installed
        """
        pid = 'theming.toolkit.views'
        installed = [p['id'] for p in self.qi_tool.listInstalledProducts()]
        self.assertTrue(pid in installed,
                        'package appears not to have been installed')
