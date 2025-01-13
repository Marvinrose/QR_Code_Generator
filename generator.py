print ("Healthy 🎉")


import qrcode

img = qrcode.make("www.react-portfolio-delta-nine.vercel.app")
img.save("qr.png",  "PNG")