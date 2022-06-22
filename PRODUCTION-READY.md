Description
 
Additional steps for production read deployment. 


**Steps for Production-ready code**

1. Code Management: Need to export the training code
 from jupyter notebooks into python scripts. Add version control. 
2. CI/CD pipeline: Integrating into continuous integration and continuous
 development 
3. Adding unit test cases and static code analysis.
4. Data management: Data versioning, exporting data into database.
5. Adding logging module to track the metrics.
6. Automatic model training and validation of newly trained model.
7. Model profiling: Need to add Model registry for versioning the trained
 Models.
7. Need to migrate the existing api server to production api server.
8. Need to add load-balancer to handle multiple requests.
9. Scaling the api servers: Orchestration of built docker containers(micro
 -services).
10. Adding authentication module for validation of users who access the api
 server end point.
11 Using web tokens for defining the user rights who access the api
 endpoint.
