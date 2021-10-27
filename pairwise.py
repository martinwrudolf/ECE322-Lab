from allpairspy import AllPairs




def getallpairspy(parameters):

    print("PAIRWISE:")
    for i, pairs in enumerate(AllPairs(parameters)):
        print("{:2d}: {}".format(i, pairs))

def main():
    parameters = [
        ["0", "1", "2"],
        ["0", "1", "2"],
        ["0", "1", "2"],
    ]


    getallpairspy(parameters)
if __name__ == "__main__":
    main()






















