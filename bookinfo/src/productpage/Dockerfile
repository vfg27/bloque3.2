FROM python:3.5.7
COPY /root/bloque3.2/bookinfo/src/productpage ./
WORKDIR ./productpage
RUN ls -l 
ENV GROUP_NUMBER '47'
RUN pip3 install -r ./requirements.txt
EXPOSE 9080
CMD ["python3", "./productpage.py", "9080"]
