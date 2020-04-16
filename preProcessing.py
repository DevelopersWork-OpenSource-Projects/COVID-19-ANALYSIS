import pandas as pd
import sys

def pre_processing(dataset):
    dataset = pd.read_csv(dataset, header=0)

    print("Structure of Data :-")
    print(dataset.dtypes,"\n")

    print("NaN values in the dataset :-")
    print(dataset.isna().sum(),"\n")

    # Considering NaN values as "0"
    dataset['Confirmed'] = dataset['Confirmed'].fillna(0)
    dataset['Deaths'] = dataset['Deaths'].fillna(0)
    dataset['Recovered'] = dataset['Recovered'].fillna(0)
    # finding active cases by confirmed,deaths and recovered
    dataset['Active'] = (dataset['Confirmed'] - dataset['Deaths']) - dataset['Recovered']

    dataset['Province_State'] = dataset['Province_State'].fillna("---")

    dataset["Date"] = pd.to_datetime(dataset['Last_Update']).dt.date

    print("After dataset preprocessing :-")
    print(dataset.isna().sum(),"\n")

    print(dataset.describe(),"\n")

    dataset.to_csv('input/dataset.csv', mode='w',index=False, header=True)

    return dataset

if __name__ == '__main__':
    if len(sys.argv) < 2:
        exit("USAGE:",sys.argv[0],"FILENAME")
    pre_processing(sys.argv[1])