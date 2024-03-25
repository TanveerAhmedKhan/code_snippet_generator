FROM python

WORKDIR /app

# Install app dependencies
COPY src/requirements.txt ./
RUN pip install -r requirements.txt


COPY src ./