import pandas as pd
import numpy as np
import random
random.seed(42)

# 定義作業和機器數量
job_count = 10
machine_count = 10

# 為作業和機器分配標識符
jobs = [f"Job{i}" for i in range(1, job_count + 1)]
machines = [f"Machine{j}" for j in range(1, machine_count + 1)]

# 生成job及其加工時間
processing_time_data = []
for job in jobs:
    for machine in machines:
        operation = f"{job}-{machine}"
        processing_time = random.randint(1,100) # 隨機加工時間
        processing_time_data.append([job, machine, processing_time])

# 生成job及其加工順序
sequence_data = []
for job in jobs:
    sequence = random.sample(range(1, machine_count+1), machine_count)  # 隨機產生加工順序
    count = 0
    for machine in machines:
        operation = f"{job}-{machine}"
        Machine_sequence = sequence[count]  # 隨機加工順序
        sequence_data.append([job, machine, Machine_sequence])
        count += 1


# 建立資料框
processing_time_df = pd.DataFrame(processing_time_data, columns=["Job", "Machine", "ProcessingTime"])
sequence_df = pd.DataFrame(sequence_data, columns=["Job", "Machine", "Machinesequence"])

# 使用pivot表格重新排列數據，使每個作業對應到每個機器
processing_time_pivot_df = processing_time_df.pivot(index="Job", columns="Machine", values="ProcessingTime")
sequence_pivot_df = sequence_df.pivot(index="Job", columns="Machine", values="Machinesequence")

# 顯示表格
print('Processing time')
print(processing_time_pivot_df)
print('Machine sequence')
print(sequence_pivot_df)


processing_time_pivot_df.to_csv('Processing_time.csv')
sequence_pivot_df.to_csv('Machine_sequence.csv')