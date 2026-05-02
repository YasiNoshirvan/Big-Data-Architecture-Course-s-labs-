# Lab 12 — Hadoop / MapReduce

Source note: extracted from `lab (12).txt`.

> This file contains typed lab notes / pseudo-code from Big Data Architecture exercises.  
> Some snippets may require syntax cleanup before execution in a real Hadoop or PySpark environment.

```java
## 1 ##

###### mapper ######

String[] fields = value.toString()split(",")


string Date = fields[0]
string CarID = fields[2]
string FailureType = fields[3]

if (Date.StartsWith("2018")) {
    context.write(new Text(CarID) , new Text(FailureType))
}



###### reducr ######

int numFailure = 0
string previouseFailureType = null
string atLeastTwodifferntType = False

for ( Text value : values){
    
    numFailures++

     //check if the current failure type is different from the previous one
     //If it is true, there are at least two different types of failurs

    if (previouseFailureType!=null && previuoseFailureType.equals(value.toString())==False)         
    {atLeastTwodifferntType = true}

    previouseFailureType=True

if (numFailures >= 5 && atLeastTwodifferntType == true ) {

    context.write( key , new IntWritable(numFailures))  }

}
```
