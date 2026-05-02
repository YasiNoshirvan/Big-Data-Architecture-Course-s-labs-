"""
Big Data Architecture — Lab 03
PySpark solution notes

Source note: extracted from lab (3).txt

IMPORTANT:
This file preserves the typed PySpark pseudo-code from the lab notes.
Some snippets may require syntax cleanup, real input paths, a SparkContext,
and dataset schemas before execution.
"""

# -
# 
# ## 2 ##
# 
# import pyspark
# import datetime
# 
# from pyspark import SparkContext
# from pyspark.sql import SparkSession
# 
# items_catalog_path = '../items.txt'
# customers_path = '../customers.txt'
# purchases_path = '../purchases.txt'
# 
# out1 = 'res/out1'
# out2 = 'res/out2'
# 
# ########## part 1 #################
# 
# PurchasedRDD = sc.TextFile(purchases_path)
# 
# 
# def Year_2010_2019 (line):
#    
#     year = int(line.split(",")[0].split("/")[0])
#     ItemID = line.split(",")[1]
# 
#     if ( year>=2010 and year<=2019) :
# 
#        return (ItemID , year)
# 
# Purchased_2010_2019 =  Year_2010_2019.map( Year_2010_2019)
# 
# 
# #check the Item is purchased in all 10 years or not
# count_Purchased_year = Purchased_2010_2019.mapValue(lambda v : {v})\
# .reduceByKey(lambda v1 , v2 : v1.union(v2) )\
# .filter(lambda p : len(p[1]) == 10 )
# 
# 
# #((Item,Year), Num Purchase Each Year)
# Item_Year_NumPurchase = Purchased_2010_2019.join(count_Purchased_year)\
# .map(lambda p : ((p[0],p[1][0]),+1))\
# .reduceByKey(lambda v1,v2 : v1+v2)
# 
# 
# result = Item_Year_NumPurchase.filter(lambda p : p[1]>=1000 )\
# .map(lambda p : (p[0][0],(p[0][1],p[1])))
# 
# result.key().saveAsTextfile(output1)
# 
# 
# ############ part 2 ################
# 
# 
# PurchasedRDD = sc.TextFile(purchases_path)
# ItemCatalogRDD = sc.TextFile(ItemsCatalogs_path)
# 
# 
# def PurchasedBefor2010 (line):
# 
#     fields=line.split(",")
# 
#     salesTime = fields[0]
#     ItemID = fields[2]
# 
#     if SalesTime < 2010/01/01-00:00:00:
# 
#        returne(ItemID,SalesTime)
#  
# Items_Purchased_Befor_2010 = PurchasedRDD.map(PurchasedBefor2010)
# 
# 
# ItemID_Catalog = ItemCatalogRDD\
# .map(lambda line: (line.split(",")[0],(line.split(",")[2],line.split(",")[3]))
# 
# 
# JoinedRDD = ItemID_Catalog.rightOuterjoin(Items_Purchased_Befor_2010)
# 
# 
# 
# def compute_difference(t1, t2):
#     t1_t = datetime.datetime(*get_data_from_timestamp(t1))
#     t2_t = datetime.datetime(*get_data_from_timestamp(t2))
#     delta = t1_t - t2_t
# 
#     return delta.days / 365
# 
# 
# 
# def get_data_from_timestamp(t, has_hours=True):
#     if has_hours:
#         first, second = t.split('-')
#         hours, minutes, seconds = second.split(':')
#         hours, minutes, seconds = int(hours), int(minutes), int(seconds)
#         year, month, day = first.split('/')
#         year, month, day = int(year), int(month), int(day)
#     else:
#         first = t
#         second = None
#     year, month, day = first.split('/')
#     year, month, day = int(year), int(month), int(day)
#     return (year, month, day) if not has_hours else (year, month, day, hours, minutes, seconds)
# 
# 
# def map_joined_data(it):
#     itemid = it[0]
#     time_catalog = it[1][1][0]
#     category = it[1][1][1]
#     
#     if it[1][0] is None :
#        purchase_date = -1
#     else:
#         purchase_date=it[1][0]    
# 
#     key = (itemid, category)
#     if purchase_date == -1 or compute_difference(purchase_date, time_catalog) > 2 :
#       value = 0 
#     else :
#       value = 1
#     return (key, value)
# 
# 
# 
# 
# sales_within_two_years_rdd = JoinedRDD.map(map_joined_data)\
# .reduceByKey(lambda it1, it2: it1 + it2)
# 
# 
# # Select only those items in which count == 0
# # These are the NotSoldFirst2Years items
# unsold_within_two_years_rdd = sales_within_two_years_rdd.filter(lambda it: it[1] == 0)
# 
# 
# 
# # count the number of items per category which was unsold within two years
# unsold_items_count_per_category = unsold_within_two_years_rdd\
# .map(lambda it: (it[0][1], 1)).reduceByKey(lambda i1, i2: i1 + i2)
# 
# 
# 
# # keep only the categories with count >= 50
# res2 = unsold_items_count_per_category.filter(lambda it: it[1] >= 50)
# 
# 
# res2.saveAsTextFile(out2)


if __name__ == "__main__":
    print("Lab 03 PySpark pseudo-code. Review the commented solution notes above before execution.")
