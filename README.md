This repository demonstrates the CORS/network issue with FastAPI when running inside a docker container.

Essentially, we run two APIs in their own separate containers, exposing respective ports. When running these APIs in 
docker, we are unable to access the 1st API from the 2nd. The 2nd API has an endpoint
that is essentially a redirect to that of the 1st API. We get a `307 Temporary Redirect` response when accessing the
endpoint on 2nd API.

To reproduce the steps, please follow the steps below:

```
# Find out host's internal IP
HOST_IP=$(hostname -I)
echo "Host IP: $HOST_IP"

# Bring up 1st API
cd myapi-1 && docker-compose up -d && cd ..

# Bring up 2nd API
export MYAPI1_URL=http://${HOST_IP}:8000
export MYAPI2_URL=http://${HOST_IP}:8001
cd myapi-2 && docker-compose up -d && cd ..

# Access the 1st API /index endpoint
curl -X GET ${MYAPI1_URL}/index

# Access the 2nd API /index endpoint
curl -v http://${HOST_IP}:8001/index
```

The last command should produce same output as the first command, however, it returns a `307 Temporary Redirect` 
response.

You can make sure that 1st API is indeed reachable from 2nd API docker by logging into its container and querying the
`/index` endpoint of 1st API:

```bash
docker exec -it myapi-2 curl -X GET -v ${MYAPI1_URL}/index
docker exec -it myapi-2 curl -X GET -v ${MYAPI2_URL}/index
```
