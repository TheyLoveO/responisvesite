with open("output.txt", "w") as f:
    for i in range(2, 10001, 2):
        f.write(str(i) + "\n")