#!/usr/bin/python
"""
    说明：
    1、akey若无法使用，请在gmap_utils.py文件中修改自己的akey

    2、本文件为下载的入口，其中函数download_tile、download_satellite里定义的的链接地址中的参数
    udt需要修改为最新版本的时间字符串，例如"20180628"，

    3、时间字符串获取方法：
    浏览器访问：http://api.map.baidu.com/api?v=2.0，获取到js中document.write中的script标签的src，
    再浏览器访问该src，获取返回的js脚本中全局变量TILE_VERSION对象中的'updateDate'属性即可，一般在第一行就能找到

    4、服务端替换离线瓦片资源时，不要忘记修改离线BaiduApi_2.0.js文件设置或者js中的window.__BMAP_EXTRA_CONFIG__
    中的各种Udt参数，要与图片的udt保持一致
"""
import urllib.request, urllib.error, urllib.parse
from threading import Thread
import os, sys
import math
from gmap_utils import *

import time
import random


def download_tiles(zoom, lat_start, lat_stop, lon_start, lon_stop, satellite=True):
    start_x, start_y = bd_latlng2xy(zoom, lat_start, lon_start)
    stop_x, stop_y = bd_latlng2xy(zoom, lat_stop, lon_stop)

    start_x = int(start_x // 256)
    start_y = int(start_y // 256)
    stop_x = int(stop_x // 256)
    stop_y = int(stop_y // 256)

    print("x range", start_x, stop_x)
    print("y range", start_y, stop_y)

    for x in range(start_x, stop_x):
        # download(x, y, zoom)
        FastThread(x, start_y, stop_y, zoom, satellite).start()


class FastThread(Thread):
    def __init__(self, x, start_y, stop_y, zoom, satellite):
        super(FastThread, self).__init__()
        self.x = x
        self.start_y = start_y
        self.stop_y = stop_y
        self.zoom = zoom
        self.satellite = satellite

    def run(self):
        for y in range(self.start_y, self.stop_y):
            if satellite:
                download_satellite(self.x, y, self.zoom)
                download_tile(self.x, y, self.zoom, True)
            else:
                download_tile(self.x, y, self.zoom)


def download_tile(x, y, zoom, satellite=False):
    url = None
    filename = None
    folder = "road/" if satellite else "tile/"
    scaler = "" if satellite else "&scaler=1"
    # styles is roadmap when downloading satellite
    styles = "sl" if satellite else "pl"

    query = "qt=tile&x=%d&y=%d&z=%d&styles=%s%s&udt=20180628" % (x, y, zoom, styles, scaler)  # 修改时间字符串(udt=后面的)
    url = "http://online0.map.bdimg.com/onlinelabel/?" + query
    filename = query + ".png"

    download_file(url, filename, folder)


def download_satellite(x, y, zoom):
    url = None
    filename = None
    folder = "it/"

    path = "u=x=%d;y=%d;z=%d;v=009;type=sate&fm=46&udt=20180628" % (x, y, zoom)  # 修改时间字符串(udt=后面的)
    url = "http://shangetu0.map.bdimg.com/it/" + path
    filename = path.replace(";", ",") + ".jpg"

    download_file(url, filename, folder)


def download_file(url, filename, folder=""):
    full_file_path = folder + filename
    if not os.path.exists(full_file_path):
        bytes = None
        try:
            req = urllib.request.Request(url, data=None)
            response = urllib.request.urlopen(req)
            bytes = response.read()
        except Exception as e:
            print("--", filename, "->", e)
            sys.exit(1)

        if bytes.startswith(b"<html>"):
            print("-- forbidden", filename)
            sys.exit(1)

        print("-- saving " + filename)

        f = open(full_file_path, 'wb')
        f.write(bytes)
        f.close()

        time.sleep(1 + random.random())
    else:
        print("-- existed " + filename)


if __name__ == "__main__":
    zoom = 11

    lat_start, lon_start = 36, 115  # 116.419791,36.871881
    lat_stop, lon_stop = 37.5, 119  # 117.04185,36.741968

    satellite = False  # 是否下载卫星图/街道

    download_tiles(zoom, lat_start, lat_stop, lon_start, lon_stop, satellite)
