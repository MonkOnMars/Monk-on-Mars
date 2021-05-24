from time import gmtime, strftime
import json
import os

inputCounts = input("How much CTF(s)?: ")

ctfs = []
for i in range(int(inputCounts)):
    ctfName = input("CTF NAME: ")
    ctfURL = input("CTF URL: ")
    ctfUsername = input("CTF Username: ")
    ctfPassword = input("CTF Password: ")

    ctfObj = {
        "ctfName": ctfName,
        "ctfURL": ctfURL,
        "ctfUsername": ctfUsername,
        "ctfPassword": ctfPassword,
    }
    ctfs.append(ctfObj)

filename = strftime("%Y_%b_%d_ctfs.json", gmtime())

with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), "output", filename), "w") as f:
    f.write(json.dumps(ctfs))
