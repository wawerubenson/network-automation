from netmiko import ConnectHandler

# access layer switches
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

# Core layer switches
iosv_l2_s5 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.80',
    'username': 'ben',
    'password': 'kogi'
}


iosv_l2_s6 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.81',
    'username': 'ben',
    'password': 'kogi'
}

iosv_l2_s7 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.82',
    'username': 'ben',
    'password': 'kogi'
}


with open('ios_layer2_cmd') as f:
    lines = f.read().splitlines()
print(lines)

all_devices = [iosv_l2_s1, iosv_l2_s2, iosv_l3_s3, iosv_l2_s4]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(lines)
    print(output)

with open('iosv_l2_core') as f:
    lines = f.read.splitlines()
print(lines)

all_devices = [iosv_l2_s1, iosv_l2_s2, iosv_l3_s3, iosv_l2_s4, iosv_l2_s5, iosv_l2_s6, iosv_l2_s7]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(lines)
    print(output)
