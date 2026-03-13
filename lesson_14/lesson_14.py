# Task 1
import numpy as np

def f_to_c(f):
    return(f - 32) * 5/9

np_vectorized = np.vectorize(f_to_c)

temps = [100, 125, 75, 60]

temps_in_c =np_vectorized(temps)

print(temps_in_c)

## Task 2
def power(number, power):
    return number ** power
listpower = np.vectorize(power)

numbers = [3, 5, 9, 4]
powers = [4, 2, 3, 5]

powered_nums = listpower(numbers, powers)
print(powered_nums)


## Task 3
A = np.array([
    [4, 5, 6],
    [3, -1, 1],
    [2, 1, -2]
])

B = np.array([7, 4, 5])

solutions = np.linalg.solve(A, B)
print(solutions)

## Task 4
A = np.array([
    [10, -2, 3],
    [-2, 8, -1],
    [3, -1, 6]
])

B = np.array([12, -5, 15])

solutions = np.linalg.solve(A, B)
print(solutions)

## image manipulation
###task 1
import numpy as np

from PIL import Image

image = Image.open(r"C:\Users\bunyo\OneDrive\Desktop\python\lesson_14\images\birds.jpeg")
img_mat = np.array(image)
flp_bird = np.flip(img_mat, axis=(0, 1))
new_img = Image.fromarray(flp_bird)
new_img.save("flipped_bird.png")

### task 2
noise = np.random.randint(0, 50, img_mat.shape, dtype='uint8')

noisy_bird_mat = img_mat.astype(np.uint16) + noise

noisy_bird_mat = np.clip(noisy_bird_mat, 0, 255).astype(np.uint8)
noisy_bird = Image.fromarray(noisy_bird_mat)
noisy_bird.save("noisy.png")

### task 3
bright = img_mat.astype(np.uint16) + 50

bright = np.clip(bright, 0, 255).astype('uint8')
brighten_img = Image.fromarray(bright)
brighten_img.save("brighten_image.png")

### task 4

mask_mat = img_mat.copy()

h, w, c = mask_mat.shape
center_h, center_w = h//2, w//2
mask_mat[center_h - 50 : center_h + 50, center_w - 50 : center_w + 50] = 0
masked_img = Image.fromarray(mask_mat)
masked_img.save("masked.jpeg")

