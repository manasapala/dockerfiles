FROM python:2

MAINTAINER prasad

RUN pip install boto3 --user

RUN mkdir /opt/upload_files/

WORKDIR /usr/src/app

COPY s3_upload.py .

ENV FILE_NAME $FILE_NAME
ENV ACCESS_KEY $ACCESS_KEY
ENV SECRET_KEY $SECRET_KEY

CMD ["python", "./s3_upload.py"]
