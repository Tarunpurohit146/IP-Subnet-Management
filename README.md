# IP Subnet Management

The Python application assigns the IPv4 subnets given a wildcard, start IP address, end IP address, CIDR, and submask. Used for class B and C IP addresses.

## Installation



```bash
pip install argparse pandas

```

## Usage

Run command
```python
python ./subnet.py -h
usage: subnet.py [-h] [-C IP Address Class]

options:
  -h, --help           show this help message and exit
  -C IP Address Class  Pass IP Address Class [B or C]
```
Class C IP address subnetting
```
python ./subnet.py -C C
######### Subnet Allocator - Class C #########
Enter the required network address as [191-244].[0-255].[0-255].0 : 192.168.1.0
Enter number of hosts required in the network [> 0] or Exit(0) : 30
   Wildcard IP Address Start IP Address End  CIDR          Submask
0         5      192.168.1.0   192.168.1.32    27  255.255.255.224
Enter number of hosts required in the network [> 0] or Exit(0) : 30
   Wildcard IP Address Start IP Address End  CIDR          Submask
0         5      192.168.1.0   192.168.1.32    27  255.255.255.224
1         5     192.168.1.32   192.168.1.64    27  255.255.255.224
Enter number of hosts required in the network [> 0] or Exit(0) : 0
```
Class B IP address subnetting
```
python ./subnet.py -C B
######### Subnet Allocator - Class B #########
Enter the required network address as [128-191].[0-255].0.0 : 172.16.0.0
Enter number of hosts required in the network [> 0] or Exit(0) : 16000
14
   Wildcard IP Address Start IP Address End  CIDR        Submask
0        14       172.16.0.0    172.16.64.0    18  255.255.192.0
Enter number of hosts required in the network [> 0] or Exit(0) : 16000
14
   Wildcard IP Address Start IP Address End  CIDR        Submask
0        14       172.16.0.0    172.16.64.0    18  255.255.192.0
1        14      172.16.64.0   172.16.128.0    18  255.255.192.0
Enter number of hosts required in the network [> 0] or Exit(0) : 0
```
