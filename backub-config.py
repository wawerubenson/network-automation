
import getpass
import telnetlib

#HOST = "localhost" #configure the switch vlan 1 with this address for remote access
user = input("Enter your telnet password: ")
password = getpass.getpass()

f = open('myswitches')

for IP in f:
    IP = ip.strip()
    print ("getting running config from switches" + (IP))
    HOST = IP
    tn = telnetlib.Telnet(HOST)
    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")
    tn.write(b"terminal length 0\n")
    tn.write(b"show run\n")
    tn.write(b"exit\n")
    
    readoutput = tn.read_all()
    save_output = open("switch" + HOST, "w") #opening a file and saving it
    save_output.write(readoutput.decode('ascii'))
    save_output.write("\n")
    save_output.close
    tn.write(b"end\n")
    
    print(tn.read_all().decode('ascii'))






