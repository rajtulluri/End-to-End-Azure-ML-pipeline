# End-to-End-Azure-ML-pipeline

## A sample End to End Azure ML pipeline deployed on heroku.

### ML studio experiment and Web service

The Machine Learning model built on Azure ML studio, predicts the Adult income category (>50k or <=50k) using a tuned and validated Two-class boosted Decision tree model. The trained model is converted to an Azure web service.

Two images below are the ML studio pipelines
1. The training experiment
2. The predictive experiment (web service)

The Web service offered by Azure is a paid service, hence the API no longer exists. Please create your own Azure Web service based on the image and save the URL and API key in the respective files under resources folder.

### Dash app (python)

A Dash app is coded to post requests to the Azure web service created. The dash app is deployed on Heroku.
The file structure of the app is,

    __ app.py
    __ Layouts
      |_ layout.py
      |_ tab1_layout.py
      |_ tab2_layout.py
    __ requirements.txt
    __ Procfile
    
The app file contains the main server code along with callback functions for dynamic API calls.
The Layouts folder contains various layout files for the app to render.

### Heroku deployment

#### Conda environment
Fork the repository, create a conda env
 
    conda create -n env_name python=3.6
    
Activate the env using,

    conda activate env_name
    
Install the following dependencies in the env using pip

    dash
    pandas
    numpy
    gunicorn
    flask
    urllib

Use the following command

    pip install _package_
    
Create a file named Procfile and fill its contents with,

    web: gunicorn app:server

The Procfile has the instance of the server which the heroku platform will run
Create a new file requirements.txt with a list of all dependencies,

    pip freeze > requirements.txt
    
Run the following commands in succession to deploy the app on heroku

    heroku create my_app
    git add .
    git commit -m "Initial push"
    git push heroku master
    heroku ps:scale web=1
    
The heroku server will provide the deployed application's link.
The app above can be viewed at - https://azure-ml-pipeline.herokuapp.com/

#### OS environment
Fork the repository, and follow the steps,
Install the following dependencies using pip

    dash
    pandas
    numpy
    gunicorn
    flask
    urllib

Use the following command

    pip install _package_
    
Create a file named Procfile and fill its contents with,

    web: gunicorn app:server

The Procfile has the instance of the server which the heroku platform will run
Create a new file requirements.txt with a list of all dependencies,

    pip freeze > requirements.txt
    
Run the following commands in succession to deploy the app on heroku

    heroku create my_app
    git add .
    git commit -m "Initial push"
    git push heroku master
    heroku ps:scale web=1
    
The heroku server will provide the deployed application's link.
