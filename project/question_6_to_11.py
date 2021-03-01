"""
ELEN060-2
2020 - 2021
Information and coding theory
Project 1 - Information measures
François LIEVENS - 20103816
Julien HUBAR - 10152485
Implementation of question 6 to 11
"""
from question_1_to_5 import *

def start_table():
    print("\\begin{table}[H]")
    print("\centering")
    print("\\begin{tabular}{|c|c|}")
    print("\hline")

def end_table(caption=None):
    print("\end{tabular}")
    print("\caption{"+caption+"}")
    print("\label{tab:my_label}")
    print("\end{table}")

def data_processing(data,name, var1 , var2 = None, var3 = None, dist = False,display = False):
    vec = []
    nb0 = 0
    nb1 = 0
    nb2 = 0
    nb3 = 0
    for i in data[name]:
        if i == var1:
            vec.append(0)
            nb1 +=1
        elif i == var2:
            vec.append(0)
            nb2 +=1
        elif i == var3:
            vec.append(0)
            nb3 +=1
        else:
            vec.append(1)
            nb0 +=1
    data[name] = vec
    if display == True:
        if var2 is None:
            if dist == False:
                print(name +" &  " +  str(entropy([nb0/len(vec),nb1/len(vec)])) + " \\\ \hline")
            else:
                print("{"+name +":" +  str([nb0/len(vec),nb1/len(vec),nb2/len(vec)]) + "},")
        elif var3 is None and var2 is not None:
            if dist == False:
                print(name +" &  " +  str(entropy([nb0/len(vec),nb1/len(vec),nb2/len(vec)]))+ ",")
            else:
                print("{"+name +":" +  str([nb0/len(vec),nb1/len(vec),nb2/len(vec)]) +"},")
        elif var3 is not None and var2 is not None:
            if dist == False:
                print(name +" &  " +  str(entropy([nb0/len(vec),nb1/len(vec),nb2/len(vec),nb3/len(vec)]))+ " \\\ \hline")
            else:
                print("{"+name +":"+ str([nb0/len(vec),nb1/len(vec),nb2/len(vec),nb3/len(vec)]) +"},")

def cond_entropy(dist_x_y, dist_data, name = None):
    vec1 = np.array(dist_x_y[1]) #age
    vec2 = np.array(dist_x_y[0]) #dis
    dist_x_y = np.matrix([vec1,vec2])
    print(name +" &  " +str(conditional_entropy(dist_x_y, dist_data['dist'][0]['DIS']))+ " \\\ \hline")

def entropy_of_mediacal_data():
    data = pd.read_csv('P1_medicalDB.csv')
    dist_data = pd.read_json('dist.json')


    start_table()
    data_processing(data,'age','lessorequalthan40', dist = True)
    data_processing(data,'sex','man', dist = True)
    data_processing(data,'obesity','thin','regular', dist = True)
    data_processing(data,'ALC','no', dist = True)
    data_processing(data,'iron','low','normal','high', dist = True)
    data_processing(data,'DIS','healthy','PBC', dist = True)
    data_processing(data,'fatigue','no', dist = True)
    data_processing(data,'TRI','normal', dist = True)
    data_processing(data,'ALT','normal', dist = True)
    data_processing(data,'AST','normal', dist = True)
    data_processing(data,'GGTP','normal', dist = True)
    data_processing(data,'CHL','low','normal', dist = True)
    data_processing(data,'AMA','no', dist = True)
    data_processing(data,'MSC','no', dist = True)
    data_processing(data,'BIL','normal', dist = True)
    data_processing(data,'ITC','no', dist = True)
    data_processing(data,'JAU','no', dist = True)
    end_table(caption = "Entropy of each variable from mediaclDB")

    start_table()
    cond_entropy(pd.crosstab(data['age'],data['DIS'],margins = False,normalize = True),dist_data,name = 'age')
    cond_entropy(pd.crosstab(data['sex'],data['DIS'],margins = False,normalize = True),dist_data,name = 'sex')
    cond_entropy(pd.crosstab(data['obesity'],data['DIS'],margins = False,normalize = True),dist_data,name = "obesity")
    cond_entropy(pd.crosstab(data['ALC'],data['DIS'],margins = False,normalize = True),dist_data,name = "ALC")
    cond_entropy(pd.crosstab(data['iron'],data['DIS'],margins = False,normalize = True),dist_data,name = "iron")
    cond_entropy(pd.crosstab(data['fatigue'],data['DIS'],margins = False,normalize = True),dist_data,name = "fatigue")
    cond_entropy(pd.crosstab(data['TRI'],data['DIS'],margins = False,normalize = True),dist_data,name = "TRI")
    cond_entropy(pd.crosstab(data['ALT'],data['DIS'],margins = False,normalize = True),dist_data,name = "ALT")
    cond_entropy(pd.crosstab(data['AST'],data['DIS'],margins = False,normalize = True),dist_data,name = "AST")
    cond_entropy(pd.crosstab(data['GGTP'],data['DIS'],margins = False,normalize = True),dist_data,name = "GGTP")
    cond_entropy(pd.crosstab(data['CHL'],data['DIS'],margins = False,normalize = True),dist_data,name = "CHL")
    cond_entropy(pd.crosstab(data['AMA'],data['DIS'],margins = False,normalize = True),dist_data,name = "AMA")
    cond_entropy(pd.crosstab(data['MSC'],data['DIS'],margins = False,normalize = True),dist_data,name = "MSC")
    cond_entropy(pd.crosstab(data['BIL'],data['DIS'],margins = False,normalize = True),dist_data,name = "BIL")
    cond_entropy(pd.crosstab(data['ITC'],data['DIS'],margins = False,normalize = True),dist_data,name = "ITC")
    cond_entropy(pd.crosstab(data['JAU'],data['DIS'],margins = False,normalize = True),dist_data,name = "JAU")
    end_table(caption = "Conditional entropy of the disease given each variables from mediaclDB")


    dist_x_y = pd.crosstab(data['obesity'],data['age'],margins = False,normalize = True)
    vec1 = np.array(dist_x_y[1]) #age
    vec2 = np.array(dist_x_y[0]) #dis
    dist_x_y = np.matrix([vec1,vec2])

    print(mutual_information(dist_x_y, dist_data['dist'][0]['obesity'],dist_data['dist'][0]['age']))
