from MyQR import  myqr
# 制作带图片的艺术二维码
myqr.run(
    words='https://www.bilibili.com/',
    picture='images/ye.jpg',
    colorized=True,  # 为False时输出为黑白二维码，为true时输出彩色二维码
    save_name='ArtQR.png',
    save_dir='images',
)

