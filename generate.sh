#!/bin/bash
python generate.py --num-start 0 --num-end 163
python generate.py --num-start 0 --num-end 163 --prompt-type few_shot
python generate.py --num-start 0 --num-end 163 --prompt-type refined