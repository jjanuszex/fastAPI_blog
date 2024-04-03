FROM python:3.12.2-slim

# Set the working directory

WORKDIR /usr/src/app


# Install PostgreSQL development packages

RUN apt-get update && apt-get install -y libpq-dev gcc

# Copy the current directory contents into the container at /app


COPY requirements.txt ./

# Install any needed packages specified in requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

# Copy the current local directory contents into the container at /app

COPY . .

# Run app.py when the container launches

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0.", "--port", "8000"]

 


