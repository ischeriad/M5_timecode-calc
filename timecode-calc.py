# TODO: parse different input

# 11:23:43:24
# 1:::12 -> 01:00:00:12
# 10:5:10: -> 10:05:10:00

# TODO: handle more frame rates

# 25, 50
# 30, 60, 29.97 (30/1001), 59.95 (60/1001)
# 24, 23.98 (24/1001)


###############
#### SETUP ####
###############

fps = 25
inputTC = {
    'hours': '00',
    'minutes': '00',
    'seconds': '00',
    'frames': '00'
}

# TODO: learn how to use unit tests

## Testcases

test_tc = "09592924"
# test_tc = "10000000"
test_tc = "01010101"
test_tc = "11234324"


###################
#### FUNCTIONS ####
###################

# Timecode to Frames
# int tc2frames(dict tc, int fps)
def tc2frames(tc, fps):
    frames = tc['frames']
    frames += tc['seconds'] * fps
    frames += tc['minutes'] * fps * 60
    frames += tc['hours'] * fps * 60 * 60

    return frames


# Frames to Timecode
# str frames2tc(int frames, int fps)
def frames2tc(frames, fps):
    framesTC    = frames % fps
    secondsTC   = frames // fps % 60
    minutesTC   = frames // fps // 60 % 60
    hoursTC     = frames // fps // 60 // 60

    return str(hoursTC).zfill(2) + ":" + str(minutesTC).zfill(2) + ":" + str(secondsTC).zfill(2) + ":" +str(framesTC).zfill(2)


# Timecode string to dict, slice 2 from the end

inputTC['frames'] = int(test_tc[-2:])
test_tc = test_tc[:-2]
inputTC['seconds'] = int(test_tc[-2:])
test_tc = test_tc[:-2]
inputTC['minutes'] = int(test_tc[-2:])
test_tc = test_tc[:-2]
inputTC['hours'] = int(test_tc[-2:])
test_tc = test_tc[:-2]


#### TESTS

# TC to Frames
myTC2frames = tc2frames(inputTC, fps)
print("myTC to Frames: " + str(myTC2frames))

# Frames to TC
frames2tc(myTC2frames, fps)
print("    Back to TC: " + str(frames2tc(myTC2frames, fps)))
