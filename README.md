# INTRODUCTION #

The main goal of this tool is to crop sub-pictures from parent pictures. This
tool also allows format-converting from a corp-list-file to a YAML file.


# INSTALL #

1. Download the compressed binary package file (e.g.,
   `PicCrop-v1.0-bin-20160119.zip`) from the
   [Download](https://bitbucket.org/YorkJong/pypiccrop/downloads) page.
2. Uncompress the package


# QUICK START #

1. Copy source (parent) pictures to the `screen` folder
2. Edit `crop.lst`
3. Run `rect.bat` to draw rectangles listing in `crop.lst`.
4. Run `crop.bat` to crop sub-pictures from source pictures.
5. Run `yaml.bat` to convert the crop-list-file (i.e., `crop.lst`) to the
   YAML file (i.e., `layout_coord.yaml`)

## Note ##
* Batch files `rect.bat`, `crop.bat`, and `yaml.bat` can be run in any order.
* Result pictures of `rect.bat` are put into `out` folder.
* Generated sub-pictures are put into `out` folder.

## Crop List File ##

A `crop.lst` looks like follows:
```
parent1.png
 0,  0, 50, 50, crop1-1.png
50, 50, 12, 34, crop1-2.png

parent2.png
 0,  1, 30, 40, crop2-1.png
90, 50, 33, 44, crop2-2.png
50, 50, 33, 22, crop2-3.png

# source file
#------------
ipod-touch-5th-black.png

# x,   y,   w,  h, target file
#------------------------------------
117, 139, 62, 62, ico_FaceTime.png
190, 139, 62, 62, ico_Calendar.png
263, 139, 62, 62, ico_Photos.png
336, 139, 62, 62, ico_Camera.png
```
* Symbol `#` is the comment prefix.
* A source file follows multiple target files
* Each target begins with an x-coordinate, a y-coordinate, a width, and a height.


# COMMAND LINE #
## Top level ##
```
usage: crop.exe [-h] [-v] {crop,yaml} ...

positional arguments:
  {crop,rect,yaml}  commands
    crop            Crop out pictures according to a crop-list file.
    rect            Mark out rectangles from a crop-list file.
    yaml            Generate a YAML file of screens with coordinate layouts.

optional arguments:
  -h, --help     show this help message and exit
  -v, --version  show program's version number and exit
```

## crop command ##
```
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
```

## rect command ##
```
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
```

## yaml command ##
```
usage: crop.exe yaml [-h] [-o <file>] crop-list-file

positional arguments:
  crop-list-file        The crop list file.

optional arguments:
  -h, --help            show this help message and exit
  -o <file>, --output <file>
                        place the output into <file>, the YAML file (default
                        "layout_coord.yaml").
```