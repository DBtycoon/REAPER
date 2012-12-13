from reaper_python import *
ourProject = 0

for track in range(RPR_CountSelectedTracks(ourProject)-1, -1, -1):
		theTrack = RPR_GetSelectedTrack(ourProject, track)
		RPR_SetMediaTrackInfo_Value(theTrack, "I_RECARM", 1)

RPR_CSurf_OnRecord()