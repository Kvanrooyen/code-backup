import os
import shutil
import datetime
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

            # Loop through looking for a language to assign to projects
            for path in cppProject:
                lang_choice = 1
                break

            for path in csProject:
                lang_choice = 2
                break

            for path in javaProject:
                lang_choice = 3
                break

            for path in pythonProject:
                lang_choice = 4
                break

            for path in webProject:
                lang_choice = 5
                break

            for path in flutterProject:
                lang_choice = 6
                break

            if 0 < lang_choice < 7:
                backup_language = language_menu_items.get(lang_choice)
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
    global project_choice
    # A pair of lists for storing the projectNo and projectName
    list_project_num = []
    list_project_name = []

    # Count the number of folder in the directory
    count = len(os.listdir(src_dir))
    total_items = len(os.listdir(src_dir))

    for item in range(0, count):
        # Number the items in the list based of number of projects in src
        list_project_num.append(item + 1)

    for item in range(0, count):
        # Separate each item and add it to corresponding number value
        # from previous for loop
        elt = (os.listdir(src_dir))[item]
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
    # Copy zip folder to backup location
    # Make sure the current directory is the src_dir
    os.chdir(src_dir)
    # Searches the directory for zip files to move.
    try:
        for file in glob.glob(f'{project_choice}--{today}.zip'):
            shutil.copy(src_dir + file, backup_location)
        print('Successfully copied the project to the backup location.')
    except OSError as e:
        print(f'Error has occurred.\n{e}')


def move_project(backup_location):
    # Move zip folder to backup location
    # Make sure the current directory is the src_dir
    os.chdir(src_dir)
    # Searches the directory for zip files to move.
    try:
        for file in glob.glob(f'{project_choice}--{today}.zip'):
            shutil.move(src_dir + file, backup_location)
        print('Successfully moved the project to the backup location.')
    except OSError as e:
        print('Error has occurred.\n %s' % e)


def zip_project(output_name, project_src_dir):
    shutil.make_archive(output_name, 'zip', project_src_dir)
    print('Finished zipping')


def run_git():
    # NOTE
    # After moving project zips to backup locations run the following:
    # git add .
    # git commit -m <commit message>
    # os.chdir(git_dir)
    subprocess.call(["git"] + ["add", "."], cwd=git_dir)
    print('Type your commit message: ')
    commit_msg = input('> ')
    subprocess.call(["git"] + ["commit", "-m"] + [commit_msg], cwd=git_dir)


project_choice()
run_git()
