FROM python:3.7-alpine
LABEL author=Sunil
ARG HOME_DIR='/pythonFlaskApp'
ADD . $HOME_DIR
EXPOSE 8080
WORKDIR $HOME_DIR
RUN pip install -r requirements.txt
RUN sh build.sh && echo ls -ld $HOME_DIR/chuck/
ENTRYPOINT ["python", "__init__.py"]
