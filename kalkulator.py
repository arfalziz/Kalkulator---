def kalkulator():
    while True :
        print("pilih operasi:")
        print ("1. tambah")
        print ("2. kurang")
        print ("3. kali")
        print ("4. bagi")
        print ("5. keluar")

       

        operasi = input ("masukan nomor pilihan (1,2,3,4):")
        bilangan1 = int(input("masukan bilangan 1:"))
        bilangan2 = int(input("masukan bilangan 2:"))
        

        if operasi == '1':
                hasil = bilangan1 + bilangan2
                print(f"{hasil}: {bilangan1} + {bilangan2} == {hasil}")
        elif operasi =='2':
                hasil = bilangan1 - bilangan2
                print(f"{hasil}: {bilangan1} - {bilangan2}== {hasil}")
        elif operasi == '3':
                hasil = bilangan1 * bilangan2
                print(f"{hasil}: {bilangan1} * {bilangan2} == {hasil}")
        elif operasi == '4':
                hasil = bilangan1 / bilangan2
                print(f"{hasil}: {bilangan1} / {bilangan2} == {hasil}")

        else :
                print("pilihan tidak valid")
kalkulator()

