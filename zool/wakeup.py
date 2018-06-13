"""Module dealing with getting people out of bed"""
import time
import subprocess
import schedule

from zool import notifications


def ping_machine(host):
    """Check if machine `host` responds to pings."""
    ping_response = subprocess.Popen(
        ["/bin/ping", "-c1", "-w100", host],
        stdout=subprocess.PIPE
    ).stdout.read()
    return ping_response.decode('utf-8')


def is_alive(host):
    """Check if given host is on"""
    return '100% packet loss' not in ping_machine(host)


def wake_up_job():
    """Schedule job to wake up people"""
    if is_alive("192.168.0.2"):
        print("Host is up, and I assume he is too")
        # Host is running, cancel alarms
        return schedule.CancelJob
    print("Uh oh, he must be in bed still")
    notifications.send_notification("WAKE UP, SUCKER!")


def activate_alarm():
    """Activate a scheduled task to periodically send an alarm"""
    schedule.every(5).minutes.do(wake_up_job)


if __name__ == '__main__':
    schedule.every().day.at('8:00').do(activate_alarm)

    while True:
        schedule.run_pending()
        time.sleep(1)
