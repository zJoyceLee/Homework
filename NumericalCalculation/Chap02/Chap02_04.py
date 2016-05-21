d={"a":0,"b":1,"c":2,"d":2,"f":4}
print(d)
mykey=raw_input("please input the key: ")

if d.has_key('%s'%mykey):
    print("key:%s->val:%d"%(mykey,d.get('%s'%mykey)))
else:
    print("Not In.")
