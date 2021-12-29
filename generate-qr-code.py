import qrcode
import numpy as np

# data to encode
userData = input('Enter data for the barcode: ')

# instantiate QRCode object
qr = qrcode.QRCode(version=1, box_size=10, border=4)

# add data to the QR code
qr.add_data(userData)

# compile the data into a QR code array
qr.make()

# print the image shape
print("Dimensions of the QR code:", np.array(qr.get_matrix()).shape)

# transfer the array into an actual image
img = qr.make_image(fill_color="white", back_color="black")

# save it to a file
img.save("site_inversed.png")

# Display the image 
img.show("site_inversed.png")