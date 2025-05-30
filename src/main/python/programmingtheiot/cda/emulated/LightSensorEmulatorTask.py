from programmingtheiot.data.SensorData import SensorData
import programmingtheiot.common.ConfigConst as ConfigConst
from programmingtheiot.common.ConfigUtil import ConfigUtil
from programmingtheiot.cda.sim.BaseSensorSimTask import BaseSensorSimTask

from pisense import SenseHAT
import random  # Solo si no hay sensor de luz real

class LightSensorEmulatorTask(BaseSensorSimTask):
	"""
	Simulador de un sensor de luz usando Sense HAT (o valores aleatorios).
	"""

	def __init__(self, dataSet = None):
		super(LightSensorEmulatorTask, self).__init__(
			name = ConfigConst.LIGHT_SENSOR_NAME,
			typeID = ConfigConst.LIGHT_SENSOR_TYPE
		)

		enableEmulation = ConfigUtil().getBoolean(
			ConfigConst.CONSTRAINED_DEVICE,
			ConfigConst.ENABLE_EMULATOR_KEY
		)

		self.sh = SenseHAT(emulate = enableEmulation)

	def generateTelemetry(self) -> SensorData:
		sensorData = SensorData(name = self.getName(), typeID = self.getTypeID())

		# Como el Sense HAT no tiene sensor de luz, generamos un valor simulado
		# Sustituye esto por un sensor real si lo tienes
		sensorVal = random.uniform(100.0, 1000.0)  # en lúmenes

		sensorData.setValue(sensorVal)
		self.latestSensorData = sensorData

		return sensorData
