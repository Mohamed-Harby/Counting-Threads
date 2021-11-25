import threading

def sequential(start, Thread_ID):
	if start > 20: # make sure that start is less than 1000. if not, return.
		return
	if start >= 20:
		print(start, 'in thread : ', Thread_ID)
		print('thread ', Thread_ID ,'finished')
		return
	print(start, 'in thread: ', Thread_ID)
	return sequential(start+1, Thread_ID) # Recursive call for sequential function with one step towards hundred

def odd(first, Thread_ID):
	if first > 20: # make sure that first is less than 999. if not, return
		return
	if first % 2 == 0: # first is even
		return odd(first + 1, Thread_ID)
	if first >= 20:
		print(first, 'from thread : ', Thread_ID)
		print('thread ', Thread_ID ,'finished')
		return
	print(first, 'from thread : ', Thread_ID)
	return odd(first+2, Thread_ID) # Recursive call for odd function with two step towards hundred


def even(first, Thread_ID):
	if first > 20: # make sure that first is less than 100. if not, return
		return
	if first % 2 == 1: # first is odd
		return even(first + 1, Thread_ID)
	if first >= 20:
		print(first, 'from thread : ', Thread_ID)
		print('thread ', Thread_ID ,'finished’')
		return
	print(first, 'from thread : ', Thread_ID)
	return even(first+2, Thread_ID) # Recursive call for even function with two step towards hundred


print('main started')
sequentialThread = threading.Thread(target=sequential, args=(0, 'SEQUENTIAL_THREAD'))
oddThread = threading.Thread(target=odd, args=(0, 'ODD_THREAD'))
evenThread = threading.Thread(target=even, args=(0, 'EVEN_THREAD'))
sequentialThread.start()
oddThread.start()
evenThread.start()
print('main finished')
