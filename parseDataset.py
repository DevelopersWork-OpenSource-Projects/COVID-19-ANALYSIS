import pandas as pd

def parse_datasets():
    # read csv files
    datasets = []
    for month in range(1,5):
        month = "0" + str(month)
        for day in range(1,32):
            try:
                if day < 10:
                    day = "0" + str(day)
                else:
                    day = str(day)
                filename = "./datasets/COVID-19-master/csse_covid_19_data/csse_covid_19_daily_reports/"+month+"-"+day+"-2020.csv"
                
                data = pd.read_csv(filename, header=0)
                data = data.rename(columns={
                    'Province/State': 'Province_State',
                    'Country/Region': 'Country_Region',
                    'Last Update': 'Last_Update',
                    'Lat' : "Latitude",
                    'Long_' : 'Longitude'
                })
                data['Last_Update'] = data['Last_Update'].astype("string") 
                data.set_index('Last_Update')
                datasets.append(data)
                # print(data.shape)
                # print(filename)
            except Exception as e: 
                # print(e)
                # break
                continue
    print("Total CSV files Read:",len(datasets),"\n")
    
    dataset = pd.concat(datasets, axis=0)
    dataset = dataset.drop(['Combined_Key','Admin2','FIPS'],1)
    dataset = dataset.drop(['Latitude','Longitude'],1)
    dataset.to_csv('input/dataset.csv', mode='w',index=False, header=True)
    
    return dataset

if __name__ == '__main__':
    dataset = parse_datasets()

    from preProcessing import pre_processing
    dataset = pre_processing('input/dataset.csv')

    print(dataset.describe())