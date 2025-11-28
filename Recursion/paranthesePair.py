#where given an integer A pair of paranthese write a function to generate all the combinations of well formed of length 2*A 

def formPair(A,s,o,c):
    if(len(s)==A*2):
        print(s)
        return
    if(o<A):
        formPair(A,s+"(",o+1,c)
    if(c<o):
        formPair(A,s+")",o,c+1)
def paranPair(A):
    formPair(A,"",0,0)

paranPair(3)