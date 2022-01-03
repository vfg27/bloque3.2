FROM python:3.5.7
RUN mkdir app
COPY ./* ./app/
WORKDIR ./app
RUN ls -l 
ENV GROUP_NUMBER '47'
RUN pip3 install -r ./app/requirements.txt
EXPOSE 9080
CMD ["python3", "./app/productpage.py", "9080"]
