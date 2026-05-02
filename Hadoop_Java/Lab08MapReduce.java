/*
 * Big Data Architecture — Lab 08
 * Hadoop / MapReduce solution notes
 *
 * Source note: extracted from lab (8).txt
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

int duration = fields[3]
string OrgID = fields[4]

context.write(new Text (OrgID) , new Text (duration))

########## reducer ############

int AVG_max = -1
string OrgID_max_Avg =  " "
int SumDuration = 0
int NumMeetings = 0
string CID = key.toString()


for (Text value = values){
    NumMeeting++
    SumDuration += value.get()
}

AVG = SumDuration/NumMeetings
                                      \\current customer ID is being processed or filtered
if(AVG > AVG_max || ( AVG==AVG_max  &&  CID.compareTo(OrgID_max_Avg)<0)){
   OrgID_max_Avg = CID
   AVG_max = AVG
}

if (OrgID_max_Avg.compareTo(" ") != 0){
   context.write( new Text (OrgID_max_Avg) , new DoubleWritable (AVG_max) )
}
*/

public class Lab08MapReduce {
    public static void main(String[] args) {
        System.out.println("Lab 08 Hadoop/MapReduce pseudo-code. See comments above for mapper/reducer logic.");
    }
}
