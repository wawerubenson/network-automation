from netmiko import ConnectHandler

iosv_l2_s1 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.71',
    'username': 'ben',
    'password': 'kogi'
}

iosv_l2_s2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.72',
    'username': 'ben',
    'password': 'kogi'
}

iosv_l3_s3 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.73',
    'username': 'ben',
    'password': 'kogi'
}

iosv_l2_s4 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.70',
    'username': 'ben',
    'password': 'kogi'
}

all_devices = [iosv_l2_s1, iosv_l2_s2, iosv_l3_s3, iosv_l2_s4]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    for n in range (2,21):
    print("Creating VLAN " + str(n))
    config_commands = ['vlan ' + str(n), 'name Python vlan ' + str(n)]
    output = net_connection.send_config_set(config_commands)
    print(output)