res = {
    "go'shtli": {
        "1. kebab": 50000,
        "2. qazon kebab": 60000,
        "3. tandir kebab": 100000,
    },
    "oddiy taomlar": {
        "1. pizza": 50000,
        "2. zaqasnoy osh 1kg": 100000,
        "3. somsa": 12000,
        "4. gamburger": 11000,
    },
    "ichimliklar": {
        "1. pepsi 1 L": 12000,
        "2. pepsi 1.5 L": 14000,
        "3. fanta 1 L": 13000,
        "4. cok --> dena 1L": 13000,
        "5. cok --> sochnaya dolina 1L": 12500,
    },
    "shirinliklar": {
        "1. shkolatli qulupnay 1 donasi": 6000,
        "2. mavali tort": 15000,
        "3. tug'ulgan kun torti": 250000,
    }
}

tanlash = []
sum_narx = []

while True:
    print("\nRestoranga xush kelibsiz!!\nBo'limlardan birini tanlang:")
    

    bolimlar = list(res.keys())  
    for idx, bolim in enumerate(bolimlar, 1):
        print(f"{idx}. {bolim}")  


    user_bolim = input("\nKategoriyani tanlash uchun raqamini kiriting (yoki xaridni yakunlash uchun '0' deb yozing): ")

    if user_bolim == '0':  
        break


    if user_bolim.isdigit() and 1 <= int(user_bolim) <= len(bolimlar):
        bolim_tanlangan = bolimlar[int(user_bolim) - 1]  

        while True:
            print(f"\n{bolim_tanlangan} bo'limidagi taomlar:")
            
      
            taomlar = list(res[bolim_tanlangan].items())  
            for idx, (nomi, narx) in enumerate(taomlar, 1):
                print(f"{idx}. {nomi} -->> {narx} UZS")  

            user_taom = input(f"Birini tanlash uchun raqamini kiriting (yoki '0' deb orqaga qaytish):\n")

            if user_taom == '0':  
                break
            if user_taom.isdigit() and 1 <= int(user_taom) <= len(taomlar):
                tanlangan_taom = taomlar[int(user_taom) - 1]  
                nomi, narx = tanlangan_taom

                miqdor = input(f"{nomi} uchun qancha buyurtma qilmoqchisiz? Kiriting: ")

                if miqdor.isdigit() and int(miqdor) > 0:
                    miqdor = int(miqdor)
                    umumiy_narx = narx * miqdor

                   
                    tanlash.append(f"{miqdor}x {nomi}")
                    sum_narx.append(umumiy_narx)

                    print(f"\n{miqdor}x {nomi} tanlandi. Narx: {umumiy_narx} UZS\n")
                else:
                    print("Noto'g'ri miqdor kiritildi. Iltimos, qayta urinib ko'ring.")
            else:
                print("Noto'g'ri tanlov! Boshqatdan urinib ko'ring.")
    else:
        print("Bunday bo'lim mavjud emas!")


if tanlash:
    print("\nSizning buyurtmalaringiz:")
    for item in tanlash:
        print(f"- {item}")
    print(f"Umumiy narx: {sum(sum_narx)} UZS")
else:
    print("Siz hech qanday buyurtma tanlamadingiz.")
