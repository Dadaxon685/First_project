class Bank:
    '''bu buyruqda pul olish va pul qoyishlar bor'''
    def __init__(self, balance):
        self.balance = balance

    def pul_olish(self, summa):
        """bu buyruq pul olish uchun ishlatildi. """
        foiz = 2
        sum_olish = summa + (summa * foiz)
        if sum_olish > self.balance:
            print("Siz kiritgan summadan katta bu summa")
        else:
            self.balance -= sum_olish
            print(f"Balansingizda {self.balance} so'm bor. \nYechildi 5% ushlanma bilan {sum_olish} so'm. Qolgan balans {self.balance}")
        return self.balance

    def pul_qoyish(self, summa):
        """bu buyru qpul qo'yish uchun ishlatiladi. """
        foiz = 3
        sum_qoyish = summa + (summa * foiz)
        self.balance += sum_qoyish
        print(f"Balansingizda {self.balance} so'm bor edi. \n10% foyda bilan balansingizga qo'shildi {sum_qoyish} so'm.")
        return self.balance

class shaxs:
    def __init__(self, name, bank_account):
        self.name = name
        self.bank_account = bank_account

    def info2(self):
        print(f"Assalomu aleykum {self.name}. Bankga xush kelibsiz!")
        print(f"Hisobingizda {self.bank_account.balance} so'm bor.")
        
       
        print("1: Pul olish")
        print("2: Pul qo'yish")
        amal = input("Amallardan birini tanlang (1 yoki 2): ")

        if amal == "1":
            summa = float(input("Qancha pul olmoqchisiz? "))
            self.bank_account.pul_olish(summa)
        elif amal == "2":
            summa = float(input("Qancha pul qo'ymoqchisiz? "))
            self.bank_account.pul_qoyish(summa)
        else:
            print("Noto'g'ri tanlov amal tanladingiz!!")

        print(f"Amaldan so'ng balansingizda {self.bank_account.balance} so'm bor.")


def balan():
    balanc_kirit = 100.000
    bank_account = Bank(balanc_kirit)
    
    ism = input("Ismingizni kiriting: ")
    mijoz = shaxs(ism, bank_account)
    
    mijoz.info2()


if __name__ == "__main__":
    balan()

