#Hinh thứ nhất - Hinh chu nhat

print('\"Hình  1 - Hinh chu nhat\"')
n = int(input('Nhập gia tri n sao cho n > 0: '))
#chay bang vong lap for

print("Hinh chu nhat theo for")
for i in range(0,n):
    print("*" * n)
#chay bang while
print("Hinh chu nhat theo while")
i = 0
while (i<n):
    print("*" * n)
    i += 1
else:
   while (i < n):
       print('*****')
       i += 1


#Hình thứ 2 - tam giac vuong
print('\n\"Hình 2- tam giac vuong\"')
n = int(input(" Nhập gia tri n sao cho n > 0: "))
while (n <= 0):
   n = int(input('Hãy nhập n > 0: '))
else:
   for i in range(1, n + 1):
       for j in range(1, i + 1):
           print("*", end="")
       print()

#Hình thứ 3 - tam giac vuong nguoc
print('\n\"Hình 3 - tam giac vuong nguoc\"')
n = int(input('Nhập n: '))
while (n < 0):
   n = int(input('Nhập gia tri n sao cho n > 0:  '))
else:
   for i in range(1, n+1):
       for j in range(1, n+1-i):
           print("", end =" ");
       for k in range(i):
           print("*", end="");
       print()

#Hình thứ 4 - tam giac deu
print('\n\"Hình 4 - tam giac deu\"')
n = int(input('Nhập n: '))

while (n < 0):
   n = int(input('Nhập gia tri n sao cho n > 0:  '))
else:
   for i in range(1, n+1):
       if (i%2 != 0):
           for j in range(1, n+1-i):
               print("", end =" ")
           for k in range(i):
               print("*", end=" ")
           print()

#Bai2: Viết chương trình tìm số dương lớn  nhất và số âm bé nhất,
#nếu dãy không có số dương hay số âm thì xuất ra dấu *.
print("\n\"Bài 2\"")
n = int(input('Nhập n > 0: '))
lst = []
while (n < 0):
   n = int(input('Hãy nhập n > 0: '))
for i in range(0, n):
   print("a[", i, "]: ", end="")
   lst.append(int(input()))
print("Danh sách số nguyên bạn đã nhập: ", lst)

maxd = 0
minam = 0
for x in lst:
   if(x > 0 and x > maxd):
       maxd = x
   elif(x < 0 and x < minam):
       minam = x

if (maxd == 0):
   print("Số dương lớn nhất: *")
else:
   print("Số dương lớn nhất: ", maxd)
if(minam == 0):
   print("Số âm bé nhất: *")
else:
   print("Số âm bé nhất: ", minam)

#Bài 3: Viết chương trình thực hiện việc xử lý từ điển Anh – Việt
print("\nBài 3")
dictA_V = {
   "hello" : "xin chào",
   "tearch" : "giáo viên",
   "student" : "sinh viên",
   "we" : "chúng tôi",
   "research" : "nghiên cứu",
   "science" : "khoa học"
}

def menu():
    print("\n-------Chương trình xử lý từ điển Anh-Việt-------")
    print("1. Thêm một từ mới vào từ điển")
    print("2. Hiển thị từ điển, cho biết từ điển hiện tại có bao nhiêu từ")
    print("3. Tìm kiếm từ tiếng Anh")
    print("4. Xóa một từ trong từ điển dựa trên key cung cấp")
    print("5. Nhập 0 để kết thúc chương trình")

def them_tu():
   word = input("Nhập từ bạn cần thêm vào: ")
   mean = input("Nghĩa tiếng Việt của từ là: ")
   dictA_V[word] = mean
   print("Từ mới được thêm thành công vào từ điển")

def hien_tu():
   print("--Danh sách từ điển--")
   for word in dictA_V:
       print(word,': ',dictA_V.get(word))
   print("-> Số lượng từ trong từ điển là: ",len(dictA_V))

def tim_tu():
   word = input("Nhập vào từ bạn muốn tìm: ")
   if word in dictA_V:
       print("Có từ này trong từ điển ->", word, ": ", dictA_V.get(word))
   else:
       print("Không tìm thấy từ", word, "trong từ điển!")

def xoa_tu():
   word = input("Nhập vào từ bạn muốn xóa: ")
   if word in dictA_V:
       del dictA_V[word]
       print("Từ", word, "đã bị xóa!")
   else:
       print ("Không tìm thấy từ", word, "trong từ điển!")


menu()
choice = int(input("\n->> Nhập vào chức năng bạn cần: "))
while choice != 0:
   if choice == 0:
       break
   elif choice == 1:
       them_tu()
   elif choice == 2:
       hien_tu()
   elif choice == 3:
       tim_tu()
   elif choice == 4:
       xoa_tu()
   else:
       print("Chương trình hông có chức năng này!")
   choice = int(input("\n->> Nhập vào chức bạn cần: "))

