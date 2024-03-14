# Python-tutorial

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







