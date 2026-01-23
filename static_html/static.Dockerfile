#what image to use
# From image_name:latest

FROM python:latest

WORKDIR /app

# COPY local_folder container_folder
# RUN mkdir -p /static_folder
# COPY ./static_html /static_folder
# RUN echo "hello" > index.html
#docker build -f .\Dockerfile -t pyapp .
#docker run -it pyapp

# same destination is /app
# COPY ./static_html /app
COPY ./src .

#docker build -f Dockerfile -t sahilusesdocker/ai-py-app-test:latest .
#docker push sahilusesdocker/ai-py-app-test:latest

#docker -m http.server 8000
#docker run -it -p 8000:8000 pyapp
CMD ["python","-m","http.server","8000"]