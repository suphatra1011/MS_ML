import sys, getopt

def main(argv):
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv,"hy:m:d:",["year=","month=","day="])
    except getopt.GetoptError:
        print ('test.py -y <Year Of Birth> -m <Month Of Birth> -d <Day Of Birth>')
        sys.exit(3)

    for opt, arg in opts:
        if opt == '-h':
            print ('test.py -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ("-y", "--year"):
            y = arg
        elif opt in ("-m", "--month"):
            m = arg
        elif opt in ("-d", "--day"):
            d = arg  
    print ('Year：', y)
    print ('Month：', m)
    print ('Day：', d)

if __name__ == "__main__":
   main(sys.argv[1:])
