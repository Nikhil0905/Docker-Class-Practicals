import os
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Configure Upload Folder
UPLOAD_FOLDER = os.environ.get('UPLOAD_FOLDER', 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024 # 16 MB max

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
# Docker class notes and experiences data
docker_notes = [
    {
        "title": "Introduction to Containerization",
        "date": "Week 1",
        "content": "Learned about the fundamentals of containerization and how Docker revolutionizes application deployment. Key takeaway: containers package applications with all dependencies, ensuring consistency across environments.",
        "topics": ["What is Docker?", "Containers vs VMs", "Docker Architecture", "Docker Engine"]
    },
    {
        "title": "Docker Images and Containers",
        "date": "Week 2",
        "content": "Explored the relationship between images and containers. Images are blueprints, containers are running instances. Practiced pulling images from Docker Hub and running containers with various configurations.",
        "topics": ["Docker Images", "Dockerfile", "Docker Hub", "Container Lifecycle", "docker run commands"]
    },
    {
        "title": "Building Custom Images",
        "date": "Week 3",
        "content": "Created our first Dockerfiles! Learned about layers, caching, and optimization strategies. Dr. Raj Mohan Singh emphasized the importance of multi-stage builds for production applications.",
        "topics": ["Dockerfile Syntax", "Layer Caching", "Multi-stage Builds", "Best Practices", ".dockerignore"]
    },
    {
        "title": "Docker Networking",
        "date": "Week 4",
        "content": "Discovered how containers communicate with each other and the outside world. Implemented bridge networks, host networks, and custom networks for microservices architecture.",
        "topics": ["Bridge Networks", "Host Networks", "Port Mapping", "DNS Resolution", "Network Drivers"]
    },
    {
        "title": "Docker Volumes and Data Persistence",
        "date": "Week 5",
        "content": "Solved the data persistence challenge! Volumes allow data to survive container restarts. Practiced with bind mounts, named volumes, and tmpfs mounts.",
        "topics": ["Named Volumes", "Bind Mounts", "Volume Drivers", "Data Backup", "Volume Management"]
    },
    {
        "title": "Docker Compose",
        "date": "Week 6",
        "content": "Game changer! Docker Compose simplifies multi-container applications. Defined entire stacks in YAML files and orchestrated complex environments with a single command.",
        "topics": ["docker-compose.yml", "Service Definition", "Networks & Volumes", "Environment Variables", "Scaling Services"]
    }
]

student_experience = {
    "name": "DevOps Enthusiast",
    "university": "Lovely Professional University",
    "faculty": "Dr. Raj Mohan Singh",
    "course": "DevOps - Docker Containerization",
    "reflection": "This Docker course has been transformative! Dr. Raj Mohan Singh's practical approach helped me understand not just the 'how' but the 'why' of containerization. From struggling with dependency conflicts to confidently deploying multi-container applications, the journey has been incredible. Docker isn't just a tool—it's a mindset shift in how we think about application deployment."
}

useful_commands = [
    {"cmd": "docker build -t myapp .", "desc": "Build an image from Dockerfile"},
    {"cmd": "docker run -d -p 8080:80 myapp", "desc": "Run container in detached mode with port mapping"},
    {"cmd": "docker ps -a", "desc": "List all containers (running and stopped)"},
    {"cmd": "docker images", "desc": "List all images"},
    {"cmd": "docker exec -it container_id bash", "desc": "Execute interactive bash in running container"},
    {"cmd": "docker logs container_id", "desc": "View container logs"},
    {"cmd": "docker-compose up -d", "desc": "Start all services defined in docker-compose.yml"},
    {"cmd": "docker system prune -a", "desc": "Clean up unused containers, images, and networks"}
]

@app.route('/')
def index():
    # Fetch list of uploaded files
    uploaded_files = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('index.html', 
                         notes=docker_notes, 
                         student=student_experience,
                         commands=useful_commands,
                         uploaded_files=uploaded_files)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(url_for('index'))
    file = request.files['file']
    if file.filename == '':
        return redirect(url_for('index'))
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return redirect(url_for('index'))
    return redirect(url_for('index'))

@app.route('/uploads/<name>')
def download_file(name):
    return send_from_directory(app.config['UPLOAD_FOLDER'], name)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
