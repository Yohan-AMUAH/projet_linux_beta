#!/usr/bin/python

import pandas as pd
#import sys

#sys.path.append("./data_processor")

data = pd.read_csv("historical_data.csv")
import data_processor
[annual_return,standard_deviation]=data_processor.processor(data)
liste=[[annual_return,standard_deviation]]
resultats=pd.DataFrame(liste, columns=["annual_return","standard_deviation"])
resultats.to_csv("resultats.csv",index=False)
#return(annual_return,standard_deviation)
