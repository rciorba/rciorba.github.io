from time import sleep
import sys

for n in range(10):
    sleep(1)
    print("echo", n)
    sys.stdout.flush()
