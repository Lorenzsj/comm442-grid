#!/bin/bash
# Script for converting DOS text file format to UNIX
# Simplifies use of shared folders on a Debian VM
# Replace /media/sf_grid/* with /your/src/*
SRC = "/media/sf_grid/*"
DES = "/home/stevie/perl5/lib/perl5/"

cp -r $SRC .
echo "Grabbed"
find . -type f -print0 | xargs -0 -n 1 -P 4 dos2unix
echo "Converted"
chmod 0755 *.cgi && chmod 0755 Grid/*.pm
echo "Permissed"
cp -r Grid $DES
echo "Sent"
