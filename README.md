# Pacman Game for iEEG

### Task Overview

This is the task code for a novel continuous-choice approach-avoidance conflict task based on the arcade game Pacman. The game was simplified to be played along a single
corridor. The decision to move towards the center of the corridor is thus associated with both potential gains (eating “dots”, resulting in points) and potential losses (ghost attack,
resulting in loss of a life). Participants may collect as much reward as they choose, before turning around and exiting the trial by leaving through the end of the corridor. Importantly,
both being chased and being caught by the ghost are determined by the player's distanceto the ghost. The closer the participant chooses to go to the ghost, the higher the
likelihood that the ghost will both 1) initiate a chase and 2) be fast enough to catch Pacman.

The game is played as a series of mini- blocks, which end when either 1) Pacman loses all three lives or 2) twenty trials are completed. We will collect
a total of 12 mini-blocks, corresponding to 240 trials.

### Versions

There are two versions of the game. The first is implemented for a large cohort prolific study and is integrated with qualtrics. The second is made to run without wifi for an intracranial EEG cohort. 

### To Do

* change photodiode square to be on left side
* edit post study questionaire
* better wrapper for the hospitals

