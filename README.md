Description
 
Author: Mahesh Sulugodu Manjunatha

Machine learning project for product category classification. 


**INSTALLATION**

1. Python version: 3.7 
1. Please install Docker.

The required packages are listed in the requirements.txt. Install the
packages as below.
 
`pip install -r requirements.txt`


**Project description:**

**Preparation of Training data  and Exploratory data analysis**

Steps involved for data pre-processing.

1. data cleaning
2. Exploratory data analysis
3. Feature engineering
4. Text data pre-processing
4. Training data preparation

All the above steps are defined in the jupyter notebook.`training.ipynb`



**Training the ML model**

Steps involved in training pipeline.

1. remove_punctuations
2. remove_numbers
3. remove_stopwords
4. word_lemmatizer
5. stemmer
6. CountVectorizer
7. tfid_vector
8. MultinomialNB() 

The above training pipeline is built and training scripts are defined in the
jupyter notebook. `training.ipynb`

**Trained Model** 

Already the trained model is available at `trained_model\model.pickle`

**Start training and save the trained Model** 

Run all the cells from `training.ipynb` to start the training and save the
pickle at `trained_model\model.pickle`.

**Building the product api server** 

Step 1. Make sure the trained model in the pickle format present at 
`trained_model\model.pickle`

Step 2. I am using docker containers as a micro service for hosting the api
server. Using the Docker file present in the current directory to define the
product api endpoint and all the required server configurations are defined
 in `docker-compose.yml`. 

Start product api server by the command \
`docker compose up` 

Product API end point will be running at `http://localhost:5000/products`.
Product id is used as a reference for mapping the predictions.

**Testing the api:** 
Run the `Testing the Product Api Server` cell in the jupyter notebook `training
.ipynb` for testing the api end point.


**Unit test for testing the api end point:**  `tests\test_product.py` 
Run `pytest` 


**Python packages description**

`src` : Contains all the essential scripts for building the api server.
`tests` : Unit test scripts for testing api endpoint.
`trained_model`: contains a pickle trained model.

**Python module description**

`src\api.py` : Contains all the essential functions for building the api
 server.
`src\model.py` : Contains functions for loading the pickle model.
`src\pre_processing.py` : Pre-processing pipeline for training..
`src\utils.py` : Util function for RESTAPI.
 
