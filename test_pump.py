import sys
sys.path.insert(0, "C:\\Users\\clarklab\\PyseqX-master-JacobEdits\\PySeqX-master")
import pyseq
import time

hs = pyseq.HiSeq()

#initialize pumps and valves
print("initializing pumps and valves")
hs.p['A'].initialize()
hs.p['B'].initialize()
hs.v10['A'].initialize()
hs.v10['B'].initialize()
hs.v24['A'].initialize()
hs.v24['B'].initialize()

time.sleep(30)

# Using 8 inlets, only valid for actual hiseq flow cells. 
#If using Kunal's flow cells with 2 holes, 8 should be changed to 2 for all below
print("Using 8 inlet ports")
hs.move_inlet(8)
hs.p['A'].update_limits(8)
hs.p['B'].update_limits(8)

print('Pump A ready: ', hs.p['A'].check_pump())
print('Pump B ready: ', hs.p['B'].check_pump())

print('Pump A position: ', hs.p['A'].check_position())
print('Pump B position: ', hs.p['B'].check_position())

hs.v10['A'].check_valve()
hs.v10['B'].check_valve()
hs.v24['A'].check_valve()
hs.v24['B'].check_valve()

print(hs.v10['A'].n_ports)
print(hs.v10['B'].n_ports)
print(hs.v24['A'].n_ports)
print(hs.v24['B'].n_ports)


#reverse pump (from waste to sippers)
# print("reverse pumping from A")
# hs.p['A'].reverse_pump(1000)





# amt = 2000
# out_rate = 500
# while True:
#     print("reverse pumping from A")
#     hs.p['A'].reverse_pump(amt, in_flow = 1000, out_flow = out_rate)

#     amt = int(input('ul to pull?'))
#     out_rate = int(input('out rate?'))

