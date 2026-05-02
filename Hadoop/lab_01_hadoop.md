# Lab 01 — Hadoop / MapReduce

Source note: extracted from `lab (1).txt`.

> This file contains typed lab notes / pseudo-code from Big Data Architecture exercises.  
> Some snippets may require syntax cleanup before execution in a real Hadoop or PySpark environment.

```java
## 1 ##

########## mapper ##############

String[] fields = value.toString().split(",")

string SID = fields[0]
string ModelID = fields[2]
string Date = fields[3]
string country = fields[4] 

if (Country == "Italy" && (Date.startsWith("2020"){

   context.write(new Text (ModelID) , new IntWritable (+1)) }

if (Country == "Italy" && (Date.startsWith("2019"){

   context.write(new Text (ModelID) , new IntWritable (-1)) }


############ reducer ##############

int difference_2020_2019 = 0

for (IntWritable value : values){
    
     difference_2020_2019 = difference_2020_2019 + value.get() }

if ( difference_2020_2019 > 0) {
     
    context.write( key , new IntWritable (difference_2020_2019)) }

}
```
