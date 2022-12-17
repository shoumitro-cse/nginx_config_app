import os
import signal
import sys


# Total arguments
n = len(sys.argv)

if n == 2:
	try:
		pid = int(sys.argv[1])
		os.killpg(os.getpgid(pid), signal.SIGTERM)
	except Exception as e:
		print(e)
		print("pid must be integer value.")

if n != 2: print("Sorry, argv[] value mismatch! it should be file name and pid.")



