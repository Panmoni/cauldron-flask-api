# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /python-docker

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY api .

EXPOSE 8000
# PORT 8000

# CMD ["python", "api/app.py"]
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=8000", "--debug"]