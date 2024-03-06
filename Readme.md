# Containerized Application README

This repository contains a containerized application that performs to perform basic operation on data and Test it.

## Prerequisites

Before you begin, ensure you have the following installed:

- Docker: [installation instructions](https://docs.docker.com/get-docker/)

## Getting Started

To build and run the container, follow these steps:

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/surya545/brine-task.git

2. Navigate to the project directory:

   ```bash
   cd brine-task

3. Build the Docker image:

   ```bash
   docker build -t <image-name>:<tag> -f <Dockerfile-Task/Dockerfile-Test> .

  Build the docker image for both test and task one by one, also give relevant <image-name> and <tag> (different value for each build).

3. Run the Docker container:

   ```bash
   docker run -it <image-name>:tag



