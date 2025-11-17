#1
nomber1=int(input("xoxlagan sonini kirit "))
try:
    nomber1=int(input("2-xoxlagan sonini kirit: "))
except(ValueError):
    print("sonni kiriting")
finally:
    print("amaliyot tugadi:")

#2
try:
    print(nomber1/0)
except(ZeroDivisionError):
    print("sonni nolga bo'lib bo'lmaydi: ")
finally:
    print("amaliyot tugadi")

#3
try:
    list1=[2,6,36,3,73,73,63,]
    print(list1[9])
except(SyntaxError):
    print("error")
finally:
    print("amaliyot yakunlandi")

#4
try:
    sa=open("aziz.txt","r")
except(IndentationError):
    print("uzuuuuur")

finally:
    print("amaliyot yakunlandi")

#5
try:
    matn="bexruz antoshka"
    print(matn+64)
except(TypeError):
    print("uzuuur siz xota qildingiz")
finally:
    print("amaliyot yakunlandi")