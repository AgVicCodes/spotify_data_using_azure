import glob
from functools import reduce
from pyspark.sql import SparkSession as SS
from pyspark.sql import DataFrame
from pyspark.sql.functions import col, explode, to_timestamp
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, TimestampType

spark = SS.builder.getOrCreate()

def merge_df(file_path):

    schema = StructType([
        StructField('artist_name', StringType()),
        StructField('album_name', StringType()),
        StructField('track_name', StringType()),
        StructField('duration', IntegerType()),
        StructField('played_at', TimestampType()),
        StructField('id', StringType()),
        StructField('popularity', IntegerType()),
        StructField('track_type', StringType())
    ])

    temp_df = spark.createDataFrame([], schema)

    df = []

    for file in file_path:

        try:
            temp_listening = spark.read.option('multiLine', True).json(file)
        except Exception as e:
            print(f'Error processing file {file}: {e}')

        temp_listening_exploded = temp_listening.select(explode('items').alias('item'))

        temp_listening_flattened = temp_listening_exploded\
        .withColumn('artist', explode('item.track.artists'))\
        .select(
            col('artist.name').alias('artist_name'),
            col('item.track.album.name').alias('album_name'),
            col('item.track.name').alias('track_name'),
            col('item.track.duration_ms').alias('duration'),
            # col('item.played_at').alias('played_at'),
            to_timestamp('item.played_at').alias('played_at'),
            col('item.track.id').alias('id'),
            col('item.track.popularity').alias('popularity'),
            col('item.track.type').alias('track_type')
        )

        temp_listening_flattened = temp_listening_flattened.withColumn('played_at', to_timestamp('played_at'))

        df.append(temp_listening_flattened)

    temp_df = reduce(DataFrame.unionAll, df) 

    return temp_df

path = glob.glob(f'data/recently_played*.json')

print(merge_df(path).count())