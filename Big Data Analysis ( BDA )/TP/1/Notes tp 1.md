voir page 5 pour les commande de hdfs

un data node est considérer mort au bout de 10min sans contact


crée un environment pour pouvoir installer hdfs : 
    python -m venv myenv
    source myenv/bin/activate
    pip install hdfs


commande a executer pour installer le docker :

```
docker pull liliasfaxi/hadoop-cluster:latest
```

```
docker network create --driver bridge hadoop
```

```
docker run -itd --net=hadoop -p 9870:9870 -p 8088:8088 -p 7077:7077 -p 16010:16010 --name hadoop-master --hostname hadoop-master liliasfaxi/hadoop-cluster:latest
```

```
docker run -itd -p 8040:8042 --net=hadoop --name hadoop-worker1 --hostname hadoop-worker1 liliasfaxi/hadoop-cluster:latest
```

```
docker run -itd -p 8041:8042 --net=hadoop --name hadoop-worker2 --hostname hadoop-worker2 liliasfaxi/hadoop-cluster:latest
```

# need to docker start the container before this commande

```
docker exec -it hadoop-master bash
```

