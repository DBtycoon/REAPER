from reaper_python import *
ourProject = 0

tr = RPR_GetTrack(0,2)
(ok, tr, vol, pan) = RPR_GetTrackUIVolPan(tr, 0, 0)
RPR_SetMediaTrackInfo_Value(tr, "D_VOL", vol*0.5)