import pandas as pd

data = pd.read_csv('ip2.csv', index_col=0)
ip_data1 = {
    'ip': ['123.123.123.123', '123.123.123.122'],
    'port': ['5000', '233']
}
ip_data2 = {
    'ip': ['123.123.123.124', '123.123.123.125'],
    'port': ['5000', '244']
}

# def a_append_b(ip_data1, ip_data2):
#     ip_a = ip_data1['ip']
#     port_b = ip_data1['ip']
df_ip1 = pd.DataFrame(ip_data1)
df_ip2 = pd.DataFrame(ip_data2)
# print(df_ip1)
# print(df_ip2)
# data = data.append(df_ip1)
# data = data.append(df_ip2)
# data = pd.merge(data, df_ip1)
# print(data)

data_a = pd.concat([data, df_ip1], axis=0)
# print(data_a)
data_b = pd.concat([data_a, df_ip2], axis=0)
df = data_b.reset_index(drop=True)
# print(df)

for i in range(len(df)):
    ip = df.iloc[[i][0]]
    print(ip[0])
    print(ip[1])

# print(df)
