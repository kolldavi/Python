import argparse

# initiate the parser
parser = argparse.ArgumentParser()  

parser.add_argument("-v","--version", help="show version",action="store_true")
parser.add_argument("-w","--width", help="set output width")


args = parser.parse_args()  

if args.version:
    print("version .01")

if args.width:
    print("set output width to %s"% args.width)