s3_buckets = ["test_demo","dev_test","sample_demo"]
print(s3_buckets)
print(s3_buckets[1])
print(len(s3_buckets))
s3_buckets.append("qa_demo")
print(s3_buckets)
s3_buckets.remove("test_demo")
print(s3_buckets)
print(len(s3_buckets))
bucket = s3_buckets[0:2]
print(bucket)
s3_buckets.append("test_demo")
print(s3_buckets + bucket)

list = [3,9,1,0,4]
list.sort()
print(list)
