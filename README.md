# OpenCV with CUDA Docker Setup

This project provides a Docker-based environment for running OpenCV with CUDA support, enabling GPU-accelerated computer vision tasks. The setup includes a complete build of OpenCV 4.12.0 with CUDA 12.8.1 and cuDNN support.

## Features

- OpenCV 4.12.0 with CUDA support
- CUDA 12.8.1 with cuDNN
- GPU-accelerated image processing
- Pre-configured Docker environment
- Example code demonstrating CUDA-enabled OpenCV operations

## Prerequisites

- Docker
- NVIDIA Container Toolkit
- NVIDIA GPU with CUDA support
- Docker Compose

## Installation

1. Clone this repository:
```bash
git clone <your-repo-url>
cd <repo-name>
```

2. Ensure you have the NVIDIA Container Toolkit installed:


## Usage

1. Build and run the container using Docker Compose:
```bash
docker-compose up --build
```

2. The example code will:
   - Check for CUDA availability
   - Create a random test image
   - Apply GPU-accelerated Gaussian blur
   - Save both original and processed images

## Project Structure

```
.
├── Code/
│   ├── Dockerfile          # OpenCV with CUDA build configuration
│   └── main.py            # Example code demonstrating CUDA usage
├── docker-compose.yml     # Docker Compose configuration
└── README.md             # This file
```

## Technical Details

- Base Image: NVIDIA CUDA 12.8.1 with cuDNN
- OpenCV Version: 4.12.0
- CUDA Architectures: 6.1, 7.0, 7.5, 8.0, 8.6, 8.9, 9.0, 10.0, 12.0 
- Python Version: 3.12
- Key Features:
  - CUDA acceleration
  - cuDNN support
  - OpenGL support
  - Video codec support
  - TBB threading

## Testing CUDA Support

The included `main.py` script demonstrates CUDA functionality by:
1. Checking CUDA availability
2. Creating a test image
3. Applying GPU-accelerated Gaussian blur
4. Saving the results

## Contributing

Feel free to submit issues and enhancement requests!
