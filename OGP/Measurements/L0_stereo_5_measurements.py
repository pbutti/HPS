import numpy as np
import math
import Al_utils

def get_sensor_origin():
	sensor_origin = np.empty([3])
	sensor_origin[0] = Al_utils.getAvg(np.array([128.74090]))
	sensor_origin[1] = Al_utils.getAvg(np.array([007.61175]))
	sensor_origin[2] = Al_utils.getAvg(np.array([004.96823]))
	return sensor_origin

def get_sensor_plane():
	sensor_plane = np.empty([5])
	sensor_plane[0] = Al_utils.getAvg(np.array([129.16818]))
	sensor_plane[1] = Al_utils.getAvg(np.array([006.79308]))
	sensor_plane[2] = Al_utils.getAvg(np.array([005.77786]))
	sensor_plane[3] = Al_utils.getAvg(np.array([-089.98081]))
	sensor_plane[4] = Al_utils.getAvg(np.array([-045.48544]))
	return sensor_plane

def get_sensor_normal():
	return Al_utils.normal_vector(math.radians(get_sensor_plane()[3]),math.radians(get_sensor_plane()[4]))

def get_sensor_active_edge():
	sensor_active_edge = np.empty([5])
	sensor_active_edge[0] = Al_utils.getAvg(np.array([129.35828]))
	sensor_active_edge[1] = Al_utils.getAvg(np.array([002.61784]))
	sensor_active_edge[2] = Al_utils.getAvg(np.array([009.88095]))
	sensor_active_edge[3] = Al_utils.getAvg(np.array([-003.55891]))
	sensor_active_edge[4] = Al_utils.getAvg(np.array([003.46799]))
	return sensor_active_edge

def get_sensor_active_edge_vector():
	return Al_utils.normal_vector(math.radians(get_sensor_active_edge()[3]),math.radians(get_sensor_active_edge()[4]))

def get_sensor_physical_edge():
	sensor_physical_edge = np.empty([5])
	sensor_physical_edge[0] = Al_utils.getAvg(np.array([129.82460]))
	sensor_physical_edge[1] = Al_utils.getAvg(np.array([002.32857]))
	sensor_physical_edge[2] = Al_utils.getAvg(np.array([010.17507]))
	sensor_physical_edge[3] = Al_utils.getAvg(np.array([-004.05243]))
	sensor_physical_edge[4] = Al_utils.getAvg(np.array([003.91766]))
	return sensor_physical_edge

def get_sensor_physical_edge_vector():
	return Al_utils.normal_vector(math.radians(get_sensor_physical_edge()[3]),math.radians(get_sensor_physical_edge()[4]))

def get_sensor_basis():
	basis = np.empty([3,3])
	basis[0] = get_sensor_active_edge_vector()
	basis[2] = get_sensor_normal()
	basis[0] = Al_utils.orthogonalize(basis[2],basis[0])
	basis[1] = np.cross(basis[2],basis[0])

	basis[0] = basis[0]/np.linalg.norm(basis[0])
	basis[1] = basis[1]/np.linalg.norm(basis[1])
	basis[2] = basis[2]/np.linalg.norm(basis[2])
	return [get_sensor_origin(),basis,get_sensor_active_edge(),get_sensor_active_edge_vector(),get_sensor_physical_edge(),get_sensor_physical_edge_vector()]