import sys , easygui , datetime , time , os , pygame , socket , threading , urllib , re
from PythonCard import model
pygame.init()
pygame.mixer.init()



class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print "Starting " + self.name
        # Get lock to synchronize threads
        threadLock.acquire()
        checkInbox(self.name, self.counter, 3)
        # Free lock to release next thread
        threadLock.release()

'''
class myThread2 (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print "Starting " + self.name
        # Get lock to synchronize threads
        threadLock.acquire()
        GUI(self.name, self.counter, 3)
        # Free lock to release next thread
        threadLock.release()
'''

def checkInbox(threadName, delay, counter):
    while True:
        if ONline == True:
            #test = str(raw_input("test: "))
            #if test == "break":
            #    break
            sock = socket.socket(socket.AF_INET, # Internet
                                 socket.SOCK_DGRAM) # UDP
            sock.bind((S_IP, int(S_PORT)))
            data, addr = sock.recvfrom(int(S_BUFFERSIZE)) #buffer size in bytes
            now = datetime.datetime.now()
            if data != "CC":
                print "Server>> ", now, " ", str(addr) + data
                easygui.msgbox(str(addr) + data, now)
                #self.components.chathistory.text = self.components.chathistory.text + "\n\n" + str(now) + " " + UDP_SENDERIP + ": " +  data
                
            if data == "CC":
                print data, str(addr)
                #send "heartbeat" to connected client
                sock = socket.socket(socket.AF_INET, # Internet
                socket.SOCK_DGRAM) # UDP
                sock.sendto(S_IP+" You have Succesfully connected to: "+ S_IP, (addr))

        elif ONline == False:
            print "Server>> OFFLINE!"
            time.sleep(1)


#def GUI(threadName, delay, counter):
class HauptFenster(model.Background):
    def on_link_mouseClick(self, event):
        os.startfile("http://whatismyip.org/")
    def on_ONLINE_mouseClick(self, event):
        global ONline
        Switch = self.components.ONLINE.checked
        if Switch == True:
            UDP_IP = self.components.UDP_IP.text
            UDP_PORT = self.components.UDP_PORT.text
            UDP_PORT = int(UDP_PORT)
            time.sleep(1)
            ONline = 1
            self.components.ONLINE.label = "Go Offline"
            #easygui.msgbox("Server>> Online!")
            time.sleep(2)
            sock = socket.socket(socket.AF_INET, # Internet
            socket.SOCK_DGRAM) # UDP
            sock.sendto("Server>> Online!", (UDP_IP, UDP_PORT))

        if Switch == False:
            UDP_IP = self.components.UDP_IP.text
            UDP_PORT = self.components.UDP_PORT.text
            UDP_PORT = int(UDP_PORT)
            time.sleep(1)
            ONline = 0
            self.components.ONLINE.label = "Go Online"
            #easygui.msgbox("Server>> Offline!")
            time.sleep(2)
            sock = socket.socket(socket.AF_INET, # Internet
            socket.SOCK_DGRAM) # UDP
            sock.sendto("Server>> Offline!", (UDP_IP, UDP_PORT))
        
    def on_startserver_mouseClick(self, event):
        self.components.startserver.enabled = False
        self.components.ONLINE.enabled = True
        self.components.ONLINE.checked = True
        self.components.ONLINE.label = "Go Offline"
        global S_IP
        global S_PORT
        global S_BUFFERSIZE
        S_IP = self.components.IP.text
        S_PORT = self.components.PORT.text
        S_BUFFERSIZE = self.components.BUFFERSIZE.text
        now = datetime.datetime.now()
        time.sleep(1)
        thread1.start()
        global ONline
        ONline = 1
        time.sleep(1)
        print "Server>> ", now, "Server is Running"
        print "Server>> IP: ", S_IP
        print "Server>> Port: ", S_PORT
        print "Server>> Buffersize: ", S_BUFFERSIZE
        print "\n\n\n"
        '''
        os.startfile("Udp Server.py")
        
        sock = socket.socket(socket.AF_INET, # Internet
                             socket.SOCK_DGRAM) # UDP
        sock.bind(("192.168.0.145", 25565))
        while True:
            test = str(raw_input("test: "))
            if test == "break":
                break
            data, addr = sock.recvfrom(2048) #buffer size in bytes
                now = datetime.datetime.now()
                #if data == "CC":
                #    print "test"
                print now, " ", data
                easygui.msgbox(data, now)
                
        
        def on_online_mouseClick(self, event):
            if self.components.online.checked == True:
                sock = socket.socket(socket.AF_INET, # Internet
                         socket.SOCK_DGRAM) # UDP
                sock.bind(("192.168.0.145", 25565))
                while True:
                    data, addr = sock.recvfrom(2048) #buffer size in bytes
                    now = datetime.datetime.now()
                    #if data == "CC":
                    #    print "test"
                    print now, " ", data
                    easygui.msgbox(data, now)
            if self.components.online.checked == False:
                sock.bind(("",""))
        '''
    def on_connect_mouseClick(self, event):
        self.components.connect.enabled = False
        self.components.send.enabled = True
        self.components.chatenter.enabled = True
        self.components.disconnect.enabled = True
        global UDP_IP
        global UDP_PORT
        global UDP_NICK
        UDP_IP = self.components.UDP_IP.text
        UDP_PORT = self.components.UDP_PORT.text
        UDP_NICK = self.components.NICK.text
        UDP_PORT = int(UDP_PORT)
        
        sock = socket.socket(socket.AF_INET, # Internet
        socket.SOCK_DGRAM) # UDP
        sock.sendto("CC", (UDP_IP, UDP_PORT))
        time.sleep(2)
        sock.sendto("Client Connected: "+UDP_NICK, (UDP_IP, UDP_PORT))

        
    def on_send_mouseClick(self, event):
        try:
            now = datetime.datetime.now()
            MESSAGE = self.components.chatenter.text
            #print now, " ", UDP_SENDERIP, ": ", MESSAGE
            #self.components.chathistory.text = self.components.chathistory.text + "\n\n" + str(now) + " " + UDP_SENDERIP + ": " +  MESSAGE
            sock = socket.socket(socket.AF_INET, # Internet
            socket.SOCK_DGRAM) # UDP
            sock.sendto(UDP_NICK + ": " + MESSAGE, (UDP_IP, UDP_PORT))
            time.sleep(1)
            self.components.chatenter.text = ""

        except:
            easygui.msgbox("Please type English!")
    
    
    def on_disconnect_mouseClick(self, event):
        sock = socket.socket(socket.AF_INET, # Internet
        socket.SOCK_DGRAM) # UDP
        sock.sendto("Client Disconnected: "+UDP_NICK, (UDP_IP, UDP_PORT))
        self.components.connect.enabled = True
        self.components.send.enabled = False
        self.components.chatenter.enabled = False
        self.components.disconnect.enabled = False

    def on_exit_mouseClick(self, event):
        really = easygui.buttonbox("Do you really want to exit?",
                                   choices = ("No","Yes"))
        if really == "No":
            pass
        if really == "Yes":
            sys.exit()



threadLock = threading.Lock()
threads = []

# Create new threads
thread1 = myThread(1, "Server", 1)
#thread2 = myThread2(2, "Thread-2", 2)

# Start new Threads
#thread2.start()
#thread1.start()

app = model.Application(HauptFenster)
app.MainLoop()

# Add threads to thread list
threads.append(thread1)
#threads.append(thread2)

# Wait for all threads to complete
for t in threads:
    t.join()
print "Exiting Main Thread"

