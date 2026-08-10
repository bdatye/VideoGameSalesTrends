#!/usr/bin/env python3
import pandas as pd

url = "https://gist.githubusercontent.com/designernatan/27da044c6dc823f7ac7fe3a01f4513ed/raw/d15b5c7d7a5efb38750b16ec935fc126ec9a6e79/vgsales.csv"

videoGameData_df = pd.read_csv(url)

print(videoGameData_df.head(10))

#videoGameData_df.to_csv('videoGameData.csv')      #saving video game data to a csv as backup

