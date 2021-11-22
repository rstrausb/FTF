#!/bin/bash

codeSourceDirectory='/home/strausbaugh/DWF/Code/fastTransientFinder'

#dataSourceDirectory='/home/strausbaugh/DWF/Data/fourhour2/files'
dataSourceDirectory=$1

#now="$(date +'%s')"

#dataWorkDirectory="$dataSourceDirectory/work_$now"

dataWorkDirectory="$dataSourceDirectory../newWork"

if [ -d $dataWorkDirectory ]
then
	echo "$dataWorkDirectory already exists"
else
	mkdir $dataWorkDirectory
fi

cd $dataWorkDirectory

#sw=5
#ip=2

sw=$2
ip=$3

if [ -f "$dataWorkDirectory/allResults.npy" ]
then
	echo "Data already analyzed"
else
	echo "Running full analysis"
	python $codeSourceDirectory/fullAnalAllFiles.py $dataSourceDirectory $dataWorkDirectory $sw $ip
fi


for i in $( eval echo {0..$ip} )
do
	if [ -f "$dataWorkDirectory/PossibleTransients_sw${sw}_ip${i}.txt" ]
	then
		echo "Found separated data"
		if [ -d "$dataWorkDirectory/PossibleTransients_sw${sw}_ip${i}" ]
		then
			echo "Already plotted possible transients for this window size and inflection count $i"
		else
			echo "Separating data by inflection points"
			mkdir PossibleTransients_sw${sw}_ip$i
#	mkdir PossibleTransients_${sw}_1_${sigma}
#	mkdir PossibleTransients_${sw}_2_${sigma}
#	mkdir PossibleTransients_${sw}_3_${sigma}
			python $codeSourceDirectory/plotPossibleTransientAndOtherNights_multiprocessing.py None PossibleTransients_sw${sw}_ip$i $dataSourceDirectory $sw $i
		fi
	else
                echo "Separating data by inflection points"
		python $codeSourceDirectory/separateData2.py $dataWorkDirectory/allResults.npy $dataWorkDirectory $sw $i
                if [ -d "$dataWorkDirectory/PossibleTransients_sw${sw}_ip${i}" ]
                then
                        echo "Already plotted possible transients for this window size and inflection count $i"
                else
                        mkdir PossibleTransients_sw${sw}_ip$i
                        echo "Separating data by inflection points"
			python $codeSourceDirectory/plotPossibleTransientAndOtherNights_multiprocessing.py None PossibleTransients_sw${sw}_ip$i $dataSourceDirectory $sw $i
		fi
	fi		
done
#if [ -d "$dataWorkDirectory/PossibleTransients_${sw}_1_${sigma}" ]
#then
#        echo "Already plotted possible transients for this window size and inflection count 1"
#else
#	mkdir PossibleTransients_${sw}_1_${sigma}
#        python $codeSourceDirectory/plotPossibleTransientAndOtherNights_multiprocessing.py None PossibleTransients_${sw}_1_$sigma $dataSourceDirectory $sw 1 $sigma
#fi
#if [ -d "$dataWorkDirectory/PossibleTransients_${sw}_2_${sigma}" ]
#then
#        echo "Already plotted possible transients for this window size and inflection count 2"
#else
#	mkdir PossibleTransients_${sw}_2_${sigma}
#        python $codeSourceDirectory/plotPossibleTransientAndOtherNights_multiprocessing.py None PossibleTransients_${sw}_2_$sigma $dataSourceDirectory $sw 2 $sigma
#fi
#if [ -d "$dataWorkDirectory/PossibleTransients_${sw}_3_${sigma}" ]
#then
#        echo "Already plotted possible transients for this window size and inflection count 3"
#else
#        mkdir PossibleTransients_${sw}_3_${sigma}
#        python $codeSourceDirectory/plotPossibleTransientAndOtherNights_multiprocessing.py None PossibleTransients_${sw}_3_$sigma $dataSourceDirectory $sw 3 $sigma
#
#fi

echo "Finished"
