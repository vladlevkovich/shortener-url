FROM python:3.11

#RUN mkdir /app

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .

#RUN #chmod  a+x bin/*.sh
#
#CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]