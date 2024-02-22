import qrcode
import image 



qr = qrcode.QRCode(
    version = 15, 
    box_size = 10,
# error_correction=qrcode.constants.ERROR_CORRECT_L,
    border = 5

)

data = "https://www.youtube.com/"


qr.add_data(data)
qr.make(fit = True)
image = qr.make_image(fill ="cery", back_color ="white")
image.save("school.png")

