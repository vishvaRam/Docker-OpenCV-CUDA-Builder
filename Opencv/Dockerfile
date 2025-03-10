# Use NVIDIA CUDA base image with cuDNN
FROM nvidia/cuda:12.4.1-cudnn-devel-ubuntu22.04

# Set environment variables to disable interactive prompts
ENV DEBIAN_FRONTEND=noninteractive \
    TZ=Etc/UTC

# Set the working directory
WORKDIR /app

# Install system dependencies (non-interactive mode)
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    software-properties-common \
    git \
    curl \
    build-essential \
    cmake \
    gcc-10 \
    g++-10 \
    pkg-config \
    libgtk2.0-dev \
    libavcodec-dev \
    libavformat-dev \
    libswscale-dev \
    libtbb2 \
    libtbb-dev \
    libjpeg-dev \
    libpng-dev \
    libtiff-dev \
    libdc1394-dev \
    libv4l-dev \
    libxvidcore-dev \
    libx264-dev \
    libatlas-base-dev \
    gfortran \
    python3.10 \
    python3.10-dev \
    python3.10-venv \
    python3-pip && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Set Python 3.10 as the default
RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.10 1

# Install OpenCV dependencies
RUN pip3 install --no-cache-dir numpy==1.26.4

# Clone OpenCV source code (non-interactive, avoid TTY)
WORKDIR /app

RUN git clone --branch 4.x --depth 1 https://github.com/opencv/opencv.git && \
    git clone --branch 4.x --depth 1 https://github.com/opencv/opencv_contrib.git

# Create a build directory
WORKDIR /app/opencv/build

# Configure OpenCV with CUDA support for multiple GPU architectures
RUN cmake -D CMAKE_BUILD_TYPE=Release \
    -D CMAKE_INSTALL_PREFIX=/usr/local \
    -D OPENCV_EXTRA_MODULES_PATH=/app/opencv_contrib/modules \
    -D WITH_CUDA=ON \
    -D ENABLE_FAST_MATH=ON \
    -D CUDA_FAST_MATH=ON \
    -D WITH_CUBLAS=ON \
    -D OPENCV_DNN_CUDA=ON \
    -D WITH_CUDNN=ON \
    -D CUDA_ARCH_BIN="6.1 7.0 7.5 8.0 8.6 8.9 9.0" \
    -D CUDA_ARCH_PTX="9.0" \
    -D BUILD_EXAMPLES=OFF \
    -D BUILD_opencv_python3=ON \
    -D PYTHON_EXECUTABLE=$(which python3) \
    -D BUILD_TESTS=OFF \
    -D BUILD_PERF_TESTS=OFF \
    -D WITH_TBB=ON \
    -D WITH_V4L=ON \
    -D WITH_OPENGL=ON ..

# Compile and install OpenCV
RUN make -j$(nproc) && make install && ldconfig

# Copy application code
COPY Code /app

# Install application dependencies
# RUN pip3 install --no-cache-dir -r /app/requirements.txt

# Set the working directory
WORKDIR /app

# Verify OpenCV installation
RUN python3 -c "import cv2; print('OpenCV version:', cv2.__version__)"

# Set default command
CMD ["python3", "main.py"]
