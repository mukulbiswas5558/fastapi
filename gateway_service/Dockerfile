# Use a Python base image
FROM python:3.8

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Install the dependencies
RUN pip install fastapi uvicorn

# Expose the port the application will run on
EXPOSE 8000  

# Command to run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
