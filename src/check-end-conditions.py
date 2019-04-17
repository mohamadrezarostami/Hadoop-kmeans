#!/usr/bin/python3
import sys 

CLUSTERS_FILENAME = 'clusters.txt'
CLUSTERS_NEW_FILENAME = 'clusters-new.txt'

max_diff = 0.01
delta_clusters = dict()

def read_from_clusters_cache_file(clusters_file):
    f = open(clusters_file, 'r')
    data = f.read()
    f.close()
    del f
    return data

def read_clusters():
    cluster_data = read_from_clusters_cache_file(CLUSTERS_FILENAME)
    cluster_new_data = read_from_clusters_cache_file(CLUSTERS_NEW_FILENAME)

    for line in cluster_data.strip().split("\n"):
        data = line.strip().split("\t")
        centroid_id, coords = data
        latitude, longitude = coords.strip().split(";")
        delta_clusters[centroid_id] = (float(latitude), float(longitude))

    for line in cluster_new_data.strip().split("\n"):
        data = line.strip().split("\t")
        centroid_id, coords = data
        latitude, longitude = coords.strip().split(";")
        if abs(delta_clusters[centroid_id][0] - float(latitude)) > max_diff or abs(delta_clusters[centroid_id][1] - float(longitude)) > max_diff :
            sys.exit(1)

    sys.exit(0)

read_clusters()

