
import time
import platform

def get_uptime():
    if platform.system() == "Windows":
        import ctypes

        # Get tick count in milliseconds
        uptime_ms = ctypes.windll.kernel32.GetTickCount64()
        uptime_sec = uptime_ms / 1000.0
    else:
        # For Linux/macOS: read from /proc/uptime (Linux) or use time
        try:
            with open('/proc/uptime', 'r') as f:
                uptime_sec = float(f.readline().split()[0])
        except FileNotFoundError:
            # Fallback (macOS)
            uptime_sec = time.time() - psutil.boot_time()

    return uptime_sec


def format_uptime(seconds):
    days = int(seconds // (24 * 3600))
    seconds %= (24 * 3600)
    hours = int(seconds // 3600)
    seconds %= 3600
    minutes = int(seconds // 60)
    seconds = int(seconds % 60)

    return f"{days}d {hours}h {minutes}m {seconds}s"


if __name__ == "__main__":
    uptime_seconds = get_uptime()
    print("System Uptime:", format_uptime(uptime_seconds))
