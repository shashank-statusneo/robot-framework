# pulling the python image
FROM python:3.10-alpine

# copy the requirements file into the image
COPY ./requirements.txt /robot-framework/requirements.txt

# switch working directory
WORKDIR /robot-framework

# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt

# copy every content from the local file to the image
COPY . /robot-framework

# configure the container to run in an executed manner
ENTRYPOINT [ "python" ]

CMD ["app.py" ]