#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.5),
    on Thu Feb  2 20:28:58 2023
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



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.5'
expName = 'Change Decision Task'  # from the Builder filename that created this script
expInfo = {
    'participant_num': '',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s' % (expInfo['participant_num'], 'group1_')

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/rochellekaper/Desktop/AdaCog/Change Decision Task/Change Detection Task.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
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

# --- Initialize components for Routine "Instructions" ---
initial_instructions = visual.TextStim(win=win, name='initial_instructions',
    text='Welcome to the Change Detection Task. \n\nDuring this experiment, you will see 2 pictures, and then a black screen. \n\nYour task is to remember whether these 2 pictures were the same or different.\n\n\nTo continue, press the space bar.\n',
    font='Open Sans',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_instructions = keyboard.Keyboard()

# --- Initialize components for Routine "trial_instructions_2" ---
textbox_2 = visual.TextBox2(
     win, text="Ready to begin the experiment? \n\nPress 's' if the stimuli are the SAME.\n\nPress 'd' if the stimuli are DIFFERENT. \n\nPress the space bar to begin.", font='Open Sans',
     pos=(0, 0),     letterHeight=0.05,
     size=(None, None), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='textbox_2',
     autoLog=True,
)
key_resp_trial_instructions = keyboard.Keyboard()

# --- Initialize components for Routine "trial" ---
jar1 = visual.ImageStim(
    win=win,
    name='jar1', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-0.25, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
text = visual.TextStim(win=win, name='text',
    text="Is this jar the same or different?\n\nPress\n's' for SAME\n'd' for DIFFERENT",
    font='Open Sans',
    pos=(-0.28, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_trials = keyboard.Keyboard()
jar2 = visual.ImageStim(
    win=win,
    name='jar2', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0.45, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
changedetection = visual.ImageStim(
    win=win,
    name='changedetection', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0.45, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "Instructions" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_resp_instructions.keys = []
key_resp_instructions.rt = []
_key_resp_instructions_allKeys = []
# keep track of which components have finished
InstructionsComponents = [initial_instructions, key_resp_instructions]
for thisComponent in InstructionsComponents:
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

# --- Run Routine "Instructions" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *initial_instructions* updates
    if initial_instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        initial_instructions.frameNStart = frameN  # exact frame index
        initial_instructions.tStart = t  # local t and not account for scr refresh
        initial_instructions.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(initial_instructions, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'initial_instructions.started')
        initial_instructions.setAutoDraw(True)
    
    # *key_resp_instructions* updates
    waitOnFlip = False
    if key_resp_instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_instructions.frameNStart = frameN  # exact frame index
        key_resp_instructions.tStart = t  # local t and not account for scr refresh
        key_resp_instructions.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_instructions, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_instructions.started')
        key_resp_instructions.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_instructions.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_instructions.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_instructions.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_instructions.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_instructions_allKeys.extend(theseKeys)
        if len(_key_resp_instructions_allKeys):
            key_resp_instructions.keys = _key_resp_instructions_allKeys[-1].name  # just the last key pressed
            key_resp_instructions.rt = _key_resp_instructions_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Instructions" ---
for thisComponent in InstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_instructions.keys in ['', [], None]:  # No response was made
    key_resp_instructions.keys = None
thisExp.addData('key_resp_instructions.keys',key_resp_instructions.keys)
if key_resp_instructions.keys != None:  # we had a response
    thisExp.addData('key_resp_instructions.rt', key_resp_instructions.rt)
thisExp.nextEntry()
# the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "trial_instructions_2" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
textbox_2.reset()
key_resp_trial_instructions.keys = []
key_resp_trial_instructions.rt = []
_key_resp_trial_instructions_allKeys = []
# keep track of which components have finished
trial_instructions_2Components = [textbox_2, key_resp_trial_instructions]
for thisComponent in trial_instructions_2Components:
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

# --- Run Routine "trial_instructions_2" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textbox_2* updates
    if textbox_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textbox_2.frameNStart = frameN  # exact frame index
        textbox_2.tStart = t  # local t and not account for scr refresh
        textbox_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textbox_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'textbox_2.started')
        textbox_2.setAutoDraw(True)
    
    # *key_resp_trial_instructions* updates
    waitOnFlip = False
    if key_resp_trial_instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_trial_instructions.frameNStart = frameN  # exact frame index
        key_resp_trial_instructions.tStart = t  # local t and not account for scr refresh
        key_resp_trial_instructions.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_trial_instructions, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_trial_instructions.started')
        key_resp_trial_instructions.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_trial_instructions.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_trial_instructions.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_trial_instructions.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_trial_instructions.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_trial_instructions_allKeys.extend(theseKeys)
        if len(_key_resp_trial_instructions_allKeys):
            key_resp_trial_instructions.keys = _key_resp_trial_instructions_allKeys[-1].name  # just the last key pressed
            key_resp_trial_instructions.rt = _key_resp_trial_instructions_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trial_instructions_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "trial_instructions_2" ---
for thisComponent in trial_instructions_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_trial_instructions.keys in ['', [], None]:  # No response was made
    key_resp_trial_instructions.keys = None
thisExp.addData('key_resp_trial_instructions.keys',key_resp_trial_instructions.keys)
if key_resp_trial_instructions.keys != None:  # we had a response
    thisExp.addData('key_resp_trial_instructions.rt', key_resp_trial_instructions.rt)
thisExp.nextEntry()
# the Routine "trial_instructions_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
Trials = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('ConditionFile.xlsx'),
    seed=None, name='Trials')
thisExp.addLoop(Trials)  # add the loop to the experiment
thisTrial = Trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in Trials:
    currentLoop = Trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "trial" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    jar1.setImage(Jar1)
    key_resp_trials.keys = []
    key_resp_trials.rt = []
    _key_resp_trials_allKeys = []
    jar2.setImage(Jar2)
    changedetection.setImage(Jar3)
    # keep track of which components have finished
    trialComponents = [jar1, text, key_resp_trials, jar2, changedetection]
    for thisComponent in trialComponents:
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
    
    # --- Run Routine "trial" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *jar1* updates
        if jar1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            jar1.frameNStart = frameN  # exact frame index
            jar1.tStart = t  # local t and not account for scr refresh
            jar1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(jar1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'jar1.started')
            jar1.setAutoDraw(True)
        if jar1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > jar1.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                jar1.tStop = t  # not accounting for scr refresh
                jar1.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'jar1.stopped')
                jar1.setAutoDraw(False)
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text.started')
            text.setAutoDraw(True)
        
        # *key_resp_trials* updates
        waitOnFlip = False
        if key_resp_trials.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_trials.frameNStart = frameN  # exact frame index
            key_resp_trials.tStart = t  # local t and not account for scr refresh
            key_resp_trials.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_trials, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_trials.started')
            key_resp_trials.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_trials.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_trials.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_trials.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_trials.getKeys(keyList=['s', 'd'], waitRelease=False)
            _key_resp_trials_allKeys.extend(theseKeys)
            if len(_key_resp_trials_allKeys):
                key_resp_trials.keys = _key_resp_trials_allKeys[-1].name  # just the last key pressed
                key_resp_trials.rt = _key_resp_trials_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *jar2* updates
        if jar2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            jar2.frameNStart = frameN  # exact frame index
            jar2.tStart = t  # local t and not account for scr refresh
            jar2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(jar2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'jar2.started')
            jar2.setAutoDraw(True)
        if jar2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > jar2.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                jar2.tStop = t  # not accounting for scr refresh
                jar2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'jar2.stopped')
                jar2.setAutoDraw(False)
        
        # *changedetection* updates
        if changedetection.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            changedetection.frameNStart = frameN  # exact frame index
            changedetection.tStart = t  # local t and not account for scr refresh
            changedetection.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(changedetection, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'changedetection.started')
            changedetection.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "trial" ---
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_trials.keys in ['', [], None]:  # No response was made
        key_resp_trials.keys = None
    Trials.addData('key_resp_trials.keys',key_resp_trials.keys)
    if key_resp_trials.keys != None:  # we had a response
        Trials.addData('key_resp_trials.rt', key_resp_trials.rt)
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'Trials'

# get names of stimulus parameters
if Trials.trialList in ([], [None], None):
    params = []
else:
    params = Trials.trialList[0].keys()
# save data for this loop
Trials.saveAsText(filename + 'Trials.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='comma')
thisExp.saveAsPickle(filename)
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
