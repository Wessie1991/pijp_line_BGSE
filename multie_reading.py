__author__ = 'des'
import multiprocessing
import time
import datetime
import os
import re
import sys

def inportfile(Naam):
    with open(Naam) as f:
        content = f.readlines()
    return content

def Read_Class_Maker(naam):
    index = 0
    setseqLijst = []
    fille = inportfile(naam)
    for i in range(0, len(fille), 4):
        #self.Read_lijst.append(Read(self.fille[i:i+4], index))
        setseqLijst.append(fille[i:i+4][1][:-2])
        index +=1
    print "alle seq zijn ingeladen "
    print datetime.datetime.now()
    del fille
    return tuple(setseqLijst)

def MaxLen(seqLijst):
    print 'Starting: maxlen'
    maxlen = len(max(seqLijst, key=len))
    print maxlen
    file = open(lijs + "Inventarisatie_Test.txt" , "a")
    file.write("max lengte reads: " + str(maxlen) + "\n")
    file.close()
    del file, maxlen
    print 'Exiting : maxlen'

def MinLen(seqLijst):
    print 'Starting: minlen'
    minlen = len(min(seqLijst, key=len))
    print minlen
    file = open(lijs + "Inventarisatie_Test.txt" , "a")
    file.write("korste lengte reads: " + str(minlen) + "\n")
    file.close()
    del file, minlen
    print 'Exiting : minlen'

def AantalReads(seqLijst):
    print 'Starting: aantalreads'
    aantalreads = len(seqLijst)
    file = open(lijs + "Inventarisatie_Test.txt" , "a")
    file.write("Aantalreads: " + str(aantalreads) + "\n")
    file.close()
    del aantalreads, file
    print 'Exiting : aantalreads'

def GemLen(seqLijst):
    print 'Starting: Gemlen'
    ff = [len(i) for i in seqLijst]
    gemlen = sum(ff)
    file = open(lijs +  "Inventarisatie_Test.txt" , "a")
    file.write("gemiddelde lengte : " + str((gemlen)/len(ff)) + "\n")
    file.close()
    del gemlen, file, ff
    print 'Exiting : Gemlen'

def gcGlobaal(seqlijst):
    print 'Starting: GC Globaal'
    gcglob = [float(len(re.findall("G|C", i))) / float(len(i))* 100.0 for i in seqlijst]
    file = open(lijs + "Inventarisatie_Test.txt" , "a")
    file.write("Globale gc content: " + str(sum(gcglob)/len(gcglob)) + "\n")
    file.close()
    del file
    del gcglob
    print 'Exiting : GC Globaal'


def getGcPositie(seqLijst):
    index = 0
    file = open(lijs + "Inventarisatie_Test.txt" , "a")
    print 'Starting: GC perpositie'
    for i in map(None, *seqLijst):
        leng = float(len(filter(None, i)))
        even = len(re.findall("G|C","".join(filter(None, i)) )) / leng
        file.write("positie: " + str(index) + " heeft een GC content van: " + str(even) + "\n")
        del leng
        del even
        index = index +1
    file.close()
    del index
    del file
    print 'Exiting : GC perpositie'



def multie(seqLijst):
    procs1 = []
    procs2 = []
    procs2.append(multiprocessing.Process(target=MaxLen, args=(seqLijst, )))
    procs2.append(multiprocessing.Process(target=MinLen, args=(seqLijst, )))
    procs1.append(multiprocessing.Process(target=AantalReads, args=(seqLijst, )))
    procs2.append(multiprocessing.Process(target=GemLen, args=(seqLijst, )))
    procs1.append(multiprocessing.Process(target=gcGlobaal, args=(seqLijst, )))


    map(lambda x: x.start(), procs2)
    map(lambda x: x.join(), procs2)
    #map(lambda x: x.shutdown(), procs2)
    map(lambda x: x.start(), procs1)
    map(lambda x: x.join(), procs1)
    #map(lambda x: x.shutdown(), procs1)
    del  procs1, procs2

    getGcPositie(seqLijst)



def main(argv):
    global lijs
    lijs= argv[2]
    try:
        os.remove(lijs + "Inventarisatie_Test.txt")
    except:
        pass
    print lijs
    file = open(lijs + "Inventarisatie_Test.txt" , "a")
    file.write("________________" + argv[1] + "________________\n")
    file.close()
    seqLijst = Read_Class_Maker(argv[1])
    multie(tuple(seqLijst))

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
			
	helloToUser = "Hello World!"

	print "wat krijg ik nou " + str(argv)
	main(argv)


if __name__ == "__main__":
    H_main(sys.argv)
