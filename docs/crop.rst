=======
PicCrop
=======
----------------
Picture Cropping
----------------

:Author: Jiang Yu-Kuan
:Contact: yukuan.jiang@gmail.com
:Revision: 0003
:Date: 2016-01-20

.. contents::


Introduction
============
PicCrop is an open source Python application to crop sub-pictures from parent
pictures. This tool also allows format-converting from a corp-list file to a
YAML layout file.

A crop-list file lists parent pictures and describes sub-pictures to crop.

A YAML layout file describes multiple picture layouts of screens. I invented
the syntax under the standard YAML and used to assemble separated sub- pictures
into whole-pictures.


Usage
=====
Top level
---------
usage: crop.exe [-h] [-v] {crop,yaml} ...

positional arguments:
  {crop,rect,yaml}  commands
    crop            Crop out pictures according to a crop-list file.
    rect            Mark out rectangles from a crop-list file.
    yaml            Generate a YAML file of screens with coordinate layouts.

optional arguments:
  -h, --help     show this help message and exit
  -v, --version  show program's version number and exit

crop command
------------
usage: crop.exe crop [-h] [-s <directory>] [-o <directory>] crop-list-file

positional arguments:
  crop-list-file        The crop list file.

optional arguments:
  -h, --help            show this help message and exit
  -s <directory>, --screen_dir <directory>
                        assign a <directory> to read screen pictures. The
                        default directory is "screen".
  -o <directory>, --out_dir <directory>
                        assign a <directory> to store output cropped
                        pictures. The default directory is "out".

rect command
------------
usage: crop.exe rect [-h] [-s <directory>] [-o <directory>] crop-list-file

positional arguments:
  crop-list-file        The crop list file.

optional arguments:
  -h, --help            show this help message and exit
  -s <directory>, --screen_dir <directory>
                        assign a <directory> to read screen pictures. The
                        default directory is "screen".
  -o <directory>, --out_dir <directory>
                        assign a <directory> to store output screen pictures.
                        The default directory is "out".

yaml command
------------
usage: crop.exe yaml [-h] [-o <file>] crop-list-file

positional arguments:
  crop-list-file        The crop list file.

optional arguments:
  -h, --help            show this help message and exit
  -o <file>, --output <file>
                        place the output into <file>, the YAML file (default
                        "layout_coord.yaml").

ToDo List
=========


Version History
===============
1.00
----
Released 2015-04-24
* Added crop command to crop out pictures from screen pictures.
* Added yaml command to generate a YAML file of screens with coordinate layouts.
* Added rect command to mark cropped extents on screen pictures

