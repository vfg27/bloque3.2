#Marta Morán, Miguel Varas y Victor Fresno
import sys
import os
import json
import time
from subprocess import call
os.chdir("/root/bloque3/bookinfo/src/reviews")
call(["pwd"])
#call(["cd Ratings/practica_creativa2/bookinfo/src/reviews/reviews-wlpcfg"], shell=True)
call(["docker run --rm -u root -v "+r'"'+"$(pwd)"+r'"'+":/home/gradle/project -w /home/gradle/project gradle:4.8.1 gradle clean build"], shell=True)
os.chdir("/root")
call(["pwd"])
#call(["cd"], shell=True)
os.chdir("/root/bloque3")
call(["pwd"])
#call(["cd bloque3"], shell=True)
call(["docker-compose up"], shell=True)
