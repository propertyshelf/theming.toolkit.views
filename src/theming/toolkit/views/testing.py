from plone.app.testing import PloneWithPackageLayer
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting

import theming.toolkit.views


THEMING_TOOLKIT_VIEWS = PloneWithPackageLayer(
    zcml_package=theming.toolkit.views,
    zcml_filename='testing.zcml',
    gs_profile_id='theming.toolkit.views:testing',
    name="THEMING_TOOLKIT_VIEWS")

THEMING_TOOLKIT_VIEWS_INTEGRATION = IntegrationTesting(
    bases=(THEMING_TOOLKIT_VIEWS, ),
    name="THEMING_TOOLKIT_VIEWS_INTEGRATION")

THEMING_TOOLKIT_VIEWS_FUNCTIONAL = FunctionalTesting(
    bases=(THEMING_TOOLKIT_VIEWS, ),
    name="THEMING_TOOLKIT_VIEWS_FUNCTIONAL")
