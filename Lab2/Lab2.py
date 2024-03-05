import cv2
def printimg(img):
    cv2.imshow("image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

image1 = cv2.imread("lena.tif")
image2 = cv2.imread("paper.tif")
# image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
# image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
# image = cv2.resize(image, (0,0), fx=0.5, fy=0.5)
# printimg(image2)
# cv2.imwrite('grey1.png',image1)
# cv2.imwrite('grey2.png',image2)
# # Addition
# added_image = cv2.add(image1, image2)
# # cv2.imwrite('added_image.png',added_image)
# # printimg(added_image)
#
# # Subtraction
# subtracted_image = cv2.subtract(image1, image2)
# cv2.imwrite('subtracted_image.png',subtracted_image)
# # printimg(subtracted_image)
#
# # Multiplication
# multiplied_image = cv2.multiply(image1, 2)
# cv2.imwrite('multiplied_image.png',multiplied_image)
# # printimg(multiplied_image)
#
# # Division
# divided_image = cv2.divide(image1, 2)
# cv2.imwrite('divided_image.png',divided_image)
# # printimg(divided_image)

binary1 = cv2.threshold(image1, 128, 255, cv2.THRESH_BINARY)[1]
binary2 = cv2.threshold(image2, 128, 255, cv2.THRESH_BINARY)[1]

# cv2.imwrite('binary1.png',binary1)
# cv2.imwrite('binary2.png',binary2)
# printimg(binary1)

# AND operation
and_image = cv2.bitwise_and(binary1, binary2)
# printimg(and_image)
# OR operation
or_image = cv2.bitwise_or(binary1, binary2)
# printimg(or_image)
# XOR operation
xor_image = cv2.bitwise_xor(binary1, binary2)

# NOT operation
not_image = cv2.bitwise_not(binary1)

# cv2.imwrite('and_image.png',and_image)
cv2.imwrite('or_image.png',or_image)
cv2.imwrite('xor_image.png',xor_image)
cv2.imwrite('not_image.png',not_image)