import datetime
from itertools import izip_longest
import os
import sys

from flask import Flask, render_template, request
from iptcinfo import IPTCInfo

app = Flask(__name__)
THIS_DIR = os.path.dirname(os.path.realpath(__file__))

def grouper(n, iterable, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    # grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx
    args = [iter(iterable)] * n
    return izip_longest(fillvalue=fillvalue, *args)

def get_imagegroups():
    """ Returns a tuple of tuples representing 
    groups of 10 image paths (each group is a page)"""
    os.chdir(os.path.join(THIS_DIR, "static", "images", "opt"))
    sorted_image_paths = sorted(filter(os.path.isfile, os.listdir('.')), reverse=True)
    os.chdir(THIS_DIR)
    groups =  tuple(grouper(10, sorted_image_paths))
    f = []
    for group in groups:
        l = []
        for name in group:
            if name:
                    path = "static/images/opt/%s" % name
                    d = {}
		    info = IPTCInfo(path, force=True) 
		    caption = info.data['caption/abstract'] or ""
                    date = datetime.datetime.fromtimestamp(int(name.replace(".jpg", ""))).strftime('%Y-%m-%d %H:%M:%S')
                    d[path] = {"date": date, "caption": caption}
                    l.append(d)
        f.append(l)
    return f

def get_pager_data(this_page, num_pages):
    page_list = [ i+1 for i in range(num_pages)]
    pages = []
    for p in page_list:
        p_dict = {}
        cur = False
        if p == this_page:
            cur = True
        p_dict["current"] = cur 
        p_dict["next"] = False
        pages.append(p_dict)

    for i, p in enumerate(pages):
        if p["current"]:
            try:
                pages[i+1]["next"] = True
            except IndexError:
                pass
    return pages


@app.route('/')
def index():
    try:
        page = int(request.args.get("page")) or 1
    except:
        page = 1
    imagegroups = get_imagegroups()
    num_pages = len(imagegroups)
    try:
        images_for_this_page = imagegroups[page-1]
    except IndexError:
        images_for_this_page = imagegroups[0]

    pager_data = get_pager_data(page, num_pages)
    return render_template("template.html", 
        title="foo",
	page=page,
        images=images_for_this_page,
        pager=pager_data
    )

if __name__ == "__main__":
    # For local testing...
    # $ python ias.py
    # $ python ias.py host port
    args =  tuple(sys.argv[1:])
    try:
        host, port = args
    except ValueError:
        if len(args) == 0:
            host = None
            port = None
        else:
            host = args[0]
            port = None

    app.run(host=host, port=int(port))
