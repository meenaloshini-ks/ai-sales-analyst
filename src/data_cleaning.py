import pandas as pd


def clean_data(df):

    print("Before Cleaning")
    print("----------------")

    print("Missing Values:")
    print(df.isnull().sum())

    print("\nDuplicate Rows:")
    print(df.duplicated().sum())


    # Remove duplicates
    df = df.drop_duplicates()


    # Remove missing values
    df = df.dropna()


    # Convert Date column
    if "Date" in df.columns:
        df["Date"] = pd.to_datetime(
            df["Date"],
            dayfirst=True
        )


    # Remove unwanted spaces
    for col in df.select_dtypes(include="object"):
        df[col] = df[col].str.strip()


    print("\nAfter Cleaning")
    print("----------------")
    print(df.info())


    return df