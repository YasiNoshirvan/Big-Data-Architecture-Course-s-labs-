# Lab 09 — PySpark

Source note: extracted from `lab (9).txt`.

> This file contains typed lab notes / pseudo-code from Big Data Architecture exercises.  
> Some snippets may require syntax cleanup before execution in a real Hadoop or PySpark environment.

```python
-

## 2 ##

students_rdd = sc.textFile('data/Students.txt')
courses_rdd = sc.textFile('data/OnlineCourses.txt')
lectures_rdd = sc.textFile('data/VideoLectures.txt')
watched_lectures_rdd = sc.textFile('data/UsersWatchedLectures.txt')


########## part 1 #################


CID_Topic = courses_rdd.map( lambda line: (line.split(",")[0],line.split(",")[2]) )

CID_Duration = lectures_rdd.map( lambda line: (line.split(",")[3],line.split(",")[2]) )



CID_Topic_Duration = CID_Topic.join(CID_Duration)

Topic_Duration = CID_Topic_Duration.map(lambda p : ( p[1][0] , p[1][1] ))



Topic_TotalDuration = Topic_Duration.reduceByKey(lambda v1,v2 : v1+v2)

def CounLongCourse (pair):

    Topic = pair[0]
    Duration = pair[1]

    if (Duration > 600):
       return(Topic,(1,1))

    else :
       return(Topic,(0,1))
       
    
Topic_CountLongCourse = Topic_TotalDuration.map(CounLongCourse)\
.reduceByKey(lambda v1,v2 : (v1[0]+v2[0] / v1[1]+v2[1]) )/

result_1 = Topic_CountLongCourse.filter( lambda p : p[1] > 0.8 )

result_1.key().saveAsTextFile(output_1)



############ part 2 ################


SID_WatchTime = lectures_rdd.map( lambda line: (line.split(",")[0],line.split(",")[1]) )


SID_Year2023 = SID_WatchTime.filter(lambda p : p[1].startsWith("2023"))
SID_Year2022 = SID_WatchTime.filter(lambda p : p[1].startsWith("2022"))
SID_Year2021 = SID_WatchTime.filter(lambda p : p[1].startsWith("2021"))


2021_2022_2023 = SID_Year2023.fullouterJoin(SID_Year2022).fullouterJoin(SID_Year2021)\
map(lambda p : (p[0],(p[1][0][0],p[1][0][1],p[1][1])))


SID_SelectedYears = SID_WatchTime.join(2021_2022_2023)



def inactive_Student (line):
     
    SID = pair[0]
    WatchYear2023 = pair[1][0]
    WatchYear2022 = pair[1][1]
    WatchYear2021 = pair[1][2]

    if (Year2023 = None):

       return(SID,(WatchYear2021,WatchYear2022))


inactive_2021_2022 = SID_SelectedYears.map(inactive_Student)


def CountNumWatch (pair):

    SID = p[0]
    WatchYear2022 = pair[1][1]
    WatchYear2021 = pair[1][0]

   if (WatchYear2021.startsWith("2021")):
      return(SID,(1,0))

   if (WatchYear2022.startsWith("2022")):
      return(SID,(0,1))


       
result_2 = inactive_2021_2022.map(CountNumWatch)\
.reduceByKey(lambda v1,v2 : v1[0]+v2[0],v1[1]+v2[1])


result_2.saveAsTextFile(output_2)
```
