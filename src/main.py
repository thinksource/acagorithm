'''
Created on 16 Jul. 2018

@author: sheng
'''
from ACalgorithm import ACBuild
if __name__ == '__main__':
    text = "ushers"
    Pattens = ["he", "she", "his", "hers"]
    ac = ACBuild(text, Pattens)
    ac.buildGotoTree()

    ac.addFailure()
    # ac.printTree()

    ac.acSearch()
    ac.printResult()
    