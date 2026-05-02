# Lab 13 — Hadoop / MapReduce

Source note: extracted from `lab (13).txt`.

> This file contains typed lab notes / pseudo-code from Big Data Architecture exercises.  
> Some snippets may require syntax cleanup before execution in a real Hadoop or PySpark environment.

```java
## 1 ##

###### mapper ######

string [] fields = value.toString().split(",")

string[] MID=fields[0]
string[] ModelName=fields[1]
string[] Brand =fields[2]

context.write ( new Text (Brand) , new Text(MID))

###### reducer ######

int CountModel = 0
string MID = null

for(Text value : values) {
   MID = value.toString()
   CountModel++
}

if (CountModel==1){
context.write( key , new Text (MID) )
}
```
