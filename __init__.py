# ComfyUI-jh-essential/__init__.py
from .nodes.timing_nodes import StartTimer, EndTimer

NODE_CLASS_MAPPINGS = {
    "StartTimer": StartTimer,
    "EndTimer": EndTimer,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "StartTimer": "Start Timer",
    "EndTimer": "End Timer",
}
