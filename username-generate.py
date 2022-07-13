
#!/usr/bin/python3

import os,argparse,sys

parser = argparse.ArgumentParser(description='AD Usernames Generator')
parser.add_argument('-u',help='UserList Path')
parser.add_argument('-o',help='Output Filename')
args = parser.parse_args()


users_file = args.u
write_file = args.o

if len(sys.argv)==1:
    parser.print_help(sys.stderr)
    sys.exit(1)
args=parser.parse_args()

print(" ")
file = open(users_file,"r")
os.system("rm "+write_file+";touch "+write_file)
file_write = open(write_file,"a+")

for i in file :

	#combine first and lastname lowercase

	firstname_1 = i.split()[0].lower()
	lastname_1 = i.split()[1].lower()
	combined_1 = firstname_1+lastname_1
	file_write.write(combined_1+"\n")
	
	#combine first and "." lastname lowercase

	firstname_2 = i.split()[0].lower()
	lastname_2 = i.split()[1].lower()
	combined_2 = firstname_2+"."+lastname_2
	file_write.write(combined_2+"\n")
	
	#combine lastname and firstname lowercase

	firstname_3 = i.split()[0].lower()
	lastname_3 = i.split()[1].lower()
	combined_3 = lastname_3+firstname_3
	file_write.write(combined_3+"\n")
	
	
	#combine lastname and "." firstname lowercase

	firstname_4 = i.split()[0].lower()
	lastname_4 = i.split()[1].lower()
	combined_4 = lastname_4+"."+firstname_4
	file_write.write(combined_4+"\n")
	

	#initial of first name combined with complete lastname

	initial = i[0].lower()
	lastname_5 = i.split()[1].lower()
	combined_5 = initial+lastname_5
	file_write.write(combined_5+"\n")
	
	#initial of first name combined with "." complete lastname

	initial = i[0].lower()
	lastname_6 = i.split()[1].lower()
	combined_6 = initial+"."+lastname_6
	file_write.write(combined_6+"\n")

	#combined first 3 characters of firstname and first 3 characters of lastname
	firstname_7 = i[0:3].lower()
	lastname_7 = i.split()[1][0:3].lower()
	combined_7 = firstname_7+lastname_7
	file_write.write(combined_7+"\n")
	
	
	#combine first and "-" lastname lowercase

	firstname_8 = i.split()[0].lower()
	lastname_8 = i.split()[1].lower()
	combined_8 = firstname_8+"-"+lastname_8
	file_write.write(combined_8+"\n")
	
	#combine lastname and "-" firstname lowercase

	firstname_9 = i.split()[0].lower()
	lastname_9 = i.split()[1].lower()
	combined_9 = lastname_9+"."+firstname_9
	file_write.write(combined_9+"\n")
	
	#initial of first name combined with "-" complete lastname

	initial = i[0].lower()
	lastname_10 = i.split()[1].lower()
	combined_10 = initial+"-"+lastname_10
	file_write.write(combined_10+"\n")

	
	#initial of first name (uppercase) combined with lastname initial uppercase

	initial = i[0].upper()
	lastname_11 = i.split()[1]
	combined_11 = initial+lastname_11
	file_write.write(combined_11+"\n")
	
	

'''
	# combine 3 letters of firstname and 3 random numbers 

	firstname_4 = i[0:3].lower()

	#use crunch to generate random numbers behind each usernames

	os.system("crunch 6 6 " + "0123456789 " + "-t " + firstname_4+"%%%"+" -o /root/HTB/sauna/crunch_"+firstname_4)

	file_crunch = open("/root/HTB/sauna/crunch_"+firstname_4,"r")

	for content in file_crunch:

		file_write.write(content)


'''

print ("Usernames Generated Successfully")
