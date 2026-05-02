/*
 * Big Data Architecture — Lab 02
 * Hadoop / MapReduce solution notes
 *
 * Source note: extracted from lab (2).txt
 *
 * IMPORTANT:
 * This file preserves the typed MapReduce pseudo-code from the lab notes.
 * The logic is Java/MapReduce-oriented, but it may require syntax cleanup,
 * real input schemas, Hadoop imports, Mapper/Reducer class definitions,
 * and job configuration before it can be executed.
 */

/*
## 1 ##

######## mapper #########

string [] fields = value.toString().split(",")

string timeStamp = fields[0]
String ItemID = fields[2]
String Purchased = fields[3]

if (timestamp.startsWith("2020")){
   
    if (purchased.equal( "True"){

       val = 1}

    else{

       val = 0}

context.write(new Text (ItemID) , new Intwritable (val) )
 
}

######## reducer #########

NumTrueAds = 0
NumAds = 0

for (IntWritable value : values){
     NumAds++
     NumTrueAds += value.get() 
}

double ConvRate = (double) NumTrueAds / NumAds

if (convRate > 0.001){
   context.write( key , new Intwritable(convRate) )
}
*/

public class Lab02MapReduce {
    public static void main(String[] args) {
        System.out.println("Lab 02 Hadoop/MapReduce pseudo-code. See comments above for mapper/reducer logic.");
    }
}
