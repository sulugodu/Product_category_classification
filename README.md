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

Steps involved for data analysis.

1. Data cleaning
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

**Start training and save the trained Model (optional)** 

Run all the cells from `training.ipynb` to start the training and save the
pickle file at `trained_model\model.pickle`.

**Building the product api server** 

Step 1. Make sure that the trained model in the pickle format should be present
 at 
`trained_model\model.pickle`

Step 2. I am using docker container for creating an micro service for hosting
the api server. Using the Docker file present in the current directory to define the
product api endpoint and all the required server configurations are defined
 in `docker-compose.yml`. 

Build the product api server and start the server by the below command \
`docker compose up` 

Product API end point will be running at `http://localhost:5000/products`. 

**Request format**

example_input_data = 
payload = {'input_data': pd.DataFrame({'id': [<product id>],'main_text
': [<main_text>], "add_text":[<add_text>],"manufacturer":[<manufacturer>]}).to_json(orient='index')}

**Response format**

`result: {'prediction': <product id>:<product category> , 'status': <status
 message>}`

Product id is used as a reference for mapping the predictions results.
Request data is validated and verified before processing.
Depending of prediction results different status message is sent as a response.

Different status messages are mentioned below

status='OK': if the model predicts the product category successfully
status='Error in the service': exception in the model prediction
status='Error in the input data': error in the request data


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
 
