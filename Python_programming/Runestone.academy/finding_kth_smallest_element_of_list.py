# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 21:50:18 2021

@author: KingaKali


Given a list of numbers in random order, write an algorithm that works in O(nlog(n)) to find the kth smallest number in the list.
"""

'''
using sorting O(nlogn) Python sort uses MergeSort
'''
def findkthsmallest(A,k):
    A.sort()
    return A[k-1]




'''
Approach based on Quick Sort 
Idea behind quicksort is to find the correct place for the selected pivot. Once the pivot is at the correct position, 
all the elements on the left side of the pivot are smaller and on the right side of the pivot are greater than the pivot. This step is partitioning.
O(n^2) worst case, O(n) on average

'''
import sys
sys.setrecursionlimit(15000)
#Quick-select approah O(n)
def kthsmallest(A,l,r,k):
   # If k is smaller than number of 
    # elements in array
    if (k > 0 and k <= r - l + 1):
     
        # Partition the array around last 
        # element and get position of pivot
        # element in sorted array
        pos = partition(A, l, r)
 
        # If position is same as k
        if pos - l == k - 1:
            return A[pos]
        elif pos - l > k - 1: # If position is more, 
                              # recur for left subarray
            return kthsmallest(A, l, pos - 1, k)
 
        
            # Else recur for right subarray
        else:
            return kthsmallest(A, pos + 1, r,
                            k - pos + l - 1)
 
    # If k is more than number of
    # elements in array
    return sys.maxsize
    
    
def partition(A,left,right):
    x=A[right]
    i=left
    for j in range(left,right):
        if A[j]<=x:  
            arr[i], arr[j] = swap(arr[i],arr[j])
            i=i+1
            
    arr[i], arr[right] = swap(arr[i],arr[right])
    return i
    
def swap(a,b):
    temp=a
    a=b
    b=temp
    return (a,b)
    


'''
Using min heap
A Heap is a special Tree-based data structure in which the tree is a complete binary tree. Since a heap is a complete binary tree, a heap with N nodes has log N height. 
In a Min-Heap the key present at the root node must be less than or equal among the keys present at all of its children.
'''

import heapq


def find_Kth_smallest(A,k):
    '''
    type A: list[int]
    type k: int
    return value type: int
    '''
   # heapify - transform list into heap, in place, in linear time 
    heapq.heapify(A);
        
    i=0
    while(i<k):
        # heappop - pop and return the smallest element from heap 
        a=heapq.heappop(A)
        i+=1
    
    return a

if __name__ == "__main__":
    arr = [3,5,6,3,1,8,2]
    n = len(arr)
    k =5
    print("K'th smallest element using quick select is", 
           kthsmallest(arr, 0, n - 1, k))
    
    print("K'th smallest element using sorting is",findkthsmallest(arr,k))
    
    print("K'th smallest element using min heap is", 
           find_Kth_smallest(arr,  k))