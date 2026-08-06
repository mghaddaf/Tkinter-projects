import cv2
minecraft = cv2.imread(r"Open CV\Images\open cv picture.png",cv2.IMREAD_GRAYSCALE)
cv2.imshow("Minecraft Grass Block", minecraft)
cv2.waitKey(0)