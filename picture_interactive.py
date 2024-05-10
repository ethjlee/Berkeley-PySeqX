import sys
sys.path.insert(0, "C:\\Users\\clarklab\\PyseqX-master-JacobEdits\\PySeqX-master")
import pyseq, time


def test_cam(hs):
    hs.initializeInstruments()
    hs.initializeCams()
    hs.optics.initialize()
    green_laser = hs.lasers['green']
    red_laser = hs.lasers['red']

    print(f'Green laser get power: {green_laser.get_power()}')
    print(f'Red laser get power: {red_laser.get_power()}')
    
    hs.optics.move_ex('green', 'open')
    hs.optics.move_ex('red', 'open')
    hs.optics.move_em_in(False)
   
    """hs.x.move(25000)
    hs.y.move(-14000000)"""
    slide = ""
    if slide != "Y":
        slide = input("Ready to insert slide. Enter \"Y\" when slide is in and lid closed").upper()


    hs.y.command('s r0x24 21')
    while True:
        move = input('move stage? y/n (exit to exit) \n')
        if move == 'exit':
            return
        if move == 'y':

            ypos = int(float(input('y position? (in millions) -15 to 0 \n')) * 1e6) 
            xpos = int(input('x position 1000 to 50000 \n'))
            zpos = int(input('z position? 1 integer 0 to 25000 \n'))
            
            if ypos < -15000000 or ypos > 0:
                print("bad y stage position", ypos)
                continue

            hs.message('moving y stage')
            yfin = hs.y.move(ypos)

            hs.message('moving x stage')
            xfin = hs.x.move(xpos)

            hs.message('moving z stage')
            zfin = hs.z.move([zpos,zpos,zpos])

            print('x position ', xfin, '\ny position ', yfin, '\nzfin ', zfin)
            
            hs.obj.move(31000)

            cont = input('take another picture? y/n (exit to exit) \n')
            if cont == 'exit':
                return
            if cont == 'n':
                continue

            """green_laser.turn_on(True)
            red_laser.turn_on(True)"""
            print('green status: ', green_laser.get_status())  ## return true, laser is on
            print('red status: ', red_laser.get_status())   ## return true, laser is on
            
            power = 450
            print("turning on laser")

            time.sleep(5)
            green_laser.set_power(power)
            red_laser.set_power(power)
            print('green laser power', green_laser.get_power()) 
            print('red laser power', red_laser.get_power()) # -1

            hs.optics.move_ex('green', 'open')
            hs.optics.move_ex('red', 'open')

            frames = int(input('frames? \n'))
            imagename = input('image name? \n')
            print(hs.image_path)
            hs.take_picture(frames, imagename)

if __name__ == '__main__':
    hs = pyseq.HiSeq()
    test_cam(hs)

