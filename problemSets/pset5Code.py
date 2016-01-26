#David Walter
#6.006 pset 5-3

'''
Score: 100%
'''

import heapq

class WhimsicalChecker(object):
    def __init__(self, A):
        """Initialize the WhimsicalChecker
        ARGS
        --------
        A: list(int)
            A set of numbers defining whimsical numbers
        RETURNS
        --------
        nothing
        """
        a = min(A)
        adj = []
        for vertex in range(a): #creates the blank adj
            adj.append([])
        for v_i in range(a): #create the edges for adj
            for a_i in A:
                if a_i != a:
                    i = (v_i+a_i)%a
                    adj[v_i].append((i,a_i))#dir edge from v_i to v_i', and the weight edge
        ###adj list created****
        #run djikstra
        d = {}#shortest path dictionary
        d[0]= 0
        Q=[(0,0)]
        for v in range(1,a):
            d[v] = float('inf')
            heapq.heappush(Q,(float('inf'),v))
        S = {}
        while Q:
            u = heapq.heappop(Q)[1]
            if u in S:
                continue
            S[u]=True
            for v_tup in adj[u]:
                v = v_tup[0]
                if d[v] > d[u] + v_tup[1]:
                    d[v] = d[u] + v_tup[1]
                    heapq.heappush(Q,(d[v],v))
        self.d = d
        self.a = a
        
    def is_whimsical(self, l):
        """Check if l is a whimsical number
        ARGS
        --------
        l: int
            number to check

        RETURNS
        --------
        True if l is a whimsical number, False otherwise
        """
        # modify this function to return true
        # if and only if l can be expressed as
        # a sum of numbers from A
        r_prime = l % self.a
        return r_prime in self.d and l >= self.d[r_prime]
        
'''
Test Cases
'''
# you may find the tests provided below helpful.
#def test():
#    solver = WhimsicalChecker([5, 8, 11])
#    assert solver.is_whimsical(0)
#    assert solver.is_whimsical(16)
#    assert not solver.is_whimsical(17)
#    assert solver.is_whimsical(18)
#    print "Great success!"
#
#def test2():
#    solver = WhimsicalChecker([1])
#    for i in range(10000):
#        assert solver.is_whimsical(i)
#    print "Great success!"
#
#if __name__ == '__main__':
#    test()
#    test2()
