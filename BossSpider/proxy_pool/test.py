import pandas as pd

data = pd.read_csv('ip.csv',index_col=False)
ip_data1 = {
    'ip': ['123.123.123.123'],
    'port': ['5000']
}
ip_data2 = {
    'ip': ['123.123.123.124'],
    'port': ['5000']
}

df_ip1 = pd.DataFrame(ip_data1)
df_ip2 = pd.DataFrame(ip_data2)
print(df_ip1)
print(df_ip2)
data.append(df_ip1)
data.append(df_ip2)

# for i in range(len(data)):
#     ip = data.ix[i][1]
#     print(ip)

print(data)


