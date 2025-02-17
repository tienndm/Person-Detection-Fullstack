FROM python:3.10-slim

WORKDIR /api
COPY ./requirements.txt /api/requirements.txt

RUN apt-get update && apt-get install -y libgl1-mesa-glx libglib2.0-0
RUN pip install --no-cache-dir -r requirements.txt

COPY ./src /api/src

EXPOSE 8000
CMD ["python3", "src/main.py"]