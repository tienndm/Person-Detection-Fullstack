FROM python:3.10-slim

WORKDIR /api
COPY ./requirements.txt /api/requirements.txt
COPY ./src/.env /api/.env

RUN apt-get update && apt-get install -y libgl1-mesa-glx libglib2.0-0 python3-tk
RUN pip install --no-cache-dir python-dotenv
RUN pip install --no-cache-dir -r requirements.txt

COPY ./src /api/src

EXPOSE 8000
CMD ["python3", "src/main.py"]