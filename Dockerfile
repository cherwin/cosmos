FROM python:3.12

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

COPY ./core/requirements.txt .

RUN pip install --upgrade pip
#RUN pip install 'channels[daphne]'
RUN pip install -r requirements.txt

COPY ./core/ /app/

EXPOSE 8000

CMD ["gunicorn", "core.wsgi", "-b :8000", "-w 4"]
