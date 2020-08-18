# Python Flask Service Blueprint
This is a basic blueprint that contains all the configuration and boilerplate setup that you will need to build a python flask service

### Configuration
- Create a .env file in the root of the application directory
- Add in the following environment variables

FLASK_APP=app.py  
FLASK_ENV=development  
SECRET_KEY=5dafc04c-0e61-44df-b940-7f2cb61ede00  
LESS_BIN=/usr/local/bin/lessc  
ASSETS_DEBUG=False  
LESS_RUN_IN_DEBUG=False  
COMPRESSOR_DEBUG=True  
POSTGRES_URI=postgres+psycopg2://postgres:@localhost:5432/test 

### Running the application
```shell
$ git clone git@github.com:Andre153/python_flask_boiler.git
$ cd python_flask_boiler
$ pipenv shell
$ pipenv update
$ sh start.sh
```



