from sky import Sky
import os
import logging
from datetime import datetime, timedelta
import pandas as pd
import google.cloud.bigquery

try:
    bigquery_client = google.cloud.bigquery.Client()
    sky = Sky(
        api_key=os.getenv('BB_API_KEY'),
        token_path='.sky-token',
        credentials={
            "client_id":os.getenv('CLIENT_ID'),
            "client_secret":os.getenv('CLIENT_SECRET'),
            "redirect_uri":os.getenv('REDIRECT_URI'),
        })

    notes = sky.getAdvancedList(73089)
    notes['Comment'] = notes['Comment'].str.replace('\n', ' ')
    notes['Comment'] = notes['Comment'].str.replace('\r', ' ')
    notes['Comment'] = notes['Comment'].str.replace('\t', ' ')
    notes['Comment'] = notes['Comment'].str.replace('\"', ' ')
    notes['Comment'] = notes['Comment'].str.replace('\\', ' ')
    notes['Comment'] = notes['Comment'].str.replace('\'', ' ')
    notes['Comment'] = notes['Comment'].str.replace(',', '')

    notes.to_csv('data/official_notes.csv', index=False)
    
    table_id = 'dtsdatastore.BlackbaudDataExports.OfficialNotes'

    job_config = google.cloud.bigquery.LoadJobConfig(
        source_format=google.cloud.bigquery.SourceFormat.CSV,
        write_disposition=google.cloud.bigquery.WriteDisposition.WRITE_TRUNCATE,
        autodetect=True,
    )

    with open('data/official_notes.csv', 'r') as file:
        data = file.read()
        data = data.replace("\\N", "")
        data = data.replace("\"", "")

    with open('data/official_notes.csv', 'w') as file:
        file.write(data)

    with open('data/official_notes.csv', 'rb') as source_file:
        job = bigquery_client.load_table_from_file(
            source_file, table_id, job_config=job_config
        )
        job.result()  # Wait for the job to complete.

    table = bigquery_client.get_table(table_id)  # Make an API request.
    logging.info(
        "Loaded {} rows and {} columns to {}".format(
            table.num_rows, len(table.schema), table_id
        )
    )

except Exception as e:
    logging.error(e)
    raise e