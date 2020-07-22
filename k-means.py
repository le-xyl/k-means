import numpy as np

class k_means():
    def __init__(self,data,k):
        self.data=data
        self.k=k
    def init_center(self):  #随机选择k个聚类中心
        row,col=np.shape(self.data)  #row为行数，col为列数
        center=np.zeros((self.k,col)) #[[0,0],[0,0]]
        center_index=np.random.randint(1,row+1,self.k)  #[2,10]
        for i in range(self.k):
            center[i]=self.data[center_index[i]]
        self.center=center
        return center
    def get_distance(self):
        row,col=np.shape(self.data)
        distance=np.zeros((row,self.k))  #[[0,0],[0,0],[0,0],..[0,0]]
        for i in range(row):
            for j in range(self.k):
                distance [i,j]=np.sqrt( np.sum((self.data[i]-self.center[j])**2) )
        self.distance=distance  #10行2列
        return distance
    def get_cluster(self):
        row,col=np.shape(self.distance)
        result=[[],[]]
        for i in range(2,col):
            result.append([])
        for i in range(row):
            minposition=np.argmin(self.distance[i])
            result [minposition].append(i)
        self.result=result
        return result
    def get_center(self):
        for i in range(self.k):
            #self.center[i] = np.mean(self.result[i])
            self.center[i]=np.mean(self.data[self.result[i]],axis=0)
        return self.center
