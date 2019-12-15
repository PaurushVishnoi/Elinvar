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


## Explanation of Code files ##
The [Testcase.java](src/AOE_Tasks/Testcase.java) file contains @Test notation which denotes the main test case to be executed. 

Testcase.java is extending the class [BrowserHandle.java](src/AOE_Tasks/BrowserHandle.java) where actions before (Setting Up Chrome Driver) and after the execution of test (Closing of Chrome browser)  have been defined.

[PageModel.java](src/AOE_Tasks/PageModel.java)
Creation of WebDriver for Page Objects using PageFactory ( An inbuilt page object model for Selenium ). With the help of PageFactory , we use @FindBy annotation to find the page elements.

[AOEWebsite.java](src/AOEWebsite.java) All the Page objects have been initialized and a method for each has been defined so that their instances can be used in other test cases or other classes as well.

## Execution ##
1. Clone the repository https://github.com/PaurushVishnoi/AOE.git or download the repo and extract it<br />
2. Open the Project AOE in any of the IDE ( Intellij or Eclipse etc.)<br />
3. Open [Testcase.java](src/AOE_Tasks/Testcase.java) and execute the file to execute the test case. <br />
4. Check the results on the terminal. The results can also be verified in the video [Recording_testcase_passed.avi](Recording_testcase_passed.avi) for better validation.

