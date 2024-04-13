
import os 
import boto3

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export_data_to_s3(data, **kwargs) -> None:
    """
    Template for exporting data to a S3 bucket.
    Specify your configuration settings in 'io_config.yaml'.

    Docs: https://docs.mage.ai/design/data-loading#s3
    """
    file_clean = data[2]
    file = data[1]
    df = data[0]
    bucket_name = os.getenv('BUCKET_NAME')
    s3_client = boto3.client('s3')

    parts = file.split('/')
    object = '/'.join(parts[1:])

    print(object)


    try:
        s3_client.upload_file(file, bucket_name, object)
        
    except Exception as e:
        print(f"Failed to upload {file} to {bucket_name}/{object}: {e}")