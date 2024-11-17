import pandas as pd
import chardet
import os
def read_files_in_folder(folder_path):
    coding_s = {}
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            with open(file_path, 'rb') as f:
                encoding = chardet.detect(f.read())['encoding']
                coding_s.setdefault(encoding, 0)
                coding_s[encoding] += 1
    return coding_s

# 示例使用
folder_path = "长春市"
s = read_files_in_folder(folder_path)
df=pd.DataFrame(list(s.items()), columns=['encoding', 'count'], index=None)
print(df.sort_values(by='count', ascending=True).to_string(index=False))
# ascending=True时根据编码方式的出现次数升序输出