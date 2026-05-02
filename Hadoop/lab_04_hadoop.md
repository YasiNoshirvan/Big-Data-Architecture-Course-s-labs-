# Lab 04 — Hadoop / MapReduce

Source note: extracted from `lab (4).txt`.

> This file contains typed lab notes / pseudo-code from Big Data Architecture exercises.  
> Some snippets may require syntax cleanup before execution in a real Hadoop or PySpark environment.

```java
## 1 ##

########## mapper ############

string[] fields = value.toString().split(",")

string AppID = fields[0] 
int Price = fields[2]
string Category = fields[3]
string company = fields[4]

if (Category == "Education" ){
    
   if (price = 0){
      context.write(new Text (Company) , new IntWritable (0)) }

   if (price > 0)){
      context.write(new Text (Company) , new IntWritable (1)) }
}

########## reducer ############

int SumPrice = 0
int NumApps = 0

for (IntWritable value : values){
    Numapps++
    SumPrice = SumPrice + value.get()
}

if (SumPrice = 0){
    context.write(key , new IntWritable( NumApps ) )
}
```
