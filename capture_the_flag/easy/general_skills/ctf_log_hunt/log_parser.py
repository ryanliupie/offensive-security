with open("server.log", "r") as f:
    for line in f:
        if "INFO FLAGPART:" in line: 
            print(line)