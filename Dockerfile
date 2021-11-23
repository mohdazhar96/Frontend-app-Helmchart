FROM python

WORKDIR /code

COPY python/ .

RUN pip install flask

CMD [ "python", "./hello.py" ]
