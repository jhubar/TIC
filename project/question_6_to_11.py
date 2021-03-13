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

def data_processing(data,name,var0, var1 , var2 = None, var3 = None, dist = True,display = True):
    vec = []
    nb0 = 0
    nb1 = 0
    nb2 = 0
    nb3 = 0
    for i in data[name]:
        if i == var0:
            vec.append(0)
            nb0 +=1
        elif i == var1:
            vec.append(1)
            nb1 +=1
        elif i == var2:
            vec.append(2)
            nb2 +=1
        elif i == var3:
            vec.append(3)
            nb3 +=1

    data[name] = vec

    if display == True:
        if var2 is None and var3 is None:
            if dist == False:
                print(name +" &  " +  str(entropy([nb0/len(vec),nb1/len(vec)])) + " \\\ \hline")
            elif name == "JAU":
                print("\""+name +"\":"+ str([nb0/len(vec),nb1/len(vec),nb2/len(vec),nb3/len(vec)]) +",")
            else:
                print("\""+name +"\":"+ str([nb0/len(vec),nb1/len(vec),nb2/len(vec),nb3/len(vec)]) +",")
        elif var3 is None and var2 is not None:
            if dist == False:
                print(name +" &  " +  str(entropy([nb0/len(vec),nb1/len(vec),nb2/len(vec)]))+ ",")
            else:
                print("\""+name +"\":"+ str([nb0/len(vec),nb1/len(vec),nb2/len(vec),nb3/len(vec)]) +",")
        elif var3 is not None and var2 is not None:
            if dist == False:
                print(name +" &  " +  str(entropy([nb0/len(vec),nb1/len(vec),nb2/len(vec),nb3/len(vec)]))+ " \\\ \hline")
            else:
                print("\""+name +"\":"+ str([nb0/len(vec),nb1/len(vec),nb2/len(vec),nb3/len(vec)]) +",")

def cond_entropy(dist_x_y, dist_data, name = None):
    dist_x_y = np.matrix(dist_x_y)
    print(name +" &  " +str(conditional_entropy(dist_x_y, dist_data['dist'][0]['DIS']))+ " \\\ \hline")

def entropy_of_mediacal_data():
    data = pd.read_csv('P1_medicalDB.csv')
    dist_data = pd.read_json('dist.json')


    head_without_DIS = ['age','sex','obesity','ALC','iron','fatigue','TRI','ALT','AST','GGTP','CHL','AMA','MSC','BIL','ITC','JAU']


    """
    Question 6 : Computation of the entropy of each varible.
    """
    # start_table()
    print("{\"dist\": [")
    print("{")
    data_processing(data,'age', var0 = 'lessorequalthan40', var1 ='morethan40' , dist = True)
    data_processing(data,'sex',var0='man',var1 = 'woman' , dist = True)
    data_processing(data,'obesity',var0 = 'thin', var1 = 'regular', var2= 'overweigh', dist = True)
    data_processing(data,'ALC',var0 = 'yes', var1= 'no', dist = True)
    data_processing(data,'iron', var0 ='low',var1 ='normal',var2 ='high',var3 ='very high', dist = True)
    data_processing(data,'DIS',var0 = 'healthy',var1= 'PBC', var2='steatosis' , dist = True)
    data_processing(data,'fatigue',var0 = 'yes', var1= 'no', dist = True)
    data_processing(data,'TRI', var0 ='abnormal', var1='normal', dist = True)
    data_processing(data,'ALT', var0 ='abnormal', var1='normal', dist = True)
    data_processing(data,'AST', var0 ='abnormal', var1='normal', dist = True)
    data_processing(data,'GGTP',var0 ='abnormal', var1='normal', dist = True)
    data_processing(data,'CHL',var0 ='low',var1 ='normal',var2 ='high', dist = True)
    data_processing(data,'AMA',var0 = 'yes', var1= 'no', dist = True)
    data_processing(data,'MSC',var0 = 'yes', var1= 'no', dist = True)
    data_processing(data,'BIL',var0 ='abnormal', var1='normal', dist = True)
    data_processing(data,'ITC',var0 = 'yes', var1= 'no', dist = True)
    data_processing(data,'JAU',var0 = 'yes', var1= 'no', dist = True)
    print("}]}")
    # end_table(caption = "Entropy of each variable from mediaclDB")


    """
    Question 7 : Computation of the conditional entropy of each varible.
    """



    start_table()
    for i in head_without_DIS:
        cond_entropy(pd.crosstab(data['DIS'],data[i],margins = False,normalize = True),dist_data,name = i)
    end_table(caption = "Conditional entropy of the disease given each variables from mediaclDB")
    


    """
    Question 8 : Computation of the mutual information between the varibles obesity and age.
    """
    # dist_x_y = pd.crosstab(data['obesity'],data['age'],margins = False,normalize = True)
    # print(mutual_information(np.matrix(dist_x_y),dist_data['dist'][0]['obesity'],dist_data['dist'][0]['age']))
    #
    # for i in head_without_DIS:
    #
    #     print("##############################################################")
    #     print(pd.crosstab(data['DIS'],data[i],margins = False,normalize = True))
    #     print("##############################################################")
    #
    # for i in head_without_DIS:
    #     dist_x_y = pd.crosstab(data['DIS'],data[i],margins = False,normalize = True)
    #     print(i +": "+ str( mutual_information(np.matrix(dist_x_y),dist_data['dist'][0]['obesity'],dist_data['dist'][0][i])))
