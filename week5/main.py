import matplotlib.pyplot as plt
from pathlib import Path
import pandas as pd
import seaborn as sns
import joblib
# from sklearn.linear_model import LinearRegression
# from sklearn.model_selection import train_test_split

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
OUTPUTS_DIR = BASE_DIR / "outputs"
MODELS_DIR = BASE_DIR / "models"

MODELS_DIR.mkdir(exist_ok=True)
OUTPUTS_DIR.mkdir(exist_ok=True)


def main():
    print("Hello World!")
    sns.set_theme(style="whitegrid")
    fig, ax = plt.subplots(figsize=(8,4))

    ax.set_title("Age and minutes")
    ax.set_xlabel("age")
    ax.set_ylabel("Minutes")

    plt.tight_layout()

    fig.savefig(OUTPUTS_DIR / "demo_train.png")
    plt.show()

    # Close the file when done with it.
    plt.close(fig)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()


# Step 1: Load the model
# model = joblib.load(MODELS_DIR / "model.joblib")
# Setp 2: Create columns
# feature_columns = ["age", "gender"]
# 
# Step 3: Create a dataframe ( maybe from file or db )
# new_examples = pd.DataFrame(
#     data:[
#         [34,1],
#         [20,0]
#     ],
# )
# 
# Step 4: Make a prediction
# predictions = model.predict(new_example)
# 
# Store the result
# results_df = new_example.copy()
# results_df["predicted_minutes"] = prediction.round(1)
# 
# print(results_df)
