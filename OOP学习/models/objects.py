class TPerson():
    def __init__(self, height, weight):
        self.height = height
        self.weight = weight

    def run(self):
        self.__think()
        print('running...')

    def __think(self):
        print('thinking...')

class TUser(TPerson):
    # username=''
    # password=''
    # 构造器
    def __init__(self, username, password, height, weight):
        TPerson.__init__(self, height, weight)
        self.__username = username
        self.__password = password

    def __str__(self):
        return "print this object: " + self.__username + ", " + self.__password

    def setUsername(self, username):
        self.__username = username

    def setPassword(self, password):
        self.__password = password

    def getUsername(self):
        return self.__username

    def getPassword(self):
        return self.__password

    # 方法重写
    def run(self):
        print("car running...")

class TSell(TPerson):
    def __init__(self, height, weight):
        TPerson.__init__(self, height, weight)

    def run(self):
        print("OFO running...")