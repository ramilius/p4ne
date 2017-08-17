import glob

files = glob.glob("C:\\Users\\rusmanov.SUPPORT\\Seafile\\p4ne_training\\config_files\\*.txt")
alist = []
for j in files:
    with open(j) as f:
        for i in f:
            substr = 'ip address'
            position = i.find(substr)
            if position != -1:
                if i != ' no ip address\n':
                    if i != ' ip address dhcp\n':
                        k = i.replace("ip address", "").strip()
                        alist.append(k)


ip = sorted(list(set(alist)))

for p in ip:
    print(p)