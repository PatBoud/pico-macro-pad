import usb_hid
import time
import random

from abstract_classes import AbstractConfiguration, AbstractMacro
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode

keyboard = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(keyboard)

## CONFIGURATIONS ##
#===========================================#
# class Terminal(AbstractConfiguration):
# 	def getName():
# 		return 'Terminal'
# 	def getColor():
# 		return (0, 255, 0)
# 	def getMacros():
# 		return [
# 			Ls, 
# 			Pwd,
# 			Home
# 		]

# class Ls(AbstractMacro):
# 	def getMacroName():
# 		return 'ls -al'
# 	def getMacro():
# 		layout.write("ls ")
# 		keyboard.send(Keycode.KEYPAD_MINUS)
# 		layout.write("al")
# 		keyboard.send(Keycode.ENTER)

# class Pwd(AbstractMacro):
# 	def getMacroName():
# 		return 'pwd'
# 	def getMacro():
# 		layout.write("pwd")
# 		keyboard.send(Keycode.ENTER)

# class Home(AbstractMacro):
# 	def getMacroName():
# 		return 'Home'
# 	def getMacro():
# 		layout.write("cd ")
# 		keyboard.send(Keycode.ENTER)
#===========================================#


# class Git(AbstractConfiguration):
# 	def getName():
# 		return 'GIT'
# 	def getColor():
# 		return (247, 78, 39)
# 	def getMacros():
# 		return [
# 			MergeDevelop,
# 			MergeMaster,
# 			GitPush
# 		]

# class MergeDevelop(AbstractMacro):
# 	def getMacroName():
# 		return "Merge develop into master"
# 	def getMacro():
# 		layout.write("git checkout master")
# 		keyboard.send(Keycode.ENTER)
# 		time.sleep(0.5)
# 		layout.write("git merge develop")
# 		keyboard.send(Keycode.ENTER)

# class MergeMaster(AbstractMacro):
# 	def getMacroName():
# 		return "Merge master into develop"
# 	def getMacro():
# 		layout.write("git checkout develop")
# 		keyboard.send(Keycode.ENTER)
# 		time.sleep(0.5)
# 		layout.write("git merge master")
# 		keyboard.send(Keycode.ENTER)

# class GitPush(AbstractMacro):
# 	def getMacroName():
# 		return "Push"
# 	def getMacro():
# 		layout.write("git push")
# 		keyboard.send(Keycode.ENTER)
#===========================================#

group1 = (64,8,8) #red
group2 = (64,32,8) #orange
group3 = (64,64,8) #yellow
group4 = (8,64,8) #green
group5 = (8,8,64) #blue
group6 = (30,8,64) #indigo
group7 = (32,8,64) #violet
group8 = (8,64,64) #teal

consumer_control = ConsumerControl(usb_hid.devices)

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

class blank(AbstractMacro):
    def getMacroName():
        return 'Blank'
    def getMacro():
        pass
    def getMacroColor():
        return (0, 0, 0)

#===========================================#

class Media(AbstractConfiguration):
    def getName():
        return 'Media Controls'
    def getColor():
        return group8
    def getMacros():
        return [
            med_prev,
            med_play,
            med_next,
            med_volUp,
            blank,
            blank,
            blank,
            med_volDown
        ]

class med_prev(AbstractMacro):
    def getMacroName():
        return 'Previous'
    def getMacro():
        consumer_control.send(ConsumerControlCode.SCAN_PREVIOUS_TRACK)
    def getMacroColor():
        return group8

class med_play(AbstractMacro):
    def getMacroName():
        return 'Play/Pause'
    def getMacro():
        consumer_control.send(ConsumerControlCode.PLAY_PAUSE)
    def getMacroColor():
        return group8

class med_next(AbstractMacro):
    def getMacroName():
        return 'Next'
    def getMacro():
        consumer_control.send(ConsumerControlCode.SCAN_NEXT_TRACK)
    def getMacroColor():
        return group8

class med_volUp(AbstractMacro):
    def getMacroName():
        return 'Volume Up'
    def getMacro():
        consumer_control.press(ConsumerControlCode.VOLUME_INCREMENT)
        time.sleep(0.5)
        consumer_control.release()
    def getMacroColor():
        return (group7[0]*.25,group7[1]* .75, group7[2]* 1.25) 

class med_volDown(AbstractMacro):
    def getMacroName():
        return 'Volume Down'
    def getMacro():
        consumer_control.press(ConsumerControlCode.VOLUME_DECREMENT)
        time.sleep(0.5)
        consumer_control.release()
    def getMacroColor():
        return (group7[0]*.25,group7[1]* .75, group7[2]* 1.25) 


#consumer_control.press(ConsumerControlCode.VOLUME_INCREMENT)
#        time.sleep(0.5)
#        consumer_control.release()

## COMMANDS ##

# Map your configurations inside this array
configurations_map = [Navigation, Media] #[Git, Navigation, Terminal] #, GoogleMeet, Obsidian, RandomEstimation, PhpStorm ]	

#=======================================================================
#disabled configurations
#=======================================================================

# class GoogleMeet(AbstractConfiguration):
# 	def getName():
# 		return 'Google Meet'
# 	def getColor():
# 		return (255, 128, 0)
# 	def getMacros():
# 		return [
# 			ToggleMicrophone, 
# 			ToggleWebcam
# 		]

# class OBS(AbstractConfiguration):
# 	def getName():
# 		return 'OBS'
# 	def getColor():
# 		return (0, 0, 255)
# 	def getMacros():
# 		return [
# 			SelectScene1, 
# 			SelectScene2,
# 			SelectScene3,
# 			MuteOn,
# 			MuteOff
# 		]

# class Obsidian(AbstractConfiguration):
# 	def getName():
# 		return 'Obsidian'
# 	def getColor():
# 		return (51, 51, 255)
# 	def getMacros():
# 		return [
# 			AddNewLog
# 		]

# class RandomEstimation(AbstractConfiguration):
# 	def getName():
# 		return 'Random Esteem'
# 	def getColor():
# 		return (255, 0, 0)
# 	def getMacros():
# 		return [
# 			OneWeekEsteem, 
# 			OneMonthEsteem,
# 			SixMonthsEsteem
# 		]

# class PhpStorm(AbstractConfiguration):
# 	def getName():
# 		return 'PHPStorm'
# 	def getColor():
# 		return (232, 49, 123)
# 	def getMacros():
# 		return [
# 			OpenInTerminal,
# 			Rename,
# 			ComposerAutoload,
# 			ListenForDebug,
# 			StepOver,
# 			StepInto,
# 			StepOut,
# 			NextBreakpoint
# 		]

#=======================================================================
#disabled macros
#=======================================================================

# class OpenInTerminal(AbstractMacro):
# 	def getMacroName():
# 		return 'Open in terminal'
# 	def getMacro():
# 		keyboard.send(Keycode.ALT, Keycode.T)

# class Rename(AbstractMacro):
# 	def getMacroName():
# 		return 'Rename'
# 	def getMacro():
# 		keyboard.send(Keycode.SHIFT, Keycode.F6)

# class ListenForDebug(AbstractMacro):
# 	def getMacroName():
# 		return 'Listen for debug'
# 	def getMacro():
# 		keyboard.send(Keycode.ALT, Keycode.D)

# class StepOver(AbstractMacro):
# 	def getMacroName():
# 		return 'Step over'
# 	def getMacro():
# 		keyboard.send(Keycode.F8)

# class StepInto(AbstractMacro):
# 	def getMacroName():
# 		return 'Step into'
# 	def getMacro():
# 		keyboard.send(Keycode.F7)

# class StepOut(AbstractMacro):
# 	def getMacroName():
# 		return 'Step out'
# 	def getMacro():
# 		keyboard.send(Keycode.SHIFT, Keycode.F8)

# class NextBreakpoint(AbstractMacro):
# 	def getMacroName():
# 		return 'Next breakpoint'
# 	def getMacro():
# 		keyboard.send(Keycode.ALT, Keycode.COMMAND, Keycode.R)

# class ComposerAutoload(AbstractMacro):
# 	def getMacroName():
# 		return 'Composer autoload'
# 	def getMacro():
# 		layout.write('composer dump')
# 		keyboard.send(Keycode.KEYPAD_MINUS)
# 		layout.write('autoload')
# 		keyboard.send(Keycode.ENTER)

# class OneWeekEsteem(AbstractMacro):
# 	def getMacroName():
# 		return '< 1 week'
# 	def getMacro():
# 		layout.write(str(random.randint(1, 5)))
# 		keyboard.send(Keycode.ENTER)

# class OneMonthEsteem(AbstractMacro):
# 	def getMacroName():
# 		return '< 1 month'
# 	def getMacro():
# 		layout.write(str(random.randint(5, 20)))
# 		keyboard.send(Keycode.ENTER)

# class SixMonthsEsteem(AbstractMacro):
# 	def getMacroName():
# 		return '< 6 months'
# 	def getMacro():
# 		layout.write(str(random.randint(20, 120)))
# 		keyboard.send(Keycode.ENTER)
# class ToggleMicrophone(AbstractMacro):
# 	def getMacroName():
# 		return 'Toggle Microphone'
# 	def getMacro():
# 		keyboard.send(Keycode.COMMAND, Keycode.D)

# class ToggleWebcam(AbstractMacro):
# 	def getMacroName():
# 		return 'Toggle Webcam'
# 	def getMacro():
# 		keyboard.send(Keycode.COMMAND, Keycode.E)

# class SelectScene1(AbstractMacro):
# 	def getMacroName():
# 		return 'Scene 1'
# 	def getMacro():
# 		keyboard.send(Keycode.LEFT_ALT, Keycode.ONE)

# class SelectScene2(AbstractMacro):
# 	def getMacroName():
# 		return 'Scene 2'
# 	def getMacro():
# 		keyboard.send(Keycode.LEFT_ALT, Keycode.TWO)

# class SelectScene3(AbstractMacro):
# 	def getMacroName():
# 		return 'Scene 3'
# 	def getMacro():
# 		keyboard.send(Keycode.LEFT_ALT, Keycode.THREE)

# class MuteOn(AbstractMacro):
# 	def getMacroName():
# 		return 'Mute'
# 	def getMacro():
# 		keyboard.send(Keycode.LEFT_ALT, Keycode.FOUR)

# class MuteOff(AbstractMacro):
# 	def getMacroName():
# 		return 'Unmute'
# 	def getMacro():
# 		keyboard.send(Keycode.LEFT_ALT, Keycode.FIVE)

# class AddNewLog(AbstractMacro):
# 	def getMacroName():
# 		return 'New Log'
# 	def getMacro():
# 		keyboard.send(Keycode.COMMAND, Keycode.P)
# 		layout.write("Insert template")
# 		time.sleep(0.1)
# 		keyboard.send(Keycode.ENTER)
# 		layout.write("New log")
# 		time.sleep(0.1)
# 		keyboard.send(Keycode.ENTER)