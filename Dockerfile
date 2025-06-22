# Step 1: Use a lightweight base image
FROM python:3.11-slim

# Step 2: Set working directory
WORKDIR /app

# Step 3: Copy app files
COPY app.py requirements.txt ./

# Step 4: Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Expose the app port
EXPOSE 5000

# Step 6: Set environment variables (optional)
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Step 7: Run the app
CMD ["python", "app.py"]
