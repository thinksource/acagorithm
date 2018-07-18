'''
Created on 16 Jul. 2018

@author: sheng
'''

class TreeNode(object):
    '''
    Grammar Tree build via search parameters
    '''
    def __init__(self, parent, ch):
        self.parent = parent
        self.ch = ch
        self.results = []
        self.sonsHash = {}
        # self.sons = []
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
        # self.sons.append(node)
        
        
    def getSonsString(self):
        re=""
        for i in self.sonsHash:
            re += i+", "
        return re[:-2]
    
    def setFailure(self, node):
        self.failure=node
        return self.failure
        
    def getSonNode(self, ch):
        if ch in self.sonsHash:
            return self.sonsHash[ch]
        else:
            return None
       
    def __str__(self):
        re=""
        if self.sonsHash:
            re+="state: {}".format(self.status)+'\n'
            if self.failure:
                f = self.failure.status
            else:
                f = 0
            re+="root ch: {}, state:{}, level: {}, failure:{}, result:{}".format(self.ch, self.status, self.depth, f, self.results)+"\n"
            re+="child: {}".format(self.getSonsString())+"\n"
            for key, value in self.sonsHash.items():
                re+="key: {}".format(key)+"\n"
                re+="value: {}".format(value.__str__())+"\n"
            
            return re
        else:
            return "empty"