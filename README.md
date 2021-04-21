# Udacity Dataengineer Degree - Project 1B

## Data Modeling with Apache Cassandra

---

### Project Context:

- A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. The analysis team is particularly interested in understanding what songs users are listening to. Currently, there is no easy way to query the data to generate the results, since the data reside in a directory of CSV files on user activity on the app.

- They'd like a data engineer to create an Apache Cassandra database which can create queries on song play data to answer the questions, and wish to bring you on the project. Your role is to create a database for this analysis. You'll be able to test your database by running queries given to you by the analytics team from Sparkify to create the results.

### Solution Description:

- As a good data modelling approach using Apache Cassandra, three new tables were created to answer three different questions, tables `music_session, user_session and songs_user`.
- All the CQL statements used to `DROP, CREATE, INSERT and SELECT` data into these tables are defined on `sql_queries.py`.
- The Whole ETL process is define inside the notebook Project*1B* `Project_Template.ipynb`.

### Project Structure:

- To reproduce the solution present in this repository, you will first have to install some dependencies:
  1. Firstly, you will need to have **Apache Cassandra** installed in your machine, refer the [official documentation](https://cassandra.apache.org/) in order to properly install it on your OS.
  2. Secondly, you will need to have a **Python 3.6+** installed on your machine, refer the [official documentation](https://www.python.org/) in order to properly install it on your OS.
  3. Third (Tested on Ubuntu 18.04 and 20.04), run the **Makefile** from the project run by typing on the terminal `$ make`. This command will run through the Makefile, in order to build a virtual environment with python and some dependencies to run this project.
  4. Once you sucessfully ran the make command, a folder named `venv` should be installed on the root of the project, aswell as the [`jupyte-notebook`](https://jupyter.org/) installed.
  5. To reproduce the whole ETL solution, first you will have to activate your created virtual environment by typing on your terminal `$ source venv/bin/activate`. Then, type on your terminal `$ jupyter-notebook`, open the notebook `Project_1B_ Project_Template.ipynb`, and execute it. All data modeling decisions are described inside the notebook.
