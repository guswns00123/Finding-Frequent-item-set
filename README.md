# Finding-Frequent-item-set

* Task
  1. A-priori algorithm을 사용하여 Single machine에서 frequent pair 찾기
     
  2. SON algorithm을 MapReduce에서 사용하여 frequent pair 찾기
     
  3. SON algorithm을 MapReduce에서 사용하여 frequent triplets 찾기
     
  4. PCY algorithm을 사용하여 candidate pair 분류하기
</br>

* Implementation
  
  a. Run mapper, reducer file
   ```sh
   hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
	-D mapred.output.key.comparator.class=org.apache.hadoop.mapred.lib.KeyFieldBasedComparator \
  -D mapred.job.name='job' \
  -D mapred.map.tasks = 20 \
	-D mapred.reduce.tasks = 10 \
	-file ./hw2/mapper1.py -mapper mapper1.py \
  -file ./hw2/reducer1.py -reducer reducer1.py \
	-input ./hw2/yelp_review \
	-output ./hw2/output1
   ```
   
  b. Move input file
  ```sh
  hdfs dfs -copyFromLocal hw2/yelp_review ./hw2
  ```

  c. check output file
  ```sh
  hdfs dfs -cat hw2/output1/part-00000 | head -10
  ```

  d. Remove output file
  ```sh
  hdfs dfs -rm -r ./hw2/output1
  ```
