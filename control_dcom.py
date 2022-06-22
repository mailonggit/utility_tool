from enum import auto
from time import sleep
import autoit
title = "Mobile Partner"
autoit.win_activate(title)
print("activate " + title)
sleep(3)
print("maximize " + title)
autoit.win_set_state(title)
autoit.win_set_state_by_handle()