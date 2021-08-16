import time
import sys
import codecs


sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

mytime = time.localtime()

if mytime.tm_hour+8 < 12:
 payload = '{ }'
 print(payload)

else:
 payload = '{ }'
 print(payload)