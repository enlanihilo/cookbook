from _thread import start_new_thread
from time import sleep

"""
	Multithreading can significantly improve the speed of
	computation on multiprocessor/multi-core systems because
	each processor/core handles a separate thread concurenntly.
"""

threadId = 1
waiting = 2

def factorial(n):
	global threadId
	rc = 0

	if n < 1:
		print(f"\nThread: {threadId}")
		threadId += 1
		rc = 1
	else:
		returnNumber = n * factorial(n - 1)
		print(f"{str(n)} != {str(returnNumber)}")
		rc = returnNumber

	return rc


start_new_thread(factorial, (5, ))
start_new_thread(factorial, (4, ))

print("Waiting for threads to return...")
sleep(waiting)

