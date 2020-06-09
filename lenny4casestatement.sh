#!/bin/bash

echo -n "Want Explosions? Press YES, No, Maybe, or mystery button????."

valid=0

while
[ $valid == 0 ]

do
	read ans
	case $ans in
	yes|YES|y|Y ) echo Big explosion BOOOOOOM
		      echo BAAAAAAAAAAAAAAAAAAAAM
		      valid=1
		      ;;
	no|No|n|N   ) echo .........nothing
		      echo No explosion
		      valid=1
		      ;;
	maybe|MAYBE ) echo MOOOOOOOOOOO
		      valid=1
		      ;;
	?	    ) echo MEOW..............
		      valid=1
		      ;;
	*	    ) echo Yes or No of some form please ;;
	esac
done

