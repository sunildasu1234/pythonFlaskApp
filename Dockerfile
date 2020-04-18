FROM python:3.7-alpine
LABEL author=Sunil
COPY pythonFlaskApp /pythonFlaskApp
RUN pip install -r requirements.txt 
ENV build_dir /pythonFlaskApp
WORKDIR build_dir
EXPOSE 8080
RUN sh build.sh
ENTRYPOINT ["python", "__init__.py"]
