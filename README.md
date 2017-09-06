# ModelNet40 Fixer

## About
This application was developed because the [Princeton ModelNet40 Dataset](http://modelnet.cs.princeton.edu/) has a bug in some classes files, where the _OFF_ header has no blank spaces (nor line breaking) with the number of vertices parameter.

## How to use
Simply run `bash run.sh` to edit all the files of the dataset. The parameters **DS_PATH** and **FIXER_PATH** must be provided without '/' as the last character. Also, **FIXER_PATH** must be the absolute path to the fixer. 
