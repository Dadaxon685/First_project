print(f"Restoranga Xush kelibsiz!\nQaysi bo'limga murojat qilasiz!")

suyuq_taomlar = ["1: sho'rva", "2: tuxumli ramyon", "3: baliqli sho'rvasi", "4: oddiy sho'rva"]
suyuq_taomlar_narxlari = [100000, 50000, 45000, 25000]

quyuq_taomlar = ["1: osh", "2: manti", "3: shashlik", "4: somsa"]
quyuq_taomlar_narxlari = [27000, 8000, 10000, 12000]

total_cost = 0

while True:
    tanlash = input(f"1: Suyuq taomlar \n2: Quyuq taomlar \n3: Xarid qilmayman  ")
    
    if tanlash == "1":
        print("\nSuyuq taomlar:")
        for item in zip(suyuq_taomlar, suyuq_taomlar_narxlari):
            print(f"{item[0]} --> {item[1]} UZS")

        tanlash2 = input("\nTaomni tanlang (raqamini kiriting): ").lower()
        
        if tanlash2 in [item.lower() for item in suyuq_taomlar]:
            index = suyuq_taomlar.index(tanlash2.title())
            qancha = int(input("Nechta? : "))
            item_cost = qancha * suyuq_taomlar_narxlari[index]
            total_cost += item_cost
            print(f"{qancha} ta {suyuq_taomlar[index]} narxi: {item_cost} UZS")
    
    elif tanlash == "2":
        print("\nQuyuq taomlar:")
        for item in zip(quyuq_taomlar, quyuq_taomlar_narxlari):
            print(f"{item[0]} --> {item[1]} UZS")
        
        tanlash2 = input("\nTaomni tanlang (raqamini kiriting): ").lower()
        
        if tanlash2 in [item.lower() for item in quyuq_taomlar]:
            index = quyuq_taomlar.index(tanlash2.title())
            qancha = int(input("Nechta? : "))
            item_cost = qancha * quyuq_taomlar_narxlari[index]
            total_cost += item_cost
            print(f"{qancha} ta {quyuq_taomlar[index]} narxi: {item_cost} UZS")
            print("Osh bolsin yana keling! :)")
            break
    
    elif tanlash == "3":
        print(f"Xaridingiz uchun raxmat! Umumiy summa: {total_cost} UZS")
        break
    
    else:
        print("Notog'ri tanlov, qaytadan urinib ko'ring.")
