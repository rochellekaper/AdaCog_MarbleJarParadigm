#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.5),
    on Fri May  5 11:01:01 2023
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
prefs.hardware['audioLib'] = 'ptb'
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
expName = 'purple_green_orange'  # from the Builder filename that created this script
expInfo = {
    'participant_num': '',
    'which_group': '',
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
    originPath='/Users/rochellekaper/Desktop/Both_Tasks/purple_green_orange/green_orange_purple.py',
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
    text="Welcome to the Marble Jar Exeriment. \n\nDuring this experiment, you will see 2 marble jars. \n\nOn half of the trials, you will randomly do a Jar Selection Task where you pick which jar you want a marble to be sampled from. \n\nOn the other half of the trials, you'll do a Change Detection Task where you'll be asked to remember if the jar is the same or different. \n\n\nPress space to continue",
    font='Open Sans',
    pos=(0, 0), height=0.051, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_instructions = keyboard.Keyboard()

# --- Initialize components for Routine "ready_to_begin" ---
text_3 = visual.TextStim(win=win, name='text_3',
    text='Ready to begin the experiment? Scores from these trials will be collected.\n\n\nPress the space bar to begin.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_ready = keyboard.Keyboard()

# --- Initialize components for Routine "trials_JarSelection" ---
jar1 = visual.ImageStim(
    win=win,
    name='jar1', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-0.25, -0.05), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
text = visual.TextStim(win=win, name='text',
    text='JAR SELECTION TASK\nChoose a jar of marbles \n\nJar 1: Press F Key              \nJar 2: Press J Key ',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_trials_JarSelection = keyboard.Keyboard()
jar2 = visual.ImageStim(
    win=win,
    name='jar2', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0.45, -0.05), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
MarbleValues = visual.ImageStim(
    win=win,
    name='MarbleValues', 
    image='/Users/rochellekaper/Desktop/Both_Tasks/purple_green_orange/purple_green_orange.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0.35), size=(0.525, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)

# --- Initialize components for Routine "trials_sample_marble" ---
# Run 'Begin Experiment' code from random_marble
gainsTotal = 0
print_marble_points = visual.TextStim(win=win, name='print_marble_points',
    text='',
    font='Open Sans',
    pos=(0, -0.13), height=0.07, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
marble = visual.ShapeStim(
    win=win, name='marble',
    size=(0.12, 0.12), vertices='circle',
    ori=0.0, pos=(0.00, 0.00), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-2.0, interpolate=True)

# --- Initialize components for Routine "trials_ChangeDetection" ---
jar1_2 = visual.ImageStim(
    win=win,
    name='jar1_2', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-0.25, -0.05), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
Same_or_Different = visual.TextStim(win=win, name='Same_or_Different',
    text="Is this jar the same or different?\n\nPress\n'f' for SAME\n'j' for DIFFERENT",
    font='Open Sans',
    pos=[0,0], height=0.07, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_trials = keyboard.Keyboard()
jar2_2 = visual.ImageStim(
    win=win,
    name='jar2_2', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0.45, -0.05), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
changedetection = visual.ImageStim(
    win=win,
    name='changedetection', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
blankscreen = visual.TextStim(win=win, name='blankscreen',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
MarbleValues_2 = visual.ImageStim(
    win=win,
    name='MarbleValues_2', 
    image='/Users/rochellekaper/Desktop/Both_Tasks/purple_green_orange/purple_green_orange.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0.35), size=(0.525, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-7.0)

# --- Initialize components for Routine "trials_Feedback_ChangeDetection" ---
fb = visual.TextStim(win=win, name='fb',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "total_points" ---
both_tasks_feedback = visual.TextStim(win=win, name='both_tasks_feedback',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

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

# --- Prepare to start Routine "ready_to_begin" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_resp_ready.keys = []
key_resp_ready.rt = []
_key_resp_ready_allKeys = []
# keep track of which components have finished
ready_to_beginComponents = [text_3, key_resp_ready]
for thisComponent in ready_to_beginComponents:
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

# --- Run Routine "ready_to_begin" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_3* updates
    if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_3.frameNStart = frameN  # exact frame index
        text_3.tStart = t  # local t and not account for scr refresh
        text_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_3.started')
        text_3.setAutoDraw(True)
    
    # *key_resp_ready* updates
    waitOnFlip = False
    if key_resp_ready.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_ready.frameNStart = frameN  # exact frame index
        key_resp_ready.tStart = t  # local t and not account for scr refresh
        key_resp_ready.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_ready, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_ready.started')
        key_resp_ready.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_ready.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_ready.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_ready.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_ready.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_ready_allKeys.extend(theseKeys)
        if len(_key_resp_ready_allKeys):
            key_resp_ready.keys = _key_resp_ready_allKeys[-1].name  # just the last key pressed
            key_resp_ready.rt = _key_resp_ready_allKeys[-1].rt
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
    for thisComponent in ready_to_beginComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "ready_to_begin" ---
for thisComponent in ready_to_beginComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_ready.keys in ['', [], None]:  # No response was made
    key_resp_ready.keys = None
thisExp.addData('key_resp_ready.keys',key_resp_ready.keys)
if key_resp_ready.keys != None:  # we had a response
    thisExp.addData('key_resp_ready.rt', key_resp_ready.rt)
thisExp.nextEntry()
# the Routine "ready_to_begin" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
which_task = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Condition_File_purple_green_orange.xlsx'),
    seed=None, name='which_task')
thisExp.addLoop(which_task)  # add the loop to the experiment
thisWhich_task = which_task.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisWhich_task.rgb)
if thisWhich_task != None:
    for paramName in thisWhich_task:
        exec('{} = thisWhich_task[paramName]'.format(paramName))

for thisWhich_task in which_task:
    currentLoop = which_task
    # abbreviate parameter names if possible (e.g. rgb = thisWhich_task.rgb)
    if thisWhich_task != None:
        for paramName in thisWhich_task:
            exec('{} = thisWhich_task[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "trials_JarSelection" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    jar1.setImage(Jar1)
    key_resp_trials_JarSelection.keys = []
    key_resp_trials_JarSelection.rt = []
    _key_resp_trials_JarSelection_allKeys = []
    jar2.setImage(Jar2)
    # keep track of which components have finished
    trials_JarSelectionComponents = [jar1, text, key_resp_trials_JarSelection, jar2, MarbleValues]
    for thisComponent in trials_JarSelectionComponents:
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
    
    # --- Run Routine "trials_JarSelection" ---
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
            jar1.setAutoDraw(True)
        if jar1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > jar1.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                jar1.tStop = t  # not accounting for scr refresh
                jar1.frameNStop = frameN  # exact frame index
                jar1.setAutoDraw(False)
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 2.5-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            text.setAutoDraw(True)
        
        # *key_resp_trials_JarSelection* updates
        waitOnFlip = False
        if key_resp_trials_JarSelection.status == NOT_STARTED and tThisFlip >= 2.5-frameTolerance:
            # keep track of start time/frame for later
            key_resp_trials_JarSelection.frameNStart = frameN  # exact frame index
            key_resp_trials_JarSelection.tStart = t  # local t and not account for scr refresh
            key_resp_trials_JarSelection.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_trials_JarSelection, 'tStartRefresh')  # time at next scr refresh
            key_resp_trials_JarSelection.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_trials_JarSelection.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_trials_JarSelection.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_trials_JarSelection.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_trials_JarSelection.getKeys(keyList=['f', 'j'], waitRelease=False)
            _key_resp_trials_JarSelection_allKeys.extend(theseKeys)
            if len(_key_resp_trials_JarSelection_allKeys):
                key_resp_trials_JarSelection.keys = _key_resp_trials_JarSelection_allKeys[-1].name  # just the last key pressed
                key_resp_trials_JarSelection.rt = _key_resp_trials_JarSelection_allKeys[-1].rt
                # was this correct?
                if (key_resp_trials_JarSelection.keys == str('')) or (key_resp_trials_JarSelection.keys == ''):
                    key_resp_trials_JarSelection.corr = 1
                else:
                    key_resp_trials_JarSelection.corr = 0
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
        
        # *MarbleValues* updates
        if MarbleValues.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            MarbleValues.frameNStart = frameN  # exact frame index
            MarbleValues.tStart = t  # local t and not account for scr refresh
            MarbleValues.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(MarbleValues, 'tStartRefresh')  # time at next scr refresh
            MarbleValues.setAutoDraw(True)
        if MarbleValues.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > MarbleValues.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                MarbleValues.tStop = t  # not accounting for scr refresh
                MarbleValues.frameNStop = frameN  # exact frame index
                MarbleValues.setAutoDraw(False)
        # Run 'Each Frame' code from check_task
        if task != "task_JarSelection":
            marble_color = -1
            marble_points = 0
            continueRoutine = False
        # Run 'Each Frame' code from keyresponse_time_2
        threshold = 6 #number of seconds allowed
        key_resp_trials.frameNStart = frameN  # exact frame index
        key_resp_trials.tStart = t  # local t and not account for scr refresh
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
        for thisComponent in trials_JarSelectionComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "trials_JarSelection" ---
    for thisComponent in trials_JarSelectionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_trials_JarSelection.keys in ['', [], None]:  # No response was made
        key_resp_trials_JarSelection.keys = None
        # was no response the correct answer?!
        if str('').lower() == 'none':
           key_resp_trials_JarSelection.corr = 1;  # correct non-response
        else:
           key_resp_trials_JarSelection.corr = 0;  # failed to respond (incorrectly)
    # store data for which_task (TrialHandler)
    which_task.addData('key_resp_trials_JarSelection.keys',key_resp_trials_JarSelection.keys)
    which_task.addData('key_resp_trials_JarSelection.corr', key_resp_trials_JarSelection.corr)
    if key_resp_trials_JarSelection.keys != None:  # we had a response
        which_task.addData('key_resp_trials_JarSelection.rt', key_resp_trials_JarSelection.rt)
    # the Routine "trials_JarSelection" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "trials_sample_marble" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from random_marble
    
    
    
    if (key_resp_trials_JarSelection.keys == 'j'): #left jar
        marble_color = random.choice(Jar2_Colors)
    elif (key_resp_trials_JarSelection.keys== 'f'): #right jar
        marble_color = random.choice(Jar1_Colors)
    else:
        #marble_color = -1
        marble_points = 0
            
            
            
    if marble_color == 'darkorange':
        marble_points = 4
        #marble_points = color_pts_dict['darkorange']
    if marble_color == 'green':
        marble_points = 3
        #marble_points = color_pts_dict['green']
    if marble_color == 'purple':
        marble_points = 2
        #marble_points = color_pts_dict['purple']
    
    gainsTotal = gainsTotal + marble_points
    thisExp.addData('Marble color', marble_color)
    thisExp.addData('Marble points', marble_points)
    print_marble_points.setText("You got " + str(marble_points) + " points"
)
    marble.setFillColor(marble_color)
    marble.setLineColor(marble_color)
    # keep track of which components have finished
    trials_sample_marbleComponents = [print_marble_points, marble]
    for thisComponent in trials_sample_marbleComponents:
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
    
    # --- Run Routine "trials_sample_marble" ---
    while continueRoutine and routineTimer.getTime() < 2.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from random_marble
        if task != "task_JarSelection":
            continueRoutine = False
        
        # *print_marble_points* updates
        if print_marble_points.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            print_marble_points.frameNStart = frameN  # exact frame index
            print_marble_points.tStart = t  # local t and not account for scr refresh
            print_marble_points.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(print_marble_points, 'tStartRefresh')  # time at next scr refresh
            print_marble_points.setAutoDraw(True)
        if print_marble_points.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > print_marble_points.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                print_marble_points.tStop = t  # not accounting for scr refresh
                print_marble_points.frameNStop = frameN  # exact frame index
                print_marble_points.setAutoDraw(False)
        
        # *marble* updates
        if marble.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            marble.frameNStart = frameN  # exact frame index
            marble.tStart = t  # local t and not account for scr refresh
            marble.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(marble, 'tStartRefresh')  # time at next scr refresh
            marble.setAutoDraw(True)
        if marble.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > marble.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                marble.tStop = t  # not accounting for scr refresh
                marble.frameNStop = frameN  # exact frame index
                marble.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trials_sample_marbleComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "trials_sample_marble" ---
    for thisComponent in trials_sample_marbleComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from random_marble
    #update total points 
    #gainsRound = gainsRound + color_pts_dict[marble_color]
    #gainsTotal.append(points)
    
    
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-2.000000)
    
    # --- Prepare to start Routine "trials_ChangeDetection" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    jar1_2.setImage(Jar1)
    Same_or_Different.setPos([Jar3_text_position_X, Jar3_text_position_Y])
    key_resp_trials.keys = []
    key_resp_trials.rt = []
    _key_resp_trials_allKeys = []
    jar2_2.setImage(Jar2)
    changedetection.setPos([Jar3_position_X, Jar3_position_Y])
    changedetection.setImage(Jar3)
    # keep track of which components have finished
    trials_ChangeDetectionComponents = [jar1_2, Same_or_Different, key_resp_trials, jar2_2, changedetection, blankscreen, MarbleValues_2]
    for thisComponent in trials_ChangeDetectionComponents:
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
    
    # --- Run Routine "trials_ChangeDetection" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *jar1_2* updates
        if jar1_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            jar1_2.frameNStart = frameN  # exact frame index
            jar1_2.tStart = t  # local t and not account for scr refresh
            jar1_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(jar1_2, 'tStartRefresh')  # time at next scr refresh
            jar1_2.setAutoDraw(True)
        if jar1_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > jar1_2.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                jar1_2.tStop = t  # not accounting for scr refresh
                jar1_2.frameNStop = frameN  # exact frame index
                jar1_2.setAutoDraw(False)
        
        # *Same_or_Different* updates
        if Same_or_Different.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
            # keep track of start time/frame for later
            Same_or_Different.frameNStart = frameN  # exact frame index
            Same_or_Different.tStart = t  # local t and not account for scr refresh
            Same_or_Different.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Same_or_Different, 'tStartRefresh')  # time at next scr refresh
            Same_or_Different.setAutoDraw(True)
        
        # *key_resp_trials* updates
        waitOnFlip = False
        if key_resp_trials.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_trials.frameNStart = frameN  # exact frame index
            key_resp_trials.tStart = t  # local t and not account for scr refresh
            key_resp_trials.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_trials, 'tStartRefresh')  # time at next scr refresh
            key_resp_trials.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_trials.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_trials.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_trials.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_trials.getKeys(keyList=['f', 'j'], waitRelease=False)
            _key_resp_trials_allKeys.extend(theseKeys)
            if len(_key_resp_trials_allKeys):
                key_resp_trials.keys = _key_resp_trials_allKeys[-1].name  # just the last key pressed
                key_resp_trials.rt = _key_resp_trials_allKeys[-1].rt
                # was this correct?
                if (key_resp_trials.keys == str(Change_Detection_Key)) or (key_resp_trials.keys == Change_Detection_Key):
                    key_resp_trials.corr = 1
                else:
                    key_resp_trials.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *jar2_2* updates
        if jar2_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            jar2_2.frameNStart = frameN  # exact frame index
            jar2_2.tStart = t  # local t and not account for scr refresh
            jar2_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(jar2_2, 'tStartRefresh')  # time at next scr refresh
            jar2_2.setAutoDraw(True)
        if jar2_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > jar2_2.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                jar2_2.tStop = t  # not accounting for scr refresh
                jar2_2.frameNStop = frameN  # exact frame index
                jar2_2.setAutoDraw(False)
        
        # *changedetection* updates
        if changedetection.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
            # keep track of start time/frame for later
            changedetection.frameNStart = frameN  # exact frame index
            changedetection.tStart = t  # local t and not account for scr refresh
            changedetection.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(changedetection, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'changedetection.started')
            changedetection.setAutoDraw(True)
        
        # *blankscreen* updates
        if blankscreen.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
            # keep track of start time/frame for later
            blankscreen.frameNStart = frameN  # exact frame index
            blankscreen.tStart = t  # local t and not account for scr refresh
            blankscreen.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blankscreen, 'tStartRefresh')  # time at next scr refresh
            blankscreen.setAutoDraw(True)
        if blankscreen.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > blankscreen.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                blankscreen.tStop = t  # not accounting for scr refresh
                blankscreen.frameNStop = frameN  # exact frame index
                blankscreen.setAutoDraw(False)
        # Run 'Each Frame' code from check_task_2
        if task != "task_ChangeDetection":
            continueRoutine = False
        
        # *MarbleValues_2* updates
        if MarbleValues_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            MarbleValues_2.frameNStart = frameN  # exact frame index
            MarbleValues_2.tStart = t  # local t and not account for scr refresh
            MarbleValues_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(MarbleValues_2, 'tStartRefresh')  # time at next scr refresh
            MarbleValues_2.setAutoDraw(True)
        if MarbleValues_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > MarbleValues_2.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                MarbleValues_2.tStop = t  # not accounting for scr refresh
                MarbleValues_2.frameNStop = frameN  # exact frame index
                MarbleValues_2.setAutoDraw(False)
        # Run 'Each Frame' code from keyresponse_time
        threshold = 6 #number of seconds allowed
        key_resp_trials.frameNStart = frameN  # exact frame index
        key_resp_trials.tStart = t  # local t and not account for scr refresh
        if t > threshold:
            marble_points = 0
            continueRoutine = False
            
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trials_ChangeDetectionComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "trials_ChangeDetection" ---
    for thisComponent in trials_ChangeDetectionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_trials.keys in ['', [], None]:  # No response was made
        key_resp_trials.keys = None
        # was no response the correct answer?!
        if str(Change_Detection_Key).lower() == 'none':
           key_resp_trials.corr = 1;  # correct non-response
        else:
           key_resp_trials.corr = 0;  # failed to respond (incorrectly)
    # store data for which_task (TrialHandler)
    which_task.addData('key_resp_trials.keys',key_resp_trials.keys)
    which_task.addData('key_resp_trials.corr', key_resp_trials.corr)
    if key_resp_trials.keys != None:  # we had a response
        which_task.addData('key_resp_trials.rt', key_resp_trials.rt)
    # the Routine "trials_ChangeDetection" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "trials_Feedback_ChangeDetection" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from feedback
    # Check if the key press was correct or not.
    
    if (key_resp_trials.keys == 'f') or (key_resp_trials.keys == 'j'):
        if key_resp_trials.corr:
            fb_text = 'Correct! You got 2 points.'
            gainsTotal += 1     
            fb_col = 'green'
        else:
            fb_text = 'Incorrect. You got 0 points.'
            fb_col = 'white'
            gainsTotal += 0     
    else:
        fb_text = 'You did not answer in time. You got 0 points.'
        fb_col = 'black'
        gainsTotal += 0
    fb.setColor(fb_col, colorSpace='rgb')
    fb.setText(fb_text)
    # keep track of which components have finished
    trials_Feedback_ChangeDetectionComponents = [fb]
    for thisComponent in trials_Feedback_ChangeDetectionComponents:
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
    
    # --- Run Routine "trials_Feedback_ChangeDetection" ---
    while continueRoutine and routineTimer.getTime() < 2.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fb* updates
        if fb.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fb.frameNStart = frameN  # exact frame index
            fb.tStart = t  # local t and not account for scr refresh
            fb.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fb, 'tStartRefresh')  # time at next scr refresh
            fb.setAutoDraw(True)
        if fb.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fb.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                fb.tStop = t  # not accounting for scr refresh
                fb.frameNStop = frameN  # exact frame index
                fb.setAutoDraw(False)
        # Run 'Each Frame' code from check_task_4
        if task != "task_ChangeDetection":
            continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trials_Feedback_ChangeDetectionComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "trials_Feedback_ChangeDetection" ---
    for thisComponent in trials_Feedback_ChangeDetectionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-2.000000)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'which_task'

# get names of stimulus parameters
if which_task.trialList in ([], [None], None):
    params = []
else:
    params = which_task.trialList[0].keys()
# save data for this loop
which_task.saveAsText(filename + 'which_task.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# --- Prepare to start Routine "total_points" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
both_tasks_feedback.setText("Congrats on completing the Marble Jar Task! You got " + str(gainsTotal) + " points!")
# Run 'Begin Routine' code from TOTAL_POINTS
thisExp.addData('TOTAL POINTS', gainsTotal)
# keep track of which components have finished
total_pointsComponents = [both_tasks_feedback]
for thisComponent in total_pointsComponents:
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

# --- Run Routine "total_points" ---
while continueRoutine and routineTimer.getTime() < 3.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *both_tasks_feedback* updates
    if both_tasks_feedback.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        both_tasks_feedback.frameNStart = frameN  # exact frame index
        both_tasks_feedback.tStart = t  # local t and not account for scr refresh
        both_tasks_feedback.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(both_tasks_feedback, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'both_tasks_feedback.started')
        both_tasks_feedback.setAutoDraw(True)
    if both_tasks_feedback.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > both_tasks_feedback.tStartRefresh + 3.0-frameTolerance:
            # keep track of stop time/frame for later
            both_tasks_feedback.tStop = t  # not accounting for scr refresh
            both_tasks_feedback.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'both_tasks_feedback.stopped')
            both_tasks_feedback.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in total_pointsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "total_points" ---
for thisComponent in total_pointsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-3.000000)

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