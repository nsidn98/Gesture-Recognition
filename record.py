'''
Author : Siddharth Nayak
email:ee16b073@smail.iitm.ac.in
'''
import serial, os, sys,signals,signals1
import numpy as np
from sklearn.externals import joblib
'''
This module is for recording new data
If the serial port prints "STARTING BATCH" the recording is started
If the serial port prints "CLOSING BATCH" the recording is done and waits for the next batch
'''
#Mode parameters, controlled using sys.argv by the terminal
SAVE_NEW_SAMPLES = False
FULL_CYCLE = False
ENABLE_WRITE = False
TARGET_ALL_MODE = False
DELETE_ALL_ENABLED = False
TRY_TO_PREDICT=True
#Serial parameters
SERIAL_PORT = "/dev/cu.usbmodem1421"
BAUD_RATE = 38400
TIMEOUT = 100

#Recording parameters
target_sign = "a"
current_batch = "0"
target_directory = "data12345"

current_test_index = 0

#Analyzes the arguments to enable a specific mode

arguments = {}

for i in sys.argv[1:]:
	if "=" in i:
		sub_args = i.split("=")
		arguments[sub_args[0]]=sub_args[1]
	else:
		arguments[i]=None

#If there are arguments, analyzes them
if len(sys.argv)>1:
	if arguments.has_key("target"):
		target_sign = arguments["target"].split(":")[0]
		current_batch = arguments["target"].split(":")[1]
		print ("TARGET SIGN: '{sign}' USING BATCH: {batch}".format(sign=target_sign, batch = current_batch))
		SAVE_NEW_SAMPLES = True
	if arguments.has_key("write"):
		ENABLE_WRITE = True
	if arguments.has_key("test"):
		current_batch = arguments["test"]
		TARGET_ALL_MODE = True
		SAVE_NEW_SAMPLES = True
	if arguments.has_key("port"):
		SERIAL_PORT = arguments["port"]

clf = None
classes = None
sentence = ""





print ("OPENING SERIAL_PORT '{port}' WITH BAUDRATE {baud}...".format(port = SERIAL_PORT, baud = BAUD_RATE))

print ("IMPORTANT!")
print ("To end the program hold Ctrl+C and send some data over serial")

#Opens the serial port specified by SERIAL_PORT with the specified BAUD_RATE
ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout = TIMEOUT)

output = []

in_loop = True
is_recording = False

current_sample = 37

#Resets the output file
output_file = open("output.txt","w")
output_file.write("")
output_file.close()

if TRY_TO_PREDICT:
	print ("Loading model...")
	clf = joblib.load('model_123456.pkl')
	classes = joblib.load('classes_123456.pkl')
	clf1=joblib.load('model_flex1.pkl')
	classes1=joblib.load('classes_flex1.pkl')
	print('Model Loaded')


try:
	while in_loop:
    	#Read a line over serial and deletes the line terminators
		line = ser.readline().replace("\r\n","")
		#If it receive "STARTING BATCH" it starts the recording
		if line=="STARTING BATCH":
			#Enable the recording
			is_recording = True
			#Reset the buffer
			output = []
			print("RECORDING...",)
		elif line=="CLOSING BATCH": #Stops recording and analyzes the result
			#Disable recording
			
			is_recording = False
			if len(output)>1: #If less than 1, it means error
				print ("DONE, SAVING...",)

				#If TARGET_ALL_MODE is enabled changes the target sign
				#according to the position
				if TARGET_ALL_MODE:
					if current_test_index<len(test_sentence):
						target_sign = test_sentence[current_test_index]
					else:
						#At the end of the sentence, it quits
						print ("Target All Ended!")
						quit()

				#Generates the filename based on the target sign, batch and progressive number
				filename = "{sign}_sample_{batch}_{number}.txt".format(sign = target_sign, batch = current_batch, number = current_sample)
				#Generates the path
				path = target_directory + os.sep + filename

				#If SAVE_NEW_SAMPLES is False, it saves the recording to a temporary file
				if SAVE_NEW_SAMPLES == False:
					path = "tmp.txt"
					filename = "tmp.txt"

				#Saves the recording in a file
				f = open(path, "w")
				f.write('\n'.join(output))
				f.close()
				print ("SAVED IN {filename}".format(filename = filename))

				current_sample += 1

				#If TRY_TO_PREDICT is True, it utilizes the model to predict the recording
				if TRY_TO_PREDICT:
					print('PREDICTING')
					sample_test = signals.Sample.load_from_file(path)
					linearized_sample = sample_test.get_linearized(reshape=True)
					number = clf.predict(linearized_sample)
					char = chr(ord('a')+number[0])
					#last_word = sentence.split(" ")[-1:][0]
					'''if char=='d' or char=='e' or char=='i' or char=='j' or char=='g' or char=='k':
						print('wait')
						sample_test1 = signals1.Sample.load_from_file(path)
						linearized_sample1 = sample_test1.get_linearized(reshape=True)
						number1 = clf1.predict(linearized_sample1)
						if number1==0:
							print('Column Formation')
						if number1==1:
							print('File Formation')
						if number1==2:
							print('Ammunition')
						if number1==3:
							print('Vehicle')
						if number1==4:
							print('Rally Point')
						if number==5:
							print("I don't Understand")'''
									
					#print(char)
					if char=='a':
						print('Come')
					if char=='b':
						print('Hurry Up')
					if char=='d':
						print('Column Formation')
					if char=='e':
						print('File Formation')
					if char=='i':
						print('Ammunition')
					if char=='j':
						print('Vehicle')
					if char=='g':
						print('Rally Point')
					if char=='k':
						print("I don't Understand")
					if char=='c':
						print('Go Here or Move U')
					if char=='f':
						print('Wedge Formation')
					if char=='h':
						print('Shotgun')
					if char=='l':
						print('Crouch or Go Prone')
					if char=='m':
						print('Window')
					if char=='n':
						print('Door')
					if char=='o':
						print('Point of Entry')
					
						
			else: #In case of a corrupted sequence
				print ("ERROR...")
				current_test_index -= 1
		
		elif line=="CLOSING BATCH1": #Stops recording and analyzes the result
			#Disable recording
			
			is_recording = False
			if len(output)>1: #If less than 1, it means error
				print ("DONE, SAVING...",)

				#If TARGET_ALL_MODE is enabled changes the target sign
				#according to the position
				if TARGET_ALL_MODE:
					if current_test_index<len(test_sentence):
						target_sign = test_sentence[current_test_index]
					else:
						#At the end of the sentence, it quits
						print ("Target All Ended!")
						quit()

				#Generates the filename based on the target sign, batch and progressive number
				filename = "{sign}_sample_{batch}_{number}.txt".format(sign = target_sign, batch = current_batch, number = current_sample)
				#Generates the path
				path = target_directory + os.sep + filename

				#If SAVE_NEW_SAMPLES is False, it saves the recording to a temporary file
				if SAVE_NEW_SAMPLES == False:
					path = "tmp.txt"
					filename = "tmp.txt"

				#Saves the recording in a file
				f = open(path, "w")
				f.write('\n'.join(output))
				f.close()
				print ("SAVED IN {filename}".format(filename = filename))

				current_sample += 1

				#If TRY_TO_PREDICT is True, it utilizes the model to predict the recording
				if TRY_TO_PREDICT:
					print('PREDICTING')
					sample_test = signals.Sample.load_from_file(path)
					linearized_sample = sample_test.get_linearized(reshape=True)
					number = clf.predict(linearized_sample)
					char = chr(ord('a')+number[0])
					last_word = sentence.split(" ")[-1:][0]
					
					#print(char)
					if char=='a':
						print('Come')
					if char=='b':
						print('Hurry Up')
					if char=='c':
						print('Go Here or Move U')
					if char=='d':
						print('Column Formation')
					if char=='e':
						print('File Formation')
					if char=='f':
						print('Wedge Formation')
					if char=='g':
						print('Rally Point')
					if char=='h':
						print('Shotgun')
					if char=='i':
						print('Ammunition')
					if char=='j':
						print('Vehicle')
					if char=='k':
						print("I don't Understand")
					if char=='l':
						print('Crouch or Go Prone')
					if char=='m':
						print('Window')
					if char=='n':
						print('Door')
					if char=='o':
						print('Point of Entry')
					
						
			else: #In case of a corrupted sequence
				print ("ERROR...")
				current_test_index -= 1
				


		else:
			#Append the current signal line in the recording
			output.append(line)
except KeyboardInterrupt: #When Ctrl+C is pressed, the loop terminates
    print ('CLOSED LOOP!')

#Closes the serial port
ser.close()
