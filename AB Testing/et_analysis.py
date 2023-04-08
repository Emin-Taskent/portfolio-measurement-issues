import joblib
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

# EDA Functions

def check_df(dataframe, head=5, display_=False):
    if not display_:
        print("##################### Shape #####################")
        print(dataframe.shape)
        print("##################### Types #####################")
        print(pd.DataFrame(dataframe.dtypes, columns=["DataType"]))
        print("##################### Head #####################")
        print(dataframe.head(head))
        print("##################### Tail #####################")
        print(dataframe.tail(head))
        print("##################### NA #####################")
        print(pd.DataFrame(dataframe.isnull().sum(), columns=["# of N/A value"]))
        print("##################### Quantiles #####################")
        print(pd.DataFrame(dataframe.quantile([0, 0.01, 0.05, 0.25, 0.50, 0.75, 0.95, 0.99, 1]).T, 
                         columns=[0, 0.01, 0.05, 0.25, 0.50, 0.75, 0.95, 0.99, 1]).round(2))
    
    if display_ == True:
        print("##################### Shape #####################")
        print(dataframe.shape)
        print("##################### Types #####################")
        display(pd.DataFrame(dataframe.dtypes, columns=["DataType"]))
        print("##################### Head #####################")
        display(dataframe.head(head))
        print("##################### Tail #####################")
        display(dataframe.tail(head))
        print("##################### NA #####################")
        display(pd.DataFrame(dataframe.isnull().sum(), columns=["# of N/A value"]))
        print("##################### Quantiles #####################")
        display(pd.DataFrame(dataframe.quantile([0, 0.01, 0.05, 0.25, 0.50, 0.75, 0.95, 0.99, 1]).T, 
                         columns=[0, 0.01, 0.05, 0.25, 0.50, 0.75, 0.95, 0.99, 1]).round(2))

def cat_summary(dataframe, col_name, plot=False, display = False):
    if not display:
        print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                            "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}).round(2))
        print("##########################################")
    if display:
        display(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                            "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}).round(2))
        print("##########################################")
    if plot:
        sns.countplot(x=dataframe[col_name], data=dataframe)
        plt.show(block=True)

def num_summary(dataframe, numerical_col, plot=False):
    quantiles = [0.01, 0.05, 0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90, 0.95, 0.99]
    print(dataframe[numerical_col].describe(quantiles).T)

    if plot:
        dataframe[numerical_col].hist(bins=20)
        plt.xlabel(numerical_col)
        plt.title(numerical_col)
        plt.show(block=True)

def target_summary_with_num(dataframe, target, numerical_col):
    print(dataframe.groupby(target).agg({numerical_col: "mean"}), end="\n\n\n")

def target_summary_with_cat(dataframe, target, categorical_col):
    print(pd.DataFrame({"TARGET_MEAN": dataframe.groupby(categorical_col)[target].mean()}), end="\n\n\n")

def correlation_matrix(df, cols):
    fig = plt.gcf()
    fig.set_size_inches(10, 8)
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)
    fig = sns.heatmap(df[cols].corr(), annot=True, linewidths=0.5, 
                      vmin= -1, vmax= 1, annot_kws={'size': 12}, linecolor='w', cmap="RdBu")
    plt.show(block=True)

def grab_col_names(dataframe, cat_th=10, car_th=20, var_num = False, var_name = False):
    """

    Veri setindeki kategorik, numerik ve kategorik fakat kardinal değişkenlerin isimlerini verir.
    Not: Kategorik değişkenlerin içerisine numerik görünümlü kategorik değişkenler de dahildir.

    Parameters
    ------
        dataframe: dataframe
                Değişken isimleri alınmak istenilen dataframe
        cat_th: int, optional
                numerik fakat kategorik olan değişkenler için sınıf eşik değeri
        car_th: int, optinal
                kategorik fakat kardinal değişkenler için sınıf eşik değeri

    Returns
    ------
        cat_cols: list
                Kategorik değişken listesi
        num_cols: list
                Numerik değişken listesi
        cat_but_car: list
                Kategorik görünümlü kardinal değişken listesi

    Examples
    ------
        import seaborn as sns
        df = sns.load_dataset("iris")
        print(grab_col_names(df))


    Notes
    ------
        cat_cols + num_cols + cat_but_car = toplam değişken sayısı
        num_but_cat cat_cols'un içerisinde.
        Return olan 3 liste toplamı toplam değişken sayısına eşittir: cat_cols + num_cols + cat_but_car = değişken sayısı

    """

    # cat_cols, cat_but_car
    cat_cols = [col for col in dataframe.columns if dataframe[col].dtypes == "O"]
    num_but_cat = [col for col in dataframe.columns if dataframe[col].nunique() < cat_th and
                   dataframe[col].dtypes != "O"]
    cat_but_car = [col for col in dataframe.columns if dataframe[col].nunique() > car_th and
                   dataframe[col].dtypes == "O"]
    cat_cols = cat_cols + num_but_cat
    cat_cols = [col for col in cat_cols if col not in cat_but_car]

    # num_cols
    num_cols = [col for col in dataframe.columns if dataframe[col].dtypes != "O"]
    num_cols = [col for col in num_cols if col not in num_but_cat]

    if var_num:
        print(f"Observations: {dataframe.shape[0]}")
        print(f"Variables: {dataframe.shape[1]}")
        print(f'cat_cols: {len(cat_cols)}')
        print(f'num_cols: {len(num_cols)}')
        print(f'cat_but_car: {len(cat_but_car)}')
        print(f'num_but_cat: {len(num_but_cat)}')

    if var_name:
        print("########## cat_cols ##########")
        print(cat_cols)
        print("########## num_cols ##########")
        print(num_cols)
        print("########## cat_but_car ##########")
        print(cat_but_car)
        print("########## num_but_cat ##########")
        print(num_but_cat)
    
    return cat_cols, num_cols, cat_but_car, num_but_cat


# Data Preprocessing & Feature Engineering Functions

def outlier_thresholds(dataframe, col_name, q1=0.25, q3=0.75):
    quartile1 = dataframe[col_name].quantile(q1)
    quartile3 = dataframe[col_name].quantile(q3)
    interquantile_range = quartile3 - quartile1
    up_limit = quartile3 + 1.5 * interquantile_range
    low_limit = quartile1 - 1.5 * interquantile_range
    return low_limit, up_limit

def replace_with_thresholds(dataframe, variable, q1=0.25, q3=0.75):
    low_limit, up_limit = outlier_thresholds(dataframe, variable, q1=q1, q3=q3)
    dataframe.loc[(dataframe[variable] < low_limit), variable] = low_limit
    dataframe.loc[(dataframe[variable] > up_limit), variable] = up_limit

def check_outlier(dataframe, col_name, q1=0.25, q3=0.75):
    low_limit, up_limit = outlier_thresholds(dataframe, col_name, q1, q3)
    if dataframe[(dataframe[col_name] > up_limit) | (dataframe[col_name] < low_limit)].any(axis=None):
        return True
    else:
        return False

def one_hot_encoder(dataframe, categorical_cols, drop_first=False):
    dataframe = pd.get_dummies(dataframe, columns=categorical_cols, drop_first=drop_first)
    return dataframe
