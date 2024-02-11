"""BigQuery data loader."""

import pandas
from google.cloud import bigquery


def get_data(query: str, gcloud_project: str) -> pandas.DataFrame:
    """Get data from bigquery."""
    data_frame = (
        bigquery.Client(project=gcloud_project)
        .query(query=query)
        .result()
        .to_dataframe()
    )
    return data_frame
