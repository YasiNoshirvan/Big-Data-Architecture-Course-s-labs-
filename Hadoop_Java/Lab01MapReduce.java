/*
 * Big Data Architecture — Lab 01
 * Hadoop / MapReduce solution notes
 *
 * Source note: extracted from lab (1).txt
 *
 * IMPORTANT:
 * This file preserves the typed MapReduce pseudo-code from the lab notes.
 * The logic is Java/MapReduce-oriented, but it may require syntax cleanup,
 * real input schemas, Hadoop imports, Mapper/Reducer class definitions,
 * and job configuration before it can be executed.
 */

/*
## 1 ##

########## mapper ##############

String[] fields = value.toString().split(",")

string SID = fields[0]
string ModelID = fields[2]
string Date = fields[3]
string country = fields[4] 

if (Country == "Italy" && (Date.startsWith("2020"){

   context.write(new Text (ModelID) , new IntWritable (+1)) }

if (Country == "Italy" && (Date.startsWith("2019"){

   context.write(new Text (ModelID) , new IntWritable (-1)) }


############ reducer ##############

int difference_2020_2019 = 0

for (IntWritable value : values){
    
     difference_2020_2019 = difference_2020_2019 + value.get() }

if ( difference_2020_2019 > 0) {
     
    context.write( key , new IntWritable (difference_2020_2019)) }

}
*/

public class Lab01MapReduce {
    public static void main(String[] args) {
        System.out.println("Lab 01 Hadoop/MapReduce pseudo-code. See comments above for mapper/reducer logic.");
    }
}
