# Lab 11 — Hadoop / MapReduce

Source note: extracted from `lab (11).txt`.

> This file contains typed lab notes / pseudo-code from Big Data Architecture exercises.  
> Some snippets may require syntax cleanup before execution in a real Hadoop or PySpark environment.

```java
## 1 ##

########## mapper ############

string[] fields = value.toString().split(",")

string UserID = fields[1]
string ItemID = fields[2]
string date = fields[0].split("-")[0]

if ( date >= 2020/01/01 && date <= 2023/12/21 ){

     context.write( new Text (UserID) , new Text (itemID)) }


########## reducer ############

string LastItemID = null
NumDistinctItem = 0

for (Text value : values){

    if ( values != LastItemID){
      
        LastItemID=Values.get()
        NumDistinctItem++
       
     }
    
}

if ( NumDistinctItem>=50 ){
   
   context.write( key , nullWritable.get() )
}
```
