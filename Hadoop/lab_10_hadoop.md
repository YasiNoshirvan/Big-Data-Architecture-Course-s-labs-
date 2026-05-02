# Lab 10 — Hadoop / MapReduce

Source note: extracted from `lab (10).txt`.

> This file contains typed lab notes / pseudo-code from Big Data Architecture exercises.  
> Some snippets may require syntax cleanup before execution in a real Hadoop or PySpark environment.

```java
## 1 ##

########## mapper ############

string[] fields = value.toString().split(",")

string SID = fields[0]
string airdate = fields[4]

context.write(new Text (SID) , new intWritable(airdate) )


########## reducer ############

firstDate=null
LastDate=null
Diff_First_Last=null
Max_diff=null
string SID = key.toString()


for (IntWritable Value : values) {

    if (FirstDate == null or )
```
