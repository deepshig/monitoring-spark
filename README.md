
# 2020_group_06_s4210875_s4199456_s4208110

Build the docker image by executing:

```bash
docker build -t 4210875/read-data -f ./Dockerfile .
```


Run the docker image by executing :

```bash
docker run --rm -it 4210875/read-data:latest python3 /work/read_data.py
```