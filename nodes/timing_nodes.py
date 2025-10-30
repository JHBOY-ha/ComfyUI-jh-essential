# nodes/timing_nodes.py
from ..utils.timer_utils import now_ns, ns_to_iso, format_elapsed

class StartTimer:
    """
    记录“开始时刻”的系统时间戳（纳秒），并输出：
      - start_ns (INT)
      - label (STRING)
    通过 trigger("*") 建立依赖，不改变主数据流。
    """
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "trigger": ("*",),  # 仅用于顺序依赖
                "label": ("STRING", {"default": ""}),
            }
        }

    # 允许 "*" 通过后端校验（v0.3.60 对 * 更严格，需要显式放行）
    @classmethod
    def VALIDATE_INPUTS(cls, input_types):
        return True

    RETURN_TYPES = ("INT", "STRING")
    RETURN_NAMES = ("start_ns", "label")
    FUNCTION = "start"
    CATEGORY = "jh-essential/timing"

    def start(self, trigger, label: str = ""):
        s_ns = now_ns()
        return (int(s_ns), ns_to_iso(s_ns), label or "")


class EndTimer:
    """
    记录“结束时刻”的系统时间戳，与 StartTimer 的 start_ns 相减得到间隔。
    输入:
      - trigger("*"): 放在被测节点之后，用于顺序依赖
      - start_ns(INT): StartTimer 输出的纳秒级时间戳
      - format: 's' / 'ms' / 'm:s'
      - label(STRING，可选): 亦可从 StartTimer 拉一根 label 线过来
    输出:
      - time_str(STRING): 已格式化的时间间隔
      - seconds(FLOAT):   原始时间间隔（秒）
      - label(STRING):    标签（若未传入则为空）
    """
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "trigger": ("*",),
                "start_ns": ("INT",),
                "format": (["s", "ms", "m:s"], {"default": "s"}),
            },
            "optional": {
                "label": ("STRING", {"default": ""}),
            }
        }

    @classmethod
    def VALIDATE_INPUTS(cls, input_types):
        return True

    RETURN_TYPES = ("STRING", "FLOAT", "STRING")
    RETURN_NAMES = ("time_str", "seconds", "label")
    FUNCTION = "stop"
    CATEGORY = "jh-essential/timing"

    def stop(self, trigger, start_ns: int, format: str = "s", label: str = ""):
        e_ns = now_ns()
        elapsed_s = max(0.0, (e_ns - int(start_ns)) / 1e9)  # 防 NTP 回拨出现负数
        return (format_elapsed(elapsed_s, format), float(elapsed_s), ns_to_iso(e_ns), label or "")
