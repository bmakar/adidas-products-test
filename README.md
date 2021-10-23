# PRODUCTS API tests #
### SETUP ENVIRONMENT 

1. Download products repo https://bitbucket.org/adichallenge/products-docker-composer/src/master/

    
4. Run docker-compose:

    ``docker-compose up -d``
    
### SETUP FRAMEWORK

1. Install python 3.x
2. Create virtual env in root directory of a project: 
   ``python3 -m venv /path/to/new/virtual/environment``
3. Install requirements: 
   ``pip install -r requirements.txt``
### RUN PRODUCTS API LOCALLY 
To run **products_api_tests** use:

 1. behave_runner_local.py
 
 2. command line command "behave"

#### Example of command:

```
    behave products_api_tests 
```
