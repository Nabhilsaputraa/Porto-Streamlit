import pandas as pd
import numpy as np

# ================= CONFIG =================
NUM_ROWS = 100  # jumlah baris yang ingin dibuat
OUTPUT_FILE = "dummy_data.csv"

# ================= RANDOM DATA GENERATOR =================
data = {
    "OverallQual": np.random.randint(1, 11, NUM_ROWS),       # 1 - 10
    "GrLivArea": np.random.randint(500, 4000, NUM_ROWS),     # luas rumah
    "GarageCars": np.random.randint(0, 4, NUM_ROWS),         # jumlah mobil
    "GarageArea": np.random.randint(0, 1200, NUM_ROWS),      # luas garasi
    "TotalBsmtSF": np.random.randint(0, 2000, NUM_ROWS),     # basement
    "FirstFlrSF": np.random.randint(0, 3000, NUM_ROWS),      # lantai pertama
    "FullBath": np.random.randint(0, 4, NUM_ROWS),           # kamar mandi penuh
    "TotRmsAbvGrd": np.random.randint(2, 12, NUM_ROWS),     # total rooms
    "YearBuilt": np.random.randint(1900, 2026, NUM_ROWS)     # tahun dibangun
}

df = pd.DataFrame(data)

# ================= SAVE TO CSV =================
df.to_csv(OUTPUT_FILE, index=False)
print(f"✅ Dummy data CSV created: {OUTPUT_FILE} with {NUM_ROWS} rows")
