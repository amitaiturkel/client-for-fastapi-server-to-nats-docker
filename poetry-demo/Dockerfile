# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy your client-side code into the container
COPY . .

# Copy your tests directory into the container
COPY tests/ tests/

# Install tox for running tests
RUN pip install --no-cache-dir poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-dev --no-interaction --no-ansi
# Define the command to run your tests using tox
CMD ["python","poetry_demo/client.py"]
