# python API tests development
Python API tests

https://stackoverflow.com/a/41972262/1546574 
https://stackoverflow.com/a/41972262/1546574 
https://docs.python.org/3/library/venv.html  



Get virtualEnv installed.
> python3 -m venv /path/to/new/virtual/environment

> source venv/bin/activate

Install all project dependencies with 
> pip install -r requirements.txt



## pytest runner setup 
Pytest runner is defined as below
![pytest runner](./readme/2021-12-14_pytest_config_api.png?raw=true "runner")


## allure report analysis
Allure command-line installation bundle can be taken from here:
 [docs.qameta.io](https://docs.qameta.io/allure/#_installing_a_commandline)    


As soon as tests executed -to generate prettified report- 
one should open root project folder,
ensure that **allure-results** folder have some data
![allure results](./readme/allure_artifacts.png?raw=true "results")
and execute 
`allure serve` command using allure command-line tool

![allure results](./readme/api_allure_res01.png?raw=true "results")
![allure results](./readme/api_allure_res02.png?raw=true "results")
![allure results](./readme/api_allure_res03.png?raw=true "results")

