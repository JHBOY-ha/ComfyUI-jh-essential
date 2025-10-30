# utils/timer_utils.py
import time
import datetime as _dt

def now_ns() -> int:
    """返回当前系统时间（纳秒级时间戳，基于 time.time_ns）。"""
    return time.time_ns()

def ns_to_iso(ns: int) -> str:
    """把纳秒级时间戳转为本地时区 ISO 字符串（到毫秒）。"""
    return _dt.datetime.fromtimestamp(ns / 1e9).isoformat(timespec="milliseconds")

def format_elapsed(seconds: float, fmt: str = "s") -> str:
    """
    把秒数格式化为字符串：
      - 's'   -> '0.842s'
      - 'ms'  -> '842.1 ms'
      - 'm:s' -> '00:00.842'
    """
    if fmt == "ms":
        return f"{seconds * 1000.0:.1f} ms"
    if fmt == "m:s":
        m, s = divmod(seconds, 60.0)
        return f"{int(m):02d}:{s:06.3f}"
    return f"{seconds:.3f}s"
