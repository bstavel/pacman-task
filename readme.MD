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

### Peripheal requirements

* photodiode
* speakers

### How to run

Currently, the instructions and questionaire are separate from the rest of the task. Hoping to fix that soon!

1) Open the instructions powerpoint (either `~/Dropbox/Brooke/pacman_iEEG/Pacman_Instructions.pdf` or `~/Dropbox/Brooke/pacman_iEEG/Pacman_Instructions.pptx`, whichever is easier) and walk the patient through the instructions. Answer all questions the patient may have.
2) Use the _Launcher_ in the lab Dropbox by double clicking `~/Dropbox/_LAUNCHER/Brooke_pacman`. This will launch `pacman_game.py` in python3.
3) Enter subject ID and follow instructions in the terminal
4) Practice will open, complete, prompt to repeat practice if necessary. Once practice is completed, the main trials will automatically begin.
5) After main trials complete (~20 minutes), questionaire will open. There is a total of 12 blocks, each comprised of 20 trials.
6) In the background, all the downloaded files should be moved and renamed to the data folder. This will only work if Dropbox is installed and named `Dropbox` in the home directory. If not, there will be an error-- in this case please manually move the files out of the `Downloads` folder and into `~/Dropbox/Brooke/pacman_iEEG/data` folder.
7) After the task concludes, there is a short questionaire that asks about the patient's mental health on a recent, normal week. After the patient finishes it will prompt you to save the file-- please save this file to the subject's folder in `~/Dropbox/Brooke/pacman_iEEG/data`. 

If you encounter any problems, my contact information is saved in  `~/Dropbox/Brooke/pacman_iEEG/contact_me.txt`. Thank you for your help

### Requirements

* python3
* chrome
* os
* sys
* selenium
* time

