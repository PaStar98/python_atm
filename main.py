PIN = "2137"
GET_BALANCE = open("_money.txt", "r")


def atm_logic(balance):
    save_balance = open("_money.txt", "w")

    choose_option = int(input("1 -> Wypłata gotówki | 2 -> Wpłata gotówki\n"))
    if choose_option == 1:
        type_value = int(input("Podaj kwotę do wypłaty: "))
        if int(type_value) > int(balance):
            print("BŁĄD! Kwota wypłaty przekracza Twoje aktualne SALDO!")
            return
        else:
            calc = int(balance) - int(type_value)
            save_balance.write(str(calc))

            print("Wypłaciłeś " + str(type_value) + " zł")
            print("Twoje obecne saldo konta to: " + str(calc) + " zł")
    elif choose_option == 2:
        type_value = int(input("Podaj kwotę do wpłaty: "))
        if int(type_value) < 0:
            # FIXME: THERE MUST BE BETTER WAY TO DO IT
            print("Nie można wykonać operacji, usuwamy ci kase biedaku")
            save_balance.write(balance)
            save_balance.close()
            return
        else:
            calc = int(balance) + int(type_value)
            save_balance.write(str(calc))
            print("Wpłaciłeś " + str(type_value) + " zł")
            print("Twoje obecne saldo konta to: " + str(calc) + " zł")

    else:
        print("Podano nieprawidłową wartość, spróbuj ponownie!")
        return

    GET_BALANCE.close()
    save_balance.close()


def enter_pin():
    pin = input("Wprowadź kod PIN: ")
    return pin


def check_user_input(pin, tries=3, balance=GET_BALANCE.readline()):
    if pin == PIN:
        print("Kod PIN prawidłowy")

        if balance == 0 or balance == "":
            print("BŁĄD! Nie posiadasz środków na koncie, nie możesz wypłacić gotówki!")
            return

        print("Saldo: " + balance)
        print("---- ---- ----")
        atm_logic(balance)
    else:
        tries -= 1
        if tries == 0:
            print("Gratulacje, Twoja karta została zablokowana!")
            return False
        print(tries)
        print("Kod PIN nieprawidłowy")
        check_user_input(enter_pin(), tries)


check_user_input(enter_pin())