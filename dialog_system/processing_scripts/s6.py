import os
import sys
import codecs

for filename in os.listdir(r"{}".format(sys.argv[1])):
    with codecs.open(sys.argv[1] + "//" + filename, "r",
                     encoding="utf-8", errors="ignore") as file:
        with open(sys.argv[1] + "//" + filename + "_proc", "w",
                  encoding="utf-8") as outp:
            for i, line in enumerate(file):
                if line.startswith("A") or line.startswith("B") and \
                   line != "":
                    outp.write(line[3:])
