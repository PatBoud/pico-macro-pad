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
consumer_control = ConsumerControl(usb_hid.devices)


class blank(AbstractMacro):
    def getMacroName():
        return "<blank>"

    def getMacro():
        pass

    def getMacroColor():
        return (0, 0, 0)


# https://colorbrewer2.org/
# https://learn.adafruit.com/fancyled-library-for-circuitpython


# ============================================================================
# ============================================================================
# ============================================================================


class OBS(AbstractConfiguration):
    def getName():
        return "OBS"

    def getColor():
        return (0, 0, 250)

    def getMacros():
        return [
            OBS_Rec, OBS_Pause, OBS_VirtualCam, blank,
            blank, blank, blank, OBS_ZoomIn,
            OBS_SelectScene1, OBS_SelectScene2, OBS_SelectScene5, OBS_ZoomOut,
            OBS_SelectScene3, blank, blank, blank,
        ]


class OBS_Rec(AbstractMacro):
    def getMacroName():
        return "Rec"

    def getMacro():
        keyboard.press(Keycode.F13)
        time.sleep(0.05)
        keyboard.release(Keycode.F13)

    def getMacroColor():
        return (255, 0, 0)


class OBS_Pause(AbstractMacro):
    def getMacroName():
        return "Pause"

    def getMacro():
        keyboard.press(Keycode.F14)
        time.sleep(0.05)
        keyboard.release(Keycode.F14)

    def getMacroColor():
        return (255, 255, 140)


class OBS_VirtualCam(AbstractMacro):
    def getMacroName():
        return "Virtual Camera"

    def getMacro():
        keyboard.press(Keycode.SHIFT, Keycode.F14)
        time.sleep(0.05)
        keyboard.release(Keycode.SHIFT, Keycode.F14)

    def getMacroColor():
        return (100, 0, 255)


class OBS_SelectScene1(AbstractMacro):
    def getMacroName():
        return "Scene 1"

    def getMacro():
        #Fond et logo MUTE
        keyboard.press(Keycode.F15)
        time.sleep(0.05)
        keyboard.release(Keycode.F15)

    def getMacroColor():
        return (0, 255, 255)


class OBS_SelectScene2(AbstractMacro):
    def getMacroName():
        return "Scene 2"

    def getMacro():
        #Webcam avec nom
        keyboard.press(Keycode.F16)
        time.sleep(0.05)
        keyboard.release(Keycode.F16)

    def getMacroColor():
        return (0, 0, 255)


class OBS_SelectScene3(AbstractMacro):
    def getMacroName():
        return "Scene 3"

    def getMacro():
        #Screencast avec pointeur
        keyboard.press(Keycode.F17)
        time.sleep(0.05)
        keyboard.release(Keycode.F17)

    def getMacroColor():
        return (0, 255, 0)


class OBS_SelectScene4(AbstractMacro):
    def getMacroName():
        return "Scene 4"

    def getMacro():
        keyboard.press(Keycode.F18)
        time.sleep(0.05)
        keyboard.release(Keycode.F18)

    def getMacroColor():
        return (255, 255, 0)


class OBS_SelectScene5(AbstractMacro):
    def getMacroName():
        return "Scene 5"

    def getMacro():
        #Webcam Full
        keyboard.press(Keycode.F19)
        time.sleep(0.05)
        keyboard.release(Keycode.F19)

    def getMacroColor():
        return (0, 80, 255)


class OBS_SelectScene6(AbstractMacro):
    def getMacroName():
        return "Scene 6"

    def getMacro():
        pass

    def getMacroColor():
        return (0, 128, 0)


class OBS_ZoomIn(AbstractMacro):
    def getMacroName():
        return "Zoom In"

    def getMacro():
        # Cursor Highlight
        keyboard.send(Keycode.CONTROL, Keycode.SHIFT, Keycode.ALT, Keycode.C)

        # ZoomIt
        keyboard.send(Keycode.CONTROL, Keycode.SHIFT, Keycode.ALT, Keycode.Z)

        # OBS Scene Screencast SANS pointeur
        keyboard.press(Keycode.F18)
        time.sleep(0.05)
        keyboard.release(Keycode.F18)

    def getMacroColor():
        return (255, 120, 0)


class OBS_ZoomOut(AbstractMacro):
    def getMacroName():
        return "Zoom Out"

    def getMacro():
        # ZoomIt
        keyboard.send(Keycode.LEFT_CONTROL, Keycode.LEFT_SHIFT, Keycode.LEFT_ALT, Keycode.Z)

        # Delay for zoom animation
        time.sleep(0.1)

        # Cursor Highlight
        keyboard.send(Keycode.CONTROL, Keycode.SHIFT, Keycode.ALT, Keycode.C)

        # OBS Scene Screencast avec pointeur
        keyboard.press(Keycode.F17)
        time.sleep(0.05)
        keyboard.release(Keycode.F17)

    def getMacroColor():
        return (255, 255, 0)


class OBS_MuteOn(AbstractMacro):
    def getMacroName():
        return "Mute"

    def getMacro():
        pass

    def getMacroColor():
        return (0, 0, 128)


class OBS_MuteOff(AbstractMacro):
    def getMacroName():
        return "Unmute"

    def getMacro():
        pass

    def getMacroColor():
        return (0, 0, 128)


# ============================================================================
# ============================================================================
# ============================================================================

class GarageBand(AbstractConfiguration):
    def getName():
        return "GarageBand"

    def getColor():
        return (255, 255, 0)

    def getMacros():
        return [
        GB_Rew,
        GB_Fwd,
        GB_Begin,
        blank,
        GB_Play,
        GB_Rec,
        GB_Loop,
        ]

class GB_Rew(AbstractMacro):
    def getMacroName():
        return "Rewind"

    def getMacro():
        keyboard.send(Keycode.COMMA)

    def getMacroColor():
        return (0, 255, 255)


class GB_Fwd(AbstractMacro):
    def getMacroName():
        return "Forward"

    def getMacro():
        keyboard.send(Keycode.PERIOD)

    def getMacroColor():
        return (0, 255, 255)


class GB_Begin(AbstractMacro):
    def getMacroName():
        return "Beginning"

    def getMacro():
        keyboard.send(Keycode.KEYPAD_ZERO)

    def getMacroColor():
        return (0, 0, 255)

class GB_Play(AbstractMacro):
    def getMacroName():
        return "Play"

    def getMacro():
        keyboard.send(Keycode.SPACE)

    def getMacroColor():
        return (255, 255, 140)

class GB_Rec(AbstractMacro):
    def getMacroName():
        return "Record"

    def getMacro():
        keyboard.send(Keycode.R)

    def getMacroColor():
        return (255, 0, 0)

class GB_Loop(AbstractMacro):
    def getMacroName():
        return "Loop"

    def getMacro():
        keyboard.send(Keycode.C)

    def getMacroColor():
        return (255, 255, 0)

# ============================================================================
# ============================================================================
# ============================================================================


class Terminal(AbstractConfiguration):
    def getName():
        return "Terminal"

    def getColor():
        return (0, 255, 0)

    def getMacros():
        return [terminal_ls, terminal_pwd, terminal_home]


class terminal_ls(AbstractMacro):
    def getMacroName():
        return "ls -al"

    def getMacro():
        layout.write("ls ")
        keyboard.send(Keycode.KEYPAD_MINUS)
        layout.write("al")
        keyboard.send(Keycode.ENTER)

    def getMacroColor():
        return (0, 200, 0)


class terminal_pwd(AbstractMacro):
    def getMacroName():
        return "pwd"

    def getMacro():
        layout.write("pwd")
        keyboard.send(Keycode.ENTER)

    def getMacroColor():
        return (0, 200, 0)


class terminal_home(AbstractMacro):
    def getMacroName():
        return "Home"

    def getMacro():
        layout.write("cd ")
        keyboard.send(Keycode.ENTER)

    def getMacroColor():
        return (0, 200, 0)


# ============================================================================
# ============================================================================
# ============================================================================


class Git(AbstractConfiguration):
    def getName():
        return "GIT"

    def getColor():
        return (247, 78, 39)

    def getMacros():
        return [
            Git_Status,
            Git_Diff,
            Git_AddCommit
            # MergeDevelop,
            # MergeMaster,
            # GitPush
        ]


class Git_Status(AbstractMacro):
    def getMacroName():
        return "Status"

    def getMacro():
        layout.write("git status")
        keyboard.send(Keycode.ENTER)

    def getMacroColor():
        return (247, 78, 39)


class Git_Diff(AbstractMacro):
    def getMacroName():
        return "Diff"

    def getMacro():
        layout.write("git diff")
        keyboard.send(Keycode.ENTER)

    def getMacroColor():
        return (247, 78, 39)


class Git_AddCommit(AbstractMacro):
    def getMacroName():
        return "Add + Commit"

    def getMacro():
        layout.write("git add .")
        keyboard.send(Keycode.ENTER)
        layout.write("git commit -m ")

    def getMacroColor():
        return (247, 78, 39)


class Git_Push(AbstractMacro):
    def getMacroName():
        return "Push"

    def getMacro():
        layout.write("git push")
        keyboard.send(Keycode.ENTER)

    def getMacroColor():
        return (247, 78, 39)


# ============================================================================#
# ============================================================================#
# ============================================================================#


# Map your configurations inside this array
configurations_map = [OBS, GarageBand, Terminal, Git]
