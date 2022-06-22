FROM python:3.7.13-buster
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY /trained_model /trained_model
COPY /src /src
ENV PYTHONPATH "${PYTHONPATH}:/src"
EXPOSE 5000
CMD [ "python", "./src/api.py"]