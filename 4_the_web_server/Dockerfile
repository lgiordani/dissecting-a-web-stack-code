FROM python:3.6

ADD app /app
ADD wsgi.py /

WORKDIR .
RUN pip install flask gunicorn
EXPOSE 8000

