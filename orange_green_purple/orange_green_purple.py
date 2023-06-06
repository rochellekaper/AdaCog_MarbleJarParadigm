#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.5),
    on Tue Jun  6 10:45:10 2023
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

import psychopy
psychopy.useVersion('2022.2.5')


# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# Run 'Before Experiment' code from check_task_3
import random


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.5'
expName = 'orange_green_purple'  # from the Builder filename that created this script
expInfo = {
    'anonymous_participant_id': '',
    'group': '',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/rochellekaper/Desktop/Both_Tasks/orange_green_purple/orange_green_purple.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1470, 956], fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}
ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='ptb')

# --- Initialize components for Routine "practice_JarSelection1" ---
jar1_3 = visual.ImageStim(
    win=win,
    name='jar1_3', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-0.25, -0.05), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
text_2 = visual.TextStim(win=win, name='text_2',
    text='JAR SELECTION TASK\nChoose a jar of marbles \n\nJar 1: Press F Key              \nJar 2: Press J Key ',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_practice_JarSelection = keyboard.Keyboard()
jar2_3 = visual.ImageStim(
    win=win,
    name='jar2_3', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0.45, -0.05), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
MarbleValues_3 = visual.ImageStim(
    win=win,
    name='MarbleValues_3', 
    image=valuepath , mask=None, anchor='center',
    ori=0.0, pos=(0, 0.35), size=(0.525, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "practice_JarSelection1" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
jar1_3.setImage(practice_Jar1)
key_resp_practice_JarSelection.keys = []
key_resp_practice_JarSelection.rt = []
_key_resp_practice_JarSelection_allKeys = []
jar2_3.setImage(practice_Jar2)
# keep track of which components have finished
practice_JarSelection1Components = [jar1_3, text_2, key_resp_practice_JarSelection, jar2_3, MarbleValues_3]
for thisComponent in practice_JarSelection1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "practice_JarSelection1" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *jar1_3* updates
    if jar1_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        jar1_3.frameNStart = frameN  # exact frame index
        jar1_3.tStart = t  # local t and not account for scr refresh
        jar1_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(jar1_3, 'tStartRefresh')  # time at next scr refresh
        jar1_3.setAutoDraw(True)
    if jar1_3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > jar1_3.tStartRefresh + 1.5-frameTolerance:
            # keep track of stop time/frame for later
            jar1_3.tStop = t  # not accounting for scr refresh
            jar1_3.frameNStop = frameN  # exact frame index
            jar1_3.setAutoDraw(False)
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_2.started')
        text_2.setAutoDraw(True)
    
    # *key_resp_practice_JarSelection* updates
    waitOnFlip = False
    if key_resp_practice_JarSelection.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_practice_JarSelection.frameNStart = frameN  # exact frame index
        key_resp_practice_JarSelection.tStart = t  # local t and not account for scr refresh
        key_resp_practice_JarSelection.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_practice_JarSelection, 'tStartRefresh')  # time at next scr refresh
        key_resp_practice_JarSelection.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_practice_JarSelection.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_practice_JarSelection.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_practice_JarSelection.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_practice_JarSelection.getKeys(keyList=['f', 'j'], waitRelease=False)
        _key_resp_practice_JarSelection_allKeys.extend(theseKeys)
        if len(_key_resp_practice_JarSelection_allKeys):
            key_resp_practice_JarSelection.keys = _key_resp_practice_JarSelection_allKeys[-1].name  # just the last key pressed
            key_resp_practice_JarSelection.rt = _key_resp_practice_JarSelection_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *jar2_3* updates
    if jar2_3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        jar2_3.frameNStart = frameN  # exact frame index
        jar2_3.tStart = t  # local t and not account for scr refresh
        jar2_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(jar2_3, 'tStartRefresh')  # time at next scr refresh
        jar2_3.setAutoDraw(True)
    if jar2_3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > jar2_3.tStartRefresh + 1.5-frameTolerance:
            # keep track of stop time/frame for later
            jar2_3.tStop = t  # not accounting for scr refresh
            jar2_3.frameNStop = frameN  # exact frame index
            jar2_3.setAutoDraw(False)
    
    # *MarbleValues_3* updates
    if MarbleValues_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        MarbleValues_3.frameNStart = frameN  # exact frame index
        MarbleValues_3.tStart = t  # local t and not account for scr refresh
        MarbleValues_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(MarbleValues_3, 'tStartRefresh')  # time at next scr refresh
        MarbleValues_3.setAutoDraw(True)
    if MarbleValues_3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > MarbleValues_3.tStartRefresh + 1.5-frameTolerance:
            # keep track of stop time/frame for later
            MarbleValues_3.tStop = t  # not accounting for scr refresh
            MarbleValues_3.frameNStop = frameN  # exact frame index
            MarbleValues_3.setAutoDraw(False)
    # Run 'Each Frame' code from check_task_3
    if practice_task != "practice_JarSelection":
        marble_color = -1
        marble_points = 0
        continueRoutine = False
    # Run 'Each Frame' code from keyresponse_time_3
    threshold = 6 #number of seconds allowed
    key_resp_practice_JarSelection.frameNStart = frameN  # exact frame index
    key_resp_practice_JarSelection.tStart = t  # local t and not account for scr refresh
    if t > threshold:
        marble_color = 0
        continueRoutine = False
        
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in practice_JarSelection1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "practice_JarSelection1" ---
for thisComponent in practice_JarSelection1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_practice_JarSelection.keys in ['', [], None]:  # No response was made
    key_resp_practice_JarSelection.keys = None
thisExp.addData('key_resp_practice_JarSelection.keys',key_resp_practice_JarSelection.keys)
if key_resp_practice_JarSelection.keys != None:  # we had a response
    thisExp.addData('key_resp_practice_JarSelection.rt', key_resp_practice_JarSelection.rt)
thisExp.nextEntry()
# the Routine "practice_JarSelection1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
