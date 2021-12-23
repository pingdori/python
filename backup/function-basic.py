#定義函式
#函式內部的程式碼沒有呼叫就不會執行
# def multiply(n1,n2):
#     print(n1*n2)
#     return n1*n2
# #呼叫函式
# # multiply(3,4)
# # multiply(10,8) 
# value=multiply(3,4)+multiply(10,5)#(3*4)+(10*5)
# print(value)

#函式可用來做程式的包裝:同樣的邏輯可重複利用
def calculate(max):
    sum=0
    for n in range(1,max+1):
            sum=sum+n
    print(sum)
calculate(10)
calculate(20)