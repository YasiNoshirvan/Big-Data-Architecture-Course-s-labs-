/*
 * Big Data Architecture — Lab 12
 * Hadoop / MapReduce solution notes
 *
 * Source note: extracted from lab (12).txt
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

String[] fields = value.toString()split(",")


string Date = fields[0]
string CarID = fields[2]
string FailureType = fields[3]

if (Date.StartsWith("2018")) {
    context.write(new Text(CarID) , new Text(FailureType))
}



###### reducr ######

int numFailure = 0
string previouseFailureType = null
string atLeastTwodifferntType = False

for ( Text value : values){
    
    numFailures++

     //check if the current failure type is different from the previous one
     //If it is true, there are at least two different types of failurs

    if (previouseFailureType!=null && previuoseFailureType.equals(value.toString())==False)         
    {atLeastTwodifferntType = true}

    previouseFailureType=True

if (numFailures >= 5 && atLeastTwodifferntType == true ) {

    context.write( key , new IntWritable(numFailures))  }

}
*/

public class Lab12MapReduce {
    public static void main(String[] args) {
        System.out.println("Lab 12 Hadoop/MapReduce pseudo-code. See comments above for mapper/reducer logic.");
    }
}
