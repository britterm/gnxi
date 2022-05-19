# -*- coding: utf-8 -*-
from operator import attrgetter
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType
from pyangbind.lib.yangtypes import RestrictedClassType
from pyangbind.lib.yangtypes import TypedListType
from pyangbind.lib.yangtypes import YANGBool
from pyangbind.lib.yangtypes import YANGListType
from pyangbind.lib.yangtypes import YANGDynClass
from pyangbind.lib.yangtypes import ReferenceType
from pyangbind.lib.base import PybindBase
from collections import OrderedDict
from decimal import Decimal
from bitarray import bitarray
import six

# PY3 support of some PY2 keywords (needs improved)
if six.PY3:
  import builtins as __builtin__
  long = int
elif six.PY2:
  import __builtin__

class openconfig_p4rt(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-p4rt - based on the path /openconfig-p4rt. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: This module defines a set of extensions that provide P4Runtime (P4RT)
specific extensions to the OpenConfig data models. Specifically, these
parameters for configuration and state provide extensions that control
the P4RT service, or allow it to be used alongside other OpenConfig
data models.

The P4RT protocol specification is linkde from https://p4.org/specs/
under the P4Runtime heading.
  """
  _pyangbind_elements = {}

  
