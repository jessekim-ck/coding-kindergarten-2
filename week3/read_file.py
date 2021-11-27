with open("test.txt", "r") as f:
    lines = f.readlines()
    print(lines)
    for line in lines:
        print(line)
