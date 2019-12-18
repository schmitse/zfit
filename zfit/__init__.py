# -*- coding: utf-8 -*-
"""Top-level package for zfit."""

#  Copyright (c) 2019 zfit
import warnings

from pkg_resources import get_distribution

__version__ = get_distribution(__name__).version

__license__ = "BSD 3-Clause"
__copyright__ = "Copyright 2018, zfit"
__status__ = "Beta"

__author__ = "Jonas Eschle"
__maintainer__ = "zfit"
__email__ = 'zfit@physik.uzh.ch'
__credits__ = ["Jonas Eschle <Jonas.Eschle@cern.ch>",
               "Albert Puig <apuignav@gmail.com",
               "Rafael Silva Coutinho <rafael.silva.coutinho@cern.ch>", ]

__all__ = ["ztf", "z", "constraint", "pdf", "minimize", "loss", "core", "data", "func",
           "Parameter", "ComposedParameter", "ComplexParameter", "convert_to_parameter",
           "Space", "convert_to_space", "supports",
           "run", "settings"]

#  Copyright (c) 2019 zfit
import tensorflow.compat.v1 as _tfv1

# tf.enable_resource_variables()  # forward compat
# tf.enable_v2_tensorshape()  # forward compat
_tfv1.enable_v2_behavior()
# _tfv1.disable_eager_execution()

warnings.warn(
    """zfit has moved from TensorFlow 1.x to 2.x, which has some profound implications behind the scenes of zfit
     and minor ones on the user side. Be sure to read the upgrade guide (README on top) to have a seemless
     transition. If this is currently not doable (upgrading is highly recommended though) you can downgrade zfit to <0.4.
     Contact us in case of problems in order to tackle them ASAP.""")

from . import z
from . import z as ztf  # legacy
from .settings import ztypes

# tf.get_variable_scope().set_use_resource(True)
# tf.get_variable_scope().set_dtype(ztypes.float)

from . import constraint, pdf, minimize, loss, core, data, func, param
from .core.parameter import Parameter, ComposedParameter, ComplexParameter, convert_to_parameter
from .core.limits import Space, convert_to_space, supports
from .core.data import Data

from .settings import run

# EOF
