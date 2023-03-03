FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY agenda/requirements.txt /app/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /app/

RUN useradd -ms /bin/bash greg
RUN chown -R greg:greg /app/
USER greg

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "projeto.wsgi:application"]
