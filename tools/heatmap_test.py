import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 엑셀 파일 이름
excel_file = "your_excel_file.xlsx"

# 엑셀 데이터 불러오기
data = pd.read_excel(excel_file)

# 시간 정보
time_index = data["datetime"]

# 지점 정보
location_index = [10, 11, 12, 4, 5, 6, 7, 8, 9]

# 측정 조도 및 예측 조도 데이터
measured_illuminance_data = data.filter(like="tual_Illum")
predicted_illuminance_data = data.filter(like="icted_Illum")

# 히트맵 생성 함수
def create_heatmap(time, location, illuminance):
    # 1조도맵 행렬 설정
    illuminance_map = np.zeros((3, 3))

    # 지점 10~12에 해당하는 행렬 위치 설정
    if location in [10, 11, 12]:
        row_index = 0
    # 지점 4~6에 해당하는 행렬 위치 설정
    elif location in [4, 5, 6]:
        row_index = 1
    # 지점 7~9에 해당하는 행렬 위치 설정
    else:
        row_index = 2

    # 열 위치 설정
    col_index = (location - 1) % 3

    # 측정 조도 또는 예측 조도 값을 행렬에 저장
    illuminance_map[row_index][col_index] = illuminance

    return illuminance_map

# 시간별 히트맵 생성 및 시각화
for time, illuminance_data in measured_illuminance_data.groupby("datetime"):
    # 측정 조도 히트맵 생성
    measured_illuminance_map = create_heatmap(time, location_index, illuminance_data)

    # 예측 조도 히트맵 생성
    predicted_illuminance_map = create_heatmap(time, location_index, predicted_illuminance_data[time])

    # 측정 조도 히트맵 시각화
    plt.subplot(121)
    plt.imshow(measured_illuminance_map, cmap="hot")
    plt.title(f"Measured Illuminance ({time})")
    plt.xticks(np.arange(3), location_index[::3])
    plt.yticks(np.arange(3), [10, 4, 7])

    # 예측 조도 히트맵 시각화
    plt.subplot(122)
    plt.imshow(predicted_illuminance_map, cmap="hot")
    plt.title(f"Predicted Illuminance ({time})")
    plt.xticks(np.arange(3), location_index[::3])
    plt.yticks(np.arange(3), [10, 4, 7])

    plt.show()
