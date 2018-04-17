# PythonToolBox
Python files that are useful for my personal projects such as image annotation, file renaming, etc.

### annotate2move

Easy to use, semi-GUI program which annotates the names of images so it is easier to rename, relabel, etc.
You need a file named 'filenames.txt' which includes the name of all the images that you want to annotate:

```sh
$ python annotate2move.py
```

### rename.py
Program that renames JPEG files into either one of the three suffixes for each state in the [caffe-cupstate] repository.
```sh
$ python rename.py DIRNAME STATE
# Where DIRNAME = name of the directory and STATE = 'liquid', 'empty' or 'unknown'
```

### resize.py

Program to resize a bunch of images into a specifiec height and width.
```sh
$ python resize.py DIRECTORYNAME HEIGHT WIDTH
# Where DIRECTORYNAME = name of the directory and HEIGHT, WIDTH are the targeted dimensions for the new images.
```
