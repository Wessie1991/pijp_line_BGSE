#!/bin/bash

# Additional information:
# =======================
#
# Remarks about the Skeleton Script Bash itself.
# Description how it works.
# Description which improvements can be done to improve the Skeleton Script Bash itself.
#ssh s1085775@145.97.16.229

# Show usage information:
if [ "$1" == "--h" ] || [ "$1" == "--help" ] || [ "$1" == "-h" ] || [ "$1" == "-help" ]
then
	echo "" 
	echo "Skeleton Script Bash is the base for making new scripts in Bash."
	echo "The user has to type here what the Bash script can perform and does."
	echo "" 
	echo "Way of usage:" 
	echo "" 
	echo "The user has to type here how he has to work with the Bash script."
	echo ""
	echo "Example:" 
	echo ""
	echo "/bin/bash SkeletonScriptBash.sh"
	echo ""
	
	exit
fi

echo $1
output1=${1::-4}"_voor_snippen_"
echo $2
output2=${2::-4}"_voor_snippen_"
echo $3 
#python multie_reading.py $1 $output1
#python multie_reading.py $2 $output2
#cat ${output1}* ${output2}* > output_voor_snippen_Inventarisatie_${3}
#rm ${output1}* ${output2}*
time bash Trimmer_pre.sh $1 $2



