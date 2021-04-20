# Udacity Dataengineer Degree - Project 1B

## Data Modeling with Apache Cassandra

---

### Project Context:

- A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. The analysis team is particularly interested in understanding what songs users are listening to. Currently, there is no easy way to query the data to generate the results, since the data reside in a directory of CSV files on user activity on the app.

- They'd like a data engineer to create an Apache Cassandra database which can create queries on song play data to answer the questions, and wish to bring you on the project. Your role is to create a database for this analysis. You'll be able to test your database by running queries given to you by the analytics team from Sparkify to create the results.

### Question for Udacity revisors:

- On Part1, why did you created an intermediate csv file with the csv library instead of pandas, any particular reason, like a memory efficient way to do I/O with csv files?
- Furthermore, is there a reason of why we didn't parsed directly file by file like in Project1A with Postgres? In this Project, we are first creating a "intermediate" csv file names event_datafile_new.csv, and the using this intermediate csv file to fill our database.
