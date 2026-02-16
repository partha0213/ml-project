from utils import load_model

def predict(input_data):
    model = load_model('model.pkl')
    return model.predict(input_data)

if __name__ == "__main__":
    print("Prediction script ready")
