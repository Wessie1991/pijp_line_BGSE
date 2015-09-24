Enter file contents hereimport os
import sys

__author__ = 'des'
def Asc11_som(String):
    return (sum([(ord(p)-64) for p in String])/len(String))

def Naar_file(seq, accii, header_lijst):
    file = open(str(naam_file) + "_trimmer_Python.txt" , "a")
    file.write(header_lijst[0] + "\n")
    file.write(max(seq, key=len) + "\n")
    file.write(header_lijst[1] + "\n")
    file.write(max(accii, key=len) + "\n")
    file.flush()
    return file

def naar_os(seq, accii, header_lijst):
    print header_lijst[0] + "\n" + max(seq, key=len) + '\n' + header_lijst[1] + '\n' + max(accii, key=len)

def score_check_over_seq(lijst):
    seq=lijst[1]
    code=lijst[3]
    index_t = False
    knip_index = []
    nieuweseq = ""
    nieuwecode = "" 
    # de afknip scoren is onder de 84 dat is gelijk aan 20+64
    for index, i in enumerate(code):
        if index >= 3:
            index_t = True
            #print seq[index-3 : index ]
            #print Asc11_som(code[index-2 : index ])
        if ord(i) <= 84 and index_t:
            if Asc11_som(code[index-3 : index ]) <= 20:
                #print seq[index-3 : index ]
                knip_index.append(index)
                nieuweseq += "*"
                nieuwecode += "*"
            else:
                nieuweseq += seq[index]
                nieuwecode += i
        elif index_t:
            nieuweseq += seq[index]
            nieuwecode += i
        if ord(i) <= 84 and not(index_t):
            nieuweseq += "*"
            nieuwecode += "*"
            knip_index.append(index)
        elif not(index_t):
            nieuweseq += seq[index]
    naar_os(nieuweseq.split("*"), nieuwecode.split("*") , [lijst[0], lijst[2]])

def main(argv, naam):
    global naam_file
    naam_file = str(naam)
    for i in range(0, len(argv), 4):

        #p = multiprocessing.Process(target=score_check_over_seq, args=(argv[i:i+4],))
        #procs1.append(p)
        score_check_over_seq(argv[i:i+4])
        #print knip_index
        #knip_functie(knip_index, [[i[1],i[3]]])
    #map(lambda x: x.start(), procs1)
    #map(lambda x: x.join(), procs1)

def showUsageInformation():
	print
	print "Skeleton Script Python is the base for making new scripts in Python."
	print "The user has to type here what the Python script can perform and does."
	print
	print "Way of usage:"
	print
	print "The user has to type here how he has to work with the Python script."
	print
	print "Example:"
	print
	print "python SkeletonScriptPython.py"
	print
	sys.exit()

def H_main(argv):


	if len(argv) >= 2:
		if argv[1] == "-h" or argv[1] == "--h" or argv[1] == "-help" or argv[1] == "--help":
			showUsageInformation()


	main(argv[1:-1], argv[-1])


if __name__ == "__main__":
    H_main(sys.argv)
