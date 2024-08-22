import pandas as pd
import matplotlib.pyplot as plt

# 엑셀 파일 불러오기
data = pd.read_excel('./data/elevator_failure_prediction.xlsx')

# 종속변수 'Status'에서 1과 2를 묶어 비정상으로 설정 (0은 정상)
data['Status'] = data['Status'].apply(lambda x: 1 if x in [1, 2] else 0)

# 독립변수 목록 설정
independent_vars = ['Temperature', 'Humidity', 'RPM', 'Vibrations', 'Pressure', 'Sensor2', 'Sensor3', 'Sensor4', 'Sensor5']

# 밀도 플롯 생성
fig, axes = plt.subplots(nrows=3, ncols=3, figsize=(12, 13))

for i, var in enumerate(independent_vars):
    ax = axes[i // 3, i % 3]
    for status in data['Status'].unique():
        subset = data[data['Status'] == status]
        subset[var].plot(kind='density', ax=ax, label=f'Status {status}')
    ax.set_title(f'Density Plot of {var}')
    ax.set_xlabel(var)
    ax.set_ylabel('Density')
    ax.legend()

plt.tight_layout()
plt.savefig('./results/density_plot_selected.png')
plt.show()
