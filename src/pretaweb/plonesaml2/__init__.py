# -*- extra stuff goes here -*-


def initialize(context):
    """Initializer called when used as a Zope 2 product."""


# init default crypto. TODO: make configurable via env var
import dm.xmlsec.binding
dm.xmlsec.binding.initialize()
