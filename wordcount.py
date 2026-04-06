# from e11: reddit_relative_hiny.py
import sys
assert sys.version_info >= (3, 8) # make sure we have Python 3.8+
from pyspark.sql import SparkSession, functions, types
# from e12 descritpion
import string, re
wordbreak = r'[%s\s]+' % (re.escape(string.punctuation),)  # regex that matches spaces and/or punctuation

# spark-submit wordcount.py wordcount-1 output

def main(in_directory, out_directory):
    # 1. Read lines from the files 
    df = spark.read.text(in_directory)

    # 2. split the lines into words with the re
    #  .lower(str) all to lower-case (case doewn't matter)
    #  split(str, pattern) split str
    #  explode(col) ret new row  all, {}, NULL
    words = df.select(functions.explode(functions.split(functions.lower(df['value']), wordbreak)).alias('word'))
    # 5. rm empty ones
    words = words.filter(words['word'] != '')

    # 3. count each word occurance
    counts = words.groupBy('word').count()  # .count() creates a coln name 'count'

    # 4. decr order, then alphabetically if tie
    sorted = counts.orderBy(functions.desc('count'), functions.asc('word'))

    # 6. results to CSV
    #sorted.show(20, truncate=False)
    sorted.write.csv(out_directory, header=True, mode='overwrite')


# from e11: reddit_relative_hiny.py
if __name__=='__main__':
    in_directory = sys.argv[1]
    out_directory = sys.argv[2]
    spark = SparkSession.builder.appName('WordCount').getOrCreate()
    assert spark.version >= '3.2' # make sure we have Spark 3.2+
    spark.sparkContext.setLogLevel('WARN')

    main(in_directory, out_directory)