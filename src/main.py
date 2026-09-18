from data_loading import load_data

def main():
    data = load_data()
    print('Row and column count')
    print(data.shape, '\n', '_'*30)



    print('Top 5 values')
    print(data.head(), '\n', '_'*30)

if __name__ == '__main__':
    main()