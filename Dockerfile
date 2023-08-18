FROM python:3.8

WORKDIR /code

COPY requirements.txt requirements.txt

RUN apt-get update && apt-get install -y vim

RUN pip3 install --upgrade pip

RUN python3 -m pip install joblib==1.2.0

RUN pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

RUN pip3 install -r requirements.txt

COPY . .

CMD ["python","manage.py","runserver", "0.0.0.0:8088"]