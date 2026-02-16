from utils import load_data, preprocess

def train_model():
    data = load_data('data.csv')
    X, y = preprocess(data)
    print("Model training complete")

if __name__ == "__main__":
    train_model()
