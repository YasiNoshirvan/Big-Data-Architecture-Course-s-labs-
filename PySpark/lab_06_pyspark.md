# Lab 06 — PySpark

Source note: extracted from `lab (6).txt`.

> This file contains typed lab notes / pseudo-code from Big Data Architecture exercises.  
> Some snippets may require syntax cleanup before execution in a real Hadoop or PySpark environment.

```python
---


## 2 ##

prodPlantPath='data/ProdPlants.txt'
robotsPath='data/Robots.txt'
outOfOrderPath='data/OutOfOrders.txt'

output1='outPart1/'
output2='outPart2/'

########## part 1 #################

outOfOrderRDD = sc.TextFile(outOfOrderPath)
robotsRDD = sc.TextFile(robotsPath)
prodPlantRDD  = sc.TextFile(prodPlantPath)


def Years_2020_2021 (line):
   
    fields = line.split(",")

    RID = fields[0]
    Date = fields[1]

    if Date > 2020/01/01 and Date < 2021/12/31

       return (RID,Date)

RID_Date_OOO = outOfOrderRDD.map(Years_2020_2021)


def Count_OOO_each_year (pair):

    RID = pair[0]
    Date = pair[1]

    if (Date.startswith("2020")):

       return (RID,(1,0))

    if (Date.startswith("2021")):

       return (RID,(0,1))

RID_Count_OOO = RID_Date_OOO.map(Count_OOO_each_year)\
.reduceByKey(lambda v1,v2: v1[0]+v2[0],v1[1]+v2[1] )


RID_2021_greater=RID_Count_OOO.filter(lambda p: p[1][1]>p[1][0])


PlantID_RID = RobotRDD.map(lambda line: line.split(",")[1],line.split(",")[0])
PlantID_City = prodPlantRDD.map(lambda line: line.split(",")[0],line.split(",")[1])
PlantI_RID_city = PlantID_RID.join(PlantID_City)
All_RID_city = PlantI_RID_city.map(lambda p: (p[1][0],p[1][1]))

result = RID_2021_greater.Join(All_RID_city).map(lambda p : (p[0],p[1][1]))

result.saveAsTextFile(output1)


############ part 2 ################

from datetime import datetime , time delta

#predefind previouse date def
def PreviousDate (myDate,n):
    currentDate = datetime.strptime(%Y/%M/%d)
    prevDate = currentDate - timedelta(days=n)

    return prevDate.strptime(%Y/%M/%d)



RID_Date = outOfOrderRDD.map(lambda line: line.split(",")[0],line.split(",")[1])

RID_PlantID = RobotRDD.map(lambda line: line.split(",")[0],line.split(",")[1])

RID_Date_plantID = RID_Date.join(RID_PlantID)


# Return 3 elements from each out of order
def WindowElements (pair):
    RID=pair[0]
    Date=pair[1][0]
    PlantID=pair[1][1]

     elementsb=[]

     elements.append((PlantID,Date),RID)
     elements.append((PlantID,previouseDate(Date,1)),RID)
     elements.append((PlantID,previouseDate(Date,2)),RID)

     return elements


WindowElements = RID_Date_plantID.FlatMap(WindowElements).Distinct()

# Count the number of distinct RIDs in each window
WindowNumRID = WindowElements.mapValue(lambda v : 1).reduceByKey(lambda v1,v2: v1+v2)


#(PID,numRobotsOutOfOrders)
#compute the maximum for each plant
PID_NumOOO=WindowNumRID.map(lambda pair: (pair[0],pair[1][1]))
PID_MaxNumOOO=PID_NumOOO.reduceByKey(lambda v1,v2:max(v1,v2))



selectedWindow = WindowNumRID.map(lambda p: ((p[0][0],p[1]),p[0][1])\
.join(PID_MaxNumOOO.map(lambda p : (p[0],p[1]),None)))

result2 = selectedWindows.map(lambda p : (p[1][0],p[0][0],p[0][1]))


result2.saveAsTextFile(output2)
```
