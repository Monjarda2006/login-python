alfabeto = {
"0": "a",
"1": "b",
"2": "c",
"3": "d",
"4": "e",
"5": "f",
"6": "g",
"7": "h",
"8": "i",
"9": "j",
"10": "k",
"11": "l",
"12": "m",
"13": "n",
"14": "o",
"15": "p",
"16": "q",
"17": "r",
"18": "s",
"19": "t",
"20": "u",
"21": "v",
"22": "w",
"23": "x",
"24": "y",
"25": "z"
}

ALFABETO = {
"0": "A",
"1": "B",
"2": "C",
"3": "D",
"4": "E",
"5": "F",
"6": "G",
"7": "H",
"8": "I",
"9": "J",
"10": "K",
"11": "L",
"12": "M",
"13": "N",
"14": "O",
"15": "P",
"16": "Q",
"17": "R",
"18": "S",
"19": "T",
"20": "U",
"21": "V",
"22": "W",
"23": "X",
"24": "Y",
"25": "Z"
}

num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

print("-=-"*10)
print("-Bem vindo ao Site do Burger King-")
print("-=-"*10)
login = str(input("Ja tens uma conta ? [S/N] "))
if login in "SsNn":
    if login in "Ss":
        print("Username")
        str(input(""))
        print("palavra-passe")
        str(input(""))

    elif login in "Nn":
        print("Registra-te")
        str(input("Username: "))
        str(input("E-Mail: "))
        print("A Password tem de ter pelo menos 6 caracteres, uma MAIUSCULA, uma minuscula e um número.")
        passwd = str(input("Password: "))
        passwdconfirm = str(input("Confirma a Password: "))
        while passwd != passwdconfirm or passwd not in alfabeto and passwd not in ALFABETO and passwd not in num and passwd and len(passwd) < 6:
            if passwd != passwdconfirm:
                print("As passwords não coincidem, Tenta Novamente")
                passwd = str(input("Password: "))
                passwdconfirm = str(input("Confirma a Password: "))
            if passwd not in alfabeto and passwd not in ALFABETO and passwd not in num and passwd:
                print("A tua Password não é forte o suficiente")
                print("A Password tem que ter pelo menos 6 caracteres, uma MAIUSCULA, uma minuscula e um número")
                passwd = str(input("Password: "))
                passwdconfirm = str(input("Confirma a Password: "))
else:
    login = str(input("Ja tens uma conta ? [S/N]"))
