import os
from MyQR import myqr
# 制作动态二维码
myqr.run(
    words='https://www.bilibili.com/bangumi/media/md425/?from=search&seid=10074084918593934101',
    picture='images/paojie.gif',
    colorized=True,  # 为False时输出为黑白二维码，为true时输出彩色二维码
    version=1,                              # 设置容错率为最高
    level='H',                              # 控制纠错水平，范围是L、M、Q、H，从左到右依次升高
    contrast=1.0,                           # 用以调节图片的对比度，1.0 表示原始图片，更小的值表示更低对比度，更大反之。默认为1.0
    brightness=1.0,                         # 用来调节图片的亮度，其余用法和取值同上
    save_dir='images',                 # 控制位置
    save_name='Dyn_QR.gif',
)