import qrcode

img = qrcode.make("https://www.youtube.com/channel/UCdULNKtG2WxWMijQq_w3bUQ")

img.save("Jot TV live QRcode.jpg")