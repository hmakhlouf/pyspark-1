"""
VectorAssembler is a transformer that combines a given list of columns 
into a single vector column. It is useful for combining raw features and 
features generated by different feature transformers into a single 
feature vector, in order to train ML models like logistic regression 
and decision trees. 

VectorAssembler accepts the following input column types: 
    all numeric types, boolean type, and vector type. 
    
In each row, the values of the input columns will be concatenated 
into a vector in the specified order.
"""
import findspark
findspark.init()

from pyspark import SparkContext
from pyspark.sql import SQLContext, SparkSession
from pyspark.ml.linalg import Vectors
from pyspark.ml.feature import VectorAssembler

sc = SparkContext("local", "Features - VectorAssembler")
sqlContext = SQLContext(sc)
spark = SparkSession.builder.getOrCreate()
        
dataset = spark.createDataFrame(
    [(0, 18, 1.0, Vectors.dense([0.0, 10.0, 0.5]), 1.0),
     (1, 15, 2.0, Vectors.dense([0.0, 5.0, 0.5]), 1.0)],
    ["id", "hour", "mobile", "userFeatures", "clicked"])

assembler = VectorAssembler(
    inputCols=["hour", "mobile", "userFeatures"],
    outputCol="features")

output = assembler.transform(dataset)
print("Assembled columns 'hour', 'mobile', 'userFeatures' to vector column 'features'")
output.select("features", "clicked").show(truncate=False)

spark.stop()