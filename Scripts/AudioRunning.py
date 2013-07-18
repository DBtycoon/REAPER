from reaper_python import *

ourProject = 0

if RPR_Audio_IsRunning():
  RPR_OnStopButton()