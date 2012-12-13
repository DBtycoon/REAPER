from reaper_python import *

def Stop():
	RPR_OnStopButton()

def Pause():
	RPR_OnPauseButton()

def Play():
	RPR_OnPlayButton()

def Record():
	RPR_CSurf_OnRecord()

def Beginning():
	RPR_CSurf_GoStart()

def End():
	RPR_CSurf_GoEnd()

def Forward(time):
	RPR_CSurf_OnFwd(time)

def Rewind(time):
	RPR_CSurf_OnRew(time)