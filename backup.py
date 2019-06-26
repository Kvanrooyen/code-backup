import os
import shutil
import datetime
import time
import sys
import glob
import subprocess
from pathlib import Path


# Current day and month
today = datetime.date.today().strftime("%d-%m")
# Working Drive directory
src_dir = r'C:\Users\kvanr\Desktop\Working Drive\\'
# Location of External backup
external_dir = r'D:\Code\2019\\'
# Location of GitHub backup
git_dir = r'C:\Users\kvanr\OneDrive\GitHub - Backup\Project-Archive\\'


language_menu_items = {
    1: 'C++',
    2: 'C#',
    3: 'Java',
    4: 'Python',
    5: 'Web',
    6: 'Flutter'
}


def language_choice(project):
    # Creating backup_language as global allows it to be used outside the function
    global backup_language
    while True:
        try:

            cppProject = Path(
                src_dir + project_choice).glob(f'{project_choice}/*.cpp')
            csProject = Path(
                src_dir + project_choice).glob(f'{project_choice}/*.cs')
            javaProject = Path(
                src_dir + project_choice).glob(f'{project_choice}/*.java')
            pythonProject = Path(src_dir + project_choice).glob('*.py')
            webProject = Path(src_dir + project_choice).glob('*.html')
            flutterProject = Path(
                src_dir + project_choice).glob(f'{project_choice}.iml')

            for path in cppProject:
                path_in_str = str(path)
                print(path_in_str)
                lang_choice = 1
                break

            for path in csProject:
                path_in_str = str(path)
                print(path_in_str)
                lang_choice = 2
                break

            for path in javaProject:
                path_in_str = str(path)
                print(path_in_str)
                lang_choice = 3
                break

            for path in pythonProject:
                path_in_str = str(path)
                print(path_in_str)
                lang_choice = 4
                break

            for path in webProject:
                path_in_str = str(path)
                print(path_in_str)
                lang_choice = 5
                break

            for path in flutterProject:
                path_in_str = str(path)
                print(path_in_str)
                lang_choice = 6
                break

            if 0 < lang_choice < 7:
                backup_language = language_menu_items.get(lang_choice)
                print(
                    f'{backup_language} is the selected langauge. Proceeding to next step.')
                time.sleep(1)
                copy_project(external_dir + backup_language)
                move_project(f'{git_dir}\\2019\\{backup_language}')
            else:
                unknown_command()
                continue
        except ValueError:
            unknown_command()
            continue
        else:
            break


def project_choice():
    global backup_project, project_choice
    # A pair of lists for storing the projectNo and projectName
    list_project_num = []
    list_project_name = []

    # Count the number of folder in the directory
    count = len(os.listdir(src_dir))
    total_items = len(os.listdir(src_dir))

    for item in range(0, count):
        # Number the items in the lsit based of number of projects in src
        # NOTE Int value. Same as language_menu_items
        list_project_num.append(item + 1)

    for item in range(0, count):
        # Seperate each item and add it to corresponding number value from previous for loop
        elt = (os.listdir(src_dir))[item]
        # NOTE String value. Same as language_menu_items
        list_project_name.append(elt)

    # Convert the lists to a dictionary
    src_dir_items = dict(zip(list_project_num, list_project_name))
    while True:
        try:
            i = 0
            while i < total_items:
                project_choice = list_project_name[i]
                # print(project_choice)
                backup_project = src_dir_items.get(project_choice)
                print(project_choice)
                os.chdir(src_dir)
                zip_project(f'{project_choice}--{today}',
                            os.path.join(src_dir + project_choice))
                language_choice(project_choice)
                i += 1
            break
        except ValueError:
            unknown_command()
            continue


def unknown_command():
    print('\nThat command is unknown.  Please try again.\n\n')


def copy_project(backup_location):
    # NOTE Copy zip folder to backup location
    # Make sure the current directory is the src_dir
    os.chdir(src_dir)
    # Searches the directory for zip files to move.
    try:
        for file in glob.glob(f'{project_choice}--{today}.zip'):
            shutil.copy(src_dir + file, backup_location)
        print('Succesfully copied the project to the backup location.')
    except OSError as e:
        print(f'Error has occured.\n{e}')


def move_project(backup_location):
    # NOTE Move zip folder to backup location
    # Make sure the current directory is the src_dir
    os.chdir(src_dir)
    # Searches the directory for zip files to move.
    try:
        for file in glob.glob(f'{project_choice}--{today}.zip'):
            shutil.move(src_dir + file, backup_location)
        print('Succesfully moved the project to the backup location.')
    except OSError as e:
        print('Error has occured.\n %s' % e)


def zip_project(output_name, project_src_dir):
    shutil.make_archive(output_name, 'zip', project_src_dir)
    print('Finished zipping')


def run_git():
    # NOTE
    # After moving project zips to backup locations run the following:
    # git add .
    # git commit -m <commit message>
    os.chdir(git_dir)
    subprocess.call(["git", "git add ."])
    time.sleep(1)
    print('Type your commit message: ')
    commit_msg = input('> ')
    subprocess.call(["git", f'git commit -m "{commit_msg}"'])


project_choice()
run_git()
