from plone.app.testing import PloneWithPackageLayer
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting

import pretaweb.plonesaml2


PRETAWEB_PLONESAML2 = PloneWithPackageLayer(
    zcml_package=pretaweb.plonesaml2,
    zcml_filename='testing.zcml',
    gs_profile_id='pretaweb.plonesaml2:testing',
    name="PRETAWEB_PLONESAML2")

PRETAWEB_PLONESAML2_INTEGRATION = IntegrationTesting(
    bases=(PRETAWEB_PLONESAML2, ),
    name="PRETAWEB_PLONESAML2_INTEGRATION")

PRETAWEB_PLONESAML2_FUNCTIONAL = FunctionalTesting(
    bases=(PRETAWEB_PLONESAML2, ),
    name="PRETAWEB_PLONESAML2_FUNCTIONAL")
