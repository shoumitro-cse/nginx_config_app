import os
import signal
import sys


# total arguments
n = len(sys.argv)

if n == 2:
	try:
		pid = int(sys.argv[1])
		os.killpg(os.getpgid(pid), signal.SIGTERM)
	except Exception as e:
		print(e)

if n != 2: print("Too much argv[]")



