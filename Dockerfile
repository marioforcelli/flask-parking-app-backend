# Use an official Python runtime as a parent image
FROM python:latest

# Set the working directory to /app
WORKDIR /api

# Copy the current directory contents into the container at /app
COPY . /api

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Run app.py when the container launches
CMD ["flask", "--app", "main", "run", "--host", "0.0.0.0", "--debug"]