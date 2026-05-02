/*
 * Big Data Architecture — Lab 09
 * Hadoop / MapReduce solution notes
 *
 * Source note: extracted from lab (9).txt
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

string CID = fields[3]
string Duration = fields[2]

context.write(new Text (CID) , new IntWritable(Duration))

########## reducer ############

int NumShortVideo = 0
int SumDuration = 0

for (IntWritable value : values){

    SumDuration += value.get()

    if (value < 15){

        NumShortVirdeo++
  
     }
}

if ( NumShortVideos > 10 && SumDuration > 600 ){
   context.write( key , nullWritable.get() )
}
*/

public class Lab09MapReduce {
    public static void main(String[] args) {
        System.out.println("Lab 09 Hadoop/MapReduce pseudo-code. See comments above for mapper/reducer logic.");
    }
}
