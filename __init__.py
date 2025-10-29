# ComfyUI-jh-essential/__init__.py
from .nodes.timing_nodes import StartTimer, EndTimer
from .nodes.math_nodes import AddNumbers

NODE_CLASS_MAPPINGS = {
    "StartTimer": StartTimer,
    "EndTimer": EndTimer,
    "AddNumbers": AddNumbers,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "StartTimer": "Start Timer",
    "EndTimer": "End Timer",
    "AddNumbers": "Add Numbers",
}
