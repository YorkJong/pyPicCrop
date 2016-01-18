# Introduction #

The main goal of this tool is to crop sub-pictures from parent pictures. This
tool also allows format-converting from a corp-list-file to a YAML file.


# Install #

1. Download the compressed binary package file (e.g.,
   `PicCrop-v1.0-bin-20160118.zip`) from the
   [Download](https://bitbucket.org/YorkJong/pypiccrop/downloads) page.
2. Uncompress the package


# Quick Start #

1. Copy source (parent) pictures to the `screen` folder
2. Edit `crop.lst`
3. Run `rect.bat` to draw rectangles listing in `crop.lst`.
 * The result pictues is put into `out` folder.
4. Run `crop.bat` to crop sub-pictures from source pictures.
 * The sub-pictures is put into `out` folder.
5. Run `yaml.bat` to convert the crop-list-file (i.e., `crop.lst`) to the
   YAML file (i.e., `layout_coord.yaml`)

NOTE: You can run `rect.bat`, `crop.bat`, and `yaml.bat` in any order.

A `crop.lst` looks like follows:
```
# source file
#------------
ipod-touch-5th-black.png

# x,   y,   w,  h, target file
#------------------------------------
117, 139, 62, 62, ico_FaceTime.png
190, 139, 62, 62, ico_Calendar.png
263, 139, 62, 62, ico_Photos.png
336, 139, 62, 62, ico_Camera.png
117, 223, 62, 62, ico_Weather.png
190, 223, 62, 62, ico_Clock.png
263, 223, 62, 62, ico_Maps.png
```

* Symbol `#` is the comment prefix.
* A source file following multiple target files
* Each target begens with a x-coordinate, a y-coordinate, width, and height.


# Command Line #
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
