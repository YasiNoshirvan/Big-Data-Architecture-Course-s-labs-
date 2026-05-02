# Lab 08 — Hadoop / MapReduce

Source note: extracted from `lab (8).txt`.

> This file contains typed lab notes / pseudo-code from Big Data Architecture exercises.  
> Some snippets may require syntax cleanup before execution in a real Hadoop or PySpark environment.

```java
## 1 ##

########## mapper ############

string[] fields = value.toString().split(",")

int duration = fields[3]
string OrgID = fields[4]

context.write(new Text (OrgID) , new Text (duration))

########## reducer ############

int AVG_max = -1
string OrgID_max_Avg =  " "
int SumDuration = 0
int NumMeetings = 0
string CID = key.toString()


for (Text value = values){
    NumMeeting++
    SumDuration += value.get()
}

AVG = SumDuration/NumMeetings
                                      \\current customer ID is being processed or filtered
if(AVG > AVG_max || ( AVG==AVG_max  &&  CID.compareTo(OrgID_max_Avg)<0)){
   OrgID_max_Avg = CID
   AVG_max = AVG
}

if (OrgID_max_Avg.compareTo(" ") != 0){
   context.write( new Text (OrgID_max_Avg) , new DoubleWritable (AVG_max) )
}
```
