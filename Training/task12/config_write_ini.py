import configparser

config_filename = "E:\\Coding\\Python\\Training\\task12\\config.ini"

configfile = open(config_filename,"w") #ini file created
config = configparser.ConfigParser() #it defines reading and writing functionality for config files. (windows)

#adding content to the file
id = str(input("Enter user ID: "))
Name = str(input("Enter User Name: "))

#camera parameters
width = 1920
height = 1080 
Exposure = 50
SLno = 1

config.add_section("Feild operator details")
config.set("Feild operator details","id",id)
config.set("Feild operator details","Name",Name)

config.add_section("camera parameters")
config.set("camera parameters","width",str(width))
config.set("camera parameters","height",str(height))
config.set("camera parameters","exposure",str(Exposure))
config.set("camera parameters","slno",str(SLno))

config.write(configfile)
print("Writing Done..!")
configfile.close()