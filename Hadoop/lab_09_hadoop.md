# Lab 09 — Hadoop / MapReduce

Source note: extracted from `lab (9).txt`.

> This file contains typed lab notes / pseudo-code from Big Data Architecture exercises.  
> Some snippets may require syntax cleanup before execution in a real Hadoop or PySpark environment.

```java
## 1 ##

########## mapper ############

string[] fields = value.toString().split(",") 

string CID = fields[3]
string Duration = fields[2]

context.write(new Text (CID) , new IntWritable(Duration))

########## reducer ############

int NumShortVideo = 0
int SumDuration = 0

for (IntWritable value : values){

    SumDuration += value.get()

    if (value < 15){

        NumShortVirdeo++
  
     }
}

if ( NumShortVideos > 10 && SumDuration > 600 ){
   context.write( key , nullWritable.get() )
}
```
