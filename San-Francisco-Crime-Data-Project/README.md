How did changing values on the SparkSession property parameters affect the throughput and latency of the data?

Parameters in SparkSession property allows increased and decrease throughput for exmaple "maxOffsetsPerTrigger" limits the offsets processed per trigger interval to a maximum number by default it's unlimited.

What were the 2-3 most efficient SparkSession property key/value pairs? Through testing multiple variations on values, how can you tell these were the most optimal?

I achived optimal resutls with "maxOffsetsPerTrigger" = 10 and "maxOffsetsPerTrigger" = 10. Furthermore, I could increase amount of memory by setting spark.executor.memory: and improve executor parallelism by setting spark.default.parallelism: on executors. 
