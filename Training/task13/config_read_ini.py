import configparser

config = configparser.ConfigParser()   
configFilePath = 'E:\\Coding\\Python\\Training\\task12\\config.ini'
config.read(configFilePath)

def read_data():
    id = config.get("Feild operator details","iD") # you can use small or big alphabets to call the value
    name = config.get("Feild operator details","Name")
    print(id)
    print(name)

#easy reading method
def read_data2():
    operator = config["Feild operator details"]
    parameters = config["camera parameters"]
    print(operator["id"])
    print(operator["name"])
    print(parameters["exposure"])


read_data2()