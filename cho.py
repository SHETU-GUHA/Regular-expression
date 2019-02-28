class ahoCorasick:
    root=None
    newstate=None

def_init_(self):
    self.root=State(0,'')
    self.newstate=0

def addKeyword(self,keywords):
    '''Adds the keyword in the tree'''

    for key in keywords.split(''):

    j=0
    state=0
    current=self.root
    key=key.upper()

    while j<len(key):
    ch= ke[j]
    j= j+1
    child= current.getTransition(ch)
    if child!=None:
        current= child
    else:
     self.newstate=self.newstate+1
     nd=State(self.newstate,ch)
     current.tranList.append(nd)
     current= nd
     while j<len(key):
        self.newstate=self.newstate+1
        nd2 = State(self.newstate,key[j])
        current.tranLis.append(nd2)
        current= nd2
        j= j+1
       break
    current.outputSet.add(key) 
