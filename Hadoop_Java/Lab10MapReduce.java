/*
 * Big Data Architecture — Lab 10
 * Hadoop / MapReduce solution notes
 *
 * Source note: extracted from lab (10).txt
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

string SID = fields[0]
string airdate = fields[4]

context.write(new Text (SID) , new intWritable(airdate) )


########## reducer ############

firstDate=null
LastDate=null
Diff_First_Last=null
Max_diff=null
string SID = key.toString()


for (IntWritable Value : values) {

    if (FirstDate == null or )
*/

public class Lab10MapReduce {
    public static void main(String[] args) {
        System.out.println("Lab 10 Hadoop/MapReduce pseudo-code. See comments above for mapper/reducer logic.");
    }
}
