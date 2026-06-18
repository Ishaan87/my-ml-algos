import random
import numpy as np

class KMeans():
    def __init__(self, n_clusters, max_iter):
        self.n_clusters = n_clusters
        self.max_iter = max_iter
        self.centroids = None
        self.clusters = None
        
    def fit_predict(self, X):
        self.clusters = np.zeros(X.shape[0], dtype=int)
        random_clusters = random.sample(range(X.shape[0]), self.n_clusters)
        # print(X)
        self.centroids = X[random_clusters]
                
        for i in range(self.max_iter):
            self.assign_clusters(X)
            self.update_centroids(X)
        return self.clusters
    
    def update_centroids(self,X):
        for i in range(self.n_clusters):
            self.centroids[i] = np.mean(X[self.clusters == i], axis=0)
        
    
    def assign_clusters(self, X):
        # print(self.centroids.shape[0])
        for i in range(X.shape[0]):
            dist = np.linalg.norm(X[i] - self.centroids[0])
            self.clusters[i] = 0
            for j in range(1, self.centroids.shape[0]):
                nd = np.linalg.norm(X[i] - self.centroids[j])
                if nd < dist:
                    dist = nd
                    self.clusters[i] = j
        # print(self.clusters)
                