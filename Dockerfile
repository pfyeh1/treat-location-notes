
FROM python:3.11-slim

# 2. Set the 'working directory' inside the cloud server
WORKDIR /app

# 3. Copy your list of libraries first (this makes builds faster)
COPY requirements.txt .

# 4. Install the libraries listed in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy all your code (main.py, etc.) into the server
COPY . .

# 6. Start the app! 
# We use the $PORT variable because GCP assigns a random port to every app
CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port ${PORT:-8080}"]