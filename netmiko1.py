from netmiko import ConnectHandler

iosv_l2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.1.2',
    'username': 'david',
    'password': 'cisco',
}
net_connection = ConnectHandler(**iosv_l2)
output = net_connection.send_command('show ip interface brief')
print(output)

config_commands = ['interface loopback 0', 'ip address 1.1.1.1 255.255.255.255']
output = net_connection.send_config_set(config_commands)
print(output)

for n in range (2,21):
    print("Creating VLAN " + str(n))
    config_commands = ['vlan ' + str(n), 'name Python vlan ' + str(n)]
    output = net_connection.send_config_set(config_commands)
    print(output)