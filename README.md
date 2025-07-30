### Network Security Projects For Phishing Data
pip install -r requirements.txt
to run python - python file_name.py
to create conda environment - conda create --name myenv python=3.9
to activate conda env   - conda activate venv/ 
use -- mlflow ui - for mlflow view

"C:\Program Files\Amazon\AWSCLIV2\aws.exe" configure  --if not running in environment to configure for s3 bucket
 
aws id--vipnce45@gmail.com   Manu@6950
pip install --upgrade pymongo

uvicorn app:app --reload -- to run fastapi file

1. make all the required directory
-Network_Data
-networksecurity
   cloud
   components
      data_ingestion.py
   constants
      training_pipeline
   entity
      artifact_entity.py
      config_entity.py
   exception
      exception.py
   logging
      logger.py
   pipeline
   utils
-notebooks   


make repository in ECR


setup github secrets:

AWS_ACCESS_KEY_ID=
AWS_SECRET_ACCESS_KEY=
AWS_REGION=us-east-1
AWS_ECR_LOGIN_URI=107548170487.dkr.ecr.us-east-1.amazonaws.com/networksecurityvk
ECR_REPOSITORY_NAME=simple-app

Docker Setup In EC2 commands to be Executed
#optinal

sudo apt-get update -y

sudo apt-get upgrade

#required

curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker ubuntu

newgrp docker