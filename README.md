# ideku_demo
 This assignment is for ideku interview. In this repo, it contains the automation test cases for the target website

 
## Target:  
 The url: https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
 The purpose is to test the function of the login page

 
## Test cases:  
 In the test case script, it contains the following test cases:   
 - Try login with correct username and password  
 - Try login with incorrect username and password
 - Try login without input username and password

 
## Test structure:
 The test is using page-object pattern: it contains tests and pages directory:  
 - tests: contains all the test cases  
    - BaseTest: It defines the setup and teardown functions for the tests  
	- LoginTest: It defines the test cases. 
	
 - pages: contains the elements and functions of the pages  
	- BasePage: It contains the common functions of all the pages. and each other pages will implement this.  
	- LoginPage: Define the identifier of username, password, submit button, and error toast. It also contains the functions to input username, password, check the error message.  
	- DashboardPage: It defines the check to verify the dashboard page is loaded  

 Besides the two directories, there's another folder for the test report: 
 - reports: directory for test reports


## How to execute the automation test:  
 The automation test cases are written in python, with selenium package. And the following are steps for executing the automation test:  
 1. Enter the project folder, and create a virtual env to make the environment clear: `python -m venv venv`  
 2. Activate the virtual env: `.\venv\Scripts\activate`   
 3. Install the required packages from the requirement file: `pip install -r requirement.txt`  
 4. Open IDE (I use PyCharm), and execute the `test_login.py` for testing  
 5. Or can use cmd tools and execute `pytest --html=reports/report.html` to run tests and create test report after execution  
