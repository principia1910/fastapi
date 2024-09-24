FROM python:3.12.6-slim
RUN apt-get update -y && apt-get install -y gcc python3-dev libpq-dev libxml2 libxslt-dev
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
RUN python -m pip install --upgrade pip
RUN pip install wheel

ENV PYTHONWARNINGS=ignore
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
ENTRYPOINT [ "fastapi","run" ]