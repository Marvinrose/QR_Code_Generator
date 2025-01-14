print ("Healthy 🎉")


import qrcode

img = qrcode.make("https://react-portfolio-delta-nine.vercel.app/")
img.save("generator.png",  "PNG")