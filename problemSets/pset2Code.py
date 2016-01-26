#David Walter
#6.006
#pset 2 Intersection

from bst import insert, search, delete
'''
get_smallest_at_least: finds a node in the given subtree with the smallest key
that is greater than or equal to the given lower bound, or decides that there is
no such node
ARGS:
  node  - the root of the subtree
  bound - the lower bound for the key
RETURN:
  if there are nodes with key at least bound, return such a node with smallest
  key; otherwise return None
'''

## TODO
'''
##fix get_smallest_at_least implementation
'''

def get_smallest_at_least(node, bound):
    try:
        if node.key==bound: #node.key is bound
            return node
        if not node.left is None: #try left
            if not get_smallest_at_least(node.left,bound) is None:
                return get_smallest_at_least(node.left,bound)
        #the left doesnt exist or node is too small
        if node.key > bound:
            return node
        if not node.right is None: #try right
            if not get_smallest_at_least(node.right,bound) is None:
                return get_smallest_at_least(node.right,bound)
        #the right doesn't exist or right is too small
        else:
            return None #everything is smaller than bound
    except AttributeError:
        return None

'''
find_intersection: finds an intersection of the given line segments, or decides
that there is no intersection
ARGS:
  segments - list of tuples of the form ((x1, y1), (x2, y2)), where (x1, y1) and
  (x2, y2) are the endpoints of the line segment; detailed specifications can be
  found in the problem statement
RETURN:
  if there are intersections between the given line segments, return one such
  intersection as a tuple (x, y); otherwise return None
'''
def find_intersection(segments):
    #seperate start pts and end pts
    segPts = []
    for pt in segments:
        segPts.append([pt[0],pt, 0]) #start pt
        segPts.append([pt[1],pt, 1]) #end pt
    #sort the segments by x value
    segPts.sort() #O(n log n)
    segTree = None
    for seg in segPts: #sweeping from left to right
        if seg[2] == 0: #it's a start pt
            if seg[1][0][1] == seg[1][1][1]: #horiz line
                segTree = insert(segTree, seg[1][0][1]) #insert the y value
                continue
            if seg[1][0][0] == seg[1][1][0]: #vertical line
                #check segTree for at least y start value of vert line
                bound = seg[1][0][1] #vert line y start val
                check = get_smallest_at_least(segTree, bound)
                if not check is None:
                    if check.key < seg[1][1][1]:
                        #the horiz y val is less than the vert line end pt y val
                        xReturn = seg[1][0][0]
                        yReturn = check.key
                        return(xReturn, yReturn)
        if seg[2] == 1: #it's an end pt
            if seg[1][0][1] == seg[1][1][1]: #horiz line
                segTree = delete(segTree, seg[1][0][1])
            else:
                continue
    #no intersections
    return None