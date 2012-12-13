from reaper_python import *
ourProject = 0

context = RPR_GetCursorContext()

if context==1:

elif context ==2:

elif context==3:

else:
	RPR_ReaScriptError("Couldn't find cursor")