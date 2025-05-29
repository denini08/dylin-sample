# Use official Python 3.10 image
FROM python:3.10-slim

# Install git
RUN apt-get update && apt-get install -y git uuid-runtime && apt-get clean 

RUN git clone --depth=1 https://github.com/sola-st/DyLin && \
    cd DyLin && \
    pip install -r requirements.txt && \
    pip install . && \
    pip install pytest

# Set the working directory
WORKDIR /app

# Default command
CMD ["bash"]
