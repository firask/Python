import time
import os

# virtualSensorName = '__NAME_OF_THE_SENSOR__'
virtualSensorName = 'vstest'

#This method change the value in data file
def printVS( data ):
	print(data)
	dataIot = open(directory + file, "w")
	dataIot.write(data)
	dataIot.flush()
	dataIot.close()

# Open the output data file
file = 'data'
directory = '/sensors/virtual/'+ virtualSensorName +'/'
print ('Checking directory exists ...')
if not os.path.exists(directory):
	print ('Directory does not exists... creating... ')
	try:
		os.makedirs(directory)
		print ('OK')
	except OSError as e:
		print ('NO \n ERROR:' + e)
		exit()
else:
	print ('OK')


while True: # Run forever
		#MAKE CALCULATIONS
		printVS(time.strftime("%c"))
		time.sleep(5)