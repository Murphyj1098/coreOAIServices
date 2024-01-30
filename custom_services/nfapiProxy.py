from typing import List, Dict

from core.config import Configuration, ConfigString
from core.configservice.base import ConfigService, ConfigServiceMode

class nfapiproxy(ConfigService):
    name: str = "5GProxy"
    group: str = "OpenAirInterface"
    directories: List[str] = []
    files: List[str] = ["start_proxy.sh"]
    executables: List[str] = []
    dependencies: List[str] = []
    startup: List[str] = ["bash start_proxy.sh"]
    validate: List[str] = []
    shutdown: List[str] = []
    validation_mode: ConfigServiceMode = ConfigServiceMode.NON_BLOCKING
    default_configs: List[Configuration] = [
        ConfigString(id="numue", label="Number of UEs", default="1"),
        ConfigString(id="gnb_ipaddr", label="gNB IP address", default="127.0.0.2"),
        ConfigString(id="proxy_ipaddr", label="proxy IP address", default="127.0.0.1"),
        ConfigString(id="ue_ipaddr", label="UE IP address", default="127.0.0.1")
    ]
    modes: Dict[str, Dict[str, str]] = {}
