import sys
sys.path.insert(0, "C:\\Users\\clarklab\\PyseqX-master-JacobEdits\\PySeqX-master")
import pyseq

hs = pyseq.HiSeq()   

def main(hs):
    init = input('Have you initialized the machine? y/n (exit to exit) \n')
    if init == 'exit':
        return
    if init == 'n':
        hs.initializeInstruments()
        hs.initializeCams()
    while True:
        action = input('What do you want to do?\n M for Move \n P for Picture \n (exit to exit) \n') #what else do we add? filters, temperature, lasers...
        if action == 'exit':
            return
        elif action == 'M' or action == 'Move' or action == 'm' or action == 'move':
            print('Not programmed yet')
        elif action == 'P' or action == 'Picture' or action == 'p' or action == 'picture':
            print('Not programmed yet')
        else:
            print('Not understood, try again')






if __name__ == '__main__':
    main(hs)