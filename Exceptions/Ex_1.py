from __future__ import print_function

net_dev_keys = [ 'ip_addr', 'username', 'password', 'vendor', 'model' ]
net_dev_value = "192.168.1.1 root RootPass Cisco 6509".split()

net_dev = dict(zip(net_dev_keys, net_dev_value))
print(net_dev)

try:
    dev_type = net_dev['device_type']
except KeyError:
    print("No 'device_type' key")
    print("Here is how dictionary looks like now:")
    print(net_dev)
finally:
    print("\nLet's make 'device_type' None")
    net_dev['device_type'] = None
    print("Here is how dictionary looks like now:")
    print(net_dev)

print()
x = net_dev.get('dev_type')
print(x)
