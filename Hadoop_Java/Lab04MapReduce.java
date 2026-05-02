/*
 * Big Data Architecture — Lab 04
 * Hadoop / MapReduce solution notes
 *
 * Source note: extracted from lab (4).txt
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
*/

public class Lab04MapReduce {
    public static void main(String[] args) {
        System.out.println("Lab 04 Hadoop/MapReduce pseudo-code. See comments above for mapper/reducer logic.");
    }
}
