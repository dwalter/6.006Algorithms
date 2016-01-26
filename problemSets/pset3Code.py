#David Walter
#6.006 pset 3
#fall 2015
'''
Score: 100%
'''

import collections as col

'''
find_occurrences(T, W): given a text string T and a target word W of length l,
returns an ascending list of indices i such that T[i : i + l] is a permutation
of W
ARGS:
  T - the string to search
  W - the string whose permutations you want to search for
RETURN:
  a list of indices in T such that T[i : i + l] is a permutation of W; if there
  are no such indices, the empty list should be returned
'''
def find_occurrences(T, W):
    test = {}
    ans = []
    for n in range(len(T)):
        try:#-1 from end elem in T
            test[T[n]] -= 1
        except KeyError:
            test[T[n]] = -1
        if test[T[n]] == 0:
            del test[T[n]]
        #n is too low
        if n < len(W):#+1 for elem in W
            try:
                test[W[n]] += 1
            except KeyError:
                test[W[n]] = 1
            if test[W[n]] == 0:
                del test[W[n]]
        #n is large enough
        #see if test is empty
        if n >= len(W):#+1 from start elem in T
            try:
                test[T[n-len(W)]] += 1
            except KeyError:
                test[T[n-len(W)]] = 1
            if test[T[n-len(W)]] == 0:
                del test[T[n-len(W)]]
            if test == {}:
                ans.append(n-len(W)+1)
        if (n+1) == len(W):
            if test == {}:
                ans.append(n-len(W)+1)
    return ans

'''
Test Cases
'''
#print find_occurrences("abca","a") #returns [0,3]
#print find_occurrences("pamama","apm") #returns [0]
#print find_occurrences("alicphack","alice") #returns []
#print find_occurrences("catacta","cat") #returns [0,2,3,4]
