#Assignment-2
#Problem-1: Write a function using only list filter lambda that can tell whether a number is a Fibonacci number or not.
#You can use a pre-calculated list/dict to store fab numbers till 10000

from functools import reduce
fib = lambda n: reduce(lambda x, _: x+[x[-1]+x[-2]], range(n-2), [0, 1])
fb = fib(21)
print("Problem1: Write a function using only list filter lambda that can tell whether a number is a Fibonacci number or not.")
while True:
  try:
    fnd = int(input("please Enter a number to check if it is a fibonacci number:" ))
  except ValueError:
    print("Please provide valid integer input")
    continue
  else:
    break
if fnd in fb:
  print("Given number is fibonacci")
else:
  print("Given number is not fibonacci")

print('*********************************************************************************************************************')
######################## End of Problem.1 #########################################################################
#Problem-2:
#Sub-1:Using list comprehension (and zip/lambda/etc if required) write expressions that
#add 2 iterables a and b such that a is even and b is odd
print("Problem-2:Sub-1: Using list comprehension write expressions that add 2 iterables a and b such that a is even and b is odd")
list_even = [2,4,6,8,10,12,14,16]
print("Even numbered List:")
print(*list_even, sep = ", ")
print("Odd numbered List:")
list_odd = [1,3,5,7,9,11,13,15]
print(*list_odd, sep = ", ")
print("Result after adding even and odd list")
print([x+y for x,y in zip(list_even,list_odd)])
print('*********************************************************************************************************************')
######################## End of Problem.2 ########################################################################
#Sub-2:
#strips every vowel from a string provided (tsai>>t s)

print('*********************************************************************************************************************')
######################## End of Problem.3 ########################################################################

#Sub-3:
#acts like a sigmoid function for a 1D array

print('*********************************************************************************************************************')
######################## End of Problem.4 ########################################################################

#Sub-4:
#takes a small character string and shifts all characters by 5 (handle boundary conditions) tsai>>yxfn
print("Problem-2:Sub-4 takes a small character string and shifts all characters by 5 (handle boundary conditions)")

abc = 'abcdefghijklmnopqrstuvwxyz'
def encrypt(msg, n=5):
  msg = ''.join(map(lambda x:abc[(abc.index(x)+n)%26] if x in abc else x, msg))
  return msg

msg = input("Please enter character string:")
print('Resultent characters after shifting all characters by 5: %s'%(encrypt(msg)))
print('*********************************************************************************************************************')
######################## End of Problem.5 ########################################################################
