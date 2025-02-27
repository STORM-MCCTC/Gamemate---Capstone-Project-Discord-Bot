import time
import style

start_time = time.time()
def print_uptime():
    end_time = time.time()
    elapsed_time = int(end_time - start_time)
    days, remainder = divmod(elapsed_time, 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes, seconds = divmod(remainder, 60)
    print(f"{style.color.BLUE}uptime:{style.color.END} {style.color.BLACK}{days}d {hours}h {minutes}m {seconds}s{style.color.END}")