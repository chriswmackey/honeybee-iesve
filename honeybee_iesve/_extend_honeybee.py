# coding=utf-8
# import all of the modules for writing geometry to IES
from honeybee.properties import ModelProperties

from .properties.model import ModelIesveProperties

# set a hidden ies attribute on each core geometry Property class to None
# define methods to produce ies property instances on each Property instance
ModelProperties._iesve = None


def model_iesve_properties(self):
    if self._iesve is None:
        self._iesve = ModelIesveProperties(self.host)
    return self._iesve


# add ies property methods to the Properties classes
ModelProperties.iesve = property(model_iesve_properties)
