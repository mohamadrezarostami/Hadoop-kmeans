#! /bin/bash
cat init-clusters.txt > clusters.txt
hdfs dfs -rm -r /p2
hdfs dfs -mkdir /p2
hdfs dfs -copyFromLocal points.csv /p2/
while true
do
	hdfs dfs -rm -r /p2/out.txt
	hadoop jar /home/hadoop/hadoop-2.8.5/share/hadoop/tools/lib/hadoop-streaming-2.8.5.jar -files mapper-cluster.py,reducer-cluster.py,clusters.txt -mapper mapper-cluster.py -reducer reducer-cluster.py -input /p2/points.csv -output /p2/out.txt
	hdfs dfs -cat /p2/out.txt/* > clusters-new.txt
	python3 check-end-conditions.py 2> /dev/null
	if [[ $? == 0 ]]; then
	    break
  	fi
	cat clusters-new.txt > clusters.txt
done

hdfs dfs -rm -r /p2/fit
hadoop jar /home/hadoop/hadoop-2.8.5/share/hadoop/tools/lib/hadoop-streaming-2.8.5.jar -files mapper-kmeans.py,reducer-kmeans.py,clusters-new.txt -mapper mapper-kmeans.py -reducer reducer-kmeans.py -input /p2/points.csv -output /p2/fit
hdfs dfs -cat /p2/fit/* > points-kmeans.txt
cat  points-kmeans.txt | awk '{if($1 != $2) print ERROR,$3,$4;}'
