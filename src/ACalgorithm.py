'''
Created on 16 Jul. 2018

@author: sheng
@algorithm: Aho-Corasick
https://en.wikipedia.org/wiki/Aho%E2%80%93Corasick_algorithm
'''
from TreeNode import TreeNode


def getchar(node):
    return node.ch

class ACBuild(object):
    '''
    Main class implement Aho–Corasick algorithm
    '''
    def __init__(self, pattens):
        self.pattens = pattens
        self.root = None

    # build goto table and output table
    # This function build finite-state machine
    def buildGotoTree(self):
        i = 0
        self.root=TreeNode(None, '')
        for word in self.pattens:
            tmp=self.root
            for ch in word:
                ch = ch.lower()
                if ch in tmp.sonsHash:
                    # if already have this status in hash table will
                    innerTem = tmp.sonsHash[ch]
                else:
                    # not in hastable will added the char into son Hash Table
                    newNode = TreeNode(tmp, ch)
                    i += 1
                    newNode.status = i
                    tmp.addSonNode(newNode)
                    innerTem = newNode
                tmp = innerTem
            # at the word end it will add the word to the finished word list
            tmp.addResult(word)
        
    # build the failure jumps of finite state machines
    def addFailure(self):
        mid = []
        # level travel of TreeNode (level 1 and level 2)
        for node in self.root.sonsHash.values():
            node.setFailure(self.root)
            mid.extend(node.sonsHash.values())
        
        while len(mid) > 0 :
            temp = []
            # leveled travel of the node tree
            for node in mid:
                r = node.parent.failure
                # if the char go to parent still do not find this branch, it will go parent's parents
                while r != None and node.ch not in r.sonsHash:
                    r = r.failure
            
                if r == None:
                    node.setFailure(self.root)
                else:
                    # if the failure string can match some treenode it will jump that branch
                    node.setFailure(r.getSonNode(node.ch))
                    for result in node.failure.results:
                        node.addResult(result)
                temp.extend(node.sonsHash.values())
            mid=temp
            
    # Search the whole string
    # really function of tree search
    def acSearch(self, text):
        text = text.lower()
        self.result = {}
        for i in self.pattens:
            self.result[i] = []
        index = 0
        mid = self.root
        while index < len(text):
            temp = None
            while temp == None and mid != None:
                temp = mid.getSonNode(text[index])
                #just make sure if they goto root it will jump out
                if mid == self.root:
                    break
                # can not find next status of the tree will jump to the failure 
                if temp == None:
                    mid = mid.failure
            if temp != None:
                mid = temp
            if mid:
                for r in mid.results:    
                    self.result[r].append(index-len(r)+2)
            index += 1
        
    def printResult(self):
        output = r'<No Output>'
        for key, value in self.result.items():
            f = lambda v: str(v)[1:-1] if(len(v)>0) else output   
            print('{} "{}"'.format(key, f(value)))

    # print tree structure
    def printTree(self):
        nodelist = []
        nodes = [self.root]
        while len(nodes)>0:
            temp = []
            for node in nodes:
                temp.extend(node.sonsHash.values())
                nodelist.append(node)
            nodes = temp
            
        sorted(nodelist, key=getchar)
        for node in nodelist:
            f = lambda x : x.failure.status if x.failure else 0
            print("{} {} {} {} {}".format(node.ch, node.depth, node.status, f(node), node.results))
