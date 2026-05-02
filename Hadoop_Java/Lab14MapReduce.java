/*
 * Big Data Architecture — Lab 14
 * Hadoop / MapReduce solution notes
 *
 * Source note: extracted from lab (14).txt
 *
 * IMPORTANT:
 * This file preserves the typed MapReduce pseudo-code from the lab notes.
 * The logic is Java/MapReduce-oriented, but it may require syntax cleanup,
 * real input schemas, Hadoop imports, Mapper/Reducer class definitions,
 * and job configuration before it can be executed.
 */

/*
#################################################################### HADOOP ###########################################################

## job1


### mapper

string[] fields = value tostring() = split(",")

string country = fields [2]
string city = fields [1]
string HID = fields[0]

context write( new Text (country+"_"+city) , new Text (HID) )


###reducer

int Num_House = 0

country = key. tostring() -split (" -") [0]
city = key. tostring() ~shlit("-")[1]

for (Text value : values) (
    Num House++ }

if Num_House>=50000 {
   context. write(new Text (country) , new Text (city))}



## job2

###mapper

String[] fields = value.toString().split("\t")

context.write(new Text (fields[0]) , new Text(fields[1]))


###reducer

int Num_Big_cities = 0

for (Text Value : values ){
     Num_Big_Cities++
}

if (Num_Big_cities>10){
   context.write(Key,nllwritable)
*/

public class Lab14MapReduce {
    public static void main(String[] args) {
        System.out.println("Lab 14 Hadoop/MapReduce pseudo-code. See comments above for mapper/reducer logic.");
    }
}
