# Project 6: Brevet time calculator service

Simple listing service from project 5 stored in MongoDB database.

## What is in this repository

You have a minimal implementation of Docker compose in DockerRestAPI folder, using which you can create REST API-based services (as demonstrated in class). 

## Recap 

You will reuse *your* code from project 5 (https://bitbucket.org/UOCIS322/proj5-mongo). Recall: you created the following functionalities.

1. Two buttons ("Submit") and ("Display") in the page where you have controle times.
2. On clicking the Submit button, the control times were be entered into the database.
3. On clicking the Display button, the entries from the database were be displayed in a new page.
4. You also handled error cases appropriately.

## Functionality you will add

This project has following four parts. Change the values for host and port according to your machine, and use the web browser to check the results.

* You will design RESTful service to expose what is stored in MongoDB. Specifically, you'll use the boilerplate given in DockerRestAPI folder, and create the following three basic APIs:
    * `http://<host:port>/listAll` should return all open and close times in the database
    * `http://<host:port>/listOpenOnly` should return open times only
    * `http://<host:port>/listCloseOnly` should return close times only

* You will also design two different representations: one in csv and one in json. For the above three basic APIs, JSON should be your default representation. 
    * `http://<host:port>/listAll/csv` should return all open and close times in CSV format
    * `http://<host:port>/listOpenOnly/csv` should return open times only in CSV format
    * `http://<host:port>/listCloseOnly/csv` should return close times only in CSV format

    * `http://<host:port>/listAll/json` should return all open and close times in JSON format
    * `http://<host:port>/listOpenOnly/json` should return open times only in JSON format
    * `http://<host:port>/listCloseOnly/json` should return close times only in JSON format

* You will also add a query parameter to get top "k" open and close times. For examples, see below.

    * `http://<host:port>/listOpenOnly/csv?top=3` should return top 3 open times only (in ascending order) in CSV format 
    * `http://<host:port>/listOpenOnly/json?top=5` should return top 5 open times only (in ascending order) in JSON format
    * `http://<host:port>/listCloseOnly/csv?top=6` should return top 5 close times only (in ascending order) in CSV format
    * `http://<host:port>/listCloseOnly/json?top=4` should return top 4 close times only (in ascending order) in JSON format

* You'll also design consumer programs (e.g., in jQuery) to use the service that you expose. "website" inside DockerRestAPI is an example of that. It is uses PHP. You're welcome to use either PHP or jQuery to consume your services. NOTE: your consumer program should be in a different container like example in DockerRestAPI.

## Data Samples

The sample data files ([sample-data.json](data-samples/sample-data.json), [sample-data.csv](data-samples/sample-data.csv), and [sample-data-pivoted.csv](data-samples/sample-data-pivoted.csv)) provide a suggested JSON and CSV format that you could follow for your exports. 

1. JSON
```json
{
   "brevets":[
      {
         "distance":200,
         "begin_date":"12/01/2021",
         "begin_time":"18:06",
         "controls":[
            {
               "km":0,
               "mi":0,
               "location":"begin",
               "open":"12/01/2021 18:06",
               "close":"12/01/2021 19:06"
            },
            {
               "km":100,
               "mi":62,
               "location":null,
               "open":"12/01/2021 21:02",
               "close":"12/02/2021 00:46"
            },
            {
               "km":150,
               "mi":93,
               "location":"second checkpoint",
               "open":"12/01/2021 22:31",
               "close":"12/02/2021 04:06"
            },
            {
               "km":200,
               "mi":124,
               "location":"last checkpoint",
               "open":"12/01/2021 23:59",
               "close":"12/02/2021 07:36"
            }
         ]
      },
      {
         "distance":1000,
         "begin_date":"01/01/2022",
         "begin_time":"00:00",
         "controls":[
            {
               "km":0,
               "mi":0,
               "location":"begin",
               "open":"01/01/2022 00:00",
               "close":"01/01/2022 01:00"
            },
            {
               "km":1000,
               "mi":621,
               "location":"finish line",
               "open":"01/01/2022 09:05",
               "close":"12/02/2021 03:00"
            }
         ]
      }
   ]
}
```

2. CSV
```csv
brevets/distance,brevets/begin_date,brevets/begin_time,brevets/controls/0/km,brevets/controls/0/mi,brevets/controls/0/location,brevets/controls/0/open,brevets/controls/0/close,brevets/controls/1/km,brevets/controls/1/mi,brevets/controls/1/location,brevets/controls/1/open,brevets/controls/1/close,brevets/controls/2/km,brevets/controls/2/mi,brevets/controls/2/location,brevets/controls/2/open,brevets/controls/2/close,brevets/controls/3/km,brevets/controls/3/mi,brevets/controls/3/location,brevets/controls/3/open,brevets/controls/3/close
200,12/01/2021,18:06,0,0,begin,12/01/2021 18:06,12/01/2021 19:06,100,62,,12/01/2021 21:02,12/02/2021 00:46,150,93,second checkpoint,12/01/2021 22:31,12/02/2021 04:06,200,124,last checkpoint,12/01/2021 23:59,12/02/2021 07:36
1000,01/01/2022,00:00,0,0,begin,01/01/2022 00:00,01/01/2022 01:00,1000,621,finish line,01/01/2022 09:05,12/02/2021 03:00,,,,,,,,,,
```

## Tasks

You'll turn in your credentials.ini (including the keys `author` and `repo` under the section `[DEFAULT]`) using which we will get the following:

* The working application with three parts.

* Dockerfile

* docker-compose.yml

## Grading Rubric

* If your code works as expected: 100 points. This includes:
    * Basic APIs work as expected. (15 points)
    * Representations work as expected. (30 points)
    * Query parameter-based APIs work as expected. (10 points)
    * Consumer program works as expected. (10 points)

* For each non-working API, 5 points will be docked off. If none of them work,
  you'll get 35 points assuming
    * README is updated with your name and email ID. (5 points)
    * The credentials.ini is submitted with the correct URL of your repo. (15 points)
    * Dockerfile is present. 
    * Docker-compose.yml works/builds without any errors. (15 points)

* If README is not updated, 5 points will be docked off. 

* If the Docker-compose.yml doesn't build or is missing, 15 points will be
  docked off. Same for Dockerfile as well.

* If credentials.ini is missing, 0 will be assigned.
