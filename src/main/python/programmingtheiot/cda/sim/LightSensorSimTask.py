import logging

import programmingtheiot.common.ConfigConst as ConfigConst

from programmingtheiot.cda.sim.BaseSensorSimTask import BaseSensorSimTask
from programmingtheiot.cda.sim.SensorDataGenerator import SensorDataGenerator

from programmingtheiot.data.SensorData import SensorData

class LightSensorSimTask(BaseSensorSimTask):
	"""
	Shell representation of class for student implementation.
	
	"""

	def __init__(self, dataSet = None):
		super( \
			LightSensorSimTask, self).__init__( \
				name = ConfigConst.LIGHT_SENSOR_NAME, \
				typeID = ConfigConst.LIGHT_SENSOR_TYPE, \
				dataSet = dataSet, \
				minVal = SensorDataGenerator.LOW_NORMAL_ENV_LIGHT, \
				maxVal = SensorDataGenerator.HI_NORMAL_ENV_LIGHT)