import os

import pandas
import google.cloud.storage as storage

import load.local.base


def get_data(file_path: str, gcloud_project: str, bucket_name: str) -> pandas.DataFrame:
    """Get data from google cloud storage."""
    file_name = file_path.split("/")[-1]
    blob = (
        storage.Client(project=gcloud_project)
        .bucket(bucket_name=bucket_name)
        .blob(blob_name=file_path)
    )
    blob.download_to_filename(filename=file_name)
    output = load.local.base.get_data(file_path=file_path)
    os.remove(file_name)
    return output
