FROM python:3.9
WORKDIR /src
RUN apt-get update && apt-get install -y graphviz xdg-utils
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python3"]
