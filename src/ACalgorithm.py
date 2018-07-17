'''
Created on 16 Jul. 2018

@author: sheng
'''
from TreeNode import TreeNode
from Cython.Debugger.Tests.TestLibCython import root

def getchar(node):
    return node.ch

class ACBuild(object):
    '''
    classdocs
    '''


    def __init__(self, text, pattens):
        self.text=text.lower()
        self.pattens=pattens
        self.buildGotoTree()
        self.root=None
        self.result={}
        for i in pattens:
            self.result[i]=[]
        # self.addFailure()
        # self.acSearch()
        
    def buildGotoTree(self):
        i=0
        self.root=TreeNode(None, '')
        for word in self.pattens:
            tmp=self.root
            for ch in word:
                ch=ch.lower()
                if ch in tmp.sonsHash:
                    innerTem=tmp.sonsHash[ch]
                else:
                    newNode= TreeNode(tmp, ch)
                    i+=1
                    newNode.status=i
                    tmp.addSonNode(newNode)
                    innerTem=newNode
                tmp=innerTem
            tmp.addResult(word)
        
    def addFailure(self):
        mid = []
#         self.root.failure=self.root
        for node in self.root.sons:
#             print(node.setFailure(self.root).status)
            mid.extend(node.sons)
        
        while(len(mid)>0):
            temp=[]
            for node in mid:
                r=node.parent.failure
                while r!=None and node.ch not in r.sonsHash:
                    r=r.failure
            
                if r==None:
                    node.setFailure(self.root)
                else:
                    node.setFailure(r.getSonNode(node.ch))
                    for result in node.failure.results:
                        node.addResult(result)
                temp.extend(node.sons)
            mid=temp
            
#         self.root.failure=self.root
            
    def acSearch(self):
        index=0
        mid=self.root

        while index< len(self.text):
            temp=None
            while temp==None and mid != None:
#                 print(index)
#                 print("mid:{},{}".format(mid.ch, mid))
                temp = mid.getSonNode(self.text[index])
                if mid==self.root:
                    break
                if temp==None:
                    mid=mid.failure
            if temp!=None:
                mid=temp
            if mid:
                for r in mid.results:    
                    self.result[r].append(index-len(r)+2)
            index+=1
        
    def printResult(self):
        for key, value in self.result.items():
            output=r'<No Output>'
            f=lambda v: str(v)[1:-1] if(len(v)>0) else output   
            print('{} "{}"'.format(key, f(value)))


    def printTree(self):
        nodelist=[]
        nodes=[self.root]
        while len(nodes)>0:
            temp=[]
            for node in nodes:
                temp.extend(node.sons)
                nodelist.append(node)
            nodes=temp
            
        sorted(nodelist, key=getchar)
        for node in nodelist:
            if node.failure:
                f=node.failure.status
            else:
                f=0
            print("{} {} {} {} {}".format(node.ch, node.depth, node.status, f, node.results))
             