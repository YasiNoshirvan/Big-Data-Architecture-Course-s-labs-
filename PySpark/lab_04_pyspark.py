"""
Big Data Architecture — Lab 04
PySpark solution notes

Source note: extracted from lab (4).txt

IMPORTANT:
This file preserves the typed PySpark pseudo-code from the lab notes.
Some snippets may require syntax cleanup, real input paths, a SparkContext,
and dataset schemas before execution.
"""

# ---
# 
# 
# ## 2 ##
# 
# usersPath = 'ExampleData/Users.txt'
# appsPath = 'ExampleData/Apps.txt'
# actionPath = 'ExampleData/Actions.txt'
# output1 = 'outPart1/'
# output2 = 'outPart2/'
# 
# ########## part 1 #################
# 
# AppsRDD = sc.TextFile(appsPath)
# ActionRDD = sc.TextFile(ActionPath)
# 
# 2022_Installed_App=ActionRDD\
# .filter(lambda line : line.split(",")[2].startsWith("2022") and
#  line.split(",")[3] == "installed")\
# .map(lambda line : (line.split(",")[0],line.split(",")[1]))
# 
# Price_APP = AppRDD.map(lambda line : (line.split(",")[0],line.split(",")[2]))
# 
# 
# #(AppID,(UserID,Price))
# Considered_apps = 2022_Installed_App.join(Price_APP)
# 
# 
# def Free_NonFree (pair):
# 
#     AppID=pair[0]
#     UserID=pair[1][0]
#     Price=int(pair[1][1])
#   
#     if price = 0:
#        return (UserID,(1,0)
# 
#     if price > 0 :
#        return (UserID,(0,1)
# 
# Count_Free_nonFree = Considered_apps.map(Free_NonFree)\
# .reduceByKey(lambda v1,v2 : v1[0]+v2[0] , v1[1]+v2[1])
# 
# 
# Users_more_NonFree = Count_Free_nonFree.filter(lambda p : p[1][1] > p[1][0])
# 
# 
# result=Users_more_NonFree.map(lambda p : (p[0],p[1][1]))
# 
# 
# result.SaveAsTextFile(output1)
#     
# 
# ############ part 2 ################
# 
# UsersRDD=sc.TextFile(UsersPath)
# 
# 
# # ( (Italin user Id , None)
# ItalianUsers=UserRDD.filter(lambda line : line.split(",")[3]=="italian")\
# .map(la,mbda line : (line.split("0"),None))
# 
# 
# #( userId, (appId, timestamp, action)) 
# ActionMap = ActionRDD.map(lambda line :
# (line.split(",")[0],(line.split(",")[1],line.split(",")[2],line.split(",")[3])) )
# 
# 
# #( Italin user Id , (appId, timestamp, action)) 
# consideredUsers = ItalianUsers.join(ActionMap)
# 
# 
# #( (Italin user Id , appId ), (timestamp, action)) )
# MapUserApp = consideredUsers.map(lambda p : ((p[0],p[1][0]),(p[1][1],p[1][2])))
# 
# 
# 
# Users = MapUserApp.reduceByKey(determineLastAction)
# 
# 
# 
# LastActionUserApp = MapUserApp.reduceByKey(lambda v1 , v2 : max(v1[0],v2[0]))
# 
# 
# 
# CurrentInstallAction = LastActionUserApp,filter(lambda p : p[1][1]=="install")
# 
# 
# 
# count_current_install_app = CurrentInstallAction.map(lambda p:(p[0][0] , +1 ))\
# .reduceByKey(lambda v1,v2 : v1+v2)
# 
# Max_Num_current_installed = count_current_install_app.max()
# 
# 
# result = count_current_install_app.filter(lambda p : p[1] == Max_Num_current_installed )
# 
# result.key().SaveAsKey()


if __name__ == "__main__":
    print("Lab 04 PySpark pseudo-code. Review the commented solution notes above before execution.")
