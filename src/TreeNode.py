'''
Created on 16 Jul. 2018

@author: sheng

'''

class TreeNode(object):
    '''
    Grammar prefix Tree is build via search parameters
    tree node example:
    -----------------------------------------------------------------------
    | char | status | sons's hash table | failure jump status | finished(result) table including all 
    ------------------------------------------------------------------------
    the result table contain all words with special char end 
    '''
    def __init__(self, parent, ch):
        self.parent = parent
        self.ch = ch
        self.results = []
        self.sonsHash = {}
        self.depth = 0
        self.status = 0
        self.failure = None
        if(self.parent != None):
            self.depth = self.parent.depth+1

    def addResult(self, result):
        if result not in self.results:
            self.results.append(result)

    
    def addSonNode(self, node):
        self.sonsHash[node.ch] = node
    
    def setFailure(self, node):
        self.failure=node
        return self.failure
        
    def getSonNode(self, ch):
        if ch in self.sonsHash:
            return self.sonsHash[ch]
        else:
            return None
       
