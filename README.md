🛍️ Product Catalogue – Task 2
This project is part of an internship assignment (Task 2). It is a basic web service built using Flask, containerized using Docker, and deployed using Kubernetes via Minikube. It provides endpoints to:

Check service health

Retrieve a list of products

Search for products by name

🧰 Technologies Used
Python 3.11 (with Flask)

Docker

Kubernetes

Minikube (Kubernetes local cluster)

📂 Project Structure
File	Description
app.py	Main Flask application
requirements.txt	Lists Python dependencies
Dockerfile	Instructions to containerize the app
deployment.yaml	Kubernetes Deployment and Service configuration
README.md	Project documentation

✅ Prerequisites
Before you begin, ensure the following tools are installed:

Python 3.x

Docker

Git

kubectl (Kubernetes CLI)

Minikube

🚀 Step-by-Step Setup
Clone this GitHub repository:

git clone https://github.com/Poojalshetty29/product-catalogue-task2-.git
cd product-catalogue-task2-

(Optional) Test Flask app locally:

pip install -r requirements.txt
python app.py

Then visit: http://localhost:5000/health

Build Docker Image:

docker build -t product-catalogue:v1 .

Start Minikube:

minikube start

Deploy application to Kubernetes:

kubectl apply -f deployment.yaml
kubectl apply -f service.yaml

Check deployment status:

kubectl get pods
kubectl get services

Access the application:

Run:
minikube service product-catalogue-service

It will return a URL, e.g.:
http://192.168.49.2:30263

🧪 API Endpoints
Once deployed, you can access these endpoints via the service URL:

GET /health
Returns { "status": "ok" }

GET /products
Returns list of all products

GET /products/search?q=Shoe
Returns matching products based on query string

Example URL:
http://192.168.49.2:30263/products/search?q=Shoe

⚠️ Common Issues
Not Found: Make sure the Flask app is correctly exposed in your Dockerfile and app.py uses if name == "main"

ImagePullBackOff: Make sure Docker image is locally available when using Minikube with local Docker daemon (minikube docker-env)

👩‍💻 Author
Pooja L Shetty
7th Semester – Computer Science Engineering
GitHub: https://github.com/Poojalshetty29
