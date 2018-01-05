# **Organizing Files**

This program currently uses two scripts.
**_from_folders.py_** takes one folder's pictures and moves them into a given destination. This is meant to be ran as many times as needed to move all contents into one folder.
**_rename_files_datetaken.py_** will rename all the jpegs in the folder to the date that they were taken in the given format:


> year_month_day.jpeg


**_rename_files_datetaken.py_** assumes that the contents of the destination folder contains all JPEG files. This leaves it up to the user to make sure that the file contains only jpegs. The script
depends on accessing EXIF data for each file in the directory.


## **Future**
* Would like to combine both files along with checks for jpegs within directories
