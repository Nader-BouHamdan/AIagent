from dotenv import load_dotenv
import os
import pandas as pd
from llama_index import PandasQueryEngine

load_dotenv()

population_path = os.path.join("data", "population.csv")
population_df = pd.read_csv(population_path)

population_query_engine = PandasQueryEngine(df=population_df, verbose=True)

print(population_df.head())
print("yupp")