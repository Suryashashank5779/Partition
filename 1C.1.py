#collabrated with bhuvan bhargav CS10052
# -*- coding: utf-8 -*-
"""
@author: 
    Name:k.Surya shashank
    Rollno:24CS10101
"""
def count_sum_of_positive_integers(n):
    L=[0]*(n+1)
    #List L contains partition of n in i parts
    # #i is index of L,ex:-L[2]'s value is no of partitions of n in 2 integer
    def split(i,n):
        if(i>n//2):
            return 0
        else :
            return n//2-i+1
    def Loop(z,n,c,j):
        if(n==0):
            return 
        for i in range(j,j+z):
            y=split(i,n-i)
            L[c]+=y
            Loop(y,n-i,c+1,i)
    #returns list L
    def partition(n):
        z=split(1,n);d=0;L[0]=z
        Loop(z,n,d+1,1)
        e=0
        for i in range(n+1):
            e+=L[i]
        return e
    y=partition(n)
    return y+1

# Test the program

if __name__ == "__main__":
    # print(count_sum_of_positive_integers(5))
    # print(count_sum_of_positive_integers(1))
    # print(count_sum_of_positive_integers(15))

    # Task 1: Number of ways to write V as a sum of positive integers
    assert (
        count_sum_of_positive_integers(5) == 7
    )  # (5, 4+1, 3+2, 3+1+1, 2+2+1, 2+1+1+1, 1+1+1+1+1)
    assert count_sum_of_positive_integers(1) == 1  # (1)
    assert count_sum_of_positive_integers(15) == 176  #

    
print("All test cases passed!")


V = 20

# Task 1: Number of ways to write V as a sum of positive integers
print(
        f"Task 1: Number of ways to write {V} as a sum of positive integers:  {count_sum_of_positive_integers(V)}"
    )
   
    










    
  
    
  