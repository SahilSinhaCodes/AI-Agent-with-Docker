#what image to use
# From image_name:latest

FROM python:latest

#docker build -f .\Dockerfile -t pyapp .
#docker run -it pyapp

#docker build -f Dockerfile -t sahilusesdocker/ai-py-app-test:latest .
#docker push sahilusesdocker/ai-py-app-test:latest

#docker -m http.server 8000
#docker run -it -p 8000:8000 pyapp
CMD ["python","-m","http.server","8000"]