print("calculator python")
print("===================")

print("1. Penjumlahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")
print("===================")

 #logic
def Penjumlahan(x,y):
        return x+y

def Penjumlahan(x,y):
        return x-y
def Penjumlahan(x,y):
        return x*y
def Penjumlahan(x,y):
        return x/y
tipe = input("input your number: ")

if tipe in ('1', '2', '3', '4'):
    angka1 = float(input("number 1 : "))
    angka2 = float(input("number 2 : "))
    print("===================")
    if tipe == '1':
          print("the answer is: ", Penjumlahan(angka1, angka2))
    if tipe == '2':
          print("the answer is: ", Penjumlahan(angka1, angka2))
    if tipe == '3':
          print("the answer is: ", Penjumlahan(angka1, angka2))
    if tipe == '4':
          print("the answer is: ", Penjumlahan(angka1, angka2))
    print("===================")
    
