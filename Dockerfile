FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

RUN python -m pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt

ADD django-setup.sh /django-setup.sh
RUN chmod a+x /django-setup.sh

ENTRYPOINT ["/django-setup.sh"]




COPY . .
