#判斷式
#x=input("請輸入數字:")#取得字串形式的使用者輸入
#x=int(x)#轉換為整數型態
#
#if x>200:
#    print("大於200")
#elif x>100:
#    print("大於100,小於200")
#else:
#    print("小於100")
#if True:
#    print("True 執行")
#else:
#    print("False 執行")
#四則運算
n1=int(input("請輸入數字:"))
n2=int(input("請輸入數字:"))
op=input("請輸入運算(+、-、*、/):")
if op=="+":
    print(n1+n2)
elif op=="-":
    print(n1-n2)
elif op=="*":
    print(n1*n2)
elif op=="/":
    print(n1/n2)
else:
    print("不支援的運算")