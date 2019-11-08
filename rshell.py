
import os
import signal
from socket import gethostname
from getpass import getuser
import sys


def sig_handler(signum, frame):
	if signum != 17:
		print("\nAll signals are forbidden!")
	return

catchable_sigs = set(signal.Signals) - {signal.SIGKILL, signal.SIGSTOP}
for sig in catchable_sigs:
	signal.signal(sig, sig_handler)



def check_chal1(x):
	bad_chars = '!#%&\'()*+,-/:;<=>?@[\\]^_`{\'}~\t\n\r\x0b\x0c'
	bad_seq = ["bash", "python"]

	if not x:
		return False

	for char in bad_chars:
		if char in x:
			print("The character '{}' is not allowed!".format(char))
			return False

	for seq in bad_seq:
		if seq in x:
			print("You are not allowed to have an input with '{}' in it.".format(seq))
			return False

	return True


def check_chal2(x):
	bad_chars = '!"#%&\'()*+,/:;<=>?@[\\]^_`{|}~\t\n\r\x0b\x0c'
	bad_seq = ["sh", "rm", "vi", "vim", "emacs", "joe", "find", "py"]

	if not x:
		return False

	for char in bad_chars:
		if char in x:
			print("The character '{}' is not allowed!".format(char))
			return False

	for seq in bad_seq:
		if seq in x:
			print("You are not allowed to have an input with '{}' in it.".format(seq))
			return False

	if x[0] == "$":
		print("You are not allowed to have an input with '$' in it.")
		return False

	return True


def check_chal3(x):
	bad_chars = '!"#%&\'*+,/()-:;<=>?@[\\]^_`{|}~\t\n\r\x0b\x0c'
	bad_seq = ["sh", "rm", "vi", "vim", "emacs", "joe", "nano", "find", "ruby", "perl"]

	if not x:
		return False

	for char in bad_chars:
		if char in x:
			print("The character '{}' is not allowed!".format(char))
			return False

	for seq in bad_seq:
		if seq in x:
			print("You are not allowed to have an input with '{}' in it.".format(seq))
			return False

	return True



def check_chal4(x):
	bad_chars = '!"#%&\'*+,./-:;<=>?@[\\]^_`{|}~\t\n\r\x0b\x0c'
	bad_seq = ["sh", "rm", "vi", "vim", "emacs", "joe", "py", "find", "ruby", "perl"]

	if not x:
		return False

	for char in bad_chars:
		if char in x:
			print("The character '{}' is not allowed!".format(char))
			return False

	for seq in bad_seq:
		if seq in x:
			print("You are not allowed to have an input with '{}' in it.".format(seq))
			return False

	return True



diff = [1, 2, 3, 4]


def main():
	if len(sys.argv) != 2:
		print("Usage: ./rshell.py <difficulty>")
		print("Difficulty is a number from {} to {}".format(diff[0], diff[-1]))
		exit()

	if not sys.argv[1].isdigit():
		print("<difficulty> must be an integer")
		exit()

	d = int(sys.argv[1])

	if d not in diff:
		print("Difficulty must be a number from {} to {}".format(diff[0], diff[-1]))
		exit()

	check = eval("check_chal" + str(d))

	print("Welcome to my secure shell!\nYour difficulty is set to {}.\nAll requests will be filtered by {}".format(d, "check_chal{}()".format(d)))
	print("Your only goal is to get a bash shell.")


	cwd = "/"
	uname = getuser()
	hname = gethostname()

	while True:
		x = input("{}@{}: ".format(uname, hname)).strip()
		if x == "exit":
			exit()
		if not check(x.lower()):
			continue
		os.system(x)


main()