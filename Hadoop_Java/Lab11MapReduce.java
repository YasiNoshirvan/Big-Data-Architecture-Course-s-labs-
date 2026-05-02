/*
 * Big Data Architecture — Lab 11
 * Hadoop / MapReduce solution notes
 *
 * Source note: extracted from lab (11).txt
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

string UserID = fields[1]
string ItemID = fields[2]
string date = fields[0].split("-")[0]

if ( date >= 2020/01/01 && date <= 2023/12/21 ){

     context.write( new Text (UserID) , new Text (itemID)) }


########## reducer ############

string LastItemID = null
NumDistinctItem = 0

for (Text value : values){

    if ( values != LastItemID){
      
        LastItemID=Values.get()
        NumDistinctItem++
       
     }
    
}

if ( NumDistinctItem>=50 ){
   
   context.write( key , nullWritable.get() )
}
*/

public class Lab11MapReduce {
    public static void main(String[] args) {
        System.out.println("Lab 11 Hadoop/MapReduce pseudo-code. See comments above for mapper/reducer logic.");
    }
}
