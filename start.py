'''
Author : Siddharth Nayak
email:ee16b073@smail.iitm.ac.in
'''

import serial, os, signals, sys
from sklearn.externals import joblib

#Serial parameters
SERIAL_PORT = "/dev/cu.usbmodem1421"
BAUD_RATE = 38400
TIMEOUT = 100

#Recording parameters
target_sign = "a"
current_batch = "0"
target_directory = "data"

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
	if arguments.has_key("port"):
		SERIAL_PORT = arguments["port"]

clf = None
classes = None
sentence = ""


#Loads the machine learning model from file
print ("Loading model...")
clf = joblib.load('model.pkl')
classes = joblib.load('classes.pkl')


print ("OPENING SERIAL_PORT '{port}' WITH BAUDRATE {baud}...".format(port = SERIAL_PORT, baud = BAUD_RATE))
print ("IMPORTANT!")
print ("To end the program hold Ctrl+C and send some data over serial")

#Opens the serial port specified by SERIAL_PORT with the specified BAUD_RATE
ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout = TIMEOUT)

output = []

in_loop = True

current_sample = 0

#Resets the output file
output_file = open("output.txt","w")
output_file.write("")
output_file.close()

#If TARGET_ALL_MODE = True, print the sentence with the current position


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
			print ("RECORDING...",)
		elif line=="CLOSING BATCH": #Stops recording and analyzes the result
			#Disable recording
			print('uno')
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
					print ("PREDICTING...")
					#It loads the recording as a Sample object
					sample_test = signals.Sample.load_from_file(path)

					linearized_sample = sample_test.get_linearized(reshape=True)
					#Predict the number with the machine learning model
					number = clf.predict(linearized_sample)
					#Convert it to a char
					char = chr(ord('a')+number[0])

					#Get the last word in the sentence
					last_word = sentence.split(" ")[-1:][0]

				
					
					
					#If the mode is WRITE, assigns special meanings to some characters
					#and builds a sentence with each char
					if ENABLE_WRITE:
						if char == 'D': #Delete the last character
							sentence = sentence[:-1]
						elif char == 'A': #Delete all characters
							if DELETE_ALL_ENABLED:
								sentence = ""
							else:
								print ("DELETE_ALL_ENABLED = FALSE")
						else: #Add the char to the sentence
							sentence += char
						#Prints the last char and the sentence
						print ("[{char}] -> {sentence}".format(char = char, sentence = sentence))
						#Saves the output to a file
						output_file = open("output.txt","w")
						output_file.write(sentence)
						output_file.close()
					else:
						print(char)
			else: #In case of a corrupted sequence
				print ("ERROR...")
				current_test_index -= 1

			#If TARGET_ALL_MODE=True it shows the current position in the sentence
			if TARGET_ALL_MODE:
				current_test_index += 1
				print_sentence_with_pointer(test_sentence, current_test_index)
		else:
			#Append the current signal line in the recording
			output.append(line)
except KeyboardInterrupt: #When Ctrl+C is pressed, the loop terminates
    print ('CLOSED LOOP!')

#Closes the serial port
ser.close()