# Use an official Python image
FROM python:3.10

# Set the working directory
WORKDIR /app

# Copy the dependencies file and install them
COPY requirements.txt /app/
COPY main.py /app/
COPY model /app/model/

RUN pip install --no-cache-dir -r requirements.txt

# Expose the FastAPI default port
EXPOSE 5757

# Command to run the app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5757", "--reload"]

