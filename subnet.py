import argparse
from pprint import pprint
import pandas as pd

def check(s,val,up_count,ip):
    flag=True
    if val>130:
        ip[-2]+=1
        ips=".".join(map(str,ip[:-1]))+".0"
        ip[-2]+=1
        ipe=".".join(map(str,ip[:-1]))+".0"
        ip[-2]-=2
        return ips,ipe
    if s != []:
        for i in range(len(s)):
            if val <= s[i][0]:
                ip[-2]=s[i][1]
                ips=".".join(map(str,ip[:-1]))+f".{256-s[i][0]}"
                ip[-1]=val+(256-s[i][0])
                s[i][0]-=val
                if s[i][0] == 0:
                    s.pop(i)
                    ip[-2]+=1
                    ip[-1]=0
                    up_count+=ip[-2]
                ipe=".".join(map(str,ip))
                flag=False
                break
        if flag==True:
            ip[-2]+=1
            ip[-1]=0
            ips=".".join(map(str,ip))
            ip[-1]=val
            ipe=".".join(map(str,ip))
            s.append([256-val,ip[-2]])
    else:
        ips=".".join(map(str,ip))
        ip[-1]+=val
        ipe=".".join(map(str,ip))
        s.append([256-val,ip[-2]])
    if s:
        up_count+=s[-1][1]
    return ips,ipe
       
def ip_class_c(df):
    count=0
    print('######### Subnet Allocator - Class C #########')
    ip=list(map(int,input("Enter the required network address as [191-244].[0-255].[0-255].0 : ").split(".")))
    if (ip[0]>191 and ip[0] < 244) and (ip[1]>0) and (ip[2]>0) and (ip[-1]==0):
        while True:
            host=int(input("Enter number of hosts required in the network [> 0] or Exit(0) : "))
            if host==0:
                exit()
            wildcard=host.bit_length()
            count+=(2**wildcard)
            if count<=256:
                CIDR=32-wildcard
                ip_start=".".join(list(map(str,ip)))
                ip[-1]+=(2**wildcard)
                ip_end=".".join(list(map(str,ip)))
                submask="255.255.255."+str(256-(2**wildcard))
                df.loc[len(df.index)]=[wildcard,ip_start,ip_end,CIDR,submask]
                df.sort_index(inplace=True)
                print(df)
            else:
                count-=(2**wildcard)
                print(f"Unable to subnet\nTotal host remaining {256-count}")
    else:
        print("Enter Valid Class C IP Address")

def ip_class_b(df):
    count=up_count=0
    remain=0
    s=list()
    print('######### Subnet Allocator - Class B #########')
    ip=list(map(int,input("Enter the required network address as [128-191].[0-255].0.0 : ").split(".")))
    if (ip[0]>128 and ip[0]<191) and (ip[1]>0) and (ip[2]==0) and (ip[3]==0):
        while True:
            host=int(input("Enter number of hosts required in the network [> 0] or Exit(0) : "))
            if host==0:
                exit()
            wildcard=host.bit_length()
            count+=2**wildcard
            CIDR=32-wildcard
            if count<=65536:
                host_can_have=2**wildcard
                if host_can_have<=256:     
                    ip_start,ip_end=check(s,host_can_have,up_count,ip)
                    submask=f"255.255.255.{256-(2**wildcard)}"
                    df.loc[len(df.index)]=[wildcard,ip_start,ip_end,CIDR,submask]
                    df.sort_index()
                else:
                    print(wildcard)
                    ip_start=".".join(map(str,ip))
                    ip[-2]+=host_can_have//256
                    ip_end=".".join(map(str,ip))
                    submask=f"255.255.{256-(2**(wildcard-8))}.0"
                    df.loc[len(df.index)]=[wildcard,ip_start,ip_end,CIDR,submask]
                    df.sort_index()
            else:
                print(f"can't assign")
                count-=2**wildcard
            pprint(df)   
    else:
        print("Enter Valid Class B IP Address")
if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("-C",metavar="IP Address Class",help="Pass IP Address Class [B or C]")
    arg=parser.parse_args()
    if arg.C=="B":
        df=pd.DataFrame(columns=["Wildcard","IP Address Start","IP Address End","CIDR","Submask"])
        ip_class_b(df)
    elif arg.C=="C":
        df=pd.DataFrame(columns=["Wildcard","IP Address Start","IP Address End","CIDR","Submask"])
        ip_class_c(df)
    else:
        parser.print_help()