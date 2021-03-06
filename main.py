from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.clock import Clock
from kivy.graphics.texture import Texture
from kivy.core.image import Image
from kivy.core.window import Window
import cv2
import socket


def connectionout():
    TCP_IP = "127.0.0.1"
    TCP_PORT = 5555
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((TCP_IP, TCP_PORT))
    print('Outbound Connection Online')
    s.listen(1)
    return s

def connectionin():
    TCP_IP = "127.0.0.1"
    TCP_PORT = 5556
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((TCP_IP, TCP_PORT))
    print('Inbound Connection Online')
    s.listen(1)
    return s

class GUIWidget(FloatLayout):
    capture = cv2.VideoCapture(-1)
    capture2 = cv2.VideoCapture(-1)
    # initialization of key press check list
    Push = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    sout = connectionout()
    sin = connectionin()
    Lim = "0000"
    conn_out = 0
    conn_in = 0

    def __init__(self, **kwargs):
        super(GUIWidget, self).__init__(**kwargs)
        Window.bind(on_key_up=self._keyup)
        Window.bind(on_key_down=self._keydown)

    def _keyup(self, *args):
        if args[1] == 119:
            self.Push[0] = False
        if args[1] == 115:
            self.Push[1] = False
        if args[1] == 97:
            self.Push[2] = False
        if args[1] == 100:
            self.Push[3] = False
        if args[1] == 104:
            self.Push[4] = False
        if args[1] == 108:
            self.Push[5] = False
        if args[1] == 113:
            self.Push[6] = False
        if args[1] == 101:
            self.Push[7] = False
        if args[1] == 110:
            self.Push[8] = False
        if args[1] == 109:
            self.Push[9] = False
        if args[1] == 99:
            self.Push[10] = False
        if args[1] == 102:
            self.Push[11] = False
        if args[1] == 111:
            self.Push[12] = False
        if args[1] == 105:
            self.Push[13] = False

    def _keydown(self, *args):
        if args[1] == 119:
            self.Push[0] = True
        if args[1] == 115:
            self.Push[1] = True
        if args[1] == 97:
            self.Push[2] = True
        if args[1] == 100:
            self.Push[3] = True
        if args[1] == 104:
            self.Push[4] = True
        if args[1] == 108:
            self.Push[5] = True
        if args[1] == 113:
            self.Push[6] = True
        if args[1] == 101:
            self.Push[7] = True
        if args[1] == 110:
            self.Push[8] = True
        if args[1] == 109:
            self.Push[9] = True
        if args[1] == 99:
            self.Push[10] = True
        if args[1] == 102:
            self.Push[11] = True
        if args[1] == 111:
            self.Push[12] = True
        if args[1] == 105:
            self.Push[13] = True
            print('i')
        if args[1] == 49:
            print(self.ids.L5top.pos_hint)
            print(self.ids.L5top.pos_hint['x'])
        if args[1] == 50:
            self.ids.L5top.pos_hint = {'x': 0,'y': 0}

    def vidupdate(self, dt):
        # print(cv2.VideoCapture.isOpened(self.capture))
        # Camera 1
        # read in frame
        ret, frame1 = self.capture.read()
        if ret:
            # finds video size for line positioning
            height, width, channels = frame1.shape
            # flips frame to correct orientation
            buf1 = cv2.flip(frame1, 0)
            # creates texture to change image
            buft1 = buf1.tostring()
            texture1 = Texture.create(size=(frame1.shape[1], frame1.shape[0]), colorfmt='bgr')
            texture1.blit_buffer(buft1, colorfmt='bgr', bufferfmt='ubyte')
            # display image from the texture
            self.ids.img1.texture = texture1
        else:
            texture = Image('NoConnection.png').texture
            self.ids.img1.texture = texture

    def vidupdate2(self, dt):
        # Camera 2
        # read in frame
        # Change capture here to use 2 different feeds
        ret, frame2 = self.capture.read()
        # ret, frame2 = self.capture2.read()
        if ret:
            # finds video size for line positioning
            height, width, channels = frame2.shape
            # adds circle to video
            centx = round(width / 2)
            centy = round(height / 2)
            frame1 = cv2.rectangle(frame2, pt1=(75, 75), pt2=(width - 75, height - 75), color=(0, 255, 0), thickness=5)
            cv2.circle(frame2, center=(centx, centy), radius=50, color=(0, 255, 0), thickness=5)
            # flips frame to correct orientation
            buf2 = cv2.flip(frame2, 0)
            # creates texture to change image
            buft2 = buf2.tostring()
            texture2 = Texture.create(size=(frame2.shape[1], frame2.shape[0]), colorfmt='bgr')
            texture2.blit_buffer(buft2, colorfmt='bgr', bufferfmt='ubyte')
            # display image from the texture
            self.ids.img2.texture = texture2
        else:
            texture = Image('NoConnection.png').texture
            self.ids.img2.texture = texture

    def cmdout(self, dt):
        cmdout = 'p'
        if sum(self.Push) <= 1:
            # command w
            if self.Push[0]:
                cmdout = 'w'
            # command s
            if self.Push[1]:
                cmdout = 's'
            # command a
            if self.Push[2]:
                cmdout = 'a'
            # command d
            if self.Push[3]:
                cmdout = 'd'
            # command h
            if self.Push[4]:
                cmdout = 'h'
            # command l
            if self.Push[5]:
                cmdout = 'l'
            # command q
            if self.Push[6]:
                cmdout = 'q'
            # command e
            if self.Push[7]:
                cmdout = 'e'
            # command n
            if self.Push[8]:
                cmdout = 'n'
            # command m
            if self.Push[9]:
                cmdout = 'm'
            # command c
            if self.Push[10]:
                cmdout = 'c'
            # command f
            if self.Push[11]:
                cmdout = 'f'
            # command o
            if self.Push[12]:
                cmdout = 'o'
            # command o
            if self.Push[13]:
                cmdout = 'i'
        print(cmdout)
        if not self.conn_out:
            self.conn_out, addr = self.sout.accept()
        self.conn_out.sendall(cmdout.encode('utf-8'))

    def vidconnect(self,dt):
        if not cv2.VideoCapture.isOpened(self.capture):
            print('Reconnecting Camera 1')
            self.capture = cv2.VideoCapture(0)
            # self.capture = cv2.VideoCapture('udp://192.168.1.30:1234?overrun_nonfatal=1&fifo_size=50000000?buffer_size=10000000',cv2.CAP_FFMPEG)
            self.capture.set(cv2.CAP_PROP_BUFFERSIZE, 1)

    def vidconnect2(self,dt):
        if not cv2.VideoCapture.isOpened(self.capture2):
            print('Reconnecting Camera 2')
            # self.capture2 = cv2.VideoCapture(0)
            # self.capture2 = cv2.VideoCapture('udp://192.168.1.30:1235?overrun_nonfatal=1&fifo_size=50000000?buffer_size=10000000',cv2.CAP_FFMPEG)
            self.capture2.set(cv2.CAP_PROP_BUFFERSIZE, 1)

    def limcheck(self, dt):
        if not self.conn_in:
            self.conn_in, addr = self.sin.accept()
        data, addr = self.conn_in.recvfrom(4)
        self.Lim = data.decode("utf-8")
        print(self.Lim)
        self.Lim = list(map(int, self.Lim))
        if self.Lim[0]:
            self.ids.L7top.col = 1, 0, 0, 1
        else:
            self.ids.L7top.col = 0, 1, 0, 1
        if self.Lim[1]:
            self.ids.L8bot.col = 1, 0, 0, 1
        else:
            self.ids.L8bot.col = 0, 1, 0, 1
        if self.Lim[2]:
            self.ids.L9left.col = 1, 0, 0, 1
        else:
            self.ids.L9left.col = 0, 1, 0, 1
        if self.Lim[3]:
            self.ids.L10right.col = 1, 0, 0, 1
        else:
            self.ids.L10right.col = 0, 1, 0, 1
# make shapes move


    def _keyup(self, *args):
        if args[1] == 57: # corresponds to key 9
            #  print(input(newposition))
            #print(self.ids.vertical.pos_hint)
            print(self.ids.vertical.pos_hint['x'])

        if args[1] == 56: # corresponds to key 8
        #  self.ids.L5top.pos_hint = {'x': 0,'y': 0}
            stringtest = int('400')
        # print(input(stringtest))
            newposition = (stringtest - 200)/200
            print(newposition)
            self.ids.vertical.pos_hint = {'x': .5,'y': .5+newposition}
            print(self.ids.vertical.pos_hint['x'])






class GUIApp(App):
    title = 'Test GUI by Charles'

    def build(self):
        gui = GUIWidget()
        Clock.schedule_interval(gui.vidupdate, 1.0/240)
        Clock.schedule_interval(gui.vidupdate2, 1.0/240)
        Clock.schedule_interval(gui.vidconnect, 1.0/30)

        # Clock.schedule_interval(gui.vidconnect2, 1.0/30)
       # Clock.schedule_interval(gui.cmdout, 1.0/30)
        #Clock.schedule_interval(gui.limcheck, 1.0/30)
        # Clock.schedule_interval(gui.cmdout, 1.0/30)
        # Clock.schedule_interval(gui.limcheck, 1.0w/30)

        return gui


if __name__ == '__main__':
    GUIApp().run()