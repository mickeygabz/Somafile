
import pandas as pd
import numpy as np
# 1. Read and Write file --Tab delimited File
def read_out_csv(filename, fileout):
    """ Returns a tab delimited csv file given a comma delimited csv file or json file

    Args:
    filename: full path of the comma delimited csv file or json file
    fileout: name of the file to return

    Return:
    a tab seprated csv file

    Egs:
    read_out_csv("myfile.csv", "outfile.csv"):
    produces a csv file with the name: outfile in the working directory.

    read_out_csv("myfile.json", "joutfile.csv"):
    produces a csv file with the name: joutfile in the working directory.
    
    """
    if filename.endswith(".json"):
       df=pd.read_json(filename)
    elif filename.endswith(".csv"):
        df = pd.read_csv(filename)
    else:
        raise ValueError("File not recognized.The file is not json nor csv")
    df.to_csv(fileout, sep ='\t')


# 2.Read csv file and Write file --json File
def read_out_json(filename, fileout):
    """ Returns a json file given a csv file

    Args:
    filename: full path of the csv file
    fileout: name of the json file to return

    Return:
    a comma separated csv file

    Egs:
    read_out_json("myfile.csv", "outfile.csv"):
    produces a csv file with the name: outfile in the working directory.
    
    """
    df = pd.read_csv(filename)
    df.to_json(fileout, orient='index')

# 2.5 .Read json file and Write csv file(Comma delimited)
def readjson_out_csv(filename, fileout):
    """ Returns a comma delimited csv file given json file

    Args:
    filename: full path of the json file
    fileout: name of the file to return

    Return:
    a comma separated csv file

    Egs:
    readjson_out_csv("myfile.json", "joutfile.csv"):
    produces a csv file with the name: joutfile in the working directory.
    
    """
    df=pd.read_json(filename)
    df.to_csv(fileout)

# 3. Convert csv and json files to list of tuples
def list_tup (filename):
    """ Returns a list of tuples given a comma delimited csv file or json file

    Args:
    filename: full path of the comma delimited csv file or json file
    fileout: name of the file to return

    Return:
    a list of tuples

    Egs:
    list_tup("myfile.csv"):
    returns data as a list of tuples

    list_tup("myfile.json"):
    returns data as a list of tuples
    
    """
    if filename.endswith(".json"):
       df=pd.read_json(filename)
    elif filename.endswith(".csv"):
        df = pd.read_csv(filename)
    else:
        raise ValueError("File not recognized.The file is not json nor csv")
    df = df.applymap(lambda s:s.lower() if type(s) == str else s)
    records = df.to_records(index=False)
    result = list(records)
    return result

# 4. Convert the csv and json filews to list of dictionaries
def list_dict(filename):
    """ Returns a list of dictionaries given a comma delimited csv file or json file

    Args:
    filename: full path of the comma delimited csv file or json file
    fileout: name of the file to return

    Return:
    a list of tuples

    Egs:
    list_dict("myfile.csv"):
    returns data as a list of dictionaries

    list_tup("myfile.json"):
    returns data as a list of dictionaries
    
    """
    if filename.endswith(".json"):
       df=pd.read_json(filename)
    elif filename.endswith(".csv"):
        df = pd.read_csv(filename)
    else:
        raise ValueError("File not recognized.The file is not json nor csv")
    df = df.applymap(lambda s:s.lower() if type(s) == str else s)
    result = df.to_dict('records')
    return result


#5. Unique Categories in csv and json files
def unique_categ(filename,column_name):
    """ Returns unique categories of a given colum given a comma delimited csv file or json file

    Args:
    filename: full path of the comma delimited csv file or json file
    column _name: variable or column to return unique categories

    Return:
    a list of unique categories

    Egs:
    unique_categ("myfile.csv", "fav_colors"):
    returns a list of unique ites in the fav_colors column

    unique_categ("myfile.json", "fav_colors"):
    returns a list of unique items in the fav_colors column
    """
    if filename.endswith(".json"):
       df=pd.read_json(filename)
    elif filename.endswith(".csv"):
        df = pd.read_csv(filename)
    else:
        raise ValueError("File not recognized.The file is not json nor csv")
    a=df[column_name].tolist()
    result =[]
    for i in a:
        if i not in result:
            result.append(i)
    return result



#6. Count Records for specific grp for tups obtained from code in #3
def count_records(my_tups,grp):
    """ Returns the count of records that have a simmilar grouping based on a certain variable
    Args:
    my_tups: list of tuples obtained from #3(my_tuple=list_tup("myfile.csv"))
    grp: category to check in each record

    Return:
    number of records that fit into that category

    Egs:
    count_records(my_tuple, "male":)
    returns number of records that are male

    """
    result=0
    for i in my_tups:
        if grp in i:
            result+=1
    return result



#7. GGet total of column b for categories in column a from dictionary from #4 in Group
def count_categories(my_dicts,grouping_column):
    """ Returns a dataframe of unique categories and counts for a given categorical variable
    Args:
    my_dicts: list of dictionaries obtained from #4(my_dict=list_dict("myfile.csv"))
    grouping_column: column or variable to obtain categories

    Return:
    a data frame of unique categories and their caounts

    Egs:
    count_categories(my_dict, "gender":)
    returns a data frame of various gender categories and counts in each category

    """
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




