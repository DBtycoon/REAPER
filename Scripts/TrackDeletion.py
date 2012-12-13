from reaper_python import *
ourProject = 0

answer = RPR_MB("Delete Track(s)", "Do you want to delete these tracks?", 4) # 4 = yes or no

if answer == 6: # 6=yes
	for track in range(RPR_CountSelectedTracks(ourProject)-1, -1, -1):
		RPR_DeleteTrack(RPR_GetSelectedTrack(ourProject, track))