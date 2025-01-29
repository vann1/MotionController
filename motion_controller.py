class MotionController:
    #... basic structure inside MotionController
    def init():
        # basic servo configuration (limits, speeds, etc.)
        # basic Tritex connection stuff
        # connect to Tritex
        # start safety watchdog (extra feature)
        pass

    def start():
        # enable control
        pass

    def __watchdog():
        # extra safety feature
        # checks if connection to Tritex is still alive
        # checks if servos are still moving and within limits
        # sets stop flag if something is wrong
        pass

    def read():
        # get servo data from Tritex, forward to user (main.py)
        # this is a bonus but prob easy to add
        return servo_data

    def write(pitch, roll):
        # checks if input data is valid (within limits, data type, etc.)
        # convert pitch/roll to servo positions
        # send servo positions to Tritex
        pass

    def stop():
        # stop actions safely by disabling control (servos can still hold position but NOT move)
        # keep connection to Tritex open (no need to re-initialize servos)
        pass

    def quit():
        # stop all actions safely
        # disconnect from Tritex (user needs to call "init" again to reconnect)
        # resets servo positions to home (sloWly!)
        # stops safety watchdog
        pass    