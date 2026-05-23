import cv2
import matplotlib.pyplot as plt

image_path = 'example.jpg'
image = cv2.imread(image_path)

image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

height, width, _ = image_rgb.shape

rect1_width, rect1_height = 150, 150
top_left1 = (20, 20)
bottom_right1 = (top_left1[0] + rect1_width, top_left1[1] + rect1_height)
cv2.rectangle(image_rgb, top_left1, bottom_right1, (0, 255, 255), 3)

rect2_width, rect2_height = 200, 150
top_left2 = (width - rect2_width - 20, height - rect2_height - 20)  
bottom_right2 = (top_left2[0] + rect2_width, top_left2[1] + rect2_height)
cv2.rectangle(image_rgb, top_left2, bottom_right2, (255, 0, 255), 3)

cv2.circle(image_rgb, (200, 200), 50, (255, 0, 0), 3)

cv2.line(image_rgb, (100, 100), (400, 400), (0, 255, 0), 3)

start_point = (100, 200)
end_point = (200, 200)

cv2.arrowedLine(image_rgb, start_point, end_point, (255, 0, 0), 4)

cv2.arrowedLine(image_rgb, end_point, start_point, (255, 0, 0), 4)

plt.imshow(image_rgb)
plt.axis('off')
plt.show()