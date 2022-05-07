# @ Jbj Zeehad

#functions

print("Hello") #print : function name, "Hello" : arguments
range(1,10,6) #multiple arguments

nums = [1, 3, 5, 2, 4]
print(len(nums))        #len() function. Output : 05

letters = ["a", "b", "c"]
letters += ["d"]
print(len(letters))   #output : 4

str = "some text"
x = len(str)   #output : 9
print(x)

nums = [1, 2, 3]
nums.append(4)   #append() function
print(nums)     

words = ["Python", "fun"]
words.insert(1, "is")     #insert() function
print(words)

letters = ['p', 'q', 'r', 's', 'p', 'u']
print(letters.index('r'))
print(letters.index('p'))   #index() function
print(letters.index('q')) 

x = [1, 8, 42, 3]

print(min(x))  #min() function : returns min value
print(max(x))  #max() function : returns max value

k = [2, 4, 6, 2, 7, 2, 9]
print(k.count(2))          #count() 
k.remove(4)                #remove()
print(k)
k.reverse()                #reverse()
print(k)

nums = [4, 5, 6]
msg = "Numbers: {0} {1} {2}". format(nums[0], nums[1], nums[2])
print(msg)    #format() function

a = "{x}, {y}".format(x=5, y=12)
print(a)

xo = "! ".join(["spam", "eggs", "ham"])  #join() function
print(xo) #output : spam!eggs!ham

str = "some text goes here"  #split() function : opposite of join()
x = str.split(' ')
print(x)   #output: ['some', 'text', 'goes', 'here']


x = "Hello ME"
print(x.replace("ME", "world")) #replace() function

def hello():
   print("Hello world!") #create a function using def
 
hello()

#Output : Hello World

print("This is a sentence.".upper()) #upper()

print("AN ALL CAPS SENTENCE".lower())  #lower()


def me(word):
   print(word + "!")   #with arguments
me("hello")

def you(x,y) :
    print(x+y)  #more arguments
you(5,6)    

def sum(x, y):
   return x+y 
print(sum(5,6))  #return statements


def double(e, f):
   return [e*2, f*2]  #using list for mul return

p = double(6, 9)
print(p)

"""

Thank You So Much.
See You Soon.
Happy Coding !!

"""


#part 06
