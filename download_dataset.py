import os
import urllib.request

os.makedirs("data/raw", exist_ok=True)

train_url = "https://raw.githubusercontent.com/mhjabreel/CharCnn_Keras/master/data/ag_news_csv/train.csv"
test_url = "https://raw.githubusercontent.com/mhjabreel/CharCnn_Keras/master/data/ag_news_csv/test.csv"

print("Downloading AG News dataset...")

urllib.request.urlretrieve(
    train_url,
    "data/raw/train.csv"
)

print("✅ train.csv downloaded")

urllib.request.urlretrieve(
    test_url,
    "data/raw/test.csv"
)

print("✅ test.csv downloaded")

print("\n🎉 Dataset ready!")
print("Location: data/raw/")