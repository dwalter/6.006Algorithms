#David Walter
#6.006 pset 4: Coding problem
'''
Score: 30/30
'''

#Implement a puzzle data structure for the 8-puzzle.
#
#Your Puzzle class must define initial_state, goal_state, and next_states(s) as
#specified in the problem statement.
#
#__init__(self, starting_state): initializes the Puzzle with the given argument
#as the initial state; must initialize initial_state and goal_state
#ARGS:
#  starting_state - the starting state of the puzzle
#
#next_state(self, s): given a state s, returns a list of all the states
#reachable from s with one slide
#ARGS:
#  s - the input state s
#RETURN:
#  a list of states that are reachable from s with one slide; must return
#  in a consistent order

from collections import deque

class Puzzle:
    def __init__(self, starting_state):
        self.initial_state = starting_state
        self.goal_state = (1,2,3,4,5,6,7,8,0)

    def next_states(self, s):
        reachable_states = {0:[1,3],2:[1,5],4:[1,3,5,7],6:[3,7],8:[5,7],1:[0,2,4],3:[0,4,6],5:[2,4,8],7:[4,6,8]}
        for space in range(len(s)):
            if s[space] == 0:
                blank = space#the index of 0 in the puzzle
                #dont assume we cant find blank
        reachable = []
        for move in reachable_states[blank]:#going thru all the moves
            next_move = list(s)
            next_move[blank] = s[move]
            next_move[move] = 0
            reachable.append(tuple(next_move))
        return reachable

#
#solve_puzzle(P): given an 8-puzzle data structure, returns the shortest sequence
#of states that can be used to solve the puzzle
#ARGS:
#  P - the 8-puzzle, with initial_state, goal_state, and next_states(s) defined
#RETURN:
#  the sequence of states used to solve the puzzle in the fewest moves (as a
#  list); if there are no possible solutions, return the empty list, and if the
#  starting state equals the ending state, return a list containing only the
#  ending state

##########################
#bfs code from class notes
##########################
class BFSResult:
    def __init__(self):
        self.level = {}
        self.parent = {}

class Graph:
    def __init__(self):
        self.adj = {}

    def add_edge(self, u, v):
        if u not in self.adj:
            self.adj[u] = []
            self.adj[u].append(v)
###################################
#altered bfs code skeleton from class notes
###################################
def solve_puzzle(P):
    r = BFSResult()
    r.parent = {P.initial_state: None}
    r.level = {P.initial_state: 0}
    queue = deque()
    queue.append(P.initial_state)
    while queue: #queue is not empty
        u = queue.popleft()#bfs
        for n in P.next_states(u): #searching thru next states
            if n not in r.level:
                r.parent[n] = u
                r.level[n] = r.level[u] + 1
                queue.append(n)
    ans = [] #now formulate the answer or return empty list
    if P.goal_state in r.level:
        ans.append(P.goal_state)
        current = P.goal_state
        for parent in range(r.level[P.goal_state]):
            current = r.parent[current]
            ans.append(current)
    else:
        return []
    return list(reversed(ans)) #return ans from start to goal state

'''
Test cases
'''


# Some examples (be sure to comment them out before submitting)

## Part (a)
#s = (1, 2, 3, 4, 0, 6, 7, 5, 8)
#s = (0,8,3,6,4,7,1,2,5)
#s = (0,8,7,6,5,4,3,2,2)
#P = Puzzle(s)
##print P.initial_state
## (1, 2, 3, 4, 0, 6, 7, 5, 8)
##print P.goal_state
##print '_______________'
## (1, 2, 3, 4, 5, 6, 7, 8, 0)
##next1 = P.next_states(s)
##for state in next1:
##    print state
## (1, 0, 3, 4, 2, 6, 7, 5, 8)
## (1, 2, 3, 0, 4, 6, 7, 5, 8)
## (1, 2, 3, 4, 6, 0, 7, 5, 8)
## (1, 2, 3, 4, 5, 6, 7, 0, 8)
#
### Part (b)
#solution = solve_puzzle(P)
##print solution.level[P.goal_state]
#print type(solution)
#print '__________________'
##print solution.parent[(1, 2, 3, 4, 5, 6, 7, 0, 8)]
#for state in solution:
#    print state
# (1, 2, 3, 4, 0, 6, 7, 5, 8)
# (1, 2, 3, 4, 5, 6, 7, 0, 8)
# (1, 2, 3, 4, 5, 6, 7, 8, 0)
