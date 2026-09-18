import pandas as pd


def basic_eda(data:pd.DataFrame):
    print('\n''+''='*60)
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


def main():
    from  data_loading import load_data

    data = load_data()
    basic_eda(data)

if __name__ == '__main__':
    main()