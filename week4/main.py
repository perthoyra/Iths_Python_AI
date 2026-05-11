
from pathlib import Path

from data.Text_Handler import Text_Handler

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"

def main():
    print("Hello World!")

    print(BASE_DIR)
    print(DATA_DIR)

    txt_handler = Text_Handler(DATA_DIR)
        
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()