#Coded By Zidan-ID\King Mr_Z17

#YouTube Mr_Z17

#Vortex Indonesia

import os,sys,time

 # SILAHKAN COSTUMISASI SENDIRI YA BOSQ #

def main():

    time.sleep(3)

    os.system ('clear')

    print '[96m'

    os.system ('figlet Tampilan Termux v3')

    print'[92m================================='

    print'[97m Author : [96mJejak Internet '

    print'[97m YouTube   : [96mJejak Internet '

    print'[92m================================='

    print'[92m++++++++++++ [97mM E N U [92m++++++++++++'

    print'[92m[[97m1[92m] [97mTampilan Termux v3 '

    print'[92m[[91m0[92m] [91mExit '

    gans = raw_input ('[97m==>[93m ')

    if gans in ['1']:

        time.sleep(3)

        os.system ('git clone https://github.com/Zidan-ID17/Theme-Me')

        print

        print (' [+] Proses Instalasi Selesai')

        print (' [+] Silakan ketik cd Theme-Me')

        print (' [+] Jika Sudah Ketik python2 umbrella.py')

        exit()

    if gans in ['0']:

        time.sleep(3)

        exit()

    else:

        time.sleep(3)

        print '[97m Pilih Yang Bener [92mBro . . .'

        time.sleep(3)

        main()

main()

