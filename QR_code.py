from MyQR import myqr

# 制作普通二维码
Ord_QR = myqr.run(
    words='https://www.v2ex.com/',
    save_name='Ord_QR.jpg',
    save_dir='images',
    )


# 制作带图片的艺术二维码
Art_QR = myqr.run(
    words='https://www.bilibili.com/',
    picture='images/ye.jpg',
    colorized=True,  # 为False时输出为黑白二维码，为true时输出彩色二维码
    save_dir='images',
    save_name='Art_QR.png',
)


# 制作动态二维码
Dyn_QR = myqr.run(
    words='https://www.bilibili.com/bangumi/media/md425/?from=search&seid=10074084918593934101',
    picture='images/paojie.gif',
    colorized=True,  # 为False时输出为黑白二维码，为true时输出彩色二维码
    version=1,
    level='H',
    contrast=1.0,
    brightness=1.0,
    save_dir='images',
    save_name='Dyn_QR.gif',
)

print(Ord_QR, Art_QR, Dyn_QR)