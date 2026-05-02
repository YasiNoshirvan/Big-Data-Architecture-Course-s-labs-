/*
 * Big Data Architecture — Lab 03
 * Hadoop / MapReduce solution notes
 *
 * Source note: extracted from lab (3).txt
 *
 * IMPORTANT:
 * This file preserves the typed MapReduce pseudo-code from the lab notes.
 * The logic is Java/MapReduce-oriented, but it may require syntax cleanup,
 * real input schemas, Hadoop imports, Mapper/Reducer class definitions,
 * and job configuration before it can be executed.
 */

/*
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
*/

public class Lab03MapReduce {
    public static void main(String[] args) {
        System.out.println("Lab 03 Hadoop/MapReduce pseudo-code. See comments above for mapper/reducer logic.");
    }
}
