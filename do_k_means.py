import numpy as np
import matplotlib.pyplot  as plt
from K_means import k_means
def do_kmeans(data,number_clusters,max_iterations):
    k=number_clusters
    mykean=k_means(data,k)
    mycenter=mykean.init_center()
    iterations=1
    fore_myclu=[]
    while iterations <max_iterations :
        mydist=mykean .get_distance()
        myclu=mykean.get_cluster()
        if myclu==fore_myclu :
            break
        fore_myclu=myclu
        mycenter=mykean.get_center()
        iterations+=1
    return fore_myclu,mycenter

# from sklearn.datasets import load_iris
# iris = load_iris()
# data = iris.data
import pandas as pd
data=pd.read_excel('D:/微信/WeChat/WeChat Files/le201412xx/FileStorage/File/2020-07/K -MEAN]  TEST.xlsx')
data=np.array(data)
#data=np.random.randint(1,30,(30,5))
result,center=do_kmeans(data,5,100)
print('the final result is:')
print(result)
print('the final center is:')
print(center)