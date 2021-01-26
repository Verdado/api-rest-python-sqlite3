# set base image (host OS)
FROM python:3.8

# install dependencies
RUN pip install Flask && \
  pip install jsonify && \
  pip install pysqlite3 && \
  pip install requests && \
  pip install make_response

# copy the content of the local src directory to the working directory
#COPY ./* ./events_api/

WORKDIR ./events_api

# command to run on container start
#CMD [ "python3", "./main.py" ]
