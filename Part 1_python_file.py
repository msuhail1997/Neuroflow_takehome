
import pandas as pd
df = pd.read_csv("/content/drive/MyDrive/Neuroflow/phq_all_final.csv")  ## Please enter the path of the csv file

df.head()

df.patient_id.unique()

df.shape
unique_ids=df.patient_id.unique()

"""## REMOVE DUPLICATE COLUMNS"""

orig_cols = df.columns
display(df.shape)
keep_df = df.T.drop_duplicates().T
display(keep_df.shape)
keep_cols = list(keep_df.columns)
dup_cols = list(set(orig_cols) - set(keep_cols))
print(dup_cols)

"""## MISSING VALUES"""

missing_counts = df.isna().sum()
print(missing_counts)

"""## DATA VISUALIZATION"""

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline
from dateutil.parser import parse
import matplotlib.pyplot as plt
def visualize(val):
  x=[]
  y=[]
  j=0
  for i in range(len(df)):
    if (df['patient_id'][i]==int(val)):
      datetime_obj1 = parse(df['patient_date_created'][i])
      datetime_obj2= parse(df['date'][i])
      diff = datetime_obj2 - datetime_obj1
      x.append(diff.total_seconds())
      y.append(df['score'][i])
  plt.plot(x, y, label = val,marker='o')
  plt.xlabel('Time Difference (sec)')
  plt.ylabel('GAD-7 Scores')
  plt.title('GAD- 7 vs Time (Patient ID: ' + val + ')')
  plt.show()

val = input("Enter patient_id: ")
if int(val) not in unique_ids:
  print('ID not found')
else:

  visualize(val)
