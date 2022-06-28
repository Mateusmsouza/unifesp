def get_array_from_file(path):
    with open(path, 'r') as reader:
        line = reader.readline()
        array = line.split(' ')
        return array