FROM python:latest

# set the workind directory
WORKDIR /myDockerFastApp

# install dependencies
COPY ./requirements.txt /myDockerFastApp
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# copy the scripts to th folder
COPY . /myDockerFastApp

# start the server
CMD ["uvicorn", "main:myDockerFastApp", "--host", "0.0.0.0", "--port", "8080"]