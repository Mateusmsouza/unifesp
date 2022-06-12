with open('dataset.txt', 'r') as dataset:
    while(True):
        register = ''
        line = dataset.readline()
        if not line:
            break
        if '----' in line and not register:
            while(True):
                line = dataset.readline()
                if '----' in line:
                    break
                register += ' ' + line.rstrip()
        
        print(register)
        register = ''