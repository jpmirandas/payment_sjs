import pandas as pd

if __name__ == "__main__":

    # read the csv file
    df = pd.read_csv("salary.csv")

    # which columns should be used in the searchs
    df_select = df[["name", "job", "relation", "place", "working_hours", "salary"]]

    # search for employee name
    # print(df[df["name"].str.contains("DALVA")])

    # max salary
    # max_salary = df["salary"].max()
    # print(df_select[df_select["salary"] == max_salary])

    # the biggest salaries by job
    # print(df_select.groupby("job").max().to_string())

    # show the employees sorted by salary
    df.sort_values(by="salary", ascending=False, inplace=True)

    # TODO: find a way to print money formatted)
    df["salary"] = df["salary"].apply(str)
    df["salary"] = df["salary"].apply(lambda x: x[:-2] + "," + x[-2:])
    df["salary"] = df["salary"].apply(lambda x: x[:-6] + "." + x[-6:] if len(x) >= 7 else x)
    df["salary"] = df["salary"].apply(lambda x: "R$ " + x)
    print(df.to_string())


