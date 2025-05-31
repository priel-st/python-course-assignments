import sys
import codecs

filename = sys.argv[1]
with open(filename, "r") as original:
    txt = original.read()
rot13_txt = codecs.encode(txt, "rot_13")
with open("rot13_file.txt", "w") as new:
    new.write(rot13_txt)
