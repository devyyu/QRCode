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
在Py_to_QR项目目录下建立images文件夹、QR_code.py;
* images文件夹存放需要的图片和生成的二维码;
* QR-code.py文件生成普通的二维码、带图片的二维码和动态的二维码。
* 其中所需要的静态图片和动态图片可以在网上下载。
### 2 生成普通二维码
只需输入两行代码即可创建一个普通的二维码：
~~~python
from MyQR import myqr
myqr.run(words='文字或链接', save_name='Ord_QR.jpg', save_dir='images')
~~~
赶快拿起手机扫一扫，看看是否有效吧。
### 3 生成带图片的二维码
普通的二维码太单调了，可给run方法传递更多的参数，制作更多好看的二维码。
~~~python
# 制作带图片的艺术二维码
from MyQR import myqr
Art_QR = myqr.run(
    words='https://www.bilibili.com/',
    picture='images/ye.jpg', # 传入图片路径
    colorized=True,  # 为False时输出为黑白二维码，为true时输出彩色二维码
    save_dir='images',     # 二维码文件保存路径
    save_name='Art_QR.png',  # 输出二维码文件名字
)
print(Art_QR)
~~~
### 4 生成动态二维码
生成动态二维码的过程和第3个一样，只需要将传入的图片换成gif格式的图片，将生成文件
改为gif格式的文件即可。
代码如下：
~~~python
# 制作动态二维码
from MyQR import myqr
Dyn_QR = myqr.run(
    words='https://www.bilibili.com/bangumi/media/md425/?from=search&seid=10074084918593934101',
    picture='images/paojie.gif',
    colorized=True,  
    save_dir='images',
    save_name='Dyn_QR.gif',
)
~~~
### 5 myqr.run()函数参数的解析
![参数解析](https://devbit.oss-cn-beijing.aliyuncs.com/img/20190303210748.png)
可以根据上述参数，对以上三种二维码的大小、颜色、对比度、亮度进行自定义操作。