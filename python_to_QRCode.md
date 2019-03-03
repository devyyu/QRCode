## Python生成二维码
### 介绍
这里是调用MyQR库接口生成普通的二维码、带图片的二维码和动态的二维码，并且可以设置二维码的尺寸、亮度、
对比度、颜色、输出文件名、存储位置以及纠错登记。
### 1 准备
#### 1.1 创建项目
 打开pycharm使用本地Python环境或者另创建一个虚拟环境，然后建立Py_to_QR项目。
#### 1.2 安装MyQR
打开终端输入下面的命令即可安装MyQR
~~~python
pip install MyQR       # 在windows里
sudo pip3 install MyQR     # 在Ubuntu里
~~~
#### 1.3 项目目录结构
在Py_to_QR项目目录下建立images文件夹、Ordinary_QR.py、Art_QR.py、Dynamic_QR.py;
images文件夹存放需要的图片和生成的二维码，其他Python文件分别是生成普通的二维码、带图片
的二维码和动态的二维码的代码文件。其中所需要的静态图片和动态图片可以在网上下载。
### 2 生成普通二维码
只需在Ordinary_QR.py文件里两行输入代码即可创建一个普通的二维码：
~~~python
from MyQR import myqr
myqr.run(words='文字或链接', save_name='Ord_QR.png', save_dir='images')
~~~
### 3 生成带图片的二维码
### 4 生成动态二维码