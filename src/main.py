'''
Created on 16 Jul. 2018

@author: sheng
'''
from ACalgorithm import ACBuild
if __name__ == '__main__':
    text = "Peter told me that peter the pickle piper piped a pitted pickle before he petered out. Phew!"
    Pattens = ["Peter", "peter", "pick", "pi", "z", "Peterz"]

    ac = ACBuild(Pattens)
    ac.buildGotoTree()

    ac.addFailure()
    ac.printTree()

    ac.acSearch(text)
    ac.printResult()
    