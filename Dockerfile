FROM ubuntu:20.04

RUN apt-get update && apt-get install -y python3-pip

RUN pip3 install pydantic==1.10.2\
                 fastapi==0.95.0\
                 uvicorn==0.20.0\
                 scikit-learn==1.2.1

WORKDIR /app

COPY main.py models.py scaler.pkl model.pkl ./

ENTRYPOINT ["uvicorn", "main:app", "--host=0.0.0.0", "--port=80"]

