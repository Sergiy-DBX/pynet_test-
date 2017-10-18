from __future__ import print_function

net_dev_keys = [ 'ip_addr', 'username', 'password', 'vendor', 'model' ]
net_dev_value = "192.168.1.1 root RootPass Cisco 6509".split()

net_dev_zip = zip(net_dev_keys, net_dev_value)
#print(net_dev_zip)
#print(type(net_dev_zip))

net_dev = dict(net_dev_zip)
#print(net_dev)

print("Key values in net_device dictionary:")
for k in net_dev:
    print("{:^10}".format(k))

print()

print("All values in net_device dictionary:")
for v in net_dev.values():
    print("{:^10}".format(v))

print()

print("Key, value pairsin net_device dictionary:")
for k,v in net_dev.items():
    print("Key: {:>20}       Value: {:>20}".format(k,v))

print()
print("Passwork update")
print()

net_dev['password'] = 'New_password_for_root'

print("New Passord:", net_dev['password'])
print()
print("Dictionary:")
print()
print(net_dev)

print()
print("Adding Secret to dictionary   ...")
print()

net_dev['secret'] = 'Secretos....'
print("Dictionary:")
print()
print(net_dev)

print()
print("Getting not existing 'device_type' key gracefully ... ")
print()

device_type = net_dev.get('device_type', 'cisco_ios')

print("device_type is {}".format(device_type))
