import os
import shutil
import datetime
import time
import sys
import glob

# Current day and month
today = datetime.date.today().strftime("%d-%m")
# Working Drive directory
src_dir = r'C:\Users\kvanr\Desktop\Working Drive\\'
# Location of External backup
external_dir = r'D:\Code\2019\\'
# Location of GitHub backup
git_dir = r'C:\Users\kvanr\OneDrive\GitHub - Backup\Project-Archive\2019\\'

language_menu_items = {
    1: 'C++',
    2: 'C#',
    3: 'Java',
    4: 'Python',
    5: 'Web'
}

# TODO Choose project language based on files in the project folder.
# NOTE Project dir to find what lang project is using.
# c++ = project_name/project_name/*.cpp
# c# = project_name/project_name/*.cs
# Java = project_name/project_name/*.java
# Python = project_name/*.py
# Web = project_name/*.html


def language_menu(project_choice):
    # Creating backup_language as global allows it to be used outside the function
    global backup_language
    while True:
        try:
            os.chdir(src_dir)
            print('Starting to check for project type')
            for file in os.listdir(f'{project_choice}/{project_choice}'):
                # Check for C++
                if file.endswith('.cpp'):
                    lang_choice = 1
                    print('C++')
                # Check for C#
                elif file.endswith('.cs'):
                    lang_choice = 2
                    print('C#')
                # Check for Java
                elif file.endswith('.java'):
                    lang_choice = 3
                    print('Java')
                else:
                    break

            for file in os.listdir(project_choice):
                # Check for Python
                if file.endswith('.py'):
                    lang_choice = 4
                    print('Python')
                # Check for Web
                elif file.endswith('.html'):
                    lang_choice = 5
                    print('Web')

            if 0 < lang_choice < 6:
                print(
                    f'\n{language_menu_items.get(lang_choice)} is the selected langauge. Proceeding to next step.')
                backup_language = language_menu_items.get(lang_choice)
            else:
                unknown_command()
                continue
        except ValueError:
            unknown_command()
            continue
        else:
            break


def project_menu():
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
                language_menu(project_choice)
                i += 1
            break
        except ValueError:
            unknown_command()
            continue


def unknown_command():
    print('\nThat command is unknown.  Please try again.\n\n')


def everything_backup():
    # NOTE Will backup to both exeternal and git
    project_menu()
    # language_menu()
   # print('Project is being moved to External Drive and Git Backup')
    # copy_project(external_dir + backup_language)
    # print('Project has been copied to External')
    # move_project(git_dir + backup_language)


def zip_project(output_name, project_src_dir):
    shutil.make_archive(output_name, 'zip', project_src_dir)
    print('Finished zipping')


print('Start')
time.sleep(2)
everything_backup()
print('End')
