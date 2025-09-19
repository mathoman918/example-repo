# example-repo

# Triathlon Award Calculator

## Overview

The Triathlon Award Calculator is a simple Python program that calculates the total time taken by a participant to complete a triathlon.
Based on the total time, the program awards the participant with the appropriate recognition:

Provincial colours
Provincial half colours
Provincial scroll
No award

## How It Works

The program asks the user to input the time (in minutes) taken for each of the three triathlon events:

Swimming
Cycling
Running

It calculates the total time taken to complete the triathlon.
Based on the total time, it determines the award according to the following criteria:

 Total Time (minutes)    Award                   
 --------------------  ----------------------- 
 >= 100                 Provincial colours      
 <= 105                 Provincial half colours 
 <= 110                 Provincial scroll       
 > 110                  No award                

## How to Run

Ensure you have Python installed on your computer.
Save the code in a file named, for example, `triathlon_award.py`.
Open a terminal or command prompt and navigate to the folder containing the file.
Run the program using the command:or the ctrl+shift+D shortcut

Enter the time taken for swimming, cycling, and running when prompted.
The program will output your award based on your total time.

## Example
How many minutes taken for swimming? 30
How many minutes taken for cycling? 40
How many minutes taken for running? 25
Provincial colours: will be printed out based on the time taken

## Notes

All inputs must be integers representing minutes.
The award thresholds are fixed and can be modified in the code if needed.
