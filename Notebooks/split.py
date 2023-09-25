# getting splitted X and y for modelling
def split_data(df):

    #define train, validation and test dataset
    train = df[df['Date'] < "2012-01-06"].reset_index(drop=True)
    validation = df[(df['Date'] >= "2012-01-06") & (df['Date'] <= "2012-06-08")].reset_index(drop=True)
    test = df[df['Date'] > "2012-06-08"].reset_index(drop=True)
 
    #define features and target
    X_train = train.drop(columns=['Weekly_Sales', 'Date'])
    y_train = train['Weekly_Sales']

    X_validation = validation.drop(columns=['Weekly_Sales', 'Date'])
    y_validation = validation['Weekly_Sales']

    X_test = test.drop(columns=['Weekly_Sales', 'Date'])
    y_test = test['Weekly_Sales']  

    # Return the datasets
    return X_train, y_train, X_validation, y_validation, X_test, y_test

def train_val_test(df):

    #define train, validation and test dataset
    train = df[df['Date'] < "2012-01-06"].reset_index(drop=True)
    validation = df[(df['Date'] >= "2012-01-06") & (df['Date'] <= "2012-06-08")].reset_index(drop=True)
    test = df[df['Date'] > "2012-06-08"].reset_index(drop=True)

    # Return the datasets
    return train, validation, test