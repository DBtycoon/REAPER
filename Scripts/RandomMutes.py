from reaper_python import *
from random import randint
ourProject = 0

for track in range(RPR_CountTracks(ourProject)-1, -1, -1):
		theTrack = RPR_GetTrack(ourProject, track)
		solo = randint(0,1)
		solo = True if solo else False
		RPR_SetMediaTrackInfo_Value(theTrack, "B_MUTE", solo)