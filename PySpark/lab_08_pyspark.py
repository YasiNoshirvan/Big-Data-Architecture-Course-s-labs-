"""
Big Data Architecture — Lab 08
PySpark solution notes

Source note: extracted from lab (8).txt

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
# ########## part 1 #################
# 
# import pyspark as ps
# 
# from pyspark import SparkContext, RDD
# from pyspark.sql import SparkSession, Row
# 
# from typing import List, Tuple, Dict, Iterable
# from typing import Optional
# 
# 
# customers_rdd = sc.textFile('data/customers.txt')
# meetings_rdd = sc.textFile('data/meetings.txt')
# invitations_rdd = sc.textFile('data/invitations.txt')
# participations_rdd = sc.textFile('data/participations.txt')
# 
# 
# CID_pricingPlan = customers_rdd.map(lambda line: (line.slit(",")[0],line.split(",")[3]) )
# CID_Duration = meetings_rdd.map(lambda line: (line.slit(",")[4],line.split(",")[3]))
# 
# 
# pricingPlan_duration = CID_pricingPlan.join(CID_Duration).map(lambda p: (p[1][0],p[1][1]))
# 
# def countLongMeeting (pair):
#     
#     pricingPlan = pair[0]
#     Duration = pair[1]
# 
#     if (Duration > 60):
#        return (pricingPlan ,(1,1))
#     else : 
#         return (pricingPlan ,(0,1))
# 
# 
# countLongMeeting = pricingPlan_duration.map(countLongMeeting)\
# reduceByKey(lambda v1,v2 : (v1[0]+v2[0]) / (v1[1]+v2[1]) )
# 
# result_1 = countLongMeeting.filter( lambda pair : pair[1][1] >= 0.9 )
# 
# result_1.key().saveAsTextFile(output_1)
# 
# 
# ############ part 2 ################
# 
# invitation_rdd = sc.TextFile(invitation_path)
# participation_rdd = sc.TextFile(participation_path)
# 
# 
# def Year2023 (line):
#     fields = line.split(",")
#  
#     MID = fields[0]
#     time  = field[2]
# 
#     if (time<2023/01/01 - 00:00):
#        return(MID,None)
# 
# 
# MID_year2023 = meeting_rdd.map(year2023)
# 
# 
# 
# MID_CID_Accepted = invitation_rdd\
#   .map(lambda line: (line.split(",")[0],line.split(",")[1],line.slit(",")[2])
# 
# invitation2023 = MID_year2023.join(MID_CID_Accepted).map(lambda p : (p[1][0],p[1][1]))
# 
# 
# MID_CID_JoinTime = participation\
#   .map(lambda line : (line.split(",")[0],(line.split(",")[1],line.split(",")[2])))
# 
# participation2023 = MID_year2023.join(MID_CID_JoinTime).map(lambda p : (p[1][0],p[1][1]))
# 
# 
# invited_CID = invitation2023.fullOuterJoin(participation2023)
# 
# def MisMatch(pair):
# 
#     CID = p[0]
#     Accepted = p[1][0]
#     Present = p[1][1]
# 
#     if ((Accepted == "Yes" and present is None):
# 
#         return (CID , (1,0))
# 
#     if (accepted == "No" and not present is None):
# 
#         return (CID , (0,1))
# 
# count_mismatch = invited_CID.map(MisMatch)\
#   .reduceByKey(lambda v1,v2 : v1[0]+v2[0],v1[1]+v2[1])
# 
# 
# CID_MaxMismatch_1=count_mismatch.filter(lambda p : max(p[1][0]))
# CID_MaxMismatch_2=count_mismatch.filter(lambda p : max(p[1][1]))
# 
# 
# 
# result_2 = CID_MaxMismatch_1.join(CID_MisMatch_2)
# 
# result_2.SaveAsTextFile(output2)


if __name__ == "__main__":
    print("Lab 08 PySpark pseudo-code. Review the commented solution notes above before execution.")
