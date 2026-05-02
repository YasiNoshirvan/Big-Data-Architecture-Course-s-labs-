# Lab 11 — PySpark

Source note: extracted from `lab (11).txt`.

> This file contains typed lab notes / pseudo-code from Big Data Architecture exercises.  
> Some snippets may require syntax cleanup before execution in a real Hadoop or PySpark environment.

```python
-

## 2 ##

########## part 1 #################

purchasePath = "data/Purchases.txt";
usersPath = "data/Users.txt"; Useless for this application
cataloguePath = "data/Catalogue.txt";

outputPath1 = "outPart1_v2/";
outputPath2 = "outPart2_v2/";



def Year_2022_2023 (line):

    fields = line.split(",")

    Year = fields[0].split("/")[0]
    UserID = fields[1]
    ItemID = fields[2]

    if (Year=2022 or Year =2023):

       return(UserID,(ItemID,Year))

2022_2023_purchases = purchasePath.map(Year_2022_2023)


def CountPurchases2022 (p):

    User = p[0]
    Item = p[1][0]
    Year = int (p[1][1]) 
    
    if (year == 2022):
       return(user,1)

def CountPurchases2023 (p):

    User = p[0]
    Item = p[1][0]
    Year = int (p[1][1]) 
    
    if (year == 2023):
       return(user,1)




count_2022_purchases = 2022_2023_purchases.map(CountPurchases2022)\
                       .reduceByKey(lambda v1,v2 : v1+v2)

max_2022_purchases = count_2022_purchases.value().max()


max_purchases_2022 = count_2022_purchases.filter(lambda p : p[1] = max_2022_purchases)




count_2023_purchases = 2022_2023_purchases.map(CountPurchases2023)
                       .reduceByKey(lambda v1,v2 : v1+v2)

max_2023_purchases = count_2023_purchases.value().max()


max_purchases_2023 = count_2023_purchases.filter(lambda p : p[1] = max_2023_purchases)




result_1 = max_purchases_2023.rightOuterJoin(max_purchases_2022)

result_1.key().saveAsTextFile(output_1)



############ part 2 ################


def Year_2022_2023 (line):

    fields = line.split(",")

    Year = fields[0].split("/")[0]
    UserID = fields[1]
    ItemID = fields[2]

    if (Year=2022 or Year =2023):

       return( ItemID , UserID )

Item_User = purchasePath.map(Year_2022_2023)


Item_category = CatalogPath.map(lambda line : (line.split(",")[0],line.split(",")[2]))



Item_User_category = Item_category.join(Item_User)

#((Categoty,ItemID),UderID)
Ctegory_Item_User = Item_User_category.map(lambda p : ((p[1][1],p[0]) ,p[1][0])).distinct()

count_Purchased_Items = Ctegory_Item_User.map(lambda p : ((p[0][0],p[1][1]),+1)\
reduceByKey.(lambda v1,v2 : v1+v2)

Max_Purchased = count_Purchased_Items.value().max()


Max_Purchased_Items = count_Purchased_Items.filter(lambda : p[1]==Max_Purchased )


#(Catalog,MaxPurchasedItem)

result_2 = Max_Purchased_Items.map(lambda p : (p[0][0],p[0][1]))


result_2.saveAsTextFile(output_2)
```
