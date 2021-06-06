# Automate Manual Repetitive Data Entry Tasks

This project contains two small modules one is sales order (JavaFX) which will take the data from the excel and other is automated 
data entering module which is developed in python. 

## Demo
* Video clip on youtube of the script execution. https://youtu.be/_jb6M0vqCLs

## Prerequisites

You must have following programs/packages in order to run this project.

* Java 1.8.0_66: https://www.java.com/download/
* Python 3.8: Download it from https://www.python.org/downloads
* Pandas: Run in command prompt pip install pandas
* Xlrd : Run in command prompt pip install xlrd
* Pyautogui: Run in command prompt pip install pyautogui
* Oracle Database 19c: Download it from https://www.oracle.com/database/technologies/oracle19c-windows-downloads.html

## Approach

* First need to clone this respiratory.
* Configure your database schema credentials in src/database/DbConnection.
* Copy database script from database/script.sql and execute in your database IDE (SQL Developer/SQL++, TOAD, etc).
* Run this project as part of java code through NetBeans IDE or command prompts.
* You will see a form as a pop up where data needed to be entered from automation/Sales Orders.xlsx
* Run python script which is in automation/script.py using py automation/script.py
* The python script will execute and take the data from excel and start entering into the form and automate save.
* The python script will iterate 10 times as there is a break statement in the python script.

Find it on youtube. https://youtu.be/_jb6M0vqCLs
