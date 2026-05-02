# Lab 06 — Hadoop / MapReduce

Source note: extracted from `lab (6).txt`.

> This file contains typed lab notes / pseudo-code from Big Data Architecture exercises.  
> Some snippets may require syntax cleanup before execution in a real Hadoop or PySpark environment.

```java
## 1 ##

########## mapper ############

string[] fields = value.toString().split(",")

string RID = fields[0]
string Date = fields[1]
string Cause = fields[2]

if (cause == "rokenMotherboard"){
   context.write( new Text( Date ) , new intwritable( +1 ))
}

############ setup #############

this.firstDate = null
this.MaxOOORobot = -1

########## reducer ############

int NumOOORobote = 0
string Date = key.toString()

for (IntWrritavle value : values){

    NumOOORobote = NumOOORobote + value.get()
}

if (maxNumOOORobote<NumOOORobote || 
    (NumOOORobote==maxNumOOORobote && Date.CopareTo(firstDate)>0) ) {
    this.maxOOORobote=NumOOORobote
    this.firstDate=Date
}


context.write( new Text (this.firstDate) , new IntWritable(maxOOORobote))
```
