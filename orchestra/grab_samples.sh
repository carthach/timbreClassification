#!/bin/bash

sourcePath="/Users/carthach/tmp/all-samples/"
#destPath="/Users/carthach/Google Drive/Code/experiments/classification/samples/"
destPath="/Users/carthach/tmp/selection3"

#Percussion
python random_samples.py "$sourcePath/percussion" "$destPath/percussion/percussion" 200

#Strings
python random_samples.py "$sourcePath/violin" "$destPath/strings/violin" 50
python random_samples.py "$sourcePath/viola" "$destPath/strings/viola" 50
python random_samples.py "$sourcePath/cello" "$destPath/strings/cello" 50
python random_samples.py "$sourcePath/double bass" "$destPath/strings/double_bass" 50

#Woodwind
python random_samples.py "$sourcePath/flute" "$destPath/woodwind/flute" 50
python random_samples.py "$sourcePath/clarinet" "$destPath/woodwind/clarinet" 50
python random_samples.py "$sourcePath/oboe" "$destPath/woodwind/oboe" 50
python random_samples.py "$sourcePath/bassoon" "$destPath/woodwind/bassoon" 50

#Brass
python random_samples.py "$sourcePath/trumpet" "$destPath/brass/trumpet" 50
python random_samples.py "$sourcePath/french horn" "$destPath/brass/french_horn" 50
python random_samples.py "$sourcePath/trombone" "$destPath/brass/trombone" 50
python random_samples.py "$sourcePath/tuba" "$destPath/brass/tuba" 50

