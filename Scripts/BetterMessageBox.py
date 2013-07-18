from reaper_python import *

'''
Possible Questions:
0 = Ok
1 = Ok Cancel
2 = Abort Retry Ignore
3 = Yes No Cancel
4 = Yes No
5 = Retry Cancel
'''
def Ok(title, comment):
	return RPR_MB(comment, title, 0)

def OkCancel(title, comment):
	return RPR_MB(comment, title, 1)

def AbortRetryIgnore(title, comment):
	return RPR_MB(comment, title, 2)

def YesNoCancel(title, comment):
	return RPR_MB(comment, title, 3)

def YesNo(title, comment):
	return RPR_MB(comment, title, 4)

def RetryCancel(title, comment):
	return RPR_MB(comment, title, 5)

'''
o = Ok
oc = Ok Cancel
arc = Abort Retry Cancel
ync = Yes No Cancel
yn = Yes No
rc = Retry Cancel
'''
def MB(title, comment, choice):
	if choice.lower() == "o":
		return Ok(title, comment)
	elif choice.lower() == "oc":
		return OkCancel(title, comment)
	elif choice.lower() == "arc":
		return AbortRetryIgnore(title, comment)
	elif choice.lower() == "ync":
		return YesNoCancel(title, comment)
	elif choice.lower() == "yn":
		return YesNo(title, comment)
	elif choice.lower() == "rc":
		return RetryCancel(title, comment)
	else:
		RPR_ReaScriptError("Not a valid message box type")
