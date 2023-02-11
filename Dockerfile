FROM python:slim-bullseye
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
RUN python manage.py migrate
CMD [ "python", "manage.py", "runserver", "7890"]