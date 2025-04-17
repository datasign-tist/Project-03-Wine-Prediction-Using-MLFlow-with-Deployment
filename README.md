# Project 03: Wine Prediction Using MLFlow with Deployment

This repository contains a comprehensive end-to-end data science project that follows a complete machine learning lifecycle pipeline. It leverages tools such as DagsHub for version control and collaboration and MLflow for experiment tracking and model management, and includes deployment capabilities locally and on AWS.

------------------------------------------------------------------------------------------------------------
## Steps to construct the folder structure and required files.

1. Create the template.py file --> This will help us avoid manually adding all the required folders and files.
2. Create the requirements.txt ( pip install -r requirements.txt) --> That contains all the required libraries needed, and it will install them in one go.
3. Create the setup.py --> requirement.txt file. It will look for this file to install our package as a local package.
4. Add the Logging Functionality in the constructor file inside src/project_name --> This customer logging function will help us debug and track our code when deployed on remote servers.
5. Add the common.py file inside the  utils --> The Utility file helps us reuse the function ( Professional OOps Programming ). We have used the config-box and ensure-annotation for better standard coding.

------------------------------------------------------------------------------------------------------------

## Now, we will follow the workflow process for each data science project step.

### The Workflow Structure :
A.  Update config.yaml  
B.  Update schema.yaml  
C.  Update params.yaml  
D.  Update the entity  
E.  Update the configuration manager in the src config  
F.  Update the components  
G.  Update the pipeline  
H.  Update the main.py  
I.  Update the app.py  

We will perform all the above operations for each data-science project stage.  
We will perform modular coding (OOPs Programming).

------------------------------------------------------------------------------------------------------------

## STAGE 01: Data Ingestion 

A. We will add all our configurations to this file. ( We will create an artifact folder to save our outputs.)  
B. We don't need this at the moment.  
C. We don't need this at the moment.  
D. We need to create the entity ( A return type of a function ) to read the config.yaml, we need to create the constructor file inside src/project_name/constants. This will help us locate all the yaml paths in our code.  
E. Add the configuration manager. It will return all the variables, add the data, and check the return type.  
F. Update the components folder needed in that stage, such as downloading/Adding Features/EDA/PCA, etc.  
G. Update the pipeline for that stage.  
H. Update the main.py

( Perform all these steps for the below Stages, and then we will create our app.py for deployment. )

## STAGE 02: Data Validation

In this stage, we will perform all operations, but will update the schema.yaml file to add the schema of the data.

## STAGE 03: Data Transformation

Perform all the above workflow.

## STAGE 04: Data Modelling

Update the Schema ( for the target variable ) and params.yaml for the hyperparameters. 

## STAGE 05: Model Evaluation

In this important stage, we will configure MLflow and Dagshub to run and understand the model outputs. 

### MLflow 
A. Documentation:(https://mlflow.org/docs/latest/index.html)
### CMD
B. mlflow ui
### dagshub
C. Go to Dagshub: (https://dagshub.com/) and run below to export as env variables:

Add the first 2 lines inside the components/Stage05_Model_Evaluation.py file.

```
import dagshub
import mlflow
dagshub.init(repo_owner='datasign-tist', repo_name='Project-03-Wine-Prediction-Using-MLFlow-with-Deployment', mlflow=True)
```
#### Run it locally using the app.py code, where we have used the Bootstrap website to create an HTML file for input and output, using Flask.
------------------------------------------------------------------------------------------------------------

## Follow the process below to run it in the AWS ( CICD Deployment ) with GitHub Actions.

## 1. Login to AWS console.

## 2. Create IAM user for deployment

	#with specific access

	1. EC2 access : It is virtual machine

	2. ECR: Elastic Container registry to save your docker image in aws


	#Description: About the deployment

	1. Build docker image of the source code

	2. Push your docker image to ECR

	3. Launch Your EC2 

	4. Pull Your image from ECR in EC2

	5. Lauch your docker image in EC2

	#Policy:

	1. AmazonEC2ContainerRegistryFullAccess

	2. AmazonEC2FullAccess

	
## 3. Create ECR repo to store/save docker image
    - Save the URI: 566373416292.dkr.ecr.ap-south-1.amazonaws.com/mlproj

	
## 4. Create EC2 machine (Ubuntu) 

## 5. Open EC2 and Install docker in EC2 Machine:
	
	
	#optinal

	sudo apt-get update -y

	sudo apt-get upgrade
	
	#required

	curl -fsSL https://get.docker.com -o get-docker.sh

	sudo sh get-docker.sh

	sudo usermod -aG docker ubuntu

	newgrp docker
	
# 6. Configure EC2 as self-hosted runner:
    setting>actions>runner>new self hosted runner> choose os> then run command one by one


# 7. Setup github secrets:

    AWS_ACCESS_KEY_ID=

    AWS_SECRET_ACCESS_KEY=

    AWS_REGION = us-east-1

    AWS_ECR_LOGIN_URI = demo>>  566373416292.dkr.ecr.ap-south-1.amazonaws.com

    ECR_REPOSITORY_NAME = simple-app




























