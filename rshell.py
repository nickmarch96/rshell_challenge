
import os
import signal
from socket import gethostname
from getpass import getuser
import sys
import modules


def sig_handler(signum, frame):
	if signum != 17:
		print("\nAll signals are forbidden!")
	return

catchable_sigs = set(signal.Signals) - {signal.SIGKILL, signal.SIGSTOP}
for sig in catchable_sigs:
	signal.signal(sig, sig_handler)



diff = [1, 2, 3, 4, 5, 6, 7, 8, 9]


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

	check = eval("modules.check_chal" + str(d))

	print("Welcome to my secure shell!\nYour difficulty is set to {}.\nAll requests will be filtered by {}".format(d, "check_chal{}()".format(d)))
	print("Your only goal is to get a bash shell.")

	if d == 8:
		print("="*80)
		print("Warning! Challenge number 8 requires 2 restricted shells to complete.")
		print("Please use 2 instances of './rshell.py 8' to complete. \nDo NOT use an easier difficulty or normal bash as the second shell.")
		print("="*80)

	cwd = "/"
	uname = getuser()
	hname = gethostname()

	while True:
		x = input("[RSHELL]:{}@{}: ".format(uname, hname)).strip()
		if x == "exit":
			exit()

		if not modules.global_check(x):
			continue

		x = check(x)
		if not x:
			continue

		os.system(x)


main()