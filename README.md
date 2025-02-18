# Project Title

A brief introduction to your project. This codebase manages image uploads and person detection using a Next.js frontend and a FastAPI backend. It also includes Docker configuration for container orchestration.

## Table of Contents
- [Overview](#overview)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Backend](#backend)
- [Docker Setup](#docker-setup)
- [Contributing](#contributing)
- [License](#license)

## Overview

This project provides:
- A modern React (Next.js) frontend for image uploads and displaying detection results.
- A FastAPI backend for processing images and simulating person detection.
- Docker configurations to easily spin up the services along with a PostgreSQL database.

## Getting Started

Clone the repository and install dependencies:
```bash
git clone https://github.com/tienndm/hometest.git
cd hometest/scripts
docker-compose up -d
```

## Usage

Upload an image via the frontend. The image is sent to the backend where it is processed, and the resulting data including the number of persons detected is displayed.

## Backend

The backend server accepts image uploads and performs person detection using FastAPI and OpenCV with a YOLOv8 model.

### API Endpoint

- POST `/api/v1/core`  
  Accepts an image file under the key "img" and returns a JSON response containing:
  - personCount: Number of persons detected.
  - message: A summary message.
  - image: Processed image in base64 format.

## Docker Setup

Docker Compose is provided to orchestrate the services:
- PostgreSQL database (`db`)
- Backend API (`api`)
- Frontend Next.js application (`fe`)

To start all services:
```bash
cd scripts
docker-compose up --build
```