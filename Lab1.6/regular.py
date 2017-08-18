import glob
import re

def clasificator(line):
    result = 0

    ip_net_match = re.match(' ip address ([0-9]{1,3})\.?([0-9]{1,3})\.?([0-9]{1,3})\.?([0-9]{1,3})\ ([0-9]{1,3})\.?([0-9]{1,3})\.?([0-9]{1,3})\.?([0-9]{1,3})',line)
    if(bool(ip_net_match)):
        ip_mask = ip_net_match.group(1,2,3,4,5,6,7,8)
        ip = ip_mask[0] + '.' +ip_mask[1] + '.' + ip_mask[2] + '.' + ip_mask[3]
        mask = ip_mask[4] + '.' + ip_mask[5] + '.' + ip_mask[6] + '.' + ip_mask[7]
        return ("IP",ip,mask)


    interface_match = re.match('interface (.+)',line)
    if(bool(interface_match)):
        interface =  interface_match.group(1)
        return ("INT",interface)

    hostname_match = re.match('hostname (.+)', line)
    if (bool(hostname_match)):
        hostname = hostname_match.group(1)
        return ("HOST", hostname)

    return ("UNCLASSIFIED",)


files = glob.glob("C:\\Users\\rusmanov.SUPPORT\\Seafile\\p4ne_training\\config_files\\*.txt")
alist = []
for j in files:
    with open(j) as f:
        for i in f:
            a = clasificator(i)
            if a[0] != "UNCLASSIFIED":
                print(a)

