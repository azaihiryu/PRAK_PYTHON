def ditulis():
    f1=open('conto.txt','a')
    data1= input('masukkan sembarang : (X= Selesai) | ')
    while data1 != 'X' :
        f1.write(data1+"\n")
        data1= input('masukkan sembarang : (X= Selesai) | ')
    f1.close()
def baca():
    f1 = open('conto.txt','r')
    data = f1.read()
    print(data)
    f1.close()

def buat():
    f1 = open('conto.txt','w')

def menu():
    p=4
    while p != 0:
        print("1.Make : ")
        print("2.Modify : ")
        print("3.Read : ")
        print("0.End : ")
        p = int(input("Choice : "))
        if p==1 :
            buat()
            print("MAKED")
        elif p==2 :
            ditulis()
            print("MODDED")
        elif p==3 :
            baca()
            print("READED")
        else :
            print("Enter a Valid Number")
    print("THX")
    
