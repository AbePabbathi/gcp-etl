from pyspark.sql.functions import lit
from datetime import datetime
# add load date
def addLoadDate(df):
    # test comment
    df = df.withColumn("_loadDate",lit(datetime.now()))
    return df