#數字運算
#x=7//6#整數除法
#print(x)
#y=2**3#次方
#print(y)
#c=2**0.5#開根號
#print(c)
#v=7%3#取餘數
#print(v)
#b=2+3
#print(b)
#b=b+1#將變數的數字+1
#x+=1
#x*=1
#x-=1
#print(b)
#字串運算
s="hell\"o"+"world"#也可用單引號，在雙引號前打斜線，是跳脫的意思，與外面的符號做區隔,用一個空白亦可做字串的串接
print(s)
s="hello\nworld"#\n=換行
print(s)
s="""hello
world"""#三個雙引或單引可直接換行
print(s)
s="hello"*3+"world"#字串乘於三遍，先乘除後加減
print(s)
s="hello"#每個字串會對內部的字元編號(索引)，從0開始算起
print(s[0])
print(s[1:4])#開頭與結束編號，包含開頭不包含結尾
print(s[1:])#包含開頭到結尾
print(s[:4])#包含開頭到結尾