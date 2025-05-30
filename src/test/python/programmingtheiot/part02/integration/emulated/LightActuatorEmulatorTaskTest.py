#####
# 
# This class is part of the Programming the Internet of Things
# project, and is available via the MIT License, which can be
# found in the LICENSE file at the top level of this repository.
# 
# Copyright (c) 2020 by Andrew D. King
# 

import logging
import unittest

from time import sleep

import programmingtheiot.common.ConfigConst as ConfigConst

from programmingtheiot.data.ActuatorData import ActuatorData
from programmingtheiot.cda.emulated.LightActuatorEmulatorTask import LightActuatorEmulatorTask


class LightActuatorEmulatorTaskTest(unittest.TestCase):
	
	@classmethod
	def setUpClass(self):
		logging.basicConfig(format = '%(asctime)s:%(module)s:%(levelname)s:%(message)s', level = logging.DEBUG)
		logging.info("Testing LightActuatorEmulatorTask class [using SenseHAT emulator]...")
		self.lightTask = LightActuatorEmulatorTask()

		
	def setUp(self):
		pass

	def tearDown(self):
		pass

	def testUpdateEmulator(self):
		ad = ActuatorData(typeID = ConfigConst.LIGHT_ACTUATOR_TYPE)
		ad.setCommand(ConfigConst.COMMAND_ON)
		ad.setValue(50.0)
		
		adr = self.lightTask.updateActuator(ad)
		
		if adr:
			self.assertEqual(adr.getCommand(), ConfigConst.COMMAND_ON)
			self.assertEqual(adr.getStatusCode(), 0)
			logging.info("ActuatorData: " + str(adr))
			
			# wait 5 seconds
			sleep(5)
		else:
			logging.warning("ActuatorData is None.")
			
		ad.setValue(35.0)
		
		adr = self.lightTask.updateActuator(ad)

		
		if adr:
			self.assertEqual(adr.getCommand(), ConfigConst.COMMAND_ON)
			self.assertEqual(adr.getStatusCode(), 0)
			logging.info("ActuatorData: " + str(adr))
			
			# wait 5 seconds
		else:
			logging.warning("ActuatorData is None.")
			
		ad.setCommand(ConfigConst.COMMAND_OFF)
		
		adr = self.lightTask.updateActuator(ad)
		
		if adr:
			self.assertEqual(adr.getCommand(), ConfigConst.COMMAND_OFF)
			self.assertEqual(adr.getStatusCode(), 0)
			logging.info("ActuatorData: " + str(adr))
		else:
			logging.warning("ActuatorData is None.")
			
if __name__ == "__main__":
	unittest.main()