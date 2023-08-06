from PIL import Image
import os
import numpy as np
import math
import cv2
import imageio
from skimage.metrics import structural_similarity as ssim

def calculate_ssim(original_image, compressed_image):

    min_dimension = min(original_image.shape)
    win_size = min(7, min_dimension)  # Set a maximum value of 7 or the smaller dimension

    # Calculate the SSIM score
    ssim_score = ssim(original_image, compressed_image, win_size=win_size, data_range=compressed_image.max() - compressed_image.min())

    return ssim_score

def calculate_psnr(original_image, reconstructed_image):
    mse = np.mean((original_image - reconstructed_image) ** 2)
    max_pixel_value = np.max(original_image)
    psnr = 20 * math.log10(max_pixel_value / math.sqrt(mse))
    return psnr

file_path = "XING_B24.bmp"
# Open the BMP image
bmp_image = Image.open(file_path)
rgb_image = bmp_image.convert("RGB")
# Save as JPEG format
rgb_image.save("image.jpg", "JPEG")


# Convert to PNG format
bmp_image.save("image.png", "PNG")

# Convert to GIF format
bmp_image.save("image.gif", "GIF")

# Convert to TIFF format
bmp_image.save("image.tiff", "TIFF")

original_image = cv2.imread(file_path)
compressed_image = cv2.imread('image.png')
psnr = calculate_psnr(original_image, compressed_image)
print("png PSNR:", psnr)
ssim_score = calculate_ssim(original_image, compressed_image)
print("png SSIM Score:", ssim_score)
file_size_bytes = os.path.getsize(file_path)
memory_size_in = file_size_bytes / 1024
file_size_bytes = os.path.getsize("image.png")
memory_size_out = file_size_bytes / 1024
print("memprysizeofin",memory_size_in)
print("memorysizeout",memory_size_out)
compression_ratio = memory_size_in/memory_size_out
print("png compression ratio:",compression_ratio)

compressed_image = cv2.imread('image.jpg')
psnr = calculate_psnr(original_image, compressed_image)
print("jpg PSNR:", psnr)
ssim_score = calculate_ssim(original_image, compressed_image)
print("jpg SSIM Score:", ssim_score)
file_size_bytes = os.path.getsize(file_path)
memory_size_in = file_size_bytes / 1024
file_size_bytes = os.path.getsize("image.jpg")
memory_size_out = file_size_bytes / 1024
print("memprysizeofin",memory_size_in)
print("memorysizeout",memory_size_out)
compression_ratio = memory_size_in/memory_size_out
print("JPEG compression ratio:",compression_ratio)

compressed_image = imageio.v2.imread('image.gif')
psnr = calculate_psnr(original_image, compressed_image)
print("gif PSNR:", psnr)
ssim_score = calculate_ssim(original_image, compressed_image)
print("gif SSIM Score:", ssim_score)
file_size_bytes = os.path.getsize(file_path)
memory_size_in = file_size_bytes / 1024
file_size_bytes = os.path.getsize("image.gif")
memory_size_out = file_size_bytes / 1024
print("memprysizeofin",memory_size_in)
print("memorysizeout",memory_size_out)
compression_ratio = memory_size_in/memory_size_out
print("gif compression ratio:",compression_ratio)

compressed_image = cv2.imread('image.tiff')
psnr = calculate_psnr(original_image, compressed_image)
print("tiff PSNR:", psnr)
ssim_score = calculate_ssim(original_image, compressed_image)
print("tiff SSIM Score:", ssim_score)
file_size_bytes = os.path.getsize(file_path)
memory_size_in = file_size_bytes / 1024
file_size_bytes = os.path.getsize("image.tiff")
memory_size_out = file_size_bytes / 1024
print("memprysizeofin",memory_size_in)
print("memorysizeout",memory_size_out)
compression_ratio = memory_size_in/memory_size_out
print("tiff compression ratio:",compression_ratio)

# Close the BMP image
bmp_image.close()
rgb_image.close()
