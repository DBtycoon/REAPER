from reaper_python import *

ourProject = 0
context = RPR_GetCursorContext()

if context == 1:
	pass
elif context == 2:
	pass
elif context == 3:
	pass
else:
	RPR_ReaScriptError("Couldn't find cursor")