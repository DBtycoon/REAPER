from reaper_python import *
from Answer import *
import BetterMessageBox as BMB

#Ok
answer0 = BMB.MB("This is the title", "This is the message", "o")
assert answer0==Ok

#Ok, Cancel
BMB.MB("T", "M", "oc")

#Abort, Retry, Ignore
BMB.MB("Sending Error", "Trouble finding server", "ari")

#Yes, No, Cancel
answer1 = BMB.MB("Forgotten component", "Do you want to include the tempo with your action?", "ync")
if answer1 == Ok:
  pass
elif answer1 == No:
  pass
else:
  pass

#Yes, No
BMB.MB("Dat drop", "did you remember to include a drop?", "yn")

#Retry, Cancel
answer2 = BMB.MB("Couldn't change envelope", "Try again?", "rc")
if answer2 == Retry:
  BMB.MB("Couldn't change envelope", "Try again?", "rc")
else:
  print("Cancel") 