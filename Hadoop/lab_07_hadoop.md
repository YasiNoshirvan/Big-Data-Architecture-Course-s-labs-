# Lab 07 — Hadoop / MapReduce

Source note: extracted from `lab (7).txt`.

> This file contains typed lab notes / pseudo-code from Big Data Architecture exercises.  
> Some snippets may require syntax cleanup before execution in a real Hadoop or PySpark environment.

```java
## 1 ##

########## mapper ############

string[] fields = value.toString().split(",")

String CodDC = fields[0]
String CodC = fields[1]
String size = fields[2]
String continent = fields[5]

if ( (continent.equals("Europe")) || (continent.equals("North American")) ) {
   if ( size>10000 ){
       context.write ( new Text (CodC) , new IntWritable (Continent) )
    }
}

########## reducer ############

int NumLargeDC_Europe = 0
int NumLargeDC_NorthAmerican = 0


for ( intWritable Value: values  ){
     if ( values.equals("Europe") ){
        NumLargeDC_Europe++
      }

      if ( values.equals("NorthAmerican") ){
         NumLargeDC_NorthAmerican++
      }
} 

if ( NumLargeDC_Europe >= 10  &&  NumLargeDC_NorthAmerican >= 10 ){
   contexet.write(key,Intwritable.get())
}
```
