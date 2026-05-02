# Lab 01 — PySpark

Source note: extracted from `lab (1).txt`.

> This file contains typed lab notes / pseudo-code from Big Data Architecture exercises.  
> Some snippets may require syntax cleanup before execution in a real Hadoop or PySpark environment.

```python
----

## 2 ##

import pyspark

from pyspark import SparkContext
from pyspark import SparkConf
from pyspark.sql import SparkSession
from pyspark.sql import functions

spark = SparkSession.builder.getOrCreate()
sc = spark.sparkContext

carModelsPath = 'data/CarModels.txt'
salesEUPath = 'data/SalesEU.txt'
salesExtraEUPath = 'data/SalesExtraEU.txt'


output1 = 'out1'
output2 = 'out2'

############### part 1 ###################

CarsRDD = sc.TextFile(carModelsPath)
SelsEURDD = sc.Textfile(salesEUPath)


ModelID_of_FIAT = CarsRDD.filter(lambda line : line.split(",")[2]=="FIAT")
map(lambda line: ( line.split(",")[0] , None ))


ModelID_price = SelsEURDD.filter(lambda line : line.split(",")[4]=="Italy")\
.map(lambda line : (line.split(",")[2],line.split(",")[5])


Selected_ModelID_Price = ModelID_price.join(ModelID_of_FIAT)


def countSele (pair) :
    
    ModelID = pair[0]
    price = pair[1]

    return ((ModelID ,(price,+1))


ModelID_price_count = Selected_ModelID_Price.map(countSele)\
reduceByKey(lambda v1,v2: v1[0]+v2[0] , v1[1]+v2[1])


def Count_AvearagePrice (pair):

    ModelID = pair[0]
    Total_income = pair[1][0]
    Tota_Num_sold = pair[1][1]

    Average_income = Total_income/Tota_Num_sold
  
    return(ModelID,(Tota_Num_sold,Average_income))


result=ModelID_price_count.map(Count_AvearagePrice)\
.filter(lambda p : p[1][0]>1000000 and p[1][1]>50000)

result.key().saveAsTextFile(output1)


########### part 2 #############

SelsEURDD = sc.Textfile(salesEUPath)
SelsExtraEURDD = sc.Textfile(salesExtraEUPath)


EU_ModelID_Year = SelsEURDD\
.map(lambda line: ( (line.split(",")[2] , line.split(",")[3].split("/")[0]) , +1)

ExtraEU_ModelID_Year = SelsExtraEURDD\
.map(lambda line: ( (line.split(",")[2] , line.split(",")[3].split("/")[0]) , +1)



global_modelID_year = EU_ModelID_Year.join(ExtraEU_ModelID_Year)

count_global_ModelID_year = global_modelID_year.reduceByKey(lambda v1 , v2 : v1+v2)


Map_count_global_ModelID_year = count_global_ModelID_year\
.map(lambda p : (p[0][0] , ( p[0][1],p[1]))).groupByKey()
#group by key to obtain a list


def check_increasing_sell(pair):

    selesList = list(pair[1])
    selesList.sort()

    LastSell =-1


    for year , sell in salesList:
        if sell <= LastSell:
           return False

        if sell > LastSell:
           LastSell =sell
           return True


result2 = Map_count_global_ModelID_year.filter(check_increasing_sell)

result2.key().saveasTextFile()
```
