
import sys
sys.path.insert(0, "C:\\Users\\clarklab\\PyseqX-master-JacobEdits\\PySeqX-master")
import pyseq
import csv
import time

with open('20240405_lserdata_r4_20sec.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    field = ["set power", "green power", "red power"]
    writer.writerow(field)

hs = pyseq.HiSeq()

green_laser = hs.lasers['green']
red_laser = hs.lasers['red']
green_laser.initialize()
red_laser.initialize()

green_laser.turn_on(True)
red_laser.turn_on(True)



for value in range(0,250,10):
    print("setting power to ", value)
    green_laser.set_power(value)
    red_laser.set_power(value)
    time.sleep(20)
    green_power = green_laser.get_power()
    red_power = red_laser.get_power()
    print('green power: ', green_power )
    print('red power: ', red_power)
    with open('20240405_lserdata_4_20sec.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([value, green_power, red_power])
