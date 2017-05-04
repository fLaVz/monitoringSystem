import time
import parser


starttime=time.time()
while True:
  parser.parse()
  time.sleep(5.0 - ((time.time() - starttime) % 5.0))
