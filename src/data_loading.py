import pandas as pd


def load_data():
    '''
    loads data from csv file
    :return: a pandas dataframe
    '''
    data = pd.read_csv('Data/Raw/telcom_customer_churn.csv.csv')
    return data



if __name__ == '__main__':
    data =load_data()
    print('Top 5 values')
    print(data.head(), 'n', '_'*30)
    print('Row and column count')
    print(data.shape, '\n', '_'*30)
    print('Column names')
    print(data.columns, '\n', '_'*30)