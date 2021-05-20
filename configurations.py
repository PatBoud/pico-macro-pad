import usb_hid
import time

from abstract_classes import AbstractConfiguration, AbstractMacro
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode

keyboard = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(keyboard)

group1 = (64,8,8) #red
group2 = (64,32,8) #orange
group3 = (64,64,8) #yellow
group4 = (8,64,8) #green
group5 = (8,8,64) #blue
group6 = (30,8,64) #indigo
group7 = (32,8,64) #violet
group8 = (8,64,64) #teal

color_obs = (0, 0, 200)
color_git = (247,78,39)


consumer_control = ConsumerControl(usb_hid.devices)

class blank(AbstractMacro):
    def getMacroName():
        return '<blank>'
    def getMacro():
        pass
    def getMacroColor():
        return (0, 0, 0)


# https://colorbrewer2.org/
# https://learn.adafruit.com/fancyled-library-for-circuitpython
  
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


class Terminal(AbstractConfiguration):
	def getName():
		return 'Terminal'
	def getColor():
		return group4
	def getMacros():
		return [
			terminal_ls, 
			terminal_pwd,
			terminal_home
		]

class terminal_ls(AbstractMacro):
	def getMacroName():
		return 'ls -al'
	def getMacro():
		layout.write("ls ")
		keyboard.send(Keycode.KEYPAD_MINUS)
		layout.write("al")
		keyboard.send(Keycode.ENTER)
	def getMacroColor():
		return (group4[0]*.25,group4[1]* .75, group4[2]* 1.25) 

class terminal_pwd(AbstractMacro):
	def getMacroName():
		return 'pwd'
	def getMacro():
		layout.write("pwd")
		keyboard.send(Keycode.ENTER)
	def getMacroColor():
		return (group4[0]*.25,group4[1]* .75, group4[2]* 1.25) 

class terminal_home(AbstractMacro):
	def getMacroName():
		return 'Home'
	def getMacro():
		layout.write("cd ")
		keyboard.send(Keycode.ENTER)
	def getMacroColor():
		return (group4[0]*.25,group4[1]* .75, group4[2]* 1.25) 


#============================================================================#
#============================================================================#
#============================================================================#

class OBS(AbstractConfiguration):
	def getName():
		return 'OBS'
	def getColor():
		return color_obs
	def getMacros():
		return [
			OBS_Rec,
			OBS_Pause,
			blank,
			blank,
			OBS_SelectScene1,
			OBS_SelectScene2,
			blank,
			OBS_ZoomIn,
			OBS_SelectScene3,
			OBS_SelectScene4,
			blank,
			OBS_ZoomOut,
			OBS_SelectScene5,
			OBS_SelectScene6
		]

class OBS_Rec(AbstractMacro):
	def getMacroName():
		return 'OBS - Rec'
	def getMacro():
		pass
		# keyboard.send(Keycode.LEFT_ALT, Keycode.ONE)
	def getMacroColor():
		return (128, 0, 0) 

class OBS_Pause(AbstractMacro):
	def getMacroName():
		return 'OBS - Pause'
	def getMacro():
		pass
		# keyboard.send(Keycode.LEFT_ALT, Keycode.ONE)
	def getMacroColor():
		return (128, 128, 128) 


class OBS_SelectScene1(AbstractMacro):
	def getMacroName():
		return 'Scene 1'
	def getMacro():
		pass
	def getMacroColor():
		return (0, 0, 200)

class OBS_SelectScene2(AbstractMacro):
	def getMacroName():
		return 'Scene 2'
	def getMacro():
		pass
	def getMacroColor():
		return (0, 0, 200)

class OBS_SelectScene3(AbstractMacro):
	def getMacroName():
		return 'Scene 3'
	def getMacro():
		pass
		#keyboard.send(Keycode.LEFT_ALT, Keycode.THREE)
	def getMacroColor():
		return (0, 128, 0)

class OBS_SelectScene4(AbstractMacro):
	def getMacroName():
		return 'Scene 4'
	def getMacro():
		pass
		#keyboard.send(Keycode.LEFT_ALT, Keycode.THREE)
	def getMacroColor():
		return (0, 128, 0)

class OBS_SelectScene5(AbstractMacro):
	def getMacroName():
		return 'Scene 5'
	def getMacro():
		pass
	def getMacroColor():
		return (0, 128, 0)

class OBS_SelectScene6(AbstractMacro):
	def getMacroName():
		return 'Scene 6'
	def getMacro():
		pass
	def getMacroColor():
		return (0, 128, 0)

class OBS_ZoomIn(AbstractMacro):
	def getMacroName():
		return 'Zoom In'
	def getMacro():
		pass
	def getMacroColor():
		return (128, 0, 64)

class OBS_ZoomOut(AbstractMacro):
	def getMacroName():
		return 'Zoom Out'
	def getMacro():
		pass
	def getMacroColor():
		return (128, 64, 64)

class OBS_SelectScene4(AbstractMacro):
	def getMacroName():
		return 'Scene 4'
	def getMacro():
		pass
	def getMacroColor():
		return (0, 128, 0)

class OBS_MuteOn(AbstractMacro):
	def getMacroName():
		return 'Mute'
	def getMacro():
		keyboard.send(Keycode.LEFT_ALT, Keycode.FOUR)
	def getMacroColor():
		return (group5[0]*.25,group5[1]* .75, group5[2]* 1.25) 

class OBS_MuteOff(AbstractMacro):
	def getMacroName():
		return 'Unmute'
	def getMacro():
		keyboard.send(Keycode.LEFT_ALT, Keycode.FIVE)
	def getMacroColor():
		return (group5[0]*.25,group5[1]* .75, group5[2]* 1.25) 


#============================================================================#
#============================================================================#
#============================================================================#

class Git(AbstractConfiguration):
	def getName():
		return 'GIT'
	def getColor():
		return color_git
	def getMacros():
		return [
			Git_Status,
			Git_Diff,
			Git_AddCommit
			#MergeDevelop,
			#MergeMaster,
			#GitPush
		]

class Git_Status(AbstractMacro):
	def getMacroName():
		return "Git status"
	def getMacro():
		layout.write("git status")
		keyboard.send(Keycode.ENTER)
	def getMacroColor():
		return (color_git[0]*.75,color_git[1]* .75, color_git[2]* 1.25) 

class Git_Diff(AbstractMacro):
	def getMacroName():
		return "Git diff"
	def getMacro():
		layout.write("git diff")
		keyboard.send(Keycode.ENTER)
	def getMacroColor():
		return (color_git[0]*.25,color_git[1]* .75, color_git[2]* 1.25) 

class Git_AddCommit(AbstractMacro):
	def getMacroName():
		return "Git Add + Commit"
	def getMacro():
		layout.write("git add .")
		keyboard.send(Keycode.ENTER)
		layout.write("git commit -m ")
	def getMacroColor():
		return (color_git[0]*1.25,color_git[1]* .75, color_git[2]* 1.25) 

class Git_Push(AbstractMacro):
	def getMacroName():
		return "Push"
	def getMacro():
		layout.write("git push")
		keyboard.send(Keycode.ENTER)

#============================================================================#
#============================================================================#
#============================================================================#


# Map your configurations inside this array
configurations_map = [OBS, Terminal, Git, Media]