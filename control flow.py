# @ Jbj Zeehad

x=True
print(x) #boolean : True or False

print(2 == 3) #value compare

print("hello" == "hello") #string compare

x=7;

print(x != 8) #true
print(x > 5)  #true
print (x < 2) #false
print( x >=7) #true
print(x <= 7) #true

print('a' > 'b') #false

y=(7 > 5)
print(int(y)) #int 0(false) or 1(true)

z=45;
if z>5 :
    print("z is greater than 5") #true

age=70
if age>5 :
    print("Five") #output : Five
if age>8 :
    print("Eight") #Eight output
if age <=47 :
    print("ok Done") #False

i=4
if i==5 :
    print("Yes")
else :
    print("No") #no


num = 3
if num == 1:
  print("One")
else: 
  if num == 2:
    print("Two")
  else: 
    if num == 3: 
      print("Three")
    else: 
      print("Something else") #three : indentation vsry importatnt

nm = 3
if nm == 1:
  print("One")
elif nm == 2:
  print("Two")
elif nm == 3: 
  print("Three")
else: 
  print("Something else") #if else : elif


print(1 == 1 and 2== 2)  #and operator : True
print(1 !=1 and 2 == 2) #false

print( 1 >= 2 or 2 <= 2) #or operator :True
print (1 != 3 or 2 > 5) #true

print(not 1 == 1) #not operator
print(not 1 > 7) #True

age = 24
limit = 18
height = 191  #compare variable
if (age > limit and height > 180) :   
   print("YES")

i=1
while i<=5:
  print(i)    #while loop
  i=i+1
print("Finished !")  

k = 0
while True:
  print(k)
  k += 1      #break
  if k >= 5:
    print("Break")
    break

print("Finished")


m = 0
while m<5:
  m += 1      #continue
  if m==3:
    print("Skipping 3")
    continue
  print(i)


#part 04