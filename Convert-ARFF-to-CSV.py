# import arff
# import pandas as pd

# #pip install liac-arff pandas

# # Load ARFF file
# with open("PhishingData.arff", "r") as f:
#     data = arff.load(f)

# # Convert to DataFrame
# df = pd.DataFrame(data["data"], columns=[attr[0] for attr in data["attributes"]])

# # Save as CSV
# df.to_csv("PhishingData.csv", index=False)

# print("Conversion completed successfully!")

from scipy.io import arff
import pandas as pd

data = arff.loadarff("PhishingData.arff")
df = pd.DataFrame(data[0])
df.to_csv("PhishingData.csv", index=False)

