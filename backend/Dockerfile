From python:3.8
WORKDIR /
RUN pip install spotipy fastapi uvicorn
RUN pip install --upgrade pip
COPY ./main.py /main.py
CMD ["uvicorn", "main:app", "--host", "127.0.0.1", "--port", "8000"]