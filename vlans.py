import getpass
import telnetlib

HOST = "192.168.1.29" #configure the switch vlan 1 with this address for remote access
user = input("Enter your telnet password: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"enable\n")
tn.write(b"cisco\n")
tn.write(b"configure terminal\n")

for n in range (2,20):
    tn.write(b"vlan " + str(n).encode('ascii') + b "\b")
    tn.write(b"name Python_VLAN_)" + str(n).encode('ascii') + b"\n")

tn.write(b"end\n")
tn.write(b"copy running-config startup-config\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))