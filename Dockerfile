FROM python
WORKDIR /code
RUN pip install flask
EXPOSE 5000
COPY . .
CMD python app.py
