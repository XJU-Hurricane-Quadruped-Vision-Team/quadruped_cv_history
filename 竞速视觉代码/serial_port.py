


import serial
import time
black=0
white=255
class Serial_port(serial.Serial):
    def __init__(self, port, baudrate, bytesize=8, stopbits=1, timeout=0.8, parity='N', **kwargs):
        """
        Args:
            port: 串口号
            baudrate: 波特率
            bytesize: 位
            stopbits:
            timeout: 延时
            parity:
            **kwargs:
        """
        super(Serial_port, self).__init__()
        self.port = port
        self.baudrate = baudrate
        self.bytesize = bytesize
        self.stopbits = stopbits
        self.timeout = timeout
        self.parity = parity
        """建立串口连接"""
        """设置串口参数：串口号，波特率，数据长度，停止位,延迟时间，校验位"""
        self.com = self.com_connect()

    def com_connect(self):
        isconnect = False
        while isconnect is False:
            mpu_ser = serial.Serial(port=self.port,
                                    baudrate=self.baudrate,
                                    bytesize=self.bytesize,
                                    stopbits=self.stopbits,
                                    timeout=self.timeout,
                                    parity=self.parity)
            isconnect = mpu_ser.is_open
            if isconnect:
                print("%s mpu connection success\r\n" % self.port)
                return mpu_ser

    def com_close(self):
        """关闭串口"""
        self.com.close()

    def send(self, send_data):
        """封装好的串口发送"""
        send_len = self.com.write(str(send_data).encode())
        return send_len

    def receive(self, read_len):
        """封装好的串口接收"""
        data = self.com.read(read_len).decode('utf-8')
        return data

    def ser_control(self,color,pixel_left,pixel_right,last_state,current_state):
        """视觉反馈数据串口控制逻辑"""

        if (pixel_left==white and color==white and pixel_right==white)or( pixel_left==black and color==black and pixel_right==white)or(pixel_left==black and color==white and pixel_right==white):
                if current_state!='ll':
                    current_state='ll'
                    self.com.write('ll\r\n'.encode())
                  
                    print("左转")

        if (pixel_left==white and color==black and pixel_right==black)or(pixel_left==white and color==white and pixel_right==black)or(pixel_left==black and color==white and pixel_right==black):
                if current_state!='rr':
                    current_state='rr'
                    self.com.write('rr\r\n'.encode())
                    
                    print("右转")      
                
        if (color==0 and pixel_left==0 and pixel_right==0):
            if current_state!='ww':
                current_state='ww'
                self.com.write('ww\r\n'.encode())
                
                print("直走")  


            #print(com)
            # q

        last_state=current_state


        return last_state,current_state

    def str2num(self, num_str):
        index = 0
        str_len = len(num_str)
        num = 0
        for c in num_str:
            index += 1
            num += (ord(c) - 48) * pow(10, str_len -    index)
        return num

    def jiguang_ceju(self):
        n = self.com.inWaiting()

        time.sleep(0.1)
        n = self.com.inWaiting()
        data = self.com.read(n).decode('utf-8')
        data = data[2:6]

        return data

        

        

