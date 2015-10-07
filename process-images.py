#!/usr/bin/env python

""" A script to optimize images:
    - Takes two arguments, indir and outdir
    - Renames input images to filenames as EXIF's DateTimeOriginal
      tag converted to unix timestamp (seconds since 1/1/1970. This
      allows a flat directory of images to be easily listed out by 
      actual date image was taken without complex sorting down the pipeline.
    - Resizes images to specified height or width, preserving aspect ratio.
"""

from __future__ import print_function

import datetime
import glob
import logging.config
import os
import shutil
import sys
import time

import exifread 
from PIL import Image

"""
logging_config = dict(
    version = 1,
    formatters = {
        'f': {'format':
              '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'}
        },
    handlers = {
        'h': {'class': 'logging.StreamHandler',
              'formatter': 'f',
              'level': logging.DEBUG}
        },
    loggers = {
        'root': {'handlers': ['h'],
                 'level': logging.DEBUG}
        }
)

logging.config.dictConfig(logging_config)

logger = logging.getLogger()
logger.log("hello", 50)
"""


def error(msg):
    """ Prints error to stderr, exiting with 1 code. """
    print(msg, file=sys.stderr)
    sys.exit(1)

def get_args():
    """ Gets the scripts arguments as a tuple """
    args = sys.argv[1:]
    try:
        indir = os.path.realpath(os.path.normpath(args[0]))
    except IndexError:
        error("Must supply at least an input directory with images")

    if not os.path.exists(indir):
        error("The input directory, %s does not exist." % indir)

    try:
        outdir = os.path.realpath(args[1])
    except IndexError:
        error("Must supply an output directory")

    if not os.path.exists(outdir):
        error("The output directory, %s does not exist." % outdir)
    return indir, outdir

def get_new_image_name_translations(indir, outdir):
    """ Renames input images using timestamp of
        EXIF's DateTimeOriginal tag. """
    origpaths = glob.glob("%s/*.[jJ][pP][gG]" % indir)
    d = {}
    for p in origpaths:
        try:
            f = open(p)
            exif = exifread.process_file(f)
        except:
            raise
        finally:
            f.close()
        try:
            orientation = str(exif["Image Orientation"])
        except KeyError:
            orientation = None
        try:
            origtime = str(exif["EXIF DateTimeOriginal"])
            time_extracted = True
        except KeyError:
            time_extracted = False
        if time_extracted:
            ts = int(time.mktime(datetime.datetime.strptime(origtime, "%Y:%m:%d %H:%M:%S").timetuple()))
        else:
            ts = int(time.time())
        newpath = os.path.join(outdir, str(ts) + ".jpg")
        d[p] = {"newpath": newpath, "orientation": orientation }
    return d

def copy_images_to_out(new_image_names):
    """ Copies original images to outdir with
        new names. """
    for oldpath in new_image_names:
        image_info = new_image_names[oldpath]
        newpath = image_info["newpath"]
        shutil.copyfile(oldpath, newpath)

def main():
    """ Runs the program. """
    indir, outdir = get_args()
    image_name_translations = get_new_image_name_translations(indir, outdir)
    copy_images_to_out(image_name_translations)
    optimize(image_name_translations.values())
    
def optimize(img_dicts):
    for img_dict in img_dicts:
        newpath = img_dict["newpath"]
        im = Image.open(newpath)
        final_im = im
        orientation = img_dict["orientation"]
        #print(img_dict)
        #print(img_dict["newpath"])
        if orientation == "Rotated 90 CW":
            #print("ROTATING -90!")
            final_im = final_im.rotate(-90)
        if orientation == "Rotated 90 CCW":
            final_im = final_im.rotate(-90)
        #print("\n")
        final_im.thumbnail((640, 480))
        final_im.save(newpath)
main()
