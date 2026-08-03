# 학습
<<<<<<< HEAD
from src.common import SEED, load_data # 데이터 불러오기 모듈
import joblib
import pandas as pd

MODEL_PATH = "models/analysis1/churn_cluster_model.joblib"

# 저장된 모델 불러오기
def load_model():
    pipeline = joblib.load(MODEL_PATH)

    return pipeline

# 군집 예측
def predict_cluster(pipeline, X):
    cluster = pipeline.predict(X)

    return cluster

# 예측 결과 생성
def make_cluster_result(X, y, cluster):
    result = X.copy()

    result["Cluster"] = cluster
    result["Churn"] = y.values

    return result
=======
from src.common import load_data # 데이터 불러오기 모듈

# 데이터 정제 및 분리 후
# 해당 모듈에서 모델 저장 후 평가 및 고도화 시 모델 블러와서 사용
# 저장 경로 models\analysis1 
# 예시
def test4():
    df = load_data()
    return df.shape

# 해당 페이지를 직접 실행 후 모델 저장
if __name__ == "__main__":
    test4()
>>>>>>> 216054d562f7b743ba18e71e1f7c19e3194538b7
