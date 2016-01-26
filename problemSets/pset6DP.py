#David Walter
#6.006 Pset 6
#12/02/2015

'''
make_sentence(s, L): given a string of letters s and a list of valid words L,
inserts spaces into s to form a valid sentence and returns the sentence as a
string. If there are multiple valid sentences, then the one with the highest
score will be returned, where score is defined as the sum of the cubes
of the lengths of the words in the sentence.
ARGS:
  s - the string of letters to transform into a sentence
  L - the list of valid words allowed in the sentence
RETURN:
  the sentence string resulting from inserting spaces into s
'''

#Solution uses Dynamic Programming

def make_sentence(s, L):
    D={}
    n_max=len(s)
    t_max=0
    for l in L: #creating the dictionary of L
        t_max=max(t_max,len(l))
        D[l]=True
    memo =[0]*(n_max) #index by n, store list of indices and score    memo[i]=[lefti,score of all prev]
    for n in xrange(n_max+1): #O(n)
        for t in xrange(t_max): #O(t)
            left,right= n, n+t
            if s[left:right+1] in D:# and right<(n_max+1):#it's valid word ... O(t)
                try:
                    if left==0:       #no prev word
                        if memo[right]==0: #memo[right] has not had a word yet
                            memo[right]=(left,len(s[left:right+1])**3)
                        else: #memo[right] already has a word, so compare scores
                            cS=len(s[left:right+1])**3 +memo[left-1][1]#current score
                            if cS > memo[right][1]:
                                memo[right]=(left,cS)
                    elif memo[left-1]!=0:    # there is a previous 
                        if memo[right]==0: #memo[right] has not had a word yet
                            memo[right]=(left,memo[left-1][1]+len(s[left:right+1])**3)                   
                        else: #memo[right] already has a word, so compare scores 
                            cS=len(s[left:right+1])**3 +memo[left-1][1]#current score
                            if cS > memo[right][1]:
                                memo[right]=(left,cS)
                except IndexError:
                    continue
    if memo[-1]!=0:
        right,ans=n_max,[]
        while left!=0: #return answer as a string
            left=memo[right-1][0]
            ans.append(s[left:right])
            right = left
        ans.reverse()
        ans= ' '.join(ans)
        return ans
    return None
    

'''
Test Cases
'''

### Examples
#s = 'abeareatspies'
#L = ['a', 'abe', 'are', 'at', 'bear', 'eats', 'pies', 'spies']
#print make_sentence(s, L)
### #sshould print 'a bear eats piess'
##
#L.remove('a')
#L.remove('at')
#print make_sentence(s, L)
## should return None


#s = 'a' * 40000
#L = []
#for i in range(25):
#    L.append('a' * (i * 2))
#print make_sentence(s, L)
#
#s = 'a' * 40001
#L = []
#for i in range(25):
#    L.append('a' * (i * 2))
#print make_sentence(s, L)
#s = 'a' * 100000
#L = ['a']
#print make_sentence(s, L)
#print 'here'


###WRONG ANSWER (suboptimal sentence returned)
###Test case details:
#s = 'ingeneralsentencesusinglongerwords'
#L = ['longer', 'inglongerwor', 'sentences', 'esusin', 'enc', 'words', 'g', 'enerals', 'in', 'using', 'ds', 'general', 'inge', 'ing', 'n', 'er', 'alsent', 'entencesus']
#print make_sentence(s, L)
###your answer: 'in general sentences using longer words'
###correct answer (or best sentence score): 3106




#s = 'dgfjccjchljibegkjlhbkhbbggibfdjeabedkiheeildedhkkh'
#L = ['dgfjccjchljibegkjlhbkhbbggibfdjeabedkiheeildedhkkh', 'dgfjccjchljibegkjlhbkhbbg', 'gibfdjeabedkiheeildedhkkh']
#print make_sentence(s, L)
###your answer: 'dgfjccjchljibegkjlhbkhbbg gibfdjeabedkiheeildedhkkh'