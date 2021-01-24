# docker pytorch-mnoavx
A docker container with latest pytorch that works in GPU for CPUs without AVX instructions (mon-avx flag).

## How to build
```bash
docker build -f Dockerfile -t pytorch-mnoavx .
```

## How to run
We run the container by specifying your user's userid, to avoid to run as root, which can cause new files in
mounted volumes to be created as the root user on your host machine.

```bash
cd docker-gpu-mnoavx/pytorch/
docker run --user $(id -u):$(id -g) --rm -it -d -v `pwd`/src:/app --gpus all --name pytorch-mnoavx-dev pytorch-mnoavx
docker exec -it pytorch-mnoavx-dev bash
```

## Example
An example of training status and `nvidia-smi` command output.
![Screenshot from 2021-01-24 11-50-46](https://user-images.githubusercontent.com/163333/105640670-8af37280-5e7f-11eb-9766-efdc3ddf58c9.png)

## Configuration tested
In the following the configurations that have been tested so far

- Mobo: Foxconn DG33M03 (Dell Inspiron 530) Micro-ATX
- Chipset: Intel G33 Express
- PSU: Foxconn Foxpower ATX 400W
- CPU: Intel Core 2 Quad Core Q9550 / Q6600 - LGA775
- GPU: Zotac GeForce GTX 1050 Ti 4GB
- HDD: Samsung EVO 860 SSD
- 8GB DDR2
