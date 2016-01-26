#David Walter
#6.006 pset 1
'''
Score: 23/25
'''
'''
find_amulet: returns the chest index of the Amulet of Rivest
ARGS: magic_map(a,b): magic_map(a,b) returns true if the Amulet
is the chest index i where a <= i < b.
RETURN: index of chest containing amulet

HINT: magic_map(a,a+1) returns true iff the Amulet is in chest a
magic_map(1,float('inf')) will always return true
'''


'''    magic_map function is already implemented for grader. 
       The magic_map below is for testing
'''   

#def magic_map(a,b):
#    answer = 99999999999999999
#    if a <= answer and b > answer:
#        return True
#    else:
#        return False

def find_amulet(magic_map):
    a = 1
    b = 2
    targeted = False  #tells if the initial range is found
    while not magic_map(a,a+1):
        #find the range of where the amulet is at the start
        if not targeted and not magic_map(a,b): # the amulet is not 
                                                #between a and b
            a = b
            b += 2*b
        else: # the index is between a and b
            targeted = True
            if magic_map(a,b-((b-a)/2)): #the index is in 
                                         #the lower half
                b -= ((b-a)/2)
                continue
            else: #index is in the upper half
                a += ((b-a)/2)
                continue
    return a
    
print find_amulet(magic_map)     