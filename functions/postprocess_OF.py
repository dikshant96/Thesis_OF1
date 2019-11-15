import numpy as np


def get_flowfieldvector(case, time, field_val):
    """
    :param case: Directory of the openfoam case
    :param time: Time stamp for which to get values from
    :param field_val: String name of quantity
    :return: vector of the internal field quantity at cell centres
    """
    file = case + '/' + time + '/' + field_val
    f = open(file, 'r')
    f_lines = f.readlines()

    start = 1000
    for i, line in enumerate(f_lines):
        if 'internalField' in line:
            start = i + 2
            entries_len = int(f_lines[i + 1])
            cell_centres_val = np.zeros((entries_len, 3))
            j = 0
        elif start < i <= entries_len + start:
            line = line.replace('(', '')
            line = line.replace(')', '')
            line = line.split(' ')
            cell_centres_val[j, 0] = line[0]
            cell_centres_val[j, 1] = line[1]
            cell_centres_val[j, 2] = line[2]
            j = j + 1

    return cell_centres_val


def get_flowfieldscalar(case, time, field_val):
    """
    :param case: Directory of OpenFoam case
    :param time: Time stamp for which to get values from
    :param field_val: String name of quantity
    :return: scalar of the internal field values
    """
    file = case + '/' + time + '/' + field_val
    f = open(file, 'r')
    f_lines = f.readlines()

    start = 1000
    for i, line in enumerate(f_lines):
        if 'internalField' in line:
            start = i + 2
            entries_len = int(f_lines[i + 1])
            cell_centres_val = np.zeros((entries_len, 1))
            j = 0
        elif i > start and i <= entries_len + start:
            line = line.replace('(', '')
            line = line.replace(')', '')
            cell_centres_val[j, 0] = float(line[0:-1])
            j = j + 1

    return cell_centres_val


def get_boundaryvector(case, time, wall, field_val):
    """
    :param case: Directory of OpenFoam case
    :param time: Time stamp for which to get values from
    :param wall: String name for wall
    :param field_val: String name of quantity
    :return: Vector of boundary values
    """
    file = case + '/' + time + '/' + field_val
    f = open(file, 'r')
    f_lines = f.readlines()

    start = 10**12
    for i, line in enumerate(f_lines):
        if wall in line:
            start = i + 5
            entries_len = int(f_lines[i + 4])
            cell_centres_val = np.zeros((entries_len, 3))
            j = 0
        elif i > start and i <= entries_len + start:
            line = line.replace('(', '')
            line = line.replace(')', '')
            line = line.split(' ')
            cell_centres_val[j, 0] = line[0]
            cell_centres_val[j, 1] = line[1]
            cell_centres_val[j, 2] = line[2]
            j = j + 1

    return cell_centres_val


def get_boundaryscalar(case, time, wall, field_val):
    """
    :param case: Directory of OpenFoam case
    :param time: Time stamp for which to get values from
    :param wall: String name for wall
    :param field_val: String name of quantity
    :return: Scalar of boundary values
    """
    file = case + '/' + time + '/' + field_val
    f = open(file, 'r')
    f_lines = f.readlines()

    start = 10**12
    for i, line in enumerate(f_lines):
        if wall in line:
            start = i + 5
            entries_len = int(f_lines[i + 4])
            cell_centres_val = np.zeros((entries_len, 1))
            j = 0
        elif i > start and i <= entries_len + start:
            line = line.replace('(', '')
            line = line.replace(')', '')
            cell_centres_val[j, 0] = line[0:-1]
            j = j + 1

    return cell_centres_val

def get_probexvalues(pos, x, axis, field_val):
    """
    :param pos: whole field position
    :param x: x location for which value is desired (closest point)
    :param axis: either y or z axis
    :param field_val: scalar value desired
    :return: y/z coordinate, scalar value from the probe
    """
    x = np.argmin(abs(pos[:, 0] - x))
    x = pos[x,0]
    indexes = np.transpose(np.array(np.where(abs(x - pos[:, 0]) <= 1e-5)))
    j = 0
    for index in indexes:
        index = int(index)
        pos[index,:] = pos[index,:]
        field_val[index] = field_val[index]
        j = j + 1
    if axis == 'y':
        loc = 1
    else:
        loc = 2
    indexes = np.argsort(pos[:,loc])
    axis_list = np.array([])
    var_list = np.array([])
    for index in indexes:
        axis_list = np.append(axis_list, pos[index,loc])
        var_list = np.append(var_list, field_val[index])
    return axis_list, var_list


def get_magvector(field_val):
    """
    :param field_val: vector field in Nx3 format
    :return: magnitude of vector
    """
    field_mag = np.zeros(len(field_val))
    for i in range(len(field_val)):
        field_mag[i] = np.linalg.norm(field_val[i,:])
    return field_mag

def get_boundaryvector1D(case, time, wall, field_val):
    """
    :param case: Directory of OpenFoam case
    :param time: Time stamp for which to get values from
    :param wall: String name for wall
    :param field_val: String name of quantity
    :return: Vector of boundary value at only 1 cell
    """
    file = case + '/' + time + '/' + field_val
    f = open(file, 'r')
    f_lines = f.readlines()

    cell_centres_val = np.zeros((1,3))
    for i, line in enumerate(f_lines):
        if wall in line:
            val_index = i + 3
            val_line = f_lines[val_index]
            val_line = val_line.replace('(', '')
            val_line = val_line.replace(')', '')
            val_line = val_line.replace(';\n', '')
            val_line = val_line.split(' ')


            cell_centres_val[0, 0] = val_line[-3]
            cell_centres_val[0, 1] = val_line[-2]
            cell_centres_val[0, 2] = val_line[-1]

    return cell_centres_val


def get_boundaryscalar1D(case, time, wall, field_val):
    """
    :param case: Directory of OpenFoam case
    :param time: Time stamp for which to get values from
    :param wall: String name for wall
    :param field_val: String name of quantity
    :return: Vector of boundary value at only 1 cell
    """
    file = case + '/' + time + '/' + field_val
    f = open(file, 'r')
    f_lines = f.readlines()

    for i, line in enumerate(f_lines):
        if wall in line:
            val_index = i + 3
            val_line = f_lines[val_index]
            val_line = val_line.replace(';\n', '')
            val_line = val_line.split(' ')

            cell_centres_val = val_line[-1]

    return cell_centres_val
