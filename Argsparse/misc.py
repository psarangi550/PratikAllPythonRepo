# import argparse
# import sys
#
# def calc(args):
#     if args.o=="+":
#         return args.x+args.y
#     elif args.o=="-":
#         return args.x+args.y
#
# parser=argparse.ArgumentParser()
# parser.add_argument("--x",type=int,default=1,help="This is a Number")
# parser.add_argument("--y",type=int,default=0,help="This is a Number")
# parser.add_argument("--o",type=str,default="+",help="Specify Operation")
# args=parser.parse_args()
# sys.stdout.write(str(calc(args)))


import os
import os.path
# print(next(os.walk(os.getcwd())))
print(os.path.join(os.getcwd(),"abc.txt"))
print(os.path.splitext("/user/home/abc.txt"))