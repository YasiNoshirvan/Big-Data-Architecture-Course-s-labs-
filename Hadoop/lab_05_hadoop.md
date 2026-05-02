# Lab 05 — Hadoop / MapReduce

Source note: extracted from `lab (5).txt`.

> This file contains typed lab notes / pseudo-code from Big Data Architecture exercises.  
> Some snippets may require syntax cleanup before execution in a real Hadoop or PySpark environment.

```java
## 1 ##

########## mapper ############

string[] fields = value.toString().split(",")

string PID = fields[0]
string SID = fields[1]
string Date = fields[2]

year = Integer.parseInt(Date.split("/")[0])

if ( Date == 2022 ){
   context.write( new Text (SID) , new Text (PID + "_" + Date) )
}

########## reducer ############

int LastDate = null
int PID_LastDate = null

for (Text value = values ) {
    fields = values.split("_")
  
    PID = fields[0]
    Date = fields[1]

    if (LastDate == null || Date.compareTo(LastDate)>0){
   
       LastDate = Date
       PID_LastDate = PID  

    }

}

context.write( key , new Text (PID_LastDate))
```
