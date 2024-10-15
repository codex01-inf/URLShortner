FROM python:3.11

#ENV APPLICATION_PORT 8086
ARG SERVER_PORT
ARG SERVER_HOST

COPY requirements.txt ./home
COPY engine ./home/engine

#RUN echo "hello"
#RUN echo "$PWD"
#RUN echo "$ls"

RUN pip install -r ./home/requirements.txt

EXPOSE $SERVER_PORT

#CMD ["uvicorn", "engine.main:app"]
#WORKDIR ./home/

RUN echo "$SERVER_PORT"

CMD ["uvicorn", "home.engine.main:app", "--host", "0.0.0.0", "--port", "7070"]