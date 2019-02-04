import bcrypt
import getpass

pswd = getpass.getpass("Enter pwd to be hashed: ")
hashed = bcrypt.hashpw(pswd, bcrypt.gensalt())

f = open("hash.txt", 'w')
f.write(hashed)

#f = open("hash.txt", 'r')
#hashed = f.read()

while True:
	pas = getpass.getpass("enter pass: ")
	if bcrypt.hashpw(pas, hashed) == hashed:
		print "correct"
		break
	else:
		print "wrong"
