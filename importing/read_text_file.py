## HOW TO READ A TEXT FILE

filename = 'huck_finn.txt'

file =  open(filename, mode='r') # 'r' is to read

text = file.read()

file.close()

print(text)

# Method 2
logfile = 'docker_logs.txt'
with open(logfile, 'r') as file:
    print(file.read())