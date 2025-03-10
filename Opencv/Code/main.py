import cv2
import numpy as np

def check_opencv_cuda():
    print("OpenCV Version:", cv2.__version__)
    print("CUDA Available:", cv2.cuda.getCudaEnabledDeviceCount() > 0)
    
    if cv2.cuda.getCudaEnabledDeviceCount() > 0:
        print("CUDA is enabled. Running a test...")

        # Create a random image
        img = np.random.randint(0, 256, (512, 512, 3), dtype=np.uint8)

        # Upload image to GPU
        gpu_img = cv2.cuda_GpuMat()
        gpu_img.upload(img)

        # Create and apply Gaussian Blur filter
        gaussian_filter = cv2.cuda.createGaussianFilter(cv2.CV_8UC3, cv2.CV_8UC3, (15, 15), 0)
        gpu_blurred = gaussian_filter.apply(gpu_img)

        # Download the result back to CPU
        blurred_img = gpu_blurred.download()

        print("CUDA processing successful! Saving images...")

        # Save the images instead of displaying them
        cv2.imwrite("/app/original_image.jpg", img)
        cv2.imwrite("/app/blurred_image.jpg", blurred_img)

        print("Images saved as /app/original_image.jpg and /app/blurred_image.jpg")

    else:
        print("CUDA is not available. Check your OpenCV installation.")

if __name__ == "__main__":
    check_opencv_cuda()
