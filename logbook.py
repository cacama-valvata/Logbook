from datetime import datetime
import os

quit_opts = ["!exit", "!e", "!quit", "!q"]

DIR = "logs"
if not os.path.isdir(DIR):
    os.makedirs(DIR)

print("Welcome to the logbook. One entry per line below. !quit to quit.")
print("=================================================================")

while 1:
    entry = input()
    now = datetime.now()

    if entry in quit_opts:
        break;
    elif entry[0] == "!":
        continue;

    datefile = DIR + "/" + now.strftime("%Y-%m-%d") + ".txt"
    
    with open(datefile, "a") as f:
        f.write(now.strftime("%H:%M:%S UTC") + "\n")
        f.write(entry + "\n")
        f.write("\n")
