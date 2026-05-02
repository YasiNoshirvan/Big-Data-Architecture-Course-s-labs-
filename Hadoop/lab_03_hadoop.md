# Lab 03 — Hadoop / MapReduce

Source note: extracted from `lab (3).txt`.

> This file contains typed lab notes / pseudo-code from Big Data Architecture exercises.  
> Some snippets may require syntax cleanup before execution in a real Hadoop or PySpark environment.

```java
## 1 ##

########## mapper ############


String[] fields = value.toString().split(",")

string TimeStamp = fields[0]
string UserID = fields[1]
string ItemID = fields[2]

string year = Integer.parseInt(TimeStamp.split("/")[0])

context.write(new Text(UserID) , new IntWritable(val))

########## setup ##############
  maxCount2010 = -1;
  maxUser = null;
    }


########## reducer ############

int oldValue = -1;

for(Text val : values) {
    String[] fields = val.toString().split("_");
    int year = Integer.parseInt(fields[0]);
    int count = Integer.parseInt(fields[1]);

    if(yearCount.containsKey(year))
       oldValue = yearCount.get(year);
    else
       oldValue = 0;
     
     yearCount.put(year, oldValue + count);

        }

     if(yearCount.entrySet().size() == 1 && yearCount.containsKey(2010)) {
        int val = yearCount.get(2010);
        if(val > maxCount2010 || (val == maxCount2010 &&
         key.toString().compareTo(maxUser) < 0)) {
            maxCount2010 = val;
            maxUser = key.toString();
            }
        }
    }

############ cleanup ############
    
if(maxUser != null)
   context.write(new Text(maxUser), new IntWritable(maxCount2010));
    }
```
