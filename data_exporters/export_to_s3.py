from pandas import DataFrame
from os import path
import os 
import boto3

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export_data_to_s3(data, **kwargs) -> None:
    """
    """
    
    data = data[1]
    file_clean = data['file_clean']
    file_name = data['file']

    bucket_name = os.getenv('BUCKET_NAME')
    s3_client = boto3.client('s3')

    parts = file_name.split('/')
    object = '/'.join(parts[2:])



    try:
        s3_client.upload_file(file_clean, bucket_name, object)
        
    except Exception as e:
        print(f"Failed to upload {file} to {bucket_name}/{object}: {e}")

    data['bucket_name'] = bucket_name
    data['s3_object'] = object

    return data

@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    bucket_name = output['bucket_name']
    object = output['s3_object']

    s3 = boto3.client('s3')
    response = s3.head_object(Bucket=bucket_name, Key=object)
    assert response, f"Object ({object}) could not be found in S3 bucket ({bucket_name})"
