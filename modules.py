


always_bad = "#%&/+,:<=>?@[~]\\^`\t\n\r\x0b\x0c"
always_bad_seq = ["bash", "man", "less", "pinfo", "lynx", "export", "nmap", "ruby", "perl"]

leftover = "!\"$\'()*-._{|}"


def global_check(x):
	if not x:
		return False

	temp = x.lower()

	for char in always_bad:
		if char in temp:
			print("[RSHELL]: Restricted Character :::{}:::".format(char))
			return False

	for seq in always_bad_seq:
		if seq in temp:
			print("[RSHELL]: Restricted Command :::{}:::".format(seq))
			return False

	return True



def _generic_check(x, bad_chars, bad_seq):
	if not x:
		return None

	temp = x.lower()

	for char in bad_chars:
		if char in temp:
			print("[RSHELL]: Restricted Character :::{}:::".format(char))
			return None

	for seq in bad_seq:
		if seq in temp:
			print("[RSHELL]: Restricted Command :::{}:::".format(seq))
			return None

	return x



def check_chal1(x):
	bad_seq = ["python"]

	return _generic_check(x, [], bad_seq)


def check_chal2(x):
	bad_chars = '!*|;'
	bad_seq = ["sh", "rm", "vi", "vim", "emacs", "joe", "find", "py"]

	x = _generic_check(x, bad_chars, bad_seq)

	if x and x[0] == "$":
		print("[RSHELL]: Restricted Character :::$:::")
		return None

	return x


def check_chal3(x):
	bad_chars = '!\"$\'()*-._{|};'
	bad_seq = ["sh", "rm", "vi", "vim", "emacs", "joe", "nano", "find"]

	return _generic_check(x, bad_chars, bad_seq)


def check_chal4(x):
	bad_chars = '!\"$\'()*-._{|};'
	bad_seq = ["sh", "rm", "vi", "vim", "emacs", "joe", "py", "find"]

	return _generic_check(x, bad_chars, bad_seq)


def check_chal5(x):
	bad_chars = '!\"$\'()*-._{|};'
	bad_seq = ["sh", "rm", "vi", "vim", "emacs", "joe", "py", "find", "nano"]

	x = _generic_check(x, bad_chars, bad_seq)

	if x and x[0] == "$":
		print("[RSHELL]: Restricted Character :::$:::")
		return None

	return x


def check_chal6(x):
	bad_chars = '!\"$\'()*-._{|};'
	bad_seq = ["sh", "rm", "vim", "emacs", "joe", "py", "find", "nano", "tee"]

	return _generic_check(x, bad_chars, bad_seq)


def check_chal7(x):
	bad_chars = '!\"$\'()-._{|};'
	bad_seq = ["sh", "rm", "emacs", "joe", "py", "find", "nano", "tee"]

	x = _generic_check(x, bad_chars, bad_seq)

	if x:
		if "vi" in x:
			if x.count("vi") != x.count("vim"):
				print("[RSHELL]: Restricted Command :::vi:::")
				return None

		if "vim" in x:
			x = x.replace("vim", "vim -Z")

	return x

def check_chal8(x):
	bad_chars = '!$_.{|}'
	bad_seq = ["sh", "rm", "emacs", "vi", "joe", "find", "nano", "tee", "os", "sys", "open"]

	x = _generic_check(x, bad_chars, bad_seq)

	if x:
		if "python" in x:
			if x.count("python") != x.count("python -c"):
				print("[RSHELL]: Restricted Command :::python -i:::")
				return None

	return x