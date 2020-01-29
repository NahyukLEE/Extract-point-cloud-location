import numpy as np
import sys
import open3d as o3d

if __name__ == "__main__" :

    ### PLY Point cloud visualization
    print("Load a ply point cloud, print it, and render it")
    pcd = o3d.io.read_point_cloud("cloud_and_poses.ply")
    print(pcd)
    o3d.visualization.draw_geometries([pcd]) #optional
    

    ### Extract points' location
    np.set_printoptions(threshold=sys.maxsize)
    
    text = open('array.txt','w')

    arr = np.asarray(pcd.points)

    print(arr[0][0])
    i = 0
    while True :
        for k in range(0, 3):
            text.write(str((arr[i][k])))
            text.write(" ")
        text.write("\n")

        i += 1
        
    text.close()
    
