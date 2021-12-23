#有序可變動列表list
#grades=[12,60,15,70,90]
#print(grades)
#print(grades[0])
#grades[0]=55#把55放到列表中的第一個位置

#grades[1:4]=[]#連續刪除列表中從編號1到編號4(不包括)的資料
#grades=grades+[12,33]
#length=len(grades)#取得列表的長度len
#print(length)
#print(grades[1:4])

#巢壯列表
#data=[[3,4,5],[6,7,8]]
#print(data[0][1])#data代表第一層[0]為第二層的位置[1]為4的位置
#data[0][0:2]=[5,5,5]
#print(data)
#有序不可變動列表Tuple
data=(3,4,5)#Tuple用小括號
data[0=5]#錯誤:Tuple的資料不可更動
print(data[0:2])