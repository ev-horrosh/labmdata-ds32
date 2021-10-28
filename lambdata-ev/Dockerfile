# using ubuntu image
FROM ubuntu

ENV PYTHONBUFFER=1

# installing necessary components
RUN apt update && \
apt install -y python3 && \
apt install -y python3-pip && \
apt install -y curl && \
pip3 install numpy pandas

# settting up working dir
WORKDIR /app
# copying files from local dir to a working dir
COPY . /app

# runs python scripts tha uses list to a dataframe
CMD [ "python", "helper_classes.py" ]
