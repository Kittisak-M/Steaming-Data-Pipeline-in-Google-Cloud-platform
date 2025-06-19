import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions, SetupOptions, StandardOptions
import json
import logging
import datetime


class ParseJson(beam.DoFn):
    def process(self, element):
        try:
            record = json.loads(element.decode('utf-8'))
            yield record
        except Exception as e:
            logging.error(f"Failed to parse JSON: {e}")


job_name = 'pubsub-to-gcs-json-' + datetime.datetime.now().strftime('%Y%m%d%H%M%S')

pipeline_options = PipelineOptions(
    runner='DataflowRunner',
    project='inspired-parsec-461804-f9',
    region='asia-east1',
    temp_location='gs://fast-fashion/temp',
    staging_location='gs://fast-fashion/streaming-sales-data',
    job_name=job_name,
)

# ✅ Set streaming mode in code
pipeline_options.view_as(StandardOptions).streaming = True
pipeline_options.view_as(SetupOptions).save_main_session = True

with beam.Pipeline(options=pipeline_options) as pipeline:
    (
        pipeline
        | "Read from Pub/Sub" >> beam.io.ReadFromPubSub(
            topic='projects/inspired-parsec-461804-f9/topics/data-demo'
        ).with_output_types(bytes)

        | "Parse JSON" >> beam.ParDo(ParseJson())

        | "Convert to JSON lines" >> beam.Map(json.dumps)

        # ✅ Add dummy key to prepare for grouped write
        | "Attach dummy key" >> beam.Map(lambda x: (None, x))

        # ✅ Group by key (required in streaming write)
        | "Group by key" >> beam.GroupByKey()

        # ✅ Flatten for output
        | "Flatten values" >> beam.FlatMap(lambda kv: kv[1])

        | "Write to GCS" >> beam.io.WriteToText(
            'gs://fast-fashion/streaming-sales-data/output/data',
            file_name_suffix='.json',
            shard_name_template='-SS-of-NN'
        )
    )
