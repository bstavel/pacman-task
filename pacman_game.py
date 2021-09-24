import os
import webbrowser
from os.path import exists
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import sys

def make_directories():
    ## make directories ##

    # get subject id #
    sub_id = input("Please type the subject ID: ")

    # give access to these folders to all functions
    global sub_dir
    global current_path

    # get paths
    current_path = os.getcwd()
    sub_dir = os.path.join(current_path, "data", sub_id)

    # make necessary folders
    if not exists(sub_dir):
        os.mkdir(sub_dir)
    else:
        correct_id = input("A folder for this subject already exists, are you sure this is the correct ID? Press 'y' for yes and 'n' for no: ")
        if correct_id != 'y':
            sub_id = input("Please type the subject ID: ")
            sub_dir = os.path.join(current_path, "data", sub_id)
            os.mkdir(sub_dir)

def run_practice():
    ## open practice ##
    practice_file = os.path.join(current_path, 'index_practice.html')
    url = 'file://{0}'.format(practice_file)

    # get no download bar extension
    extension_path = os.path.join(current_path, 'extension_1_5_0_0.crx')
    chrome_options = Options()
    chrome_options.add_extension(extension_path);
    chrome_options.add_argument("--start-fullscreen");

    # open file
    chrome_driver_path = os.path.join(current_path, 'chromedriver')
    driver = webdriver.Chrome(executable_path=chrome_driver_path, chrome_options=chrome_options)
    driver.get(url)

    # wait for practice to finish
    download_folder = os.path.join(current_path, '../../../Downloads')
    practice_done = os.path.join(download_folder, 'practice_done.json')
    practice_done = os.path.normpath(practice_done)
    print(practice_done)
    while not exists(practice_done):
        time.sleep(0.1)

    # Close Practice #
    time.sleep(3)
    driver.close()

    # move practice file #
    moved_practice = os.path.join(sub_dir, 'practice_done.json')
    os.rename(practice_done, moved_practice)

def run_main_trials():

    ## open main ##
    main_file = os.path.join(current_path, 'index_main.html')
    url = 'file://{0}'.format(main_file)

    # get no download bar extension
    extension_path = os.path.join(current_path, 'extension_1_5_0_0.crx')
    chrome_options = Options()
    chrome_options.add_extension(extension_path);
    chrome_options.add_argument("--start-fullscreen");

    # open file
    chrome_driver_path = os.path.join(current_path, 'chromedriver')
    driver = webdriver.Chrome(executable_path=chrome_driver_path, chrome_options=chrome_options)
    driver.get(url)

    ## wait for practice to conclude ##
    file_num = 11
    download_folder = os.path.join(current_path, '../../../Downloads')
    data_file = os.path.join(download_folder, 'pacman-task-data.json')
    data_file = os.path.normpath(data_file)
    while file_num < 12:
        if exists(data_file):
            saved_file = os.path.join(sub_dir, "pacman-task-data{0}.json".format(file_num))
            os.rename(data_file, saved_file)
            file_num  = file_num  + 1

    # sleep and close
    time.sleep(3)
    driver.close()

def open_questionaire():

    ## open pacman questionaire ##
    quest_file = os.path.join(current_path, 'Pacman_Questionaire.pdf')
    url = 'file://{0}'.format(quest_file)

    # get no download bar extension
    extension_path = os.path.join(current_path, 'extension_1_5_0_0.crx')
    chrome_options = Options()
    chrome_options.add_extension(extension_path);

    # open file
    chrome_driver_path = os.path.join(current_path, 'chromedriver')
    driver = webdriver.Chrome(executable_path=chrome_driver_path, chrome_options=chrome_options)
    driver.get(url)
    driver.maximize()



def main():

    # get ID and create directories
    make_directories()

    # Run Practice #
    run_practice()

    # Repeat Practice? #
    repeat_practice = input("Great job! Are you ready move to the main trials? Type 'y' to continue or 'n' to repeat the practice: ")
    if repeat_practice == 'y':
        print("Continuing...")
    elif repeat_practice == 'n':
        run_practice()
    else:
        repeat_practice = input("Great job! Are you ready move to the main trials? Type 'y' to continue or 'n' to repeat the practice: ")

    # Run Main #
    run_main_trials()

    # Open pdf questionaire #
    input("Thank you! Please press enter to continue to a short questionaire")
    open_questionaire()


if __name__ == "__main__":
    main()
