# -*- coding: utf8 -*-
import time
import sys
import io
import codecs

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding="utf8",line_buffering=True)

mytime = time.localtime()

if mytime.tm_hour+8 < 12:
 payload = " "
 print(payload)

else:
 payload = " "
 print(payload)