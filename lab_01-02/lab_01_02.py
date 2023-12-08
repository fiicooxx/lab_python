## 2
age = int(input("Podaj wiek: "))
money = float(input("Ile masz pieniędzy? "))
missing_age = 18 - age
missing_money = 20 - money
if age < 18:
    print(f"Brakuje Ci {missing_age} lat by kupić alko")
    if money < 20:
        print(f"Brakuje Ci {missing_money} zł do zakupu")
else:
     if money < 20:
        print(f"Brakuje Ci {missing_money} zł do zakupu")
     else:
        print("Jest ok, kupuj")
