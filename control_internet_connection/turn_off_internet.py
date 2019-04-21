# In this way you can activate it whenever you have
# something specific to search

# Is run from crontab (every 10 minutes)
# export VISUAL=vim
# export EDITOR="$VISUAL"
# sudo -E crontab -e
import os
import logging
import subprocess


cmd = 'sudo ifconfig wlp3s0 down'
os.system(cmd)
# New way to do it
# subprocess.call([cmd])

# logging
# LOG = "/tmp/ccd.log"
# logging.basicConfig(filename=LOG, filemode="w", level=logging.DEBUG)

# console handler
# console = logging.StreamHandler()
# console.setLevel(logging.ERROR)
# logging.getLogger("").addHandler(console)

"""
import datetime
def time_in_range(start, end, x):
    "Return true if x is in the range [start, end]"
    if start <= end:
        return start <= x <= end
    else:
        return start <= x or x <= end


start = datetime.time(7, 0, 0)
stop = datetime.time(19, 0, 0)
curent = datetime.datetime.now().time()

# Block internet si on est dans la période de travail
if time_in_range(start, stop, curent):
    os.system('sudo ifconfig wlp3s0 down')
"""

