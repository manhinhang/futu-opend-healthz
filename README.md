# futu-opend-healthz

Health check for futu-opend.

## Build

```bash
docker build -t futu-opend-healthz .
```

## Run

| Environment Variable | Description |
| -------------------- | ----------- |
| FUTU_OPEND_HOST     | futu-opend host |
| FUTU_OPEND_PORT     | futu-opend port |
| FUTU_OPEND_RSA_FILE | futu-opend rsa file |

```bash
docker run -p 8000:8000 -e FUTU_OPEND_HOST=127.0.0.1 \
-e FUTU_OPEND_PORT=11111 \
-e FUTU_OPEND_RSA_FILE=.futu/futu.pem \
-v $(pwd)/.futu:/app/.futu futu-opend-healthz
```
