# Lab 13 — PySpark

Source note: extracted from `lab (13).txt`.

> This file contains typed lab notes / pseudo-code from Big Data Architecture exercises.  
> Some snippets may require syntax cleanup before execution in a real Hadoop or PySpark environment.

```python
------


## 2 ##

inputPathPurchases = "exam_ex2_data/Purchases.txt"
outputPathPart1 = "outPart1/"
outputPathPart2 = "outPart2/"


######### part 1 ###########


purchasesRDD= sc.TextFile(inputPathPurchases)


Purchases_year_2019 = purchasesRDD.filter(lambda line: line.split(",")[2].startsWith(2019))

MID_price = Purchases_year_2019.map(lambda line: (line.split(",")[0],line.split(",")[3]))

MID_sum_sell = MID_price.reduceByKey(lambda v1,v2 : v1+v2)

Max_income = MID_sum_sell.value().max()

MID_MAX_Income = MID_price.filter(lambda p : p[1]== Max_income)

MID_MAX_Income.key().SaveasTextFile()


######### part 2 ###########


def year_2010_2019 (line):

    year = int(line.split(",")[2].split(",")[0])
    MID= line.split(",")[0]

    if year>=2010 and year<=2019 :
       return (MID,Year)

purchased_2010_to_2019=purchasesRDD.map(year_2010_2019)


def Count_sold (pair):
    
    MID = fields[0]
    year = fields[1]
  
    return ((MID,Year),+1)


MID_Year_AnnualPurchases = purchased_2010_to_2019\
.map(Count_sold).reduceByKey(lambda v1,v2: v1+v2)


Year_AnnualPurchases = MID_Year_AnnualPurchases.map(lambda p : (p[0][1],p[1]))


maxAnualPurchase = Year_AnnualPurchases.value().max()


Year_MaxAnnualPurchases = Year_AnnualPurchases.filter(lambda p : p[1]==maxAnualPurchase)


Year_MID_AnnualPurchases = MID_Year_AnnualPurchases\
.map(lambda p : (p[0][1],(p[0][0],p[1])))


#(Year , (MID , AnnualPurchases) , MaxAnnualPurchases)
Year_MID_MaxAnnualPurchases = Year_MID_AnnualPurchases.join(Year_MaxAnnualPurchases)

Select_max = Year_MID_MaxAnnualPurchases.filter(lambda p : p[1][0][1] == p[1][1])

Count_YEAR_MaxAnnualPurchases = Select_max\
map(lambda p : ( p[0][1][1] , +1 )).reduceByKey(lambda v1 , v2 : v1+v2)

result = Count_YEAR_MaxAnnualPurchases.filter(lambda p : p[1]>=2 )

result.key().saveAsTextFile()







result.key().saveAsTextFile(output2)
```
