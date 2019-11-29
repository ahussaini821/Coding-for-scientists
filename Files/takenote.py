done = False

outf = open("notes.txt", "a")

while not done:
	new_line = raw_input("Enter a line or exit: ")
	if new_line == "exit" or new_line == "Exit":
		done = True
	else:
		outf.write(new_line+"\n")
outf.close()
