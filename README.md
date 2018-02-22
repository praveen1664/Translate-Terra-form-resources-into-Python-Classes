# Translate-Terra-form-resources-into-Python-Classes

# terra-py
Translate terraform resources into python classes


Example: 
Python

``` 
➜  terra-py git:(master) ✗ python
Python 2.7.10 (default, Jul 14 2015, 19:46:27)
[GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.39)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import json
>>> import tf_plan
>>> 
>>> args = {'region':'us-west-1', 'name':'isa-nat', 'subnetId':'subnet-12345678', 'keyName':'isa_keypair'}
>>> 
>>> nat = tf_plan.tfNatInstance(args)
>>># terra-py
Translate terraform resources into python classes


Example: 
Python

``` 
➜  terra-py git:(master) ✗ python
Python 2.7.10 (default, Jul 14 2015, 19:46:27)
[GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.39)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import json
>>> import tf_plan
>>> 
>>> args = {'region':'us-west-1', 'name':'isa-nat', 'subnetId':'subnet-12345678', 'keyName':'isa_keypair'}
>>> 
>>> nat = tf_plan.tfNatInstance(args)
>>> 
>>> print nat.id
${aws_instance.isa-nat.id}
>>> 
>>> print json.dumps(nat.terraform, indent=2)
{
  "isa-nat": {
    "ami": "ami-004b0f60",
    "instance_type": "t2.micro",
    "provider": "aws.us-west-1",
    "subnet_id": "subnet-12345678",
    "key_name": "isa_keypair",
    "tags": {
      "Name": "isa-nat"
    },
    "associate_public_ip_address": true
  }
}
>>>
```


>>> print nat.id
${aws_instance.isa-nat.id}
>>> 
>>> print json.dumps(nat.terraform, indent=2)
{
  "isa-nat": {
    "ami": "ami-004b0f60",
    "instance_type": "t2.micro",
    "provider": "aws.us-west-1",
    "subnet_id": "subnet-12345678",
    "key_name": "isa_keypair",
    "tags": {
      "Name": "isa-nat"
    },
    "associate_public_ip_address": true
  }
}
>>>
```

