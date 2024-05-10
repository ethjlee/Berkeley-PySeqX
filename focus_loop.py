import sys
sys.path.insert(0, "C:\\Users\\clarklab\\PyseqX-master-JacobEdits\\PySeqX-master")
import pyseq

def test_cam(hs):
    hs.initializeInstruments() #if you comment out to test something, please uncomment after
    hs.initializeCams()
    hs.optics.initialize()
    green_laser = hs.lasers['green']
    red_laser = hs.lasers['red']

    print(f'Green laser get power: {green_laser.get_power()}')
    print(f'Red laser get power: {red_laser.get_power()}')

    hs.optics.move_ex('green', 'open')
    hs.optics.move_ex('red', 'open')
    hs.optics.move_em_in(True)
   
    hs.x.move(38000)
    hs.y.move(-3000000)
    green_laser.turn_on(True)
    red_laser.turn_on(True)

    for z in range(10000,12000,100):
            hs.z.move([z,z,z])
            for obj in range(2000,62000,1000):
                hs.obj.move(obj)
                


                print('green status: ', green_laser.get_status())  ## return true, laser is on
                print('red status: ', red_laser.get_status())   ## return true, laser is on
                
                power = 200
                green_laser.set_power(power)
                red_laser.set_power(power)
                print('green laser power', green_laser.get_power()) 
                print('red laser power', red_laser.get_power()) # -1

                hs.optics.move_ex('green', 'open')
                hs.optics.move_ex('red', 'open')
                hs.optics.move_em_in(True)

                frames = 32
                imagename = ('z' + str(z) + '_obj' + str(obj))
                print(hs.image_path)
                hs.take_picture(frames, imagename)
                hs.y.move(-3000000)


if __name__ == '__main__':
    hs = pyseq.HiSeq()
    test_cam(hs)

