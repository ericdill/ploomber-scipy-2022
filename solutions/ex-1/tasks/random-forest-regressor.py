# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.13.6
# ---

# %% tags=["soorgeon-imports"]
import seaborn as sns
from sklearn.ensemble import RandomForestRegressor
from pathlib import Path
import pickle
import pandas as pd

# %% tags=["parameters"]
upstream = ['train-test-split']
product = None

# %% tags=["soorgeon-unpickle"]
X_test = pickle.loads(Path(upstream['train-test-split']['X_test']).read_bytes())
X_train = pickle.loads(Path(upstream['train-test-split']['X_train']).read_bytes())
y_test = pickle.loads(Path(upstream['train-test-split']['y_test']).read_bytes())
y_train = pickle.loads(Path(upstream['train-test-split']['y_train']).read_bytes())

# %% [markdown]
# ## Random Forest Regressor

  # %%
  # noqa

# %%
rf = RandomForestRegressor()
rf.fit(X_train, y_train)
y_pred = rf.predict(X_test)
sns.scatterplot(x=y_test, y=y_pred)
