import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
import random
import datetime

class GenerateRandomSalesData(beam.DoFn):
    def process(self, element):
        # Generate one random sales record as CSV line
        order_id = random.randint(1000, 9999)
        customer_id = random.randint(10000, 99999)
        branch_id = random.randint(1, 5)
        order_date = datetime.datetime.now().strftime('%Y-%m-%d')
        sales_channel = random.choice(['online', 'offline'])
        total_amount = round(random.uniform(10.0, 5000.0), 2)
        # CSV format: order_id,customer_id,branch_id,order_date,sales_channel,total_amount
        csv_line = f"{order_id},{customer_id},{branch_id},{order_date},{sales_channel},{total_amount}"
        yield csv_line

pipeline_options = PipelineOptions(
    runner='DataflowRunner',  # or DirectRunner for local testing
    project='inspired-parsec-461804-f9',
    region='asia-east1',
    temp_location='gs://fast-fashion/temp',
    staging_location='gs://fast-fashion/streaming-sales-data',
    job_name='random-sales-csv-' + datetime.datetime.now().strftime('%Y%m%d%H%M%S'),
)

with beam.Pipeline(options=pipeline_options) as p:
    (
        p
        | "Create seed" >> beam.Create([None] * 100)  # Generate 100 random records
        | "Generate random sales data" >> beam.ParDo(GenerateRandomSalesData())
        | "Write to GCS as CSV" >> beam.io.WriteToText(
            'gs://fast-fashion/streaming-sales-data/temp/random_sales',
            file_name_suffix='.csv',
            shard_name_template='-SS-of-NN'
        )
    )
