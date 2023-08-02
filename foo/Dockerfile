FROM python:3.10.4
COPY . .
WORKDIR .
RUN pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org --no-cache-dir --upgrade -r requirements.txt
CMD ["python3", "main.py"]