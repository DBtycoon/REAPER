from reaper_python import *
ourProject = 0
  

if RPR_GetPlayState()==1:
	RPR_OnPauseButton()
elif RPR_GetPlayState()==2:
	RPR_OnPlayButton()
else:
	RPR_OnStopButton()
