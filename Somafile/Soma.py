
import pandas as pd
import numpy as np
# 1. Read and Write file --Tab delimited File
def read_out_csv(filename, fileout):
    df = pd.read_csv(filename)
    df.to_csv(fileout, sep ='\t')


# 2.Read and Write file --json File
def read_out_json(filename, fileout):
    df = pd.read_csv(filename)
    df.to_json(fileout, orient='index')


# 3. Convert files to list of tuples
def list_tup (filename):
    df = pd.read_csv(filename)
    df = df.applymap(lambda s:s.lower() if type(s) == str else s)
    records = df.to_records(index=False)
    result = list(records)
    return result

# 4. Convert the file to list of dictionaries
def list_dict(filename):
    df = pd.read_csv(filename)
    df = df.applymap(lambda s:s.lower() if type(s) == str else s)
    result = df.to_dict('records')
    return result


#5. Unique Groups
def unique_grps(filename):
    df = pd.read_csv(filename)
    a=df['Group'].tolist()
    result =[]
    for i in a:
        if i not in result:
            result.append(i)
    return result

#6. Unique Categories
def unique_categ(filename,column_name):
    df = pd.read_csv(filename)
    a=df[column_name].tolist()
    result =[]
    for i in a:
        if i not in result:
            result.append(i)
    return result



#7. Count Records for specific grp for tups obtained from code in #3
def count_records(my_tups,grp):
    result=0
    for i in my_tups:
        if grp in i:
            result+=1
    return result



#8. GGet total of column b for categories in column a from dictionary from #4 in Group
def count_categories(my_dicts,grouping_column):
    x=[i for i in grouping_column]
    j=np.unique(x)
    mydict={}
    for obj in j:
        count=0
        for k in grouping_column:
            if k== obj:
                count+=1
        mydict[obj]=count
    data_items = mydict.items()

    data_list = list(data_items)
    ndf = pd.DataFrame(data_list, columns=[grouping_column,"Count"])
    return ndf




