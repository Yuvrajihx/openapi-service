FROM python

WORKDIR /app
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app
EXPOSE 80
# CMD ["python3","app.py"]
CMD ["uvicorn", "app:app","--host","0.0.0.0", "--port", "80"]