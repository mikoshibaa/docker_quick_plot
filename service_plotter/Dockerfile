FROM python:3.9-slim

WORKDIR /home

COPY requirement.txt ./
RUN pip install --no-cache-dir -r requirement.txt

COPY . .