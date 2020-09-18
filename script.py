from mainMenu import MenuPesanan

food1 = MenuPesanan("Kupat", 10000)
food2 = MenuPesanan("Bakso", 15000)

# List foods
foods = [food1, food2]

index = 1
for food in foods:
    print(str(index) + " . " + food.information())
    index += 1

pesanan = int(input("Mau pesan Apa? :"))

print("Anda pesan " + foods[pesanan-1].name)
porsi = int(input("Berapa porsi? :"))
print("Siap, anda pesan " + foods[pesanan-1].name + " dengan " + str(porsi) + " porsi")
print("Total pesanan anda :" + str(foods[pesanan-1].biaya(porsi)))