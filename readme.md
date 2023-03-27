```bash

docker load --input blockchain.tar

unzip joyce.zip

docker run -it --rm -v /Document/Bio_blockchain/joyce/:/root hipforth/rgbd_map:blockchain bash

cd /root

bash generate.bash

bash recover.bash

```# 1
# 1
