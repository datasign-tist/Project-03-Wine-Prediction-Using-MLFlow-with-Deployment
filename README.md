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

## Now, we will follow the workflow that will be processed for each data science project step.

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
F. Update the components folder needed in that stage. Downloading/Adding Features/EDA/PCA, etc.  
G. Update the pipeline for that stage.  
H. Update the main.py

( Perform all these steps for the below Stages, and then we will create our app.py for deployment. )

## STAGE 02: Data Validation

In this stage, we will perform all operations, but will update the schema.yaml file to add the schema of the data.

## STAGE 03: Data Transformation

Perform all the above workflow.

## STAGE 04: Data Modelling





























