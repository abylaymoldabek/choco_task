FROM python:3.9
ENV PYTHONUNBUFFERED 1

# App setup
ADD . /code
WORKDIR /code

# Requirements installation
RUN pip install -r requirements.txt

#COPY . .
#ENTRYPOINT ["entrypoint.sh"]
#CMD ["python manage.py runserver"]