import pandas as pd
import matplotlib.pyplot as plt

# 엑셀 파일 불러오기
data = pd.read_excel('./data/elevator_failure_prediction.xlsx')

# 종속변수 'Status'에서 1과 2를 묶어 비정상으로 설정 (0은 정상)
data['Status'] = data['Status'].apply(lambda x: 1 if x in [1, 2] else 0)

# 독립변수 목록 설정
independent_vars = ['Temperature', 'Humidity', 'RPM', 'Vibrations', 'Pressure', 'Sensor2', 'Sensor3', 'Sensor4',
                    'Sensor5']

# 밀도 플롯 생성
fig, axes = plt.subplots(nrows=3, ncols=3, figsize=(12, 13))

for i, var in enumerate(independent_vars):
    ax = axes[i // 3, i % 3]
    for status in data['Status'].unique():
        subset = data[data['Status'] == status]
        label = 'Normal Status' if status == 0 else 'Broken or Recovering'
        subset[var].plot(kind='density', ax=ax, label=label)

    # 그래프 제목에서 "Density Plot of" 제거하고 변수명만 남김
    ax.set_title(var, fontsize=14, fontweight='bold')

    # x축 레이블 설정 (글꼴 크기 작게)
    ax.set_xlabel(var, fontsize=10)

    # y축 레이블 설정 (글꼴 크기 작게)
    ax.set_ylabel('Density', fontsize=10)

    # 범례 설정
    ax.legend(fontsize=10)

    # x축과 y축을 0부터 시작하되 약간의 여백을 줌
    x_min = data[var].min() * 0.95  # x축 최소값에 약간의 여백
    ax.set_xlim(left=x_min)  # x축에 여백을 두기 위한 설정

    y_min = 0 - 0.05  # y축에 약간의 여백을 줌
    ax.set_ylim(bottom=y_min)

    # x축과 y축 눈금의 글꼴 크기 설정
    ax.tick_params(axis='x', labelsize=8)
    ax.tick_params(axis='y', labelsize=8)

# 서브플롯 간격 조정
plt.subplots_adjust(hspace=0.6, wspace=0.4)  # 상하 간격(hspace) 및 좌우 간격(wspace) 설정

plt.savefig('./results/density_plot_selected.png')
plt.show()
