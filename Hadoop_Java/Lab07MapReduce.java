/*
 * Big Data Architecture — Lab 07
 * Hadoop / MapReduce solution notes
 *
 * Source note: extracted from lab (7).txt
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

String CodDC = fields[0]
String CodC = fields[1]
String size = fields[2]
String continent = fields[5]

if ( (continent.equals("Europe")) || (continent.equals("North American")) ) {
   if ( size>10000 ){
       context.write ( new Text (CodC) , new IntWritable (Continent) )
    }
}

########## reducer ############

int NumLargeDC_Europe = 0
int NumLargeDC_NorthAmerican = 0


for ( intWritable Value: values  ){
     if ( values.equals("Europe") ){
        NumLargeDC_Europe++
      }

      if ( values.equals("NorthAmerican") ){
         NumLargeDC_NorthAmerican++
      }
} 

if ( NumLargeDC_Europe >= 10  &&  NumLargeDC_NorthAmerican >= 10 ){
   contexet.write(key,Intwritable.get())
}
*/

public class Lab07MapReduce {
    public static void main(String[] args) {
        System.out.println("Lab 07 Hadoop/MapReduce pseudo-code. See comments above for mapper/reducer logic.");
    }
}
