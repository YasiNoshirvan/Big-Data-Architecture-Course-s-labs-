"""
Big Data Architecture — Lab 05
PySpark solution notes

Source note: extracted from lab (5).txt

IMPORTANT:
This file preserves the typed PySpark pseudo-code from the lab notes.
Some snippets may require syntax cleanup, real input paths, a SparkContext,
and dataset schemas before execution.
"""

# -
# 
# ## 2 ##
# 
# servers_path = 'data/Servers.txt'
# patches_path = 'data/Patches.txt'
# applied_patches_path = 'data/AppliedPatches.txt'
# 
# outpath1 = 'out1'
# outpath2 = 'out2'
# 
# ########## part 1 #################
# 
# AppliedPatchsRDD = sc.TextFile(applied_patches_path)
# 
# 2022Applied = AppliedPatchsRDD.filter(lambda line : line.split(",")[2].startsWith("2022"))
# 
# SID_PID_2022 = 2022Applied.map(lambda line:(line.split(",")[1],line.split(",")[0]))
# 
# Count_PID = SID_PID_2022.map(line p : ( p[0] , +1 )).reduceByKey(lambda v1,v2 : v1+v2)
# 
# MaxNumPath = Count_PID.max()
# 
# result = Count_PID.filter( lambda p : p[1]==MaxNumPath )
# 
# result.key().saveasTextfile()
# 
# 
# ############ part 2 ################
# 
# ServersRDD = sc.TextFile(Servers_path)
# PatchsRDD = sc.TextFile(patches_path)
# AppliedPatchsRDD = sc.TextFile(applied_patches_path)
# 
# 
# #count avaliable patchs for each OS
# #(OS,NumPatchs)
# patchs_per_OS=patchsRDD\
# .map(lambda line : ( line.split(",")[2] , +1 ) )\
# .reduceByKey(lambda v1 , v2 : v1+v2)
# 
# 
# 
# 
# #count applied patchs for each server
# #(SID,NumPatchs)
# Patchs_per_server = AppliedPatchRDD\
# map(lambda line : ( line.split(",")[1] , +1 ) )\
# reduceByKey(lambda v1,v2 :v1+v2)
# 
# 
# 
# 
# # retrieve for each server its OS
# #(SID , OS)
# server_os_rdd = servers_rdd.map(lambda line:(line.split(',')[0],line.split(',')[1]))\
# .cache()
# 
# 
# 
# 
# #(SID, (count Applied Patches, OS))
# patch_per_server_with_os = Patchs_per_server.rightouterJoin(server_os_rdd)
# 
# 
# # map missing count values to 0
# SID_patchs_OS = patch_per_server_with_os\
# .map(lambda p : ( p[0],( 0 if p[1][0] is None else p[1][0] , p[1][1])))
# 
# 
# #(OS,(SID , count Applied Patches))
# OS_SID_Patchs = SID_patchs_OS.map(lambda p : (p[1][1],(p[0],p[1][0]))
# 
# 
# 
# 
# #( OS , ((SID, number_of_applied_patches), number_of_available_patches))
# joinRDD = OS_SID_Patchs.leftOuterJoin(patchs_per_OS)
# 
# 
# 
# 
# def filter_servers_with_all_applilied_patchs(pair):
# 
#     SID , applied_patchs = pair[1][0]
#     avaliabl_patchs = 0 if pair[1][1] is None else pair[1][1]
# 
#     return applied_patchs == avaliabl_patchs
# 
# result2= joinRDD.filter(filter_servers_with_all_applilied_patchs).map(lambda p:p[1][0][0])
# 
# result2.saveAsTextFile(output2)


if __name__ == "__main__":
    print("Lab 05 PySpark pseudo-code. Review the commented solution notes above before execution.")
