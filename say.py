say1=float(input("1. sayıyı girin"))
say2=float(input("2. sayıyı girin"))
islem=input("lütfen yapmak istediğiniz işlem için parametreyi girin +,-,*,/,**")

if(islem=="+"):
    print(f"sonuç {say1+say2}")
elif(islem=="-"):
    print(f"sonuç {say1-say2}")
elif(islem=="*"):
    print(f"sonuç {say1*say2}")
elif(islem=="/"):
    print(f"sonuç {say1/say2}")
elif(islem=="**"):
    print(f"{say1**say2}")
else:
    print(f"hatalı parametre girdiniz")