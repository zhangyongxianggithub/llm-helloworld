# 准备数据
# openai tools fine_tunes.prepare_data -f ./tune/妇产科-28001.csv -q

# curl https://api.openai.com/v1/files \
#   -H "Authorization: Bearer $OPENAI_API_KEY" \
#   -F purpose="fine-tune" \
#   -F file="@mydata.jsonl"
from openai_base import client

data_file = client.files.create(
    file=open("./妇产科-28001_prepared.jsonl", "rb"), purpose="fine-tune"
)
print(data_file.to_json())
data_list = client.files.list()
print(data_list.to_json())
