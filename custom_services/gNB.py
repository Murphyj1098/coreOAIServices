from typing import List, Dict

from core.config import Configuration
from core.configservice.base import ConfigService, ConfigServiceMode

class gNB(ConfigService):
    name: str = "gNB"
    group: str = "OpenAirInterface"
    directories: List[str] = []
    files: List[str] = [
        "gNB_proxy.conf",
        "start_gnb.sh"
    ]
    executables: List[str] = []
    dependencies: List[str] = []
    startup: List[str] = ["bash start_gnb.sh"]
    validate: List[str] = []
    shutdown: List[str] = []
    validation_mode: ConfigServiceMode = ConfigServiceMode.NON_BLOCKING
    default_configs: List[Configuration] = []
    modes: Dict[str, Dict[str, str]] = {}
