# BaiduMap tiles

## Getting Started

### 下载地图瓦片数据

更改 `download_tiles.py` 文件中的区域(lat_和lon_)和缩放(zoom).

```py
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
