# 🐳 Docker DevOps Journey - Student Learning Portal

A beautifully designed web application showcasing a student's learning journey through Docker and containerization at Lovely Professional University, taught by **Dr. Raj Mohan Singh**.

## 🌟 Features

- **Interactive Learning Notes**: Organized weekly notes covering Docker fundamentals to advanced concepts
- **Command Reference**: Quick access to essential Docker commands with descriptions
- **Modern UI**: Terminal-inspired design with smooth animations and Docker-themed aesthetics
- **Responsive Design**: Works seamlessly on desktop, tablet, and mobile devices
- **Containerized**: Fully Dockerized application demonstrating real-world DevOps practices

## 🛠️ Technologies Used

- **Backend**: Python 3.11 + Flask
- **Frontend**: HTML5, CSS3 (Custom styling with animations)
- **Containerization**: Docker
- **Fonts**: JetBrains Mono, Outfit, Space Mono

## 📋 Prerequisites

### Option 1: Run with Docker (Recommended)
- Docker installed on your system
  - [Install Docker on Windows](https://docs.docker.com/desktop/install/windows-install/)
  - [Install Docker on Mac](https://docs.docker.com/desktop/install/mac-install/)
  - [Install Docker on Linux](https://docs.docker.com/engine/install/)

### Option 2: Run Locally
- Python 3.11 or higher
- pip (Python package manager)

## 🚀 Quick Start

### Method 1: Using Docker (Production-Ready)

1. **Clone or download this project**

2. **Build the Docker image**
```bash
docker build -t student-docker-journey:latest .
```

3. **Run the container**
```bash
docker run -d -p 5000:5000 --name docker-journey student-docker-journey:latest
```

4. **Access the application**
   - Open your browser and navigate to: `http://localhost:5000`

5. **View container logs** (optional)
```bash
docker logs docker-journey
```

6. **Stop the container**
```bash
docker stop docker-journey
```

7. **Remove the container**
```bash
docker rm docker-journey
```

### Method 2: Running Locally (Development)

1. **Create a virtual environment** (recommended)
```bash
python -m venv venv
```

2. **Activate the virtual environment**
   - Windows:
   ```bash
   venv\Scripts\activate
   ```
   - Mac/Linux:
   ```bash
   source venv/bin/activate
   ```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run the application**
```bash
python app.py
```

5. **Access the application**
   - Open your browser and navigate to: `http://localhost:5000`

## 📦 Project Structure

```
docker-journey/
│
├── app.py                 # Flask application (main backend)
├── requirements.txt       # Python dependencies
├── Dockerfile            # Docker configuration
├── .dockerignore         # Files to exclude from Docker build
├── README.md             # This file
│
├── templates/
│   └── index.html        # Main HTML template
│
└── static/
    └── css/
        └── style.css     # Custom styling and animations
```

## 🐳 Docker Commands Reference

Here are some useful Docker commands for this project:

| Command | Description |
|---------|-------------|
| `docker build -t student-docker-journey:latest .` | Build the Docker image |
| `docker run -d -p 5000:5000 student-docker-journey:latest` | Run container in detached mode |
| `docker ps` | List running containers |
| `docker ps -a` | List all containers (including stopped) |
| `docker logs <container_id>` | View container logs |
| `docker exec -it <container_id> bash` | Access container shell |
| `docker stop <container_id>` | Stop a running container |
| `docker rm <container_id>` | Remove a container |
| `docker images` | List all images |
| `docker rmi student-docker-journey:latest` | Remove the image |

## 🎨 Design Philosophy

The website features a **terminal-inspired, tech-forward aesthetic** that reflects the Docker and DevOps theme:

- **Color Palette**: Docker blue (#0db7ed) with cyberpunk-inspired accents
- **Typography**: Monospace fonts (JetBrains Mono, Space Mono) for technical authenticity
- **Animations**: Smooth CSS transitions and keyframe animations
- **Layout**: Terminal window wrapper with header controls
- **Responsive**: Mobile-first approach with breakpoints

## 📚 Learning Topics Covered

1. **Introduction to Containerization** - Docker basics and architecture
2. **Images and Containers** - Understanding the Docker ecosystem
3. **Building Custom Images** - Dockerfile creation and optimization
4. **Docker Networking** - Container communication patterns
5. **Data Persistence** - Volumes and bind mounts
6. **Docker Compose** - Multi-container orchestration

## 👨‍🏫 Course Information

- **University**: Lovely Professional University
- **Course**: DevOps - Docker Containerization
- **Faculty**: Dr. Raj Mohan Singh
- **Focus**: Practical, hands-on approach to containerization

## 🔧 Customization

To customize the content:

1. **Edit Student Information**: Modify the `student_experience` dictionary in `app.py`
2. **Update Notes**: Edit the `docker_notes` list in `app.py`
3. **Add Commands**: Extend the `useful_commands` list in `app.py`
4. **Styling**: Customize colors and animations in `static/css/style.css`

## 🐛 Troubleshooting

**Port already in use?**
```bash
# Use a different port
docker run -d -p 8080:5000 student-docker-journey:latest
# Then access at http://localhost:8080
```

**Container won't start?**
```bash
# Check logs
docker logs <container_id>

# Check if port 5000 is available
# Windows: netstat -ano | findstr :5000
# Mac/Linux: lsof -i :5000
```

**Build failing?**
```bash
# Clean up and rebuild
docker system prune -a
docker build --no-cache -t student-docker-journey:latest .
```

## 📄 License

This project is created for educational purposes as part of DevOps coursework at Lovely Professional University.

## 🙏 Acknowledgments

Special thanks to **Dr. Raj Mohan Singh** for excellent teaching and making Docker concepts accessible and practical.

---

**Built with ❤️ for DevOps Learning**
