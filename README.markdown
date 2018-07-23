# BaiduMap tiles

## Getting Started

### 下载地图瓦片数据

更改 `download_tiles.py` 文件中的区域(lat_和lon_)和缩放(zoom).

```py
zoom = 8

lat_start, lon_start = 31.717714,105.540665
lat_stop, lon_stop = 39.659668,111.262224

satellite = True    # 是否下载卫星图/街道

download_tiles(zoom, lat_start, lat_stop, lon_start, lon_stop, satellite)
```

坐标点获取： [http://api.map.baidu.com/lbsapi/getpoint/](http://api.map.baidu.com/lbsapi/getpoint/).

编辑完毕(安装python3)运行cmd `$ python download_tiles.py` 运行过后图片在 `tile` 文件夹.

### 合并地图瓦片(ps.我看代码中只是合并的街道和卫星图,貌似与普通地图无关)

Edit `merge_tiles.py` to specify the area and the zoom level you want, it's just the same as before.

    zoom = 19
 
    lat_start, lon_start = 31.022547,121.429391
    lat_stop, lon_stop = 31.041453,121.45749

    satellite = True    # roads if false

Then, run `$ python merge_tiles.py` and get `map_s.jpg` for satellite or `map_r.png` for roads.


Note: merging the tiles requires [Python Image Library](http://www.pythonware.com/products/pil/).

## 参考

- <http://api.map.baidu.com/lbsapi/getpoint/>
- <http://developer.baidu.com/map/jsdemo.htm#a1_2>
- <http://developer.baidu.com/map/reference/index.php>
- <http://lbsyun.baidu.com/index.php?title=jspopular>
