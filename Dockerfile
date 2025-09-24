FROM ubuntu

COPY . /test/

RUN pip install pandas sqlalchemy psycopg2

CMD [“python”, “test/pipeline.py”]