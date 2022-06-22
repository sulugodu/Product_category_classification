Description
 
Additional steps need to take for deployment in the production environment. 


**Steps for Production-ready code**

1. Code Management: Need to export the training code
 from jupyter notebook into python scripts. Add version control. 
2. CI/CD pipeline: Integrating the code into continuous integration and
 continuous development pipeline.
3. Adding unit test cases and static code analysis.
4. Data management: Data versioning, exporting the data into database.
5. Adding logging modules for tracking the training metrics.
6. Automatic model re-training and validation.
7. Model profiling: Need to add trained models into Model registry for
 versioning.
7. Need to migrate the existing development api server to production api
 server.
8. Need to add load-balancer to handle multiple requests.
9. Scaling the api servers: Orchestration of built docker containers(micro-services).
10. Adding authentication modules for validation of users who access the api
 server end point.
11 Using web tokens for defining the access rights for users accessing the api
 endpoint.
