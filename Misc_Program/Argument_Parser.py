import argparse#importing the argparse module
import sys #importing the sys module
def calc(args):
    if args.o=="+":
        return (args.no+args.no2)
    elif args.o=="-":
        return (args.no - args.no2)
    elif args.o=="*":
        return (args.no * args.no2)
    elif args.o=="^":
        return(pow(args.no,args.no2))
if __name__ == "__main__":
    # step:-1 initializing the parser by creating the Object of Argumentparser class in args parse    module
    parser = argparse.ArgumentParser()
    # Step:2-once the Argument Parser Object being ready then we can parse the argument parameter passed over the command line
    #here we need to add the code which type of element argument parameter of cmd should be
    parser.add_argument("-no","--no",help="Please provide a float Number",type=float)
    parser.add_argument("-no2","--no2",help="Please privide another float value",type=float)
    parser.add_argument("-o","--o",help="Please provide which operation you want to perform",type=str,default="+")
    # step3:-once the command line parameter entered capture those value into the python script
    args = parser.parse_args()
    # print(args)
    # print(type(args))
    sys.stdout.write(str(calc(args)))#here it should of string type while reading to the console
