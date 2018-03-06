#!/bin/bash
shuf -n 32 cookbook.txt | tr '\n' ' ' > cookbook.out
