import pandas as pd
import os


Artifacts_path = "../artifacts/reports"
os.makedirs(Artifacts_path, exist_ok=True)


def basic_eda(data:pd.DataFrame):
    print('\n' + '=' * 60)
    print('Exploratory Data Analysis'.center(60))
    print('='*60)


    print(f'\nDataset Shape: {data.shape}')

    print('\nTarget Variable Distribution')
    print(data['Churn'].value_counts())
    print('\nNumerical Variable Distribution')
    print(data.describe())

    print('\nVariable Distribution')
    print(data['gender'].value_counts())

    print(pd.crosstab(data['gender'], data['Churn']))

    with open('dataset_summary.txt', 'w') as file:
        print('started')
        file.write('\n' + '=' * 60)



        file.write('\nExploratory Data Analysis\n'.center(60))
        file.write('\n' + '=' * 60)
        print('mid')

        file.write(f'\nDataset Shape: {data.shape}')

        file.write('\nTarget Variable Distribution\n')
        file.write(str(data['Churn'].value_counts()))


        file.write('\nVariable Distribution\n')
        file.write(str(data['gender'].value_counts()))




def main():
    from  data_loading import load_data

    data = load_data()
    basic_eda(data)

if __name__ == '__main__':
    main()