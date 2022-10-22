# hours

## use SQLite to store events
update 2022-10-22

use _sqlgsheet.database_ to create and update the sqlite database

## update()

1. clean and transform the new events
2. updat ethe db with _only_ new events
3. query the db for the events in the _reporting_year_ from the gsheet
4. create the reports _main_ and _subcategory_ and post to gsheet

## update steps

1. export the Blockytime to email
2. download and save the .csv into the root directory as _events.csv_
3. run _update()_ from terminal



--- 
1. Duplicate the Old Folder
2. Rename Files To Appropriate Project
    1. Add X to the Ending of the Folder
3. Delete the Hidden Files/Folders
    1. Delete LICENSE File 
4. Go into Github and Create a NEW Repository
    1. Set to Public
    2. Add a GNU License
5. Open up PyCharm Projects
    1. Get from VCS
    2. Go to Github in CODE
    3. Copy the HTTPS
6. Folder Should now contain License Only
    1. Transfer files from X folder to Pycharm Created folder
    2. Set up VENV: System > Preferences > Project:X > Python Interpreter
        1. Gear Icon: Add
        2. Existing Environment > OK
7. Copy an Existing .gitignore from Another Folder
    1. On the gitignore file, Right click, Git > Add
    2. On x.py and gsheetconfig and readme, Right click, Git > Add
8. To check if things are working click on VENV
    1. Select Terminal from Bottom List of Options
    2. Terminal should show “(venv)”
9. To import all requirements, On Terminal:
    1. pip install -r requirements.txt