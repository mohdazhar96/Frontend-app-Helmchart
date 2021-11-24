FROM python

COPY python/ .

RUN pip install flask

CMD [ "python", "./hello.py" ]
