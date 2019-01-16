import configparser

class ReadCase:

    def __init__(self,file):
        self.cf = configparser.ConfigParser()
        self.cf.read(file,encoding='utf-8')

    def get_value(self,section,option):
        return self.cf.get(section,option)




if __name__ == '__main__':
    print(ReadCase('case.ini').get_value('CASE', 'button'))