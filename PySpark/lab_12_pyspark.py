"""
Big Data Architecture — Lab 12
PySpark solution notes

Source note: extracted from lab (12).txt

IMPORTANT:
This file preserves the typed PySpark pseudo-code from the lab notes.
Some snippets may require syntax cleanup, real input paths, a SparkContext,
and dataset schemas before execution.
"""

# --------
# 
# 
# ## 2 ##
# 
# ##### part 1 ######
# 
# inputPathCars = "exam_ex2_data/Cars.txt"
# inputPathFailures = "exam_ex2_data/CarsFailures.txt"
# outputPathPart1 = "outPart1"
# outputPathPart2 = "outPart2"
# 
# 
# carsRDD = sc.TextFile("inputPathCars")
# FailuresRDD = sc.TextFile("inputPathFailures")
# 
# 
# Engin_2017_2018 = FailuresRDD\
# .filter(lambda line : (line.split(",")[3]=="Engine") and 
# (line.split(",")[0].startsWith("2017") or line.split(",")[0].startsWith("2018")) )
# 
# 
# 
# #(CarID , year Of failure)
# pair_carID_year = Engin_2017_2018\
# .map(lambda line : ( line.split(",")[2] , line.split(",")[0].split("/")[0] ))
# 
# 
# 
# def count_failures (pair) : 
#     
#     CarID = pair[0]
#     Year = int (pair[1])
# 
#     if year == 2018 :
#   
#        return (carID,+1)
# 
#     if year == 2017 :
# 
#        return (carID,-1)
# 
# difference_2017_2018 = pair_carID_year.map(count_failures).reduceByKey(lambda v1,v2: v1+v2)
# 
# #(selected CarID , year Of failure)
# selected_cars = difference_2017_2018.filter(lambda p : p[1] > 0)
# 
# 
# #(carId,model)
# carID_model = carsRDD.map(lambda line : ( line.split(",")[0] , line.split(",")[1] )
# 
# #(selected carId,model)
# selected_carID_model=carID_model.join(selected_cars).map(lambda p: ( p[0] ,p [1][0] ))
# 
# 
# selected_carID_model.saveAsTextFile(output2)
# 
# 
# ########## part 2 #########
# 
# from datetime import detetime , timeDelta
# 
# 
# def previouseDate (myDate):
#     currentTime = datetime.strptime(myDate,"%Y/%M/%d")
#     previouseDate = currentTime - timedelata(days=1)
#     return previouseDate.strptime("%Y/%M/%d")
# 
# 
# 
# CarID_Date = FailureRDD.map(lambda line:(line.split(",")[2],line.split(",")[0]).distinct()
# 
# 
# 
# 
# def FlatMap (pair):
# 
#     returnedPair =[]
# 
#     CarID = pair[0]
#     CurrDate = pair[1]
#     prevDate = previouseDate(currDate)
# 
#     returnedPair.append(((CarID,CurrDate,+1))
#     returnedPair.append(((CarID,PrevDate,+1))
# 
#     return returnedPair
# 
# WindowElementsRDD = CarID_Date.map(FlatMap).reduceByKey(lambda v1,v2 : v1+v2)
# 
# SelectedWindowRDD = WindowElementsRDD.filter(lambda p : p[1] == 2)
# 
# result = selectedWindowRDD.saveAsTextFile(output2)
# 
# ---------------------------------------------------------------------------------------


if __name__ == "__main__":
    print("Lab 12 PySpark pseudo-code. Review the commented solution notes above before execution.")
