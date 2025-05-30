import logging
from time import sleep

import programmingtheiot.common.ConfigConst as ConfigConst

from programmingtheiot.common.ConfigUtil import ConfigUtil
from programmingtheiot.cda.sim.BaseActuatorSimTask import BaseActuatorSimTask

from pisense import SenseHAT

class LightActuatorEmulatorTask(BaseActuatorSimTask):
    """
    Emulador del actuador de luz. Usa SenseHAT para mostrar el estado de la luz.
    """

    def __init__(self):
        super(LightActuatorEmulatorTask, self).__init__(
            name = ConfigConst.LIGHT_ACTUATOR_NAME,
            typeID = ConfigConst.LIGHT_ACTUATOR_TYPE,
            simpleName = "LIGHT")
        
        enableEmulation = ConfigUtil().getBoolean(
            ConfigConst.CONSTRAINED_DEVICE, ConfigConst.ENABLE_EMULATOR_KEY)
        
        self.sh = SenseHAT(emulate = enableEmulation)

    def _activateActuator(self, val: float = ConfigConst.DEFAULT_VAL, stateData: str = None) -> int:
        if self.sh.screen:
            msg = self.getSimpleName() + ' ON'
            self.sh.screen.scroll_text(msg) 
            return 0
        else:
            logging.warning("No SenseHAT LED screen instance to write.")
            return -1

    def _deactivateActuator(self, val: float = ConfigConst.DEFAULT_VAL, stateData: str = None) -> int:
        if self.sh.screen:
            msg = self.getSimpleName() + ' OFF'
            self.sh.screen.scroll_text(msg)
            sleep(2)
            self.sh.screen.clear()
            return 0
        else:
            logging.warning("No SenseHAT LED screen instance to clear / close.")
            return -1
