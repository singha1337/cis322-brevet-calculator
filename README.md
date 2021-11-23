## Brevet time calculator

This application calculates brevet opening and closing times using Randonneurs USA specifications. https://rusa.org/pages/acp-brevet-control-times-calculator. The user enters starting time and date, selects the total brevet distance from the dropdown list, and the control point distance. The appllication will automatically populate the Open and Close fields with the proper times. The timezone used is 'US/Pacific'

* Using AJAX in the front end, the data for the starting date and time, total brevet distance (in km) and the control point distance (in either miles or km, automatically converts to km) is supplied.

* acp_times.py is where the two functions to calculate the times are located. Using the control point distance and the RUSA specified maximum and minimum speeds, the opening and closing times are calculated respectively. 
	* If data that isn't a positive number is supplied, the functions return "Invalid input!"
	* If the control distance is more than 20% greater than the total brevet distance, the functions return "Invalid input"
	* If the control distance is greater than the brevet distance, open_times will use the brevet distance in the calculation, and			  close_times will use the max time limits.
	* If a control distance is within 60km, close_times calculates the closing time with a speed of 20km/hr and adds 1 hour.
	* If the control distance is 0km, this is the start, and the closing time will be 1 hour after the specified start.

* There are two buttons at the bottom of the page. Submit will enter all the opening and closing times and put them into a MongoDB database. Display will display all the opening and closing times fron the database into a new page.

* Test cases: If there are no opening/closing times, if a user presses Submit, they will be directed to a new page indicating that there is no opening/closing times to input into the database. If there is nothing in the database and a user presses Display, they will be directed to a page informing them there is nothing in the database.

Consumer program: localhost:5431
To access the API's use localhost:5432/(services as listed below)
    * `http://<host:port>/listAll` should return all open and close times in the database
    * `http://<host:port>/listOpenOnly` should return open times only
    * `http://<host:port>/listCloseOnly` should return close times only
    * `http://<host:port>/listAll/csv` should return all open and close times in CSV format
    * `http://<host:port>/listOpenOnly/csv` should return open times only in CSV format
    * `http://<host:port>/listCloseOnly/csv` should return close times only in CSV format
    * `http://<host:port>/listAll/json` should return all open and close times in JSON format
    * `http://<host:port>/listOpenOnly/json` should return open times only in JSON format
    * `http://<host:port>/listCloseOnly/json` should return close times only in JSON format
    * `http://<host:port>/listOpenOnly/csv?top=3` should return top 3 open times only (in ascending order) in CSV format 
    * `http://<host:port>/listOpenOnly/json?top=5` should return top 5 open times only (in ascending order) in JSON format
    * `http://<host:port>/listCloseOnly/csv?top=6` should return top 5 close times only (in ascending order) in CSV format
    * `http://<host:port>/listCloseOnly/json?top=4` should return top 4 close times only (in ascending order) in JSON format


Author: Arjun Singh
Contact: asingh7@uoregon.edu
Date: 11/16/2021
