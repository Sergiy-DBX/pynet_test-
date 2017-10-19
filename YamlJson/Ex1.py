import yaml

STREAM = 'test_file.yml'

with open(STREAM) as file_in:
    device_descriptor = yaml.load(file_in)
print(device_descriptor)

print(yaml.dump(device_descriptor))

#print(yaml.dump(device_descriptor)
