
FROM python
EXPOSE 5000
WORKDIR /usr/src/app
RUN pip install Flask 
RUN pip install Requests
RUN pip install mysql-connector
COPY . .
CMD python app.py