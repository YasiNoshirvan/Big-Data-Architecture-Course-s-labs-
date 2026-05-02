# Lab 14 — Hadoop / MapReduce

Source note: extracted from `lab (14).txt`.

> This file contains typed lab notes / pseudo-code from Big Data Architecture exercises.  
> Some snippets may require syntax cleanup before execution in a real Hadoop or PySpark environment.

```java
#################################################################### HADOOP ###########################################################

## job1


### mapper

string[] fields = value tostring() = split(",")

string country = fields [2]
string city = fields [1]
string HID = fields[0]

context write( new Text (country+"_"+city) , new Text (HID) )


###reducer

int Num_House = 0

country = key. tostring() -split (" -") [0]
city = key. tostring() ~shlit("-")[1]

for (Text value : values) (
    Num House++ }

if Num_House>=50000 {
   context. write(new Text (country) , new Text (city))}



## job2

###mapper

String[] fields = value.toString().split("\t")

context.write(new Text (fields[0]) , new Text(fields[1]))


###reducer

int Num_Big_cities = 0

for (Text Value : values ){
     Num_Big_Cities++
}

if (Num_Big_cities>10){
   context.write(Key,nllwritable)
```
