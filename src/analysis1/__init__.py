<<<<<<< HEAD
from .eda import (
    get_cluster_data,
    get_descriptive_stats,
    get_missing_values,
    get_duplicate_count,
    get_feature_name_mapping,
    plot_feature_distribution,
    plot_correlation,
)

from .train import (
    load_model,
    predict_cluster,
    make_cluster_result
)

from .evaluate import (
    validate_model,
    plot_validation,
    get_cluster_mean,
    plot_cluster_feature,
    evaluate_cluster_churn,
    plot_cluster_churn,
    plot_cluster_pca,
    validate_model,
    plot_validation,
    validate_k,
    plot_k_validation,
)

from .advanced import (
    train_upgrade_model,
    evaluate_upgrade,
    compare_before_after,
    plot_before_after,
    validate_k_upgrade,
    plot_k_validation_upgrade
)
=======
# 예시 추후 수정
from .eda import test2 as eda_test
from .evaluate import test3 as evaluate_test

# 사용법
"""
from src.analysis1 import eda_test, evaluate_test
"""
>>>>>>> 216054d562f7b743ba18e71e1f7c19e3194538b7
