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
# test_tc = "11234324"


input_str = test_tc

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


# Cleanup timecode:
# remove colons, pad with zeros
# str clean_tc(str input_str)
def clean_tc(input_str):
    # timecode string as list
    input_list = list(input_str)
    clean_tc = ""

    while bool(input_list):
        last_item = input_list.pop()
        print("Last item: " + last_item)

        for item in ("frames", "seconds", "minutes", "hours"):
            print("The item: " + item)
            item = list("00")
            for digit in range (-1, -2):
                print("The digit: " + digit)
                if last_item == ":":
                    break
                else:
                    clean_tc = last_item + clean_tc
            # print("building clean tc: " + clean_tc)

clean_tc(input_str)

# Timecode string to dict, slice 2 from the end

inputTC['frames'] = int(input_str[-2:])
input_str = input_str[:-2]
inputTC['seconds'] = int(input_str[-2:])
input_str = input_str[:-2]
inputTC['minutes'] = int(input_str[-2:])
input_str = input_str[:-2]
inputTC['hours'] = int(input_str[-2:])
input_str = input_str[:-2]



#### TESTS

# TC to Frames
myTC2frames = tc2frames(inputTC, fps)
print("myTC to Frames: " + str(myTC2frames))

# Frames to TC
frames2tc(myTC2frames, fps)
print("    Back to TC: " + str(frames2tc(myTC2frames, fps)))


#### trying OOP

class TimeCode():
    def __init__(self, fps, hours, minutes, seconds, frames):
        """Initialize TimeCode"""
        self.fps = fps
        self.hours = list(str(hours))
        self.minutes = list(str(minutes))
        self.seconds = list(str(seconds))
        self.frames = list(str(frames))

    def return_absolute_frames(self):

        fra = int(''.join(str(each) for each in self.frames))
        sec = int(''.join(str(each) for each in self.seconds))
        min = int(''.join(str(each) for each in self.minutes))
        hrs = int(''.join(str(each) for each in self.hours))

        frames = fra
        frames += sec * self.fps
        frames += min * self.fps * 60
        frames += hrs * self.fps * 60 * 60

        return frames

    def return_tc_string(self):

        return ':'.join([self.hours, self.minutes, self.seconds, self.frames])

    def set_absolute_frames(self, absolute_frames):
        # framesTC = frames % fps
        # secondsTC = frames // fps % 60
        # minutesTC = frames // fps // 60 % 60
        # hoursTC = frames // fps // 60 // 60

        self.frames = str(absolute_frames % self.fps).zfill(2)
        self.seconds = str(absolute_frames // self.fps % 60).zfill(2)
        self.minutes = str(absolute_frames // self.fps // 60 % 60).zfill(2)
        self.hours = str(absolute_frames // self.fps // 60 // 60).zfill(2)

my_tc_25 = TimeCode(25, "01", 00, 00, 10)
my_tc_24 = TimeCode(24, 0, 0, 0, 0)

my_tc_25.set_absolute_frames(90000)

my_tc_24.set_absolute_frames(my_tc_25.return_absolute_frames())

print(my_tc_25.return_absolute_frames())

print(my_tc_25.return_tc_string() + " @ " + str(my_tc_25.fps) + "fps")
print(my_tc_24.return_tc_string() + " @ " + str(my_tc_24.fps) + "fps")