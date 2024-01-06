import socket

# ( Make sure below ip address and port numbers are correct )
# ip = "192.168.1.108"
ip = input("enter ip address: ")
port = 5002


class Client:
    def __init__(self):
        self.content = None
        self.ip = ip
        self.port = port

    def send_file(self, filename):
        file = "test_files/" + filename
        with open(file, 'rb') as f:
            self.content = f.read()
        return self.content

    def connect(self):
        try:
            s = socket.socket()
            s.connect((ip, port))
            # filename = "input_file_1.xlsx")
            filename = input("Enter input file name : ")
            content = self.send_file(filename)
            s.send(content)
            s.close()
            print("[SUCCESS] File sent successfully")
        except Exception as e:
            print("[ERROR] Opps something went wrong, check below error message")
            print("[ERROR MESSAGE] ", e)




if __name__ == '__main__':
    client = Client()
    client.connect()

