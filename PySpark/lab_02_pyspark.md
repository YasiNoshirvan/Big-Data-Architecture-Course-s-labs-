# Lab 02 — PySpark

Source note: extracted from `lab (2).txt`.

> This file contains typed lab notes / pseudo-code from Big Data Architecture exercises.  
> Some snippets may require syntax cleanup before execution in a real Hadoop or PySpark environment.

```python
----


## 2 ##

items_path = './exampleData20210705/items.txt'
ads_path = './exampleData20210705/ads_sales.txt'
users_path = './exampleData20210705/users.txt'


######## part 1 #########

itemsRDD = sc.TextFile(items_path)
adsRDD = sc.TextFile(ads_path)


Item_RecomPrice_Cat = itemsRDD\
.map(lambda line:(line.split(",")[0],(line.split(",")[2],line.split(",")[3])))

Item_SalePrice_True = itemsRDD\
filter(lambda line : line.split(",")[3] == "True")\
.map(lambda line:(line.split(",")[2],(line.split(",")[4],line.split(",")[3])))

joinRDD = Item_RecomPrice_Cat.join(Item_SalePrice_True)

for GreatersoldPrice (pair):
    
    RecomPrice = pair[1][0][0]
    soldPrice = pair[1][1][0]
    ItemID = pair[0]
    Category = pair[1][1][1]

    if soldPrice > RecomPrice : 

       return ( ItemID , (category,(1,1)))

    else : 

       return ( ItemID , (category,(0,1)))

    
Items_Greater_Sold_price = joinRDD.map(GreatersoldPrice)\
reduceByKey(lambda v1,v2 : (v1[1][0]+v2[1][0],v1[1][1]+v2[1][1]) )\
.filter(lambda p : p[1][1][0]/p[1][1][1]>0.9 )

result = Items_Greater_Sold_price.map(lambda pair : (pair[0],p[1][0]))


result.saveAsTextFile(output1)

######## part 2 #########

item_category = items\
.map(line.split(",")[0],line.split(",")[3]))


items_salePrice = AdsRDD.map(lambda line:(line.split(",")[2],line.split(",")[4]) )

profit_items = items_salePrice.reduceByKey(lambda v1,v2 : v1+v2)


item_profit_category = profit_items.join(item_category)

def UnAdv_LowProfit (pair):

    if (pair[1][0] is None or (pair[1][0]>0 and pair[1][0]<100)) :
   
        return True

    else :

        return False

UnAdv_LowProfit_Item = item_profit_category.filter(UnAdv_LowProfit)


def determine_UnAdv_LowProfit (pair) :

    if(pair[1][0] is None):

      U=1
      L=0

    if ( not pair[1][0] is None or (pair[1][0]>0 and pair[1][0]<100)) :

      U=0
      L=1

    return (pair[0] ,((U,L),pair[1][1]))

Count_UnAdv_LowProfit =  UnAdv_LowProfit_Item.map(determine_UnAdv_LowProfit)\
reduceByKey( lambda v1,v2 : v1[1][0][0]+v2[1][0][1])


result = Count_UnAdv_LowProfit.filter (lambda p : p[1][0][0]>10 and p[1][0][1]>10 )\
map(lambda p : (p[0],p[1][1]))


result.saveAsTextFile(output2)
```
