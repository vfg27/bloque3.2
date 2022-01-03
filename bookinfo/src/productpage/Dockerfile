FROM python:3.5.7
RUN os.mkdir("app")
COPY ./* ./app
ENV GROUP_NUMBER '47'
RUN pip3 install -r requirements.txt
EXPOSE 9080
CMD ["python3", "productpage.py", "9080"]
