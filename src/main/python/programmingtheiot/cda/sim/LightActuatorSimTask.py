#####
# 
# This class is part of the Programming the Internet of Things
# project, and is available via the MIT License, which can be
# found in the LICENSE file at the top level of this repository.
# 
# Copyright (c) 2020 by Andrew D. King
# 
import programmingtheiot.common.ConfigConst as ConfigConst

from programmingtheiot.data.ActuatorData import ActuatorData
from programmingtheiot.cda.sim.BaseActuatorSimTask import BaseActuatorSimTask

class LightActuatorSimTask(BaseActuatorSimTask):

	def __init__(self):
		super( \
			LightActuatorSimTask, self).__init__( \
				name = ConfigConst.LIGHT_ACTUATOR_NAME, \
				typeID = ConfigConst.LIGHT_ACTUATOR_TYPE, \
				simpleName = "LIGHT")
