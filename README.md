# Elinvar
Implement a script, utility or application on using any programming language to
extract the following information about each service:
1. Name of service
2. Number of requests made to the service
3. Maximum time of request execution

<br></br>

## Technologies Used ##

To create the scripts for development of the data following technologies have been used: -
 

#### 1. For extracting the data and feeding the data into the database #### 
Python - Version (3.7)

#### Database for storing the values #### 
DB Browser for SQLite

<br></br>


## Prerequisites ##
1. Python 3.7 should be installed on the local system<br />
2. DB Browser SQLite should be installed on the local system

<br></br>

## Explanation of Code files ##
The [elinvar.py](elinvar.py) file contains all the functions and implementation of the logic to extract the data from [test.log](test.log) file and store it in the database and finally print the results as well.

To store the values of global variables [parameters.py](parameters.py) have been used

[tables.py](tables.py) is used for the creation of the tables and vies in the [elinvarDatabase.db](elinvarDatabase.db) which is database file.

## Execution ##
1. Clone the repository https://github.com/PaurushVishnoi/AOE.git or download the repo and extract it<br />
2. Open the Project AOE in any of the IDE ( Intellij or Eclipse etc.)<br />
3. Open [Testcase.java](src/AOE_Tasks/Testcase.java) and execute the file to execute the test case. <br />
4. Check the results on the terminal. The results can also be verified in the video [Recording_testcase_passed.avi](Recording_testcase_passed.avi) for better validation.

