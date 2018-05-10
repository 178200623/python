import socket,time,threading
socket.setdefaulttimeout(3)
screenLock = threading.Semaphore(value=1)
def socket_port(ip,port):
    '''
    输入IP和端口号，扫描判断端口是否开放
    :param ip:
    :param port:
    :return:
    '''
    try:
        connSkt = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        host = socket.gethostname()
        connSkt.connect((host,9999))
        result = connSkt.recv(1024)
        print(result.decode('utf-8'))
        if result == 0:
            screenLock.acquire()
            print(ip,"的端口",port,"开放")
            screenLock.release()
    except:
        screenLock.release()
        print("扫描异常",port)
    finally:
        screenLock.release()
        connSkt.close()


def ip_scan(ip) :
    '''
    请输入ip,扫描0-65534端口
    :param ip:
    :return:
    '''
    try:
        print("开始扫描")
        start_time = time.time()
        for port in range(0,1):
            t = threading.Thread(target=socket_port,args=(ip,int(33899)))
            t.start()
        print("扫描端口完成，总用时： %。2f" % (time.time() - start_time))
        input("Press Enter to Exit")
    except:
        print("扫描ip出错")

if __name__ == "__main__" :
    #url = input("Please Input the Ip that you want to scan :")
    lock = threading.local()
    ip_scan('192.168.0.1')
