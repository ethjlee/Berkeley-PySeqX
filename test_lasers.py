import sys
sys.path.insert(0, "C:\\Users\\clarklab\\PyseqX-master-JacobEdits\\PySeqX-master")
import pyseq
import time


hs = pyseq.HiSeq()

green_laser = hs.lasers['green']
red_laser = hs.lasers['red']
green_laser.initialize()
red_laser.initialize()

green_laser.turn_on(True)
red_laser.turn_on(True)

print("green", green_laser.version)
print("red", red_laser.version)

print(green_laser.get_power())
print(red_laser.get_power())

# green_laser.turn_on(True)
# red_laser.turn_on(True)
green_laser.set_power(500)
red_laser.set_power(500)
# print('laser power',green_laser.get_power())
# print(red_laser.get_power())

print(green_laser.get_status())
print(red_laser.get_status())

while True:
    print("green power", green_laser.get_power())
    print("red power", red_laser.get_power())
# hs.lasers['green'].set_power(100)   #Set green laser power to 100 mW
# hs.lasers['red'].set_power(100)     #Set red laser power to 100 mW

# hs.y.move(-180000)                  #Move stage to top right corner of Flow Cell A
# hs.x.move(17571)
# hs.z.move([21250, 21250, 21250])    #Raise z stage

# hs.obj.move(30000)                  #Move objective to middle-ish

# hs.optics.move_ex('green','open')                #Move excitation filter 1 to open position
# hs.optics.move_ex('red','open')                #Move excitation filter 2 to open position

# print(hs.lasers['green'].get_status())     #Get green laser power (mW i think)
# print(hs.lasers['red'].get_status())  

# print(hs.lasers['green'].get_power() )     #Get green laser power (mW i think)
# print(hs.lasers['red'].get_power())        #Get red laser power   (mW i think)
# # stat
# print("STAT:\n")
# print(hs.lasers['green'].command('STAT?'))     #Get green laser power (mW i think)
# print(hs.lasers['red'].command('STAT?'))  

# # power
# print("Power:\n")
# print(hs.lasers['green'].command('POWER?'))     #Get green laser power (mW i think)
# print(hs.lasers['red'].command('POWER?'))  

# # current
# print("Current:\n")
# print(hs.lasers['green'].command('CURRENT?'))     #Get green laser power (mW i think)
# print(hs.lasers['red'].command('CURRENT?'))  

# # TEMP
# print("TEMP:\n")
# print(hs.lasers['green'].command('LASTEMP?'))     #Get green laser power (mW i think)
# print(hs.lasers['red'].command('LASTEMP?'))  

# # POWER SUPPLY
# print("POWER SUPPLY:\n")
# print(hs.lasers['green'].command('PSUTEMP?'))     #Get green laser power (mW i think)
# print(hs.lasers['red'].command('PSUTEMP?'))  