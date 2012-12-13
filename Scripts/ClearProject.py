from reaper_python import *
ourProject = 0

answer = RPR_MB("Do you want to start over?", "Clear Project", 4)

if answer==6:
	for track in range(RPR_CountTracks(ourProject)-1, -1, -1):
		#RPR_ShowConsoleMsg(str(track) + "\n")
		RPR_DeleteTrack(RPR_GetTrack(ourProject, track))