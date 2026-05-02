/*
 * Big Data Architecture — Lab 05
 * Hadoop / MapReduce solution notes
 *
 * Source note: extracted from lab (5).txt
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
*/

public class Lab05MapReduce {
    public static void main(String[] args) {
        System.out.println("Lab 05 Hadoop/MapReduce pseudo-code. See comments above for mapper/reducer logic.");
    }
}
