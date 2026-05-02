"""
Big Data Architecture — Lab 07
PySpark solution notes

Source note: extracted from lab (7).txt

IMPORTANT:
This file preserves the typed PySpark pseudo-code from the lab notes.
Some snippets may require syntax cleanup, real input paths, a SparkContext,
and dataset schemas before execution.
"""

# ---
# 
# 
# 
# ## 2 ##
# 
# ########## part 1 #################
# 
# companies_rdd = sc.textFile('companies.txt')
# dc_rdd = sc.textFile('dataCenters.txt')
# gpus_rdd = sc.textFile('gpus.txt')
# 
# 
# 
# #(codC,CompanyName)
# codC_companyName = companies_rdd\
# .filter(lambda line:int(line.split(",")[2])>=200)\
# .map(lambda line : (line.split(",")[0],line.split(",")[1]))
# 
# 
# 
# #(codC,None)
# codC_more_than_200_employee = companies_rdd\
# .filter(lambda line:int(line.split(",")[2])>=200)\
# .map(lambda line : (line.split(",")[0],None))
# 
# 
# 
# #(CodC,(size,continnt))
# DC_info = dc_rdd\
# .map(lambda line:(line.split(",")[1], (line.split(",")[2],line.split(",")[5]) ))
#  
# def CounEuropencities (pair):
# 
#     codC=p[0]
#     Size=p[1][0]
#     continent=p[1][1]
# 
#     if (continent=="Europe"):
#         returne(codC,(size,1))
#     else:
#         returne(codC,(size,0))
# 
# CodeC_Size_NumEU = DC_info.map(DC_info).reduceByKey(lambda v1,v2: v1[1]+v2[1])\
# .filter(lambda p : p[1][1]>=10)
# 
# 
# #(CodeC , Size)
# SelectedCompany = CodeC_Size_NumEU.map(lambda p : (p[0],p[1][0]))
# 
# Min_Size =  CodeC_Size.values().min()
# Max_Size =  CodeC_Size.values().max()
# 
# CodC_MinSize = SelectedCompany.filter(lambda p : p[1]==Min_Size )
# CodC_MaxSize = SelectedCompany.filter(lambda p : p[1]==Max_Size )
# join_MinMax = CodC_MinSize.join(CodC_MaxSize)
# 
# 
# #(codC , CompanyName , MinSize , MaxSize)
# result_1 = SelectedCompany.join(codC_companyName).join(join_MinMax)\
# map(lambda p : (p[0] , p[1][0][1] , p[1][1][0], p[1][1][1]))
# 
# 
# result_1.saveAsTextFile(output1)
# 
# 
# ############ part 2 ################
# 
# #(CodDC , type GPU)
# CodeDC_GPU_Type = gpu_rdd.map(lambda line : (line.split(",")[2],line.split(",")[1]) )
# 
# #(CodDC ,CodC)
# CodDC_CodC = DC_rdd.map(lambda line : (line.split(",")[0],line.split(",")[1]) )
# 
# #(CodC,(CodDC,type))
# CodC_CodDC_Type=CodDC_CodC.join(CodeDC_GPU_Type).map(lambda p: (p[1][0] , (p[0],p[1][1]) ))
# 
# #(CodeC,None)
# codeC=Company_rdd.map(lambda line:(lambda.split(",")[1],None))
# 
# #(CodC,(CodDC,type))
# 
# All = CodeC.join(CodC_CodDC_Type)
# 
# 
# def Special_Type_GPU (pair):
# 
#     CodC=pair[0]
#     CodDC=pair[1][0]
#     Type=pair[1][1]
# 
#     if Type=="NVIDIA RTX A5000":
#        return ((CodC,CodeDc),+1)
#         
# #((CodC,CodeDc),+1)
# Specal_GPU = All.map(Special_Type_GPU)
# 
# 
# #((CodC,CodeDc),Num GPU in each DC)
# Total_GPU_each_DC = Specal_GPU.reduceByKey(lambda v1,v2 : v1+v2)
# 
# 
# #( CodC , Num GPU in each DC )
# CodC_NumGPU = Total_GPU_each_DC.map(lambda p : (p[0],p[1][1]) )
# 
# result_2 = CodC_NumGPU.mapValue(lambda v : {v}).reduceByKey(lambda v1,v2: v1.union(v2))\
# .filter(lambda pair : len(pair[1]==1))
# 
# result_2.key().saveAsTextFile(output2)


if __name__ == "__main__":
    print("Lab 07 PySpark pseudo-code. Review the commented solution notes above before execution.")
