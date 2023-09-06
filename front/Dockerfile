FROM python:3.9

RUN pip3 install streamlit==1.26.0

WORKDIR /app

COPY app.py ./

ENTRYPOINT ["streamlit", "run", "app.py"]