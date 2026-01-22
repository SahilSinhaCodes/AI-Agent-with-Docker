# Common Docker Commands

## Docker-specific
### Clear System

```bash
docker system prune -a
docker image prune -a
```

### Build and Run Locally

Container image tag: `pyapp`

```bash
docker build -f Dockerfile -t pyapp .
```

```bash
docker run -it pyapp
```


### Build and Push to Docker Hub

- Docker Hub Repo/username: codingforentrepreneurs
- Container image name: `ai-py-app-test`
- Container image tag: `v1`

```bash
docker build -f Dockerfile -t codingforentrepreneurs/ai-py-app-test:v1 .
```

```bash
docker push codingforentrepreneurs/ai-py-app-test:v1
# or
docker push codingforentrepreneurs/ai-py-app-test --all-tags
```


## Docker Compose

#### Build with Docker Compose

```
```