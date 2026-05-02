"""
Big Data Architecture — Lab 14
PySpark solution notes

Source note: extracted from lab (14).txt

IMPORTANT:
This file preserves the typed PySpark pseudo-code from the lab notes.
Some snippets may require syntax cleanup, real input paths, a SparkContext,
and dataset schemas before execution.
"""

# ####################### part 1 #####################
# 
# 
# housesPath= 'Houses. txt'
# consumptionPath= 'MonthlyWaterConsumption.txt'
# output1= 'outPart1/'
# output2= 'outPart2/'
# 
# 
# # Write your code here
# house_rad=sc.TextFite (housespath)
# consumption_rad=sc. TextFite (consumptionpath)
# 
# #(HID, country)
# HID_country=house_rdd.map(lambda line : (line.split(",")[0],line.split(", ")[2]))
# 
# #(HID, monthly consumption 2021)
# consumption2021 = consumption rdd. filter (lambda line : line split(",")[1 lastartsWith("2021"))\
# •map (lambda line : (line-split(", ")[0],line.split(",")[2]))
# 
# #(HID, monthly consumption 2022)
# consumption2022 = consumption rdd. filter(lambda line : line.split(",") [1lastartswith("2022"))\
# •map (lambda line : (line.split(",")[0],line.split(",")[1]))
# 
# #(HID , AVG 2021)
# AVG_consumption2021=Consumption2021.reduceByKey(lambda V1, v2 : v1+v2) -mapValue(lambda v : v/12)
# 
# #(HID , AVG 2022)
# AVG_consumption2022=Consumption2022. reduseByKey (lambda v1, v2 : V1+v2) _mapValue (Lambda v : v/12)
# 
# #(HID, (AVG 2021 , AVG 2022))
# HID_AVG2021_AVG2022 = Avg_consumption2021.join(Avg_consumption2022)
# 
# 
# result_1 = HID_AVG2021_AVG2022. filter (lambda pair : pair [1][1]/pair [1][0] >= 1.1 )\
# • join(HID_country) \
# •map (lambda p : (p[0],p[1][1]))
# 
# 
# result 1. saveAsTextFite(output_ 1)
# 
# 
# ####################### part2 #############################
# 
# year2022 = consumption_rdd. filter (lambda line : line.split(",")[1]-startsWith("2022"))
# 
# HID_monyhlyConsumption2022 = year2022.map(lambda line : (line.split(",")[0],(line.split(",")[1],line.split(",")[2])))
# 
# 
# def determineIncreasing (P)
#     LastMonth = " "
#     maxConsumption = 0
#     NumIncreasing = 0
#     HID = p[0]
#     date = p[1]
#     m3 = P|2]
# 
# 
#     if ( (LastMonth != " ") and (date>LastMonth) and (m3>maxConsumption) ):
#         LastMonth = date
#         MaxConsumption = m3
#      
#         return (HID,+1)
#    else :
#         return(HID,)
# 
# 
# 
# Coumt_Num_Increasing = HID_monthlyConsumption2022.map(determineIncreasing)\
#   .reduceByKey(lambda v1,v2 :  v1+v2)
# 
# House_with_inceasing_consumption=Count_num_increasing.filter(lambda p : p[1]>=1)
# 
# 
# #(HID, country)
# HID_country=house_rdd.map(lambda line : (line.split(",")[0],line.split(", ")[2]))
# 
# #(selected Houses , country)
# result_2 = House_with_increasing_consumption.join(HID_country).filter(lambda p : (p[0],p[1][1]))
# 
# result_2.saveAsTextFile(output_2)


if __name__ == "__main__":
    print("Lab 14 PySpark pseudo-code. Review the commented solution notes above before execution.")
