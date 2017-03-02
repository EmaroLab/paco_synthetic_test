
#!/bin/bash

python ./generate_problems.py -d 1 -o 3 10 -r 4 -a
python ./generate_problems.py -d 1 -o 7 10 -r 4 -a
python ./generate_problems.py -d 1 -o 10 10 -r 4 -a
python ./generate_problems.py -d 1 -o 3 10 -r 8 -a
python ./generate_problems.py -d 1 -o 7 10 -r 8 -a
python ./generate_problems.py -d 1 -o 10 10 -r 8 -a
python ./generate_plans.py -a