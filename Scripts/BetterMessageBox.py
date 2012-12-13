from reaper_python import *
'''
Possible Questions:
0 = Ok
1 = Ok Cancel
2 = Abort Retry Ignore
3 = Yes No Cancel
4 = Yes NO
5 = Retry Cancel
'''
def Ok(title, comment):
	RPR_MB(comment, title, 0)

def OkCancel(title, comment):
	RPR_MB(comment, title, 1)

def AbortRetryIgnore(title, comment):
	RPR_MB(comment, title, 2)

def YesNoCancel(title, comment):
	RPR_MB(comment, title, 3)

def YesNo(title, comment):
	RPR_MB(comment, title, 4)

def RetryCancel(title, comment):
	RPR_MB(comment, title, 5)

'''
o = Ok
oc = Ok Cancel
ari = Abort Retry Cancel
ync = Yes No Cancel
yn = Yes No
rc = Retry Cancel
'''
def MB(title, comment, choice):
	if choice.lower() == "o":
		Ok(title, comment)
	elif choice.lower() == "oc":
		OkCancel(title, comment)
	elif choice.lower() == "ari":
		AbortRetryIgnore(title, comment)
	elif choice.lower() == "ync":
		YesNoCancel(title, comment)
	elif choic.lower() == "yn":
		YesNo(title, comment)
	elif choice.lower() == "rc":
		RetryCancel(title, comment)
	else:
		RPR_ReaScriptError("Not a valid message box type")