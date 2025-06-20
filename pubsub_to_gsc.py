import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
import json
import logging
from apache_beam.transforms.window import FixedWindows
from apache_beam.transforms.trigger import AfterProcessingTime, AccumulationMode, AfterCount, Repeatedly

class ParseJson(beam.DoFn):
    def process(self, element):
        try:
            record = json.loads(element.decode('utf-8'))
            yield record
        except Exception as e:
            logging.error(f"Failed to parse JSON: {e}")

pipeline_options = PipelineOptions(
    streaming=True,
    runner='DataflowRunner',
    project='inspired-parsec-461804-f9',
    region='asia-east1',
    temp_location='gs://fast-fashion/temp',
    staging_location='gs://fast-fashion/streaming-sales-data',
    job_name='pubsub-to-gcs-json'
)

with beam.Pipeline(options=pipeline_options) as pipeline:
    (
        pipeline
        | "Read data from Pub/Sub" >> beam.io.ReadFromPubSub(
            topic='projects/inspired-parsec-461804-f9/topics/data-demo'
        )
        | "Parse JSON" >> beam.ParDo(ParseJson())
        | "Convert to JSON lines" >> beam.Map(lambda x: json.dumps(x))
        | "Window & Trigger" >> beam.WindowInto(
            FixedWindows(60),  # Still needed to support WriteToText
            trigger=Repeatedly(AfterCount(1)),  # Trigger after each element
            accumulation_mode=AccumulationMode.DISCARDING  # Don't keep old elements
        )
        | "Write to GCS" >> beam.io.WriteToText(
            'gs://fast-fashion/streaming-sales-data/output',
            file_name_suffix='.json',
            shard_name_template='',
            num_shards=1
        )
    )
