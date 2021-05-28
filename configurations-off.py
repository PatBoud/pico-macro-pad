#============================================================================#
#============================================================================#
#============================================================================#

class Navigation(AbstractConfiguration):
    def getName():
        return 'Navigation'
    def getColor():
        return group1
    def getMacros():
        return [
            nav_home,
            nav_up,
            nav_end,
            nav_pageUp,
            nav_left,
            nav_down,
            nav_right,
            nav_pageDn,
            blank,
            blank,
            blank,
            blank,
            nav_cut,
            nav_copy,
            nav_paste
        ]

class nav_home(AbstractMacro):
    def getMacroName():
        return 'Home'
    def getMacro():
        keyboard.send(Keycode.HOME)
    def getMacroColor():
        return group2

class nav_up(AbstractMacro):
    def getMacroName():
        return 'Up'
    def getMacro():
        keyboard.send(Keycode.UP_ARROW)
    def getMacroColor():
        return group1

class nav_end(AbstractMacro):
    def getMacroName():
        return 'End'
    def getMacro():
        keyboard.send(Keycode.END)
    def getMacroColor():
        return group2

class nav_pageUp(AbstractMacro):
    def getMacroName():
        return 'Page Up'
    def getMacro():
        keyboard.send(Keycode.PAGE_UP)
    def getMacroColor():
        return group6

class nav_left(AbstractMacro):
    def getMacroName():
        return 'Left'
    def getMacro():
        keyboard.send(Keycode.LEFT_ARROW)
    def getMacroColor():
        return group1

class nav_down(AbstractMacro):
    def getMacroName():
        return 'Down'
    def getMacro():
        keyboard.send(Keycode.DOWN_ARROW)
    def getMacroColor():
        return group1

class nav_right(AbstractMacro):
    def getMacroName():
        return 'Right'
    def getMacro():
        keyboard.send(Keycode.RIGHT_ARROW)
    def getMacroColor():
        return group1

class nav_pageDn(AbstractMacro):
    def getMacroName():
        return 'Page Down'
    def getMacro():
        keyboard.send(Keycode.PAGE_DOWN)
    def getMacroColor():
        return group6

class nav_cut(AbstractMacro):
    def getMacroName():
        return 'cut'
    def getMacro():
        keyboard.send(Keycode.LEFT_CONTROL,Keycode.X)
    def getMacroColor():
        return group7

class nav_copy(AbstractMacro):
    def getMacroName():
        return 'Copy'
    def getMacro():
        keyboard.send(Keycode.LEFT_CONTROL,Keycode.C)
    def getMacroColor():
        return group7

class nav_paste(AbstractMacro):
    def getMacroName():
        return 'Paste'
    def getMacro():
        keyboard.send(Keycode.LEFT_CONTROL,Keycode.V)
    def getMacroColor():
        return group7

#============================================================================#
#============================================================================#
#============================================================================#

class Media(AbstractConfiguration):
    def getName():
        return 'Media Controls'
    def getColor():
        return group8
    def getMacros():
        return [
            media_prev,
            media_play,
            media_next,
            media_volUp,
            blank,
            blank,
            blank,
            media_volDown
        ]

class media_prev(AbstractMacro):
    def getMacroName():
        return 'Previous'
    def getMacro():
        consumer_control.send(ConsumerControlCode.SCAN_PREVIOUS_TRACK)
    def getMacroColor():
        return group8

class media_play(AbstractMacro):
    def getMacroName():
        return 'Play/Pause'
    def getMacro():
        consumer_control.send(ConsumerControlCode.PLAY_PAUSE)
    def getMacroColor():
        return group8

class media_next(AbstractMacro):
    def getMacroName():
        return 'Next'
    def getMacro():
        consumer_control.send(ConsumerControlCode.SCAN_NEXT_TRACK)
    def getMacroColor():
        return group8

class media_volUp(AbstractMacro):
    def getMacroName():
        return 'Volume Up'
    def getMacro():
        consumer_control.press(ConsumerControlCode.VOLUME_INCREMENT)
        time.sleep(0.5)
        consumer_control.release()
    def getMacroColor():
        return (group7[0]*.25,group7[1]* .75, group7[2]* 1.25)

class media_volDown(AbstractMacro):
    def getMacroName():
        return 'Volume Down'
    def getMacro():
        consumer_control.press(ConsumerControlCode.VOLUME_DECREMENT)
        time.sleep(0.5)
        consumer_control.release()
    def getMacroColor():
        return (group7[0]*.25,group7[1]* .75, group7[2]* 1.25)


#============================================================================#
#============================================================================#
#============================================================================#
