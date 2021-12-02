# Automation Setup
## Code setup

### Local environment

1.  Open your terminal
2.  Navigate to the project folder:  `cd <path>/paf`
3.  Install the python dependencies:  `pip install -r requirements.txt`
4.  Install the playwright browser bindings:  `playwright install`

### Local environment runs

1.  In the terminal, navigate to the paf project location
2.  Run the following command to add the environment variable to the current terminal session:  `export ENVIRONMENT="<some env>"`
    1.  Alternatively you can add that environment variable to the system/user itself in windows
    2.  For more information about environment variables, please google:  `How to add environment vairables on [OS type]`
3.  Run the tests in the following ways:
    1.  To run ALL tests, run the following command:  `pytest`
    2.  To run a specific tag, run the following command:  `pytest -m login`  where “login” is the tag name
    3.  To run tests by filters with logical operators:
        1.  `pytest -m "not login"`  Will run all tests that do not have the tag  `login`
        2.  `pytest -m "login and api"`  Will run all tests that have both tags at the same time
        3.  `pytest -m "login or api"`  Will run all tests that have at least 1 of the 2 tags
    4.  To run tests in a specific file:  `pytest tests/test_login_page.py`
    5.  To run a specific test from a file without using tags:  `pytest tests/test_playground.py::Tests::test_input`  where “Tests” is the class and “test_input” is the specific test
    6.  To run tests in headed mode:  `pytest -m login --headed`
    7.  To run tests on a specific browser (default is chromium):  `pytest -m login --browser firefox`
        1.  To run tests on multiple browsers: ``pytest -m login --browser firefox --browser chromium --browser webkit`
        2.  Playwright supports Chrome (chromium), Firefox and Safari/Mobile (webkit)   
    8.  To run tests and get a list of the slowest tests run the tests in the following way:  `pytest -m login --durations=2 --durations-min=0.1`  where  `--durations=2`  are the number of tests to be displayed and  `--durations-min=0.1`  is the minimum duration above which to collet the info in seconds 
4.  After test execution, a reports folder will be created which will have a  `report.html`  file and folders containing the screenshots and video recordings of the failing tests.
    1.  The report will display the screenshots and the videos of the failing tests as embedded so even if  `report.html`  is moved or sent through an email, it should still contain them

### Docker environment runs

1.  Open your terminal
2.  Navigate to the project folder:  `cd ........ /paf`
3.  Create the docker image:  `docker build -t paf .`
    1.  `-t paf`  tells docker to name the docker image  `paf`
4.  After the image is created, make sure you have a folder called  `reports`  in your current path
5.  To run all tests from the docker image:  `docker run -d -e ENVIRONMENT="<some env>" --rm -v ${PWD}/reports:/paf/reports --name pff paf --template=html1/index.html`
    1.  `-d`  tells docker to run in detached mode
    2.  `-e ENVIRONMENT="<some env>"`  tells docker to add an environment variable called  `ENVIRONMENT`  with the value  `<some env>`
    3.  `--rm`  tells docker to remove the container after it finished
    4.  `-v ${PWD}/reports:/paf/reports`  tells docker to attach your current path to the  `reports`  folder to the  `/paf/reports`  folder inside docker to have access to the reports after completion
        1.  `${PWD}`  will print your current working directory and will work on all linux and Mac systems
        2.  For Windows PowerShell use:  `-v "$((Get-Item reports).FullName)":/paf/reports`
        3.  For Windows Command prompt use:  `-v (@echo %cd%\reports):/paf/reports`
    5.  `--name pff`  tells docker to name the started container  `pff`
    6.  `paf`  is the docker image we are executing which we named in step 3.
    7.  `--template=html1/index.html`  specifies the to use as a global template from the python packages
6.  The docker container can take all the filters and flags from the normal pytest run for it’s execution such as:
    1.  `docker run -d -e ENVIRONMENT="<some env>" --rm -v ${PWD}/reports:/paf/reports --name pff paf --template=html1/index.html -m=login`  will run all the tests marked with the  `login`  tag
        1.  Caveat, all flags must use the  `=`  operator to assign the values
    2.  `docker run -d -e ENVIRONMENT="<some env>" --rm -v ${PWD}/reports:/paf/reports --name pff paf --template=html1/index.html -m="not login"`  will execute exactly as the local version
    3.  `docker run -d -e ENVIRONMENT="<some env>" --rm -v ${PWD}/reports:/paf/reports --name pff paf --template=html1/index.html --browser firefox --browser chromium --browser webkit`  will run exactly as the local version
7.  While docker runs in detached mode, you will not have access to the console output. to get it, you must follow the logs:
    1.  `docker run -d -e ENVIRONMENT="<some env>" --rm -v ${PWD}/reports:/paf/reports --name pff paf --template=html1/index.html ;docker logs -f pff`
        1.  Caveat is that the colouring of the logs will not be done

### Running playwright in interactive browser mode with code generation

After the above local setup has been completed
1.  Run the following command to start the playwright interactive codegen browser:  `playwright codegen`
2.  The above browser and interactive code console will be displayed
    1.  Please note that this tool is best suited to formulate selectors and strategies to approach pages or to experiment potential scripts to interact with the page before transforming the code into the normal framework standard
3.  While the record button is running, all interactions on the page and all page navigations will be recorded in the form of code that can be executed to replicate those interactions.

# Framework and PyTest walkthrough

### File structure

As we can see, the project is comprised of 8 major directories and 9 root files.

1.  `api_tests`  is the folder that will contain automated api tests
2.  `bases`  is the folder that will contain the common settings and any base objects that may be needed
3.  `data`  is the folder that will contain information such as enums for users, or environments or any such information
4.  `endpoints`  is the folder that will contain the AOM (Api Object Model) which is essentially identical to the POM but is designed to be used for API endpoints and interactions
5.  `helpers`  is the folder that will contain any necessary helpers written for the project
6.  `page`  is the folder that will contain the actual page objects from the POM pattern
7.  `reports`  is the folder that will be populated with reports when tests complete execution
    1.  Note that this is for local test runs, this folder will be different for Jenkins docker runs. Please see the docker section of the code setup
8.  `tests`  is the folder than will primarily contain UI tests
    1.  Note, the folder can be renamed to  `ui_tests`  if desired
9.  `.dockerignore`  is the file that contains the list of items that will be ignored when performing a docker build
10.  `.gitignore`  is the file that contains the list of items to be ignored by git when committing work
11.  `__init__.py`  is the file that denotes a package in Python
12.  `conftest.py`  is the most important file which contains the bulk of the framework interaction as per the PyTest standard.
    1.  The aim is to have this file be a separate repository and package installed in the testing project and only be modified when new functionality must be added to the framework or fixes must be applied
13.  `Dockerfile`  is the file that defines how the docker image will be built
14.  `pytest.ini`  is the PyTest standard configuration file
15.  `requirements.txt`  is the file that defines the Python packages that need to be installed for the project to work
    1.  Note that the python package installation requires PyPi access unless all required packages are hosted locally in a manager such as Artifactory
16.  `sources.list`  is a linux sources file that defines what sources to be added to the package repository.

For more information about PyTest, please visit:  [https://docs.pytest.org/en/latest/contents.html](https://docs.pytest.org/en/latest/contents.html)

### Conftest.py file

The  `conftest.py`  file is the PyTest standard hooks and fixtures file that generally includes all framework functionality. The conftest.py file automatically gets injected into the tests based on the functionality and scope.
Note: the current conftest.py contains a custom versions of  [https://pypi.org/project/pytest-playwright/](https://pypi.org/project/pytest-playwright/)  with modifications and additional features.

### TestRail integration

The TestRail integration is currently not available but code has been put in place for its support. In the conftest.py file, identify the  `def test_listeners`  method and modify it there.

```python
@pytest.fixture(autouse=True, scope="function")  
def test_listeners(request):  
    yield  
  # request.node is an "item" because we use the default  
  #"function" scope  if request.node.rep_call.failed:  
        # TODO Testrail code for "fail" goes here  
  logging.info(f"executing test failed! {request.node.rep_call.longrepr.reprcrash.message}")  
    elif request.node.rep_call.passed:  
        # TODO Testrail code for "pass" goes here  
  logging.info(f"executing test passed {request.node.nodeid}")  
    elif request.node.rep_call.skipped:  
        # TODO Testrail code for "skipped" goes here  
  logging.info(f"executing test skipped {request.node.nodeid}")
```

In each of the conditionals above, code can be added to handle the TestRail API requests. The  `request`  object will have all of the information pertaining to the test at each point and status of the test. For example, different actions can be performed if a test passes as opposed to the test failing or being skipped.

**Note:**  This will run individually for each test which means that care must be given to the level of parallelization of the tests to ensure the TestRail server does not get overwhelmed.

Test description and long names are also supported:

```python
@pytest.mark.parametrize('email, password', [  
  (Users.ADMINISTRATOR["username"], Users.ADMINISTRATOR["password"]),  
  (Users.ACCOUNT_MANAGER["username"], Users.ACCOUNT_MANAGER["password"]),  
  (Users.MARKETEER["username"], Users.MARKETEER["password"]),  
  (Users.MERCHANDISER["username"], Users.MERCHANDISER["password"]),  
  (Users.PLANNER["username"], Users.PLANNER["password"]),  
  (Users.READ_ONLY["username"], Users.READ_ONLY["password"]),  
  (Users.CUSTOMER["username"], Users.CUSTOMER["password"])  
])
@pytest.mark.login  
def test_login(self, email, password):  
    """Login page very long description here for user"""  
	self.login_page.navigate_to_page()  
    self.login_page.click_login_redirect_button()  
    self.login_page.okta_login(email, password)  
    self.brands_page.click_avatar_button()  
    role = self.brands_page.get_profile_modal_role()  
    assert role.lower() in email.lower()
```

In the above code we can see the sequence  `"""Login page very long description here for user"""`. This is called a docstring and is parable inside any fixture, including the  `test_listeners`  area. This can be used to add long descriptive names to tests including extra data to be parsed and sent to TestRail as part of potential TestRail test creation if the test Does not already exist in TestRail. The exact point where the description can be obtained is  `request.node.rep_call.description`  which can be parsed as needed.

### Test Parallelization

The test parallelization is handled by a PyPi package called  [https://pypi.org/project/pytest-xdist/](https://pypi.org/project/pytest-xdist/)  which handles distributing the tests to defined workers.

The worker number definition is located inside the  `pytest.ini`  file under the flag  `-n 3`  which states that there should be 3 workers defined for the tests. This number can be bumped up to any level as long as there is an understanding that more workers essentially means more power for the docker container and the underlying system.

The test to worker distribution is done via the  `--dist loadscope`  flag which tells the tests how to handle the parallelism which is currently defined for classes.

-   `--dist no`: The default algorithm, distributing one test at a time.
-   `--dist loadscope`: Tests are grouped by **module** for _test functions_ and by **class** for _test methods_. Groups are distributed to available workers as whole units. This guarantees that all tests in a group run in the same process. This can be useful if you have expensive module-level or class-level fixtures. Grouping by class takes priority over grouping by module.
-   `--dist loadfile`: Tests are grouped by their containing file. Groups are distributed to available workers as whole units. This guarantees that all tests in a file run in the same worker.
    
What this means is that classes will be distributed to workers instead of individual tests which allows for sequential tests to be performed if necessary, by grouping the tests into a flow inside the same class.

As an example, (at the time of writing this) there are 3 files for tests and each with it’s own class, and since 3 workers were defined, each class will be executed in it’s own worker and in that worker in the class, the tests will be run sequentially. A good rule of thumb is to group tests into flows for e2e functionality and separate the flows in multiple classes to achieve a fast result.

The  `-n 3`  and  `--dist loadscope`  can be removed from the  `pytest.ini`  file and passed in to the tests dynamically as per the local and docker runs example section.

A good rule of thumb if running on multiple browsers at the same time is to bump up the executor number by a factor of  `n (where n is the number of browsers)`  to ensure the tests will not take very long to execute.

**Note:**  This is valid for all the flags in the  `pytest.ini`  file except the  `--report=reports/report.html`  which must be loaded at PyTest initialization AFTER the  `--output reports`  flag

**Note 2:**  The fixture scope level  `session`  is not inherently supported by test distribution if the fixture itself requires blocking I/O operations. This is due to the fact that all tests run those fixtures regardless of the fact that they were already ran or not. A good workaround for this can be found here  [https://pypi.org/project/pytest-xdist/#making-session-scoped-fixtures-execute-only-once](https://pypi.org/project/pytest-xdist/#making-session-scoped-fixtures-execute-only-once)  using FileLocks. The locking functionality has already been implemented in the framework and only needs to be used as needed.

### Coding standards

The coding style standards followed by this project will be in line with the python PEP-8 standards.  [https://www.python.org/dev/peps/pep-0008/](https://www.python.org/dev/peps/pep-0008/)

For more information about the PlayWright please follow:  [https://playwright.dev/python/docs/intro/](https://playwright.dev/python/docs/intro/)
        

### Example report

The following is an example report generated by the tests with some intentional failures to display the screenshot and video capture capabilities of the test framework.

NOTE: The  `playground`  tests are just example tests for general playwright use cases
