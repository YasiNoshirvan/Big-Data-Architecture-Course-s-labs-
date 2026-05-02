# Lab 02 — Hadoop / MapReduce

Source note: extracted from `lab (2).txt`.

> This file contains typed lab notes / pseudo-code from Big Data Architecture exercises.  
> Some snippets may require syntax cleanup before execution in a real Hadoop or PySpark environment.

```java
## 1 ##

######## mapper #########

string [] fields = value.toString().split(",")

string timeStamp = fields[0]
String ItemID = fields[2]
String Purchased = fields[3]

if (timestamp.startsWith("2020")){
   
    if (purchased.equal( "True"){

       val = 1}

    else{

       val = 0}

context.write(new Text (ItemID) , new Intwritable (val) )
 
}

######## reducer #########

NumTrueAds = 0
NumAds = 0

for (IntWritable value : values){
     NumAds++
     NumTrueAds += value.get() 
}

double ConvRate = (double) NumTrueAds / NumAds

if (convRate > 0.001){
   context.write( key , new Intwritable(convRate) )
}
```
