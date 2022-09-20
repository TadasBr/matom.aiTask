import numpy as np
import laspy
import open3d as o3d

with laspy.open('2743_1234.las') as fh:
    las = fh.read()

print("Given points count:", len(las.points))

points = las.xyz
# points = points[::8]  # Reducing point cloud for testing

pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(points)
octree = o3d.geometry.Octree(max_depth=5)
octree.convert_from_point_cloud(pcd, size_expand=0.01)
# o3d.visualization.draw_geometries([pcd], "Point cloud")  # Point cloud visualisation
o3d.visualization.draw_geometries([octree], "Octree")  # Could not find a way to color octree visualisation
