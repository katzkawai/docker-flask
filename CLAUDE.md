# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

### Building and Running the Application

**Docker Build:**
```bash
docker build -t flask-app .
```

**Docker Run:**
```bash
docker run -p 5000:5000 flask-app
```

**Run Flask App Locally (without Docker):**
```bash
pip install flask
python app.py
```

## Architecture Overview

This is a minimal Flask web application containerized with Docker. The application:

- Uses Flask framework to create a simple web server
- Runs on port 5000 and binds to all interfaces (0.0.0.0)
- Has a single route "/" that returns "Hello, Docker!"
- Uses Python 3.8 base image in Docker
- Installs Flask during the Docker build process

The codebase consists of:
- `app.py`: Flask application entry point with a single route
- `Dockerfile`: Container definition that packages the Flask app