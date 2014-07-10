rollcall.py
========

A simple Python command-line scraper that converts legislative roll calls from Maine.gov/legis to csv files. 

Requires the urllib and re modules.

To use, find the bill and the roll call you're interested in on www.mainelegislature.org (a single bill will have multiple roll-call votes in the House and Senate as it progresses from committee to final passage).

Each bill has a unique ID number on the website, which is visible after the '?ID=' pattern in the URL. And each roll call also has a unique 'serial number', visible after the "&serialnumber=" pattern in the URL. 

This script runs from the command line: open Terminal, navigate to the directory where the script is saved, and type "python rollcall.py". 

When running, it will prompt you to input the bill ID number, the roll call serial number, and to specify whether it's a "House" vote or a "Senate" vote. It then returns a csv file saved in the working directory named rollcall.csv. Each row of the CSV file includes (in this order) the district number, the legislator's last name, the legislator's home town, the legislator's party, and the legislator's vote. 
