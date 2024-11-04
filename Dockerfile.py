From python:3.9

WORKDIR /code

copy ./requirements.txt /code/requirements.txt

RUN pip install --no-cach-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

CMD ["fastapi", "run", "app/main.py", "--port", "4242"]
