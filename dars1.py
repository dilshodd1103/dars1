
print("Assalom alaykum \n'ARISTOKRAT AVTO' saloniga xush kelibsiz ")
a=input("sizga mashinalarimizni ro'yxatini beraymi? ")
if a=="ha":
    print ("kia k5"  ,   "jetour" ,   "cherry ", )
    b=input("sizga qaysi biri maqul ")

    if b=="kia k5":
        print ("bizda uning 'lux', 'Komfort', 'Premium' kabi pazitsiyalar mavjud. \n Sizga qaysi biri maqul: ")
        f=input("menga narxlari haqida ham ma'lumot bersangiz ")
        if f==" narxlar":
            print("HOZIRGI KUNDAGI NARXLAR")
        g=["lux --- 33 000 $" , "komfort --- 35 000$" , "premium --- 38 000$"]
        print(g)
        d=input("sizga qaysi biri ma'qul: ")
        if d=='lux':
            print ("kechirasiz bu pozitsiya hozir pozitsiya sotuvda qolmabdi. ")
        elif d=="komfort":
            s="naqd pulga 34 000 $ qilib beramiz \n agar variantga bo'lsa 4 000 $ bilan chiqarib beramiz"
            print(s, "\n sizga ma'qul kelsa xujjatlarni rasmiylashtirammiz")
        elif d=="premium":
            s="naqd pulga 36 000 $ qilib beramiz \n agar variantga bo'lsa 7 000 $ bilan chiqarib beramiz"
            print(s, "\n sizga ma'qul kelsa xujjatlarni rasmiylashtirammiz")
        else:
            print("mashina emas arava oling")

    if b=="jetaur":
        print("bizda uning  'Komfort' 'Premium' kabi pazitsiyalar mavjud. \n Sizga qaysi biri maqul: ")
        f=input("menga narxlari haqida ham ma'lumot bersangiz ")
        if f==" narxlar":
            print("HOZIRGI KUNDAGI NARXLAR")
        g=[ "komfort --- 32 000$" , "premium --- 38 000$"]
        print(g)
        d=input("sizga qaysi biri ma'qul: ")
        if d=='lux':
            print ("kechirasiz bu pozitsiya hozir pozitsiya sotuvda qolmabdi. ")
        elif d=="komfort":
            s="naqd pulga 32 000 $ qilib beramiz \n agar variantga bo'lsa 4 000 $ bilan chiqarib beramiz"
            print(s, "\n sizga ma'qul kelsa xujjatlarni rasmiylashtirammiz")
        elif d=="premium":
            s="naqd pulga 38 000 $ qilib beramiz \n agar variantga bo'lsa 7.5 000 $ bilan chiqarib beramiz"
            print(s, "\n sizga ma'qul kelsa xujjatlarni rasmiylashtirammiz")
        else:
            print("sizga mashina minishni kim qo'yibdi")

    if b=="cherry":
        print ("bizda uning 'lux', 'Komfort',  kabi pazitsiyalar mavjud. \n Sizga qaysi biri maqul: ")
        f=input("menga narxlari haqida ham ma'lumot bersangiz ")
        if f==" narxlar":
            print("HOZIRGI KUNDAGI NARXLAR")
        g=["lux --- 30 000 $" , "komfort --- 35 000$" ]
        print(g)
        d=input("sizga qaysi biri ma'qul: ")
        if d=='lux':
            print ("kechirasiz bu pozitsiya hozir pozitsiya sotuvda qolmabdi. ")
        elif d=="komfort":
            s="naqd pulga 28 000 $ qilib beramiz \n agar variantga bo'lsa 4 000 $ bilan chiqarib beramiz"
            print(s, "\n sizga ma'qul kelsa xujjatlarni rasmiylashtirammiz")
        elif d=="premium":
            s="naqd pulga 34 000 $ qilib beramiz \n agar variantga bo'lsa 7 000 $ bilan chiqarib beramiz"
            print(s, "\n sizga ma'qul kelsa xujjatlarni rasmiylashtirammiz")
        else:
            print("mashina emas arava oling")

# print("bizda sotuvda mavjud mashinalar:")
# mashinalar=[]
# mashinalar.append('lacetti')
# mashinalar.append("nexia")
# mashinalar.append("damas")
# mashinalar.append("tico")
# mashinalar.append("malibu")
# mashinalar.append("tracker")
# mashinalar.append("cobalt")
# mashinalar.append("lacetti")
# print(mashinalar)
# r=input ('siz qaysi birini olasiz:  ' )
# b=mashinalar.pop(0)
# print("siz bining salondan " , b , "oldingiz\nbizda qolgan mashinalar: ")
# print(mashinalar)
# a=input ('siz qaysi birini olasiz:  ' )
# d=mashinalar.pop(1)
# print("siz bizning salondan " , d , "oldingiz\nbizda qolgan mashinalar: ")
# print(mashinalar)
# b=input ('yana mashina olishni istaysizmi?:  ' )
# e=mashinalar.pop(2)
# print("siz bizning salondan " , e , "oldingiz\nbizda qolgan mashinalar: ")
# print(mashinalar)
# u=input ('yutuqli o\'yinda ishtirok etish uchun yana xarid qiling :  ' )
# c=mashinalar.pop(3)
# print("siz bizning salondan " , c, "oldingiz\nbizda qolgan mashinalar: ")
# print(mashinalar)
# t=input ('sotib oluvchilarga qaysi birini tavsiya qilasiz :  ' )
# f=mashinalar.pop(4)
# print("siz bizning salondan " , f, "oldingiz\nbizda qolgan mashinalar: ")
# print(mashinalar)
# q=input ('aslida olishni xohlagan mashinangiz:  ' )
# l=mashinalar.pop(5)
# print("siz bizning salondan " , l, "oldingiz\nbizda qolgan mashinalar: ")
# print(mashinalar)
# z=input ('arzonlashtirib bersak boshqa moshina olasizmi?:  ' )
# w=mashinalar.pop(6)
# print("siz bizning salondan " , w, "oldingiz\nbizda qolgan mashinalar: ")
# print(mashinalar)
# h=input ('yutuqli o\'yinning bonusiga mashina tanlang:  ' )
# k=mashinalar.pop(7)
# print("siz bizning salondan " , k , "oldingiz\nbizda qolgan mashinalar: ")
# print(mashinalar)
