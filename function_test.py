# Written by Pat Farnach
# 1/8/2014 @ PDX Code Guild

import sys  # for quit function

# initializes temporary address book
book = {}

# function to add to temporary address book
def add():
	name = raw_input(">> What's the name?: ").title()
	phone = raw_input(">> What's the phone number?: ")
	book[name] = phone
	print "\nAdded to temporary address book.\n"

# function to find entry based on name in temporary address book
def find():
	name = raw_input(">> Whose phone number are you looking for?: ").title()
	if name in book:
		print "%s's phone number is %s" % (name, book[name])
	else:
		print "Name not found in address book."

# function to remove entry based on name in temporary address book
def remove():
	name = raw_input(">> Whose entry do you want to delete?: ").title()
	if name in book:
		del book[name]
		print "Entry deleted."
	else:
		print "Name not found in address book."

# function to print contents of temp address book
def contents():
	print book

# funtion to save/commit temp address book to external file. Appends to this file.
def save():
	with open("function_test_out.txt", "a") as current_file:
		for key in book:	
			current_file.write(key + "\t" + book[key] + "\n")
			print key + "'s entry saved to external address book."

# function to open and print contents of perm address book (external file)
def open_book():
	with open("function_test_out.txt", "r") as current_file:
		print current_file.read()

# function to totally reset/empty external address book
def reset():
	sure = raw_input(">> Are you sure you want to remove all contents from file? y/n: ").lower()

	if sure == "y":
		with open("function_test_out.txt", "w") as current_file:
			# current_file.write("")
			print "\nExternal address book reset."
	else:
		print "\nA wise choice"

# function to remove single entry based on name from external address book
def remove_perm():

	name = raw_input(">> What name do you want to delete from the permanent address book?: ").title()

	# opens and closes file after reading because r+ wasn't overwriting previous data (!?)
	current_file = open("function_test_out.txt", "r")
	lines = current_file.readlines()
	current_file.close()

	temp_book = []

	for line in lines:
		if name not in line:
			temp_book.append(line)

	current_file = open("function_test_out.txt", "w")

	for item in temp_book:
		current_file.write(item)
	
	current_file.close()

	# if no differences/changes between two files, then nothing changed/entry not found
	if lines == temp_book:
		print "\nSorry, name not found in permanent address book.\n"
	else:
		print "\n" + name + "'s entry removed from external address book."

# function to quit program
def quit():
	sys.exit(0)
	
# main loop that executes to get user input
while True:

	# gives user options on what to do
	user_input = raw_input("\n>> Select a number: \n1. Add to temporary address book\n2. Find a user in temporary address book\n3. Delete entry from temporary address book\n4. List contents in temporary address book\n5. Save temporary address book to external address book\n6. List contents in external address book\n7. Delete entry from external address book\n8. Clear external address book\n9. Quit \n>> ")
	print
	
	# points to functions based on what user inputs
	if user_input == "1":
		add()
	elif user_input == "2":
		find()
	elif user_input == "3":
		remove()
	elif user_input == "4":
		contents()
	elif user_input == "5":
		save()
		book = {}
	elif user_input == "6":
		open_book()
	elif user_input == "8":
		reset()
	elif user_input == "7":
		remove_perm()
	elif user_input == "9":
		quit()
	else:
		print "Invalid input. Try again."
