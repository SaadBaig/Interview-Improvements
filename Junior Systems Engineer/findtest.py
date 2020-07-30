with open('test.txt', 'r') as searchfile:
        for line in searchfile:
                line = line.lower()
                count = line.count("test")
                print(count)