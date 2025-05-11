import cv2
import numpy as np

row = 64
middle_base = 100
left_base = 50
right_base = 150
def find_consecutive_ten(nums):
    nums = sorted(set(nums))  # 去重并排序

    for i in range(len(nums) - 9):  # 至少需要10个数
        if all(nums[i] + j == nums[i + j] for j in range(10)):  # 检查10个相连
            return nums[i]  # 返回第一个相连的数字

    return None  # 如果没有找到相连的十个数，则返回None

def middle_point(image, last_state):
    # 检查图像是否成功加载
    if image is None:
        print("Error loading image.")
        exit()
    # 膨胀腐蚀
    image = cv2.dilate(image, None, iterations=2)
    image = cv2.erode(image, None, iterations=2)
    # 提取第row行像素点
    pixel_row = image[row]
    # 找到黑色像素的位置（假设黑色为0）
    black_pixels = np.where(pixel_row == 0)[0]

    result = find_consecutive_ten(black_pixels)
    if result is not None:
        print(f"{result: 4d}", end="\t")
        last_state = result
    else:
        result = last_state
        print("none", end="\t")

    image = cv2.line(image, (result, row), (result, row), (0, 0, 255), 3)
    image = cv2.line(image, (middle_base, row), (middle_base, row), (155, 155, 155), 3)
    image = cv2.line(image, (left_base, row), (left_base, row), (155, 155, 155), 3)
    image = cv2.line(image, (right_base, row), (right_base, row), (155, 155, 155), 3)

    cv2.imshow('image', image)

    return result, middle_base, left_base, right_base, last_state
