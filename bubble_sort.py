import random
import datetime

def bubble(arr):
	sorted = len(arr)-1

	index = 0
	while sorted > 0:
		if arr[index] > arr[index+1]:
			temp = arr[index]
			arr[index] = arr[index+1]
			arr[index+1] = temp
		index+=1
		if index == sorted:
			sorted-=1
			index = 0
	return arr

a = []
i = 0
while i < 100:
	a.append(random.randint(0, 10000))
	i+=1

time1 = datetime.datetime.now()
print bubble(a)
time2 = datetime.datetime.now()

print "Elapsed time: " + str((time2.microsecond - time1.microsecond)/1e6) + " seconds"