FROM python:3.6.8-slim

# Set working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packagges specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r  requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run app.py when the container launches
CMD python3 ./website/manage.py runserver
