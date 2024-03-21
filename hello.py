print("Hello World")

if 5 > 2:
  print("Five is greater than two!")

# indentation error

#if 5 > 2: 
#print("Five is greater than two!")

# 콜론 중요!

if 5 > 2:
 print("Five is greater than two!") 
if 5 > 2:
        print("Five is greater than two!") 


x = 5
y = "Hello, World!"


#print("Hello, World!") 주석
print("Cheers, Mate!")


x = 5
y = "John"
print(x)
print(y)


x = 4       # x is of type int
x = "Sally" # x is now of type str 뒤에 쓴걸 출력
print(x)


# 타입이 다 다름
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0


# 따옴표 상관 없음
x = "John"
# is the same as
x = 'John'


# 대소문자 구별함
a = 4
A = "Sally"
#A will not overwrite a



# 숫자 앞, '-', 띄어쓰기 앞에 쓰고 변수 선언 시 오류
#2myvar = "John"
#my-var = "John"
#my var = "John"



# 동일한 변수 선언 가능
x = y = z = "Orange"
print(x)
print(y)
print(z)



# list 문
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)



# 연산자
x = 5
y = 10
print(x + y)



# 연산 오류 (변수 타입)
#x = 5
#y = "John"
#print(x + y)



# 다른 타입 출력 (한 줄에 출력)
x = 5
y = "John"
print(x, y)



# global로 선언한 함수는 변수를 어디에 넣든 동일한 값으로 출력
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)


x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)


x = "Hello World"	# str	
x = 20	# int	
x = 20.5	# float	
x = 1j	# complex	
x = ["apple", "banana", "cherry"]	# list	
x = ("apple", "banana", "cherry")	# tuple	
x = range(6)	# range	
x = {"name" : "John", "age" : 36}     # dict
x = True	# bool



# 랜덤 함수
import random

print(random.randrange(1, 10))



# 타입 선언
x = int(2.8)  # x will be 2
y = float("3")   # y will be 3.0
z = str(3.0)  # z will be '3.0'



# str 여러 문장 출력
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)



# 자릿수에 맞는 글자 출력
a = "Hello, World!"
print(a[1])


# 글자 수 출력
a = "Hello, World!"
print(len(a))



# if, not, if not 응용
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

txt1 = "The best things in life are free!"
print("expensive" not in txt1)

txt2 = "The best things in life are free!"
if "expensive" not in txt2:
  print("No, 'expensive' is NOT present.")


# def: 함수 정의할 때

# 여러개의 값을 지정할 수 있다.
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")


# 함수를 여러개 정의해서 순서대로 대입
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")
# 단, 다음과 같이 작성 시 지정된 값이 하나여서 오류가 발생함.
# def my_function(fname, lname):
#   print(fname + " " + lname)
# my_function("Emil", "Refsnes")


# 함수 안에 여러개의 값을 한 번에 지정하고 그중 몇 번째 값을 출력할지 지정
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

# 함수 안에 여러개의 값을 한 번에 지정 후 함수 안의 어떤 값을 출력할지 지정
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

# 지정된 값이 없는 경우 빈 곳에 고정 값을 넣어서 출 
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

# 리스트를 추가하는 방법
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)

# 리턴 함수를 통해 수식을 계산하는 방법
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))


# lambda: 지정된 값에 대한 수식을 정리하여 간단히 표현 가능

# lambda 함수로 제곱 표현하기
x = lambda a : a * a      # a: a ** 2
print(x(10))


# 













