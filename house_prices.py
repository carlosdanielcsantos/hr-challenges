#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 23:48:16 2017

@author: carlos
"""

from itertools import groupby
    
def trendTrackFast(prices, K):
    # input  vector length
    N = len(prices)
    
    # initialize result vector with zeroes
    result = [0]*(N-K+1)
    
    """
    define two offseted lists to vectorize comparison between each two
    consecutive values
    """
    a = prices[0:N-1]
    b = prices[1:N]

    # resulting vectorized comparison lists
    increasing = [ x<y for (x,y) in zip(a, b)]
    decreasing = [ x>y for (x,y) in zip(a, b)]
                 
    # for each window
    for i in range(0, N-K+1):
        
        # filter comparison lists for current window
        inc_window = increasing[i:i+K-1]
        dec_window = decreasing[i:i+K-1]

        # count length of consecutive increasing and decreasing sequences
        num_increasing = [x.count(True) for x in \
                          [list(j) for _i, j in groupby(inc_window)]]
        num_decreasing = [x.count(True) for x in \
                          [list(j) for _i, j in groupby(dec_window)]]
        
        """
        each increasing/decreasing sequence of length n will contribute 
        positively/negatively with the arithmetic series of common
        difference 1 from 1 up to n.
        """
        result[i] = sum([n*(n+1)/2 for n in num_increasing]) \
                    - sum([n*(n+1)/2 for n in num_decreasing])
                  
    return result
    
    
N,K = raw_input().strip().split(' ')
N,K = [int(N),int(K)]
       
arr = map(int,raw_input().strip().split(' '))

# input conditioning
if N>len(arr):
    N=len(arr)
if K > N:
    K=N


result = trendTrackFast(arr[0:N], K)

print ""
for r in result:
    print r

          