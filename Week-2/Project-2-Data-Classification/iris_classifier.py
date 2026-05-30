from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, classification_report, f1_score


def load_data():
    iris = load_iris()
    X = iris.data
    y = iris.target
    class_names = iris.target_names
    return X, y, class_names


def explore_data(X, y, class_names):
    print("=" * 60)
    print("  DATASET OVERVIEW")
    print("=" * 60)
    print("  Dataset       : Iris Benchmark")
    print("  Total Samples : " + str(X.shape[0]))
    print("  Features      : " + str(X.shape[1]))
    print("  Classes       : " + str(len(class_names)))
    print("  Class Names   : " + ", ".join(class_names))
    print()
    print("  Features:")
    print("    [0] Sepal Length (cm)")
    print("    [1] Sepal Width  (cm)")
    print("    [2] Petal Length (cm)")
    print("    [3] Petal Width  (cm)")
    print()
    print("  Sample of first 5 rows:")
    for i in range(5):
        print("    " + str(X[i]) + " -> " + class_names[y[i]])
    print()


def split_data(X, y):
    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=0.2,
        random_state=42,
        shuffle=True
    )
    print("=" * 60)
    print("  TRAIN / TEST SPLIT")
    print("=" * 60)
    print("  Total samples  : " + str(len(X)))
    print("  Training set   : " + str(len(X_train)) + " samples (80%)")
    print("  Testing set    : " + str(len(X_test))  + " samples (20%)")
    print()
    return X_train, X_test, y_train, y_test


def scale_features(X_train, X_test):
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled  = scaler.transform(X_test)

    print("=" * 60)
    print("  FEATURE SCALING  (StandardScaler)")
    print("=" * 60)
    print("  Mean before scaling : " + str(X_train.mean().round(2)))
    print("  Mean after scaling  : " + str(X_train_scaled.mean().round(2)))
    print("  Variance after      : " + str(X_train_scaled.var().round(2)))
    print()
    return X_train_scaled, X_test_scaled, scaler


def train_model(X_train_scaled, y_train):
    model = KNeighborsClassifier(n_neighbors=5)
    model.fit(X_train_scaled, y_train)

    print("=" * 60)
    print("  MODEL TRAINING  (K-Nearest Neighbors)")
    print("=" * 60)
    print("  Algorithm     : KNeighborsClassifier")
    print("  K Value       : 5  (Optimal - Elbow Method)")
    print("  Training Done : " + str(len(y_train)) + " samples processed")
    print()
    return model


def evaluate_model(model, X_test_scaled, y_test, class_names):
    predictions = model.predict(X_test_scaled)

    cm = confusion_matrix(y_test, predictions)
    f1 = f1_score(y_test, predictions, average="weighted")
    report = classification_report(y_test, predictions, target_names=class_names)

    print("=" * 60)
    print("  OUTPUT VALIDATION")
    print("=" * 60)

    print()
    print("  Confusion Matrix:")
    print("  (Rows = Actual | Columns = Predicted)")
    print()
    header = "          " + "  ".join([name[:10].center(10) for name in class_names])
    print(header)
    for i, row in enumerate(cm):
        label = class_names[i][:10].ljust(10)
        print("  " + label + "  " + "  ".join([str(val).center(10) for val in row]))
    print()

    print("  Classification Report:")
    print()
    for line in report.strip().split("\n"):
        print("  " + line)
    print()

    print("  F1 Score (Weighted) : " + str(round(f1, 4)))
    print()

    correct = sum(predictions == y_test)
    total   = len(y_test)
    print("  Correct Predictions : " + str(correct) + " / " + str(total))
    print()

    return predictions


def predict_single(model, scaler, class_names):
    print("=" * 60)
    print("  LIVE PREDICTION")
    print("=" * 60)
    print("  Enter flower measurements to classify it.")
    print("  (Press Enter to skip and use default test sample)")
    print()

    try:
        sl = input("  Sepal Length (cm) e.g. 5.1 : ").strip()
        sw = input("  Sepal Width  (cm) e.g. 3.5 : ").strip()
        pl = input("  Petal Length (cm) e.g. 1.4 : ").strip()
        pw = input("  Petal Width  (cm) e.g. 0.2 : ").strip()

        if sl == "" or sw == "" or pl == "" or pw == "":
            sample = [[5.1, 3.5, 1.4, 0.2]]
            print()
            print("  Using default sample: [5.1, 3.5, 1.4, 0.2]")
        else:
            sample = [[float(sl), float(sw), float(pl), float(pw)]]

        sample_scaled = scaler.transform(sample)
        result = model.predict(sample_scaled)
        print()
        print("  Predicted Class : " + class_names[result[0]].upper())
        print()

    except ValueError:
        print("  Invalid input. Skipping live prediction.")
        print()


def main():
    print()
    print("=" * 60)
    print("  IRIS DATA CLASSIFICATION  |  DecodeLabs 2026")
    print("  Algorithm : K-Nearest Neighbors (KNN)")
    print("=" * 60)
    print()

    X, y, class_names = load_data()
    explore_data(X, y, class_names)

    X_train, X_test, y_train, y_test = split_data(X, y)

    X_train_scaled, X_test_scaled, scaler = scale_features(X_train, X_test)

    model = train_model(X_train_scaled, y_train)

    evaluate_model(model, X_test_scaled, y_test, class_names)

    predict_single(model, scaler, class_names)

    print("=" * 60)
    print("  Pipeline Complete.")
    print("=" * 60)
    print()


if __name__ == "__main__":
    main()
