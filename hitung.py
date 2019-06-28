#Warna
r = '\033[31;1m'
g = '\033[32;1m'
u = '\033[35;1m'
b = '\033[34;1m'
y = '\033[33;1m'
a = '\033[36;1m'
#Arya Endank Soekamti
print(a),("Kalkulator")
print(r),("By Arya Soekamti")
print " FB : Arya Endank soekamti"
print " WA : +6283869559930"
print "github : AryaEndankSoekamti"
# Data diri
namakamu =raw_input("Nama kamu : ")
print "Nama yang bagus"
# fungsi penjumlahan
def add(x, y):
   return x + y
# fungsi pengurangan
def subtract(x, y):
   return x - y
# fungsi perkalian
def multiply(x, y):
   return x * y
# fungsi pembagian
def divide(x, y):
   return x / y
# menu operasi
print("Pilih Operasi.")
print("1.Jumlah")
print("2.Kurang")
print("3.Kali")
print("4.Bagi")
# Meminta input dari user
raw_input("Masukkan pilihan(1/2/3/4): ")
num1 = int(input("Masukkan bilangan pertama: "))
num2 = int(input("Masukkan bilangan kedua: "))
if choice == '1':
   print(num1,"+",num2,"=", add(num1,num2))
elif choice == '2':
   print(num1,"-",num2,"=", subtract(num1,num2))
elif choice == '3':
   print(num1,"*",num2,"=", multiply(num1,num2))
elif choice == '4':
   print(num1,"/",num2,"=", divide(num1,num2))
else:
   print("Input salah")
#pesan
print "Tengkiuu"
print "Good Bye"
