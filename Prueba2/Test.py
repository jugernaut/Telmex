'''
Created on 31 oct. 2022

@author: academicos
'''

def factorial(n):
    res = 1
      
    for i in range(2, n+1):
        res *= i
    return res
    # Driver Code

#if __name__ == '__main__':
print(factorial(5))