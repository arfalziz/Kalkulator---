def kalkulator():
    print("pilih operasi:")
    print ("tambah")
    print ("kurang")

operasi = input ("masukan nomor pilihan (1,2):")
bilangan1 = int(input("masukan bilangan 1:"))
bilangan2 = int(input("masukan bilangan 2:"))

#output

if operasi == '1':
    hasil = bilangan1 + bilangan2
    print(f"{hasil}: {bilangan1} + {bilangan2} == {hasil}")
elif operasi =='2':
    hasil = bilangan1 - bilangan2
    print(f"{hasil}: {bilangan1} - {bilangan2}== {hasil}")
else :
    print("pilihan tidak valid")

    
