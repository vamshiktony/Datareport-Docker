# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.8-slim-buster

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Update GCC
RUN apt-get update -y && apt-get install -y gcc

# Install pip requirements
ADD requirements.txt .
RUN pip install psutil
RUN python -m pip install -r requirements.txt

WORKDIR /app
ADD . /app

# Switching to a non-root user, please refer to https://aka.ms/vscode-docker-python-user-rights
RUN useradd appuser && chown -R appuser /app
USER appuser

# ENV AWS_ACCESS_KEY_ID="AKIA6B66MSX46SVWHBV3"
# ENV AWS_SECRET_ACCESS_KEY="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"
# ENV ReportName="IRN Doc Details"
# ENV UserLoginId="Ankit1"
# ENV UserGstin="25,1,43,121,130,131,17,23,123,2,127,117,27,26,28,72,31,32,6,7,8,9,10,12,18,15,4,16,20,21,22,24,11,35,37,40,42,44,46,50,51,57,58,60,48,64,67,109,118,122,114,88,62,29,89,39,75,38,78,70,66,95,55,103,19,56,71,86,116,128,115,91,106,41,100,105,87,119,108,92,99,14,63,74,133,90,53,101,65,97,94,79,81,77,54,113,134,34,47,112,102,80,93,96,33,98,36,132,5,110,120,76,3,83,84,85,104,52,126,73,107,82,125"
# ENV Location="11,12,13,14,19,22,26,1,63,88,98,100,38,45,90,91,94,96,85,48,49,55,8,27,28,29,30,31,33,39,35,25,37,40,43,44,46,47,2,32,56,57,59,61,62,64,65,69,70,71,72,73,74,66,76,5,67,78,81,86,82,89,92,0"
# ENV Bu="105,103,98,92,72,13,29,26,25,24,23,22,21,16,15,14,12,1,101,111,112,48,53,104,107,5,2,108,96,58,56,55,0,65,64,83,9,61,36,35,37,27,38,39,40,42,49,46,33,47,50,52,51,54,44,67,66,69,71,74,79,78,81,82,84,76,86,89,91,90,97,102,109,70,75,59,95,106"
# ENV Sbu="0,71,62,11,30,27,26,25,24,23,22,21,20,34,19,10,18,14,13,12,54,1,94,100,101,47,52,96,5,2,98,91,58,59,57,56,55,64,65,63,79,8,36,35,42,37,28,38,60,39,40,43,48,45,33,46,49,51,50,53,44,67,66,69,70,76,77,78,80,74,82,84,86,85,92,95,99,73,89,97"
# ENV fromDate="05/10/2020"
# ENV toDate="05/10/2020"
# ENV UserLoginEmail="rakesh.com007@gmail.com"
# ENV database='{"readonly_host":"irn-stg-db-cluster.cluster-ro-chsjqt1rncee.ap-south-1.rds.amazonaws.com","user":"pocmaster","password":"consider123","database":"demo1_customer_QA","port":"5432"}'
# ENV customer_id=1
# ENV email_sqs_url="https://sqs.ap-south-1.amazonaws.com/966297163257/qa-irn-email-demo1"
# ENV bucket_name="qa-irn-stg-demo1-raw"
# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["python", "DownloadDataReport.py"]
