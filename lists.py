
# @ Jbj Zeehad

words = ["Hello","world","!"] #like array
print(words[1]) #world

x = ["a", "b", "c"]
y = [1, 2, 3, 4, 5]    #diff data types
print(x[1])
print(y[3])

m=[
    [1,2,3],
    [4,5,6]
]
print(m[1][2])  #matrix


things = ["text",0,[1,2,8],4.56]
print(things[2][2])  #output: 8

str = "Hello world!"
print(str[6])      #strings in list

nums = [5, 8, 2]
nums[1] = 42     #reassigned

print(nums) #[5,42,2]

nums = [1, 2, 3]
print(nums + [4, 5, 6]) #add list like string : [1,2,3,4,5,6]
print(nums * 3) #mul list like string : [1,2,3,1,2,3,1,2,3]

words = ["spam", "egg", "spam", "sausage"]
print("spam" in words)   #in operator
print("egg" in words)    #true or false
print("tomato" in words)

x = "hello world"

if "world" in x:
  print("Yes")

nums = [1, 2, 3]
print(not 4 in nums)
print(4 not in nums)   #not operators
print(not 3 in nums)
print(3 not in nums)

words = ["hello", "world", "spam", "eggs"]
for word in words:      #for loop
  print(word + "!")


nums = [4, 7, 3, 1]
for x in nums:
    print(x*2) #output: 8,14,6,2


str = "dont go"
count = 0
for x in str:
  if(x == 't'):  #iterate over strings
    count += 1   #output : 02
print(count) 


text = "do it brother"
for x in text:
  if x == 'e':  #break in for loop
    break
  print(x)

umber=range(10) #range() function
print(umber)    
umber=list(range(10)) #range(0,10)
print(umber)        #[0,1,2,3,4,5,6,7,8,9]


frnd = list(range(3, 8))
print(frnd)       #output : [3,4,5,6,7]


cls = list(range(5, 20, 2))  #3rd arg interval
print(cls)

xy = list(range(7, 3, -1)) #backward using negative number
print(xy)  #decreasing

for k in range(5):  #for in range()
  print("hello!")


squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[2:6])
print(squares[3:8])   #list slices
print(squares[0:1])
print(squares[:7]) #start from first number
print(squares[3:]) #to the end
print(squares[::2]) #output: [0,4,16,36,64]
print(squares[2:8:3]) #output: [4,25]
print(squares[1::4])    #output : [1,25,81]
print(squares[1:-1])  #output: [1, 4, 9, 16, 25, 36, 49, 64]
print(squares[7:5:-1])  #output : [49,36]
print(squares[::-1])  #reverse

N = int(input())
sum=0
k=list(range(0,N+1))
for x in k:
    sum=x+sum
print(sum)



#part 05