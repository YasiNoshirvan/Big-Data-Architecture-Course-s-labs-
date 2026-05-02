/*
 * Big Data Architecture — Lab 13
 * Hadoop / MapReduce solution notes
 *
 * Source note: extracted from lab (13).txt
 *
 * IMPORTANT:
 * This file preserves the typed MapReduce pseudo-code from the lab notes.
 * The logic is Java/MapReduce-oriented, but it may require syntax cleanup,
 * real input schemas, Hadoop imports, Mapper/Reducer class definitions,
 * and job configuration before it can be executed.
 */

/*
## 1 ##

###### mapper ######

string [] fields = value.toString().split(",")

string[] MID=fields[0]
string[] ModelName=fields[1]
string[] Brand =fields[2]

context.write ( new Text (Brand) , new Text(MID))

###### reducer ######

int CountModel = 0
string MID = null

for(Text value : values) {
   MID = value.toString()
   CountModel++
}

if (CountModel==1){
context.write( key , new Text (MID) )
}
*/

public class Lab13MapReduce {
    public static void main(String[] args) {
        System.out.println("Lab 13 Hadoop/MapReduce pseudo-code. See comments above for mapper/reducer logic.");
    }
}
