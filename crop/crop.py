# -*- coding: utf-8 -*-
"""
This main goal of this tool is to crop sub-pictures from screen pictures. This
tool also allows format-converting from a corp-list-file to a YAML file.
"""
__software__ = "Picture Crop"
__version__ = "1.0"
__author__ = "Jiang Yu-Kuan <yukuan.jiang@gmail.com>"
__date__ = "2015/04/17 (initial version); 2015/04/24 (last revision)"

import re
import sys
import os
import argparse

from collections import defaultdict

import Image, ImageDraw
from myutil import prefix_info, main_basename, read_unicode, save_utf8_file


#------------------------------------------------------------------------------

def prefix_authorship(lines, comment_mark='//'):
    """Prefix authorship infomation to the given lines
    with given comment-mark.
    """
    return prefix_info(lines,
                       __software__, __version__, __author__,
                       comment_mark)


def is_numeric(str):
    try:
        offset = int(eval(str))
    except:
        return False
    return True


#------------------------------------------------------------------------------

def read_list(fn='crop.lst'):
    """Read a crop list file.
    """
    def check_row(row):
        if len(row) != 1 and len(row) != 5:
            msg = 'Line {}: number of arguments must be 1 or 5'.format(line_no)
            print >> sys.stderr, msg
        for x in row[:-1]:
            if not is_numeric(x):
                msg = 'Line {}: "{}" is not a number'.format(line_no, x)
                print >> sys.stderr, msg

    lines = read_unicode(fn).splitlines()
    pat = re.compile('\s*,\s*')
    ret = []
    key = None

    for line_no, line in enumerate(lines):
        l = line.split("#", 1)[0].strip()
        if len(l) == 0:
            continue
        row = pat.split(l)
        check_row(row)
        if len(row) == 1:
            if key and val:
                ret += [(key, val)]
            key = row[0]
            val = []
        elif len(row) == 5:
            row = tuple(eval(x) if is_numeric(x) else x for x in row)
            val += [row]
    ret += [(key, val)]
    return ret


def crop_pics_from_screens(crop_lst, src_dir='screen', out_dir='out'):
    """Crop pictures from screens descripted in a cropping list.

    Arguments
    ---------
    crop_lst
        a list of (screen, cropping list) pairs
    src_dir
        source directory that stores the source screen pictures
    out_dir
        output directory to store the cropped pictures
    """
    for screen_fn, crops in crop_lst:
        screen = Image.open('{}/{}'.format(src_dir, screen_fn))
        for x, y, w, h, fn in crops:
            im = screen.crop((x, y, x+w, y+h))
            im.save('{}/{}'.format(out_dir, fn))


def draw_rects_on_screens(crop_lst, src_dir='screen', out_dir='out',
                          color='red'):
    """Draw rectangles on screens descripted in a cropping list.

    Arguments
    ---------
    crop_lst
        a list of (screen, cropping list) pairs
    src_dir
        source directory that stores the source screen pictures
    out_dir
        output directory to store the target screen pictures
    """
    d = defaultdict(int)
    for screen_fn, crops in crop_lst:
        screen = Image.open('{}/{}'.format(src_dir, screen_fn))
        draw = ImageDraw.Draw(screen)
        for x, y, w, h, fn in crops:
            draw.rectangle((x, y, x+w, y+h), outline='red')

        d[screen_fn] += 1
        fn = '{}/{}_{}.png'.format(out_dir, screen_fn, d[screen_fn])
        screen.save(fn)


def lst_to_yaml(crop_lst, out_fn='layout_coord.yaml'):
    """Generate a YAML file with coordinate layout.

    Arguments
    ---------
    crop_lst
        a list of (screen, cropping list) pairs
    out_fn
        filename of the YAML file
    """
    lines = []
    for screen_fn, crops in crop_lst:
        name = main_basename(screen_fn)
        lines += ['---']
        lines += ['name: {}'.format(name)]
        lines += ['layout: {kind: coordinate}']
        lines += ['align: left']
        lines += ['parts:']
        for x, y, w, h, fn in crops:
            lines += ['  - {{image: {}, coord: [{}, {}]}}'.format(fn, x, y)]
    lines += ['...']

    lines = prefix_authorship(lines, '#')
    save_utf8_file(out_fn, lines)


#------------------------------------------------------------------------------

def parse_args(args):
    def do_crop(args):
        crop_pics_from_screens(args.crop_lst, args.screen_dir, args.out_dir)

    def do_rect(args):
        draw_rects_on_screens(args.crop_lst, args.screen_dir, args.out_dir)

    def do_yaml(args):
        lst_to_yaml(args.crop_lst, args.outfile)

    def check_dir(name):
        """Check if the given directory is existing.
        This function is for output directory only.
        """
        if not os.path.isdir(name):
            os.makedirs(name)
        return name

    # create top-level parser
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('-v', '--version', action='version',
                        version='%s v%s by %s' %
                        (__software__, __version__, __author__))
    subparsers = parser.add_subparsers(help='commands')

    #--------------------------------------------------------------------------

    # create the parent parser of src
    src = argparse.ArgumentParser(add_help=False)
    src.add_argument('crop_lst', metavar='crop-list-file',
        type=read_list,
        help='The crop list file.')

    # create the parser for the "crop" command
    sub = subparsers.add_parser('crop', parents=[src],
        help='Crop out pictures according to a crop-list file.')
    sub.set_defaults(func=do_crop,
        screen_dir='screen', out_dir='out')
    sub.add_argument('-s', '--screen_dir', metavar='<directory>',
        help='''assign a <directory> to read screen pictures.
            The default directory is "%s".
            ''' % sub.get_default('screen_dir'))
    sub.add_argument('-o', '--out_dir', metavar='<directory>',
        type=check_dir,
        help='''assign a <directory> to store output cropped pictures.
            The default directory is "%s".
            ''' % sub.get_default('out_dir'))

    # create the parser for the "rect" command
    sub = subparsers.add_parser('rect', parents=[src],
        help='Mark out rectangles from a crop-list file.')
    sub.set_defaults(func=do_rect,
        screen_dir='screen', out_dir='out')
    sub.add_argument('-s', '--screen_dir', metavar='<directory>',
        help='''assign a <directory> to read screen pictures.
            The default directory is "%s".
            ''' % sub.get_default('screen_dir'))
    sub.add_argument('-o', '--out_dir', metavar='<directory>',
        type=check_dir,
        help='''assign a <directory> to store output screen pictures.
            The default directory is "%s".
            ''' % sub.get_default('out_dir'))

    # create the parser for the "yaml" command
    sub = subparsers.add_parser('yaml', parents=[src],
        help='Generate a YAML file of screens with coordinate layouts.')
    sub.set_defaults(func=do_yaml,
        outfile='layout_coord.yaml')
    sub.add_argument('-o', '--output', metavar='<file>', dest='outfile',
        help='''place the output into <file>, the YAML file (default "%s").
            ''' % sub.get_default('outfile'))

    #--------------------------------------------------------------------------

    # parse args and execute functions
    args = parser.parse_args(args)
    args.func(args)


def main():
    """Start point of this module.
    """
    try:
        parse_args(sys.argv[1:])
    except IOError as err:
        print err
    except ValueError as err:
        print err


def test():
    lst = read_list('crop.lst')
    crop_pics_from_screens(lst)
    lst_to_yaml(lst)


if __name__ == '__main__':
    main()
    #parse_args(sys.argv[1:])
    #test()
