# Pacman Game for iEEG

### Task Overview

This is the task code for a novel continuous-choice approach-avoidance conflict task based on the arcade game Pacman. The game was simplified to be played along a single
corridor. The decision to move towards the center of the corridor is thus associated with both potential gains (eating “dots”, resulting in points) and potential losses (ghost attack,
resulting in loss of a life). Participants may collect as much reward as they choose, before turning around and exiting the trial by leaving through the end of the corridor. Importantly,
both being chased and being caught by the ghost are determined by the player's distanceto the ghost. The closer the participant chooses to go to the ghost, the higher the
likelihood that the ghost will both 1) initiate a chase and 2) be fast enough to catch Pacman.

The game is played as a series of mini- blocks, which end when either 1) Pacman loses all three lives or 2) twenty trials are completed. We will collect
a total of 12 mini-blocks, corresponding to 240 trials.

### Requirements & Instructions for New sites

* python3
* chrome (the webbrowser, it should be installed already)
* selenium
* os
* sys
* time

This task should normally be run in the linux os (unless the site uses BCI2000), and runs within the `python3_exp` conda environment that should already be configured. If the `python3_exp` environment exists open a terminal an enter the following lines of code:

```
source ~/anaconda3/etc/profile.d/conda.sh
conda activate python3_exp
conda install -c conda-forge selenium
```

If there are no errors, you can close the environment with `conda deactivate`


### Peripheal requirements

* photodiode
* speakers

### How to run

There are three ways to run the task. The first is using the `_LAUCNHER` and is the easiest. Second, you can launch the task using python in the terminal. Third, if you are seeing errors with the first two methods, you can run the task by manually clicking on some files. I will explain each in detail below.

If you encounter any problems, my contact information is saved in  `~/Dropbox/Brooke/pacman_iEEG/contact_me.txt`. Thank you for your help!

#### Method 1

1) Open the instructions powerpoint (either `~/Dropbox/Brooke/pacman_iEEG/Pacman_Instructions.pdf` or `~/Dropbox/Brooke/pacman_iEEG/Pacman_Instructions.pptx`, whichever is easier) and walk the patient through the instructions. Answer all questions the patient may have.
2) Use the _Launcher_ in the lab Dropbox by double clicking `~/Dropbox/_LAUNCHER/Brooke_pacman`. This will launch `pacman_game.py` in python3.
3) Enter subject ID and follow instructions in the terminal
4) Practice will open, complete, prompt to repeat practice if necessary. Once practice is completed, the main trials will automatically begin. There are a total of 12 blocks, each comprised of 20 trials.
5) After main trials complete (~20 minutes), questionaire will open. When prompted please save this file to the subject's folder in `~/Dropbox/Brooke/pacman_iEEG/data/`. 
6) In the background, all the downloaded files should be moved and renamed to the data folder. This will only work if Dropbox is installed and named `Dropbox` in the home directory. If not, there will be an error-- in this case please manually move the files out of the `Downloads` folder and into `~/Dropbox/Brooke/pacman_iEEG/data` folder.


#### Method 2

1) Open the instructions powerpoint (either `~/Dropbox/Brooke/pacman_iEEG/Pacman_Instructions.pdf` or `~/Dropbox/Brooke/pacman_iEEG/Pacman_Instructions.pptx`, whichever is easier) and walk the patient through the instructions. Answer all questions the patient may have.
2) Open a terminal
3) Type in the terminal: `source ~/anaconda3/etc/profile.d/conda.sh`
4) Type in the terminal: `conda activate python3_exp`
5) Type in the terminal `cd ~/Dropbox/Brooke/pacman_iEEG/`
6) Type in the terminal: `python pacman_game.py`
7) Enter subject ID and follow instructions in the terminal
8) Practice will open, complete, prompt to repeat practice if necessary. Once practice is completed, the main trials will automatically begin. There are a total of 12 blocks, each comprised of 20 trials.
9) After main trials complete (~20 minutes), a pdf questionaire will open. When prompted please save this file to the subject's folder in `~/Dropbox/Brooke/pacman_iEEG/data`. 
10) In the background, all the downloaded files should be moved and renamed to the data folder. This will only work if Dropbox is installed and named `Dropbox` in the home directory. If not, there will be an error-- in this case please manually move the files out of the `Downloads` folder and into `~/Dropbox/Brooke/pacman_iEEG/data` folder.
12) In the terminal, please close the conda environemnt so that other tasks don't use the wrong software! Type in the terminal: `conda deactivate`

#### Method 3

1) Double click `~/Dropbox/Brooke/pacman_iEEG/extension_1_5_0_0.crx`. This should hopefully disable the download bar.
2) Open the instructions powerpoint (either `~/Dropbox/Brooke/pacman_iEEG/Pacman_Instructions.pdf` or `~/Dropbox/Brooke/pacman_iEEG/Pacman_Instructions.pptx`, whichever is easier) and walk the patient through the instructions. Answer all questions the patient may have.
3) Tell the patient they will do a short practice. Then double-click to open the file `~/Dropbox/Brooke/pacman_iEEG/index_practice.html`
8) There will be four practice trials. After the last trial, ask if the patient would like to repeat the practice. If not close the window.
9) Double-click to open the file `~/Dropbox/Brooke/pacman_iEEG/index_main.html` There are a total of 12 blocks, each comprised of 20 trials. (~20 minutes)
10) After main trials complete (~20 minutes), they need to complete a short questionaire that asks about the patient's mental health on a recent, normal week. Double-click to open the file `~/Dropbox/Brooke/pacman_iEEG/Pacman_Quastionaire.pdf`
11) After they complete the questionaire, it will prompt you to save the file. Please navigate to `~/Dropbox/Brooke/pacman_iEEG/data/` and create a new folder using the patient's subject id.
12) **IMPORTANT: After the patient finishes the questionaire, please go to the Downloads folder. Please copy all the pacman-task-data.json files you see and paste them into the data folder you created in step 7.**


### Repo Versions

There are two versions of the game. The first is implemented for a large cohort prolific study and is integrated with qualtrics. The second is made to run without wifi for an intracranial EEG cohort. For iEEG versions, use the stable released version, on the iEEG_live branch
