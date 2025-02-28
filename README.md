<div align="center">
  <h1>🔍 Person Detection System</h1>
  <p>A full-stack solution for image processing and person detection</p>
  
  [![Next.js](https://img.shields.io/badge/Next.js-black?style=for-the-badge&logo=next.js&logoColor=white)](https://nextjs.org/)
  [![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
  [![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
  [![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
</div>

## 📋 Table of Contents
- [Overview](#-overview)
- [Features](#-features)
- [System Architecture](#-system-architecture)
- [Getting Started](#-getting-started)
- [Usage Guide](#-usage-guide)
- [API Documentation](#-api-documentation)
- [Project Structure](#-project-structure)
- [Docker Setup](#-docker-setup)
- [Contributing](#-contributing)
- [License](#-license)

## 🌟 Overview

This Person Detection System is a comprehensive solution that enables users to upload images and automatically detect people within them. Built with modern technologies, the system offers a seamless experience from upload to result visualization.

The project combines a reactive frontend with a powerful AI-driven backend, all orchestrated through Docker for easy deployment and scalability.

## ✨ Features

- **User-friendly Interface**: Intuitive Next.js frontend for seamless image uploads and result viewing
- **AI-Powered Detection**: Uses YOLOv8 model to accurately detect and count people in images
- **Real-time Processing**: Fast image processing with instant feedback
- **Containerized Deployment**: Easy setup and consistent environment with Docker
- **Database Integration**: Persistent storage with PostgreSQL for tracking uploads and results

## 🏗 System Architecture

The system consists of three main components:

1. **Frontend**: A Next.js application providing the user interface
2. **Backend API**: FastAPI server handling image processing and person detection
3. **Database**: PostgreSQL for data persistence

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   Next.js   │────▶│   FastAPI   │────▶│ PostgreSQL  │
│  Frontend   │◀────│   Backend   │◀────│  Database   │
└─────────────┘     └─────────────┘     └─────────────┘
```

## 🚀 Getting Started

### Prerequisites

- Docker and Docker Compose
- Git

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/tienndm/hometest.git
   cd hometest
   ```

2. Start the application:
   ```bash
   cd scripts
   docker-compose up -d
   ```

3. Access the application:
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:8000
   - API Documentation: http://localhost:8000/docs

## 📝 Usage Guide

### Uploading Images

1. Navigate to the web interface
2. Click on the upload area to select an image or drag-and-drop
3. The system will process the image and display:
   - Number of people detected
   - Processed image with bounding boxes
   - Detection confidence scores

### Viewing Results

The results page displays:
- Original and processed images side by side
- Total count of people detected
- Detection metadata including timestamps

## 📚 API Documentation

### Core Endpoints

#### Person Detection
- **URL**: `/api/v1/core`
- **Method**: `POST`
- **Request Body**: Form data with `img` field containing the image file
- **Response**:
  ```json
  {
    "personCount": 3,
    "message": "Successfully processed. 3 persons detected.",
    "image": "base64-encoded-image-data"
  }
  ```

For complete API documentation, visit the Swagger UI at http://localhost:8000/docs when the server is running.

## 📁 Project Structure

```
person-detection-fullstack/
├── frontend/              # Next.js frontend application
│   ├── components/        # Reusable React components
│   ├── pages/             # Next.js pages
│   └── public/            # Static assets
├── backend/               # FastAPI backend service
│   ├── app/               # Main application code
│   ├── models/            # ML models and schemas
│   └── tests/             # Backend tests
├── scripts/               # Helper scripts
│   └── docker-compose.yml # Service orchestration
└── README.md              # This documentation
```

## 🐳 Docker Setup

The project uses Docker Compose to orchestrate the following services:
- **db**: PostgreSQL database
- **api**: FastAPI backend
- **fe**: Next.js frontend

### Environment Configuration

Create a `.env` file in the root directory with the following variables:

```
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=app
```

### Starting Services

```bash
cd scripts
docker-compose up --build
```

### Service Management

- Stop all services: `docker-compose down`
- View logs: `docker-compose logs -f [service_name]`
- Restart a specific service: `docker-compose restart [service_name]`

## 👥 Contributing

We welcome contributions to improve the Person Detection System!

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.