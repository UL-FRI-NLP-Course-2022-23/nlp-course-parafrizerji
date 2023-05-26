import numpy as np
import pandas as pd

tabelaPrevedenihStavkov = np.load('prevedeniOdstavki.npy',allow_pickle=True).tolist()
skupna = pd.DataFrame(np.column_stack([tabelaPrevedenihStavkov]))

skupna.to_excel("PrevedeniOdstavki.xlsx")