#This file is to run at the beginning of the session once
# it takes several minutes 9(p to 15)
#It initializes all the instruments: cameras, stage, fgpa, laser, optics, objectives, temperature
# To run an experiment, use .\main_executable.py

import sys
sys.path.insert(0, "C:\\Users\\clarklab\\PyseqX-master-JacobEdits\\PySeqX-master")
import pyseq

hs = pyseq.HiSeq()   

hs.initializeInstruments()
hs.initializeCams()