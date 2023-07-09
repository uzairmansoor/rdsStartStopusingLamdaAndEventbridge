import boto3
import botocore
import os
import json
import sys
import logging

rds = boto3.client('rds')

dbInstancelist = ["devops-poc-db-us-east-1"]
def lambda_handler(event, context):
  action = event.get("action")
  for i in range(len(dbInstancelist)):   
    if (action == "stop"):
      response  = rds.stop_db_instance(DBInstanceIdentifier=dbInstancelist[i])  	 
    elif (action == "start"):
      response  = rds.start_db_instance(DBInstanceIdentifier=dbInstancelist[i])
  return dbInstancelist
