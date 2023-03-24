import numpy as np

def calculate(list):

    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    array = np.array(list)
    
    axis2_mean = ([array[[0,1,2]].mean(), array[[3,4,5]].mean(), array[[6,7,8]].mean()])
    axis1_mean = ([array[[0,3,6]].mean(), array[[1,4,7]].mean(), array[[2,5,8]].mean()])


    axis2_var = ([array[[0,1,2]].var(), array[[3,4,5]].var(), array[[6,7,8]].var()])
    axis1_var = ([array[[0,3,6]].var(), array[[1,4,7]].var(), array[[2,5,8]].var()])

    axis2_std = ([array[[0,1,2]].std(), array[[3,4,5]].std(), array[[6,7,8]].std()])
    axis1_std = ([array[[0,3,6]].std(), array[[1,4,7]].std(), array[[2,5,8]].std()])
    
    
    axis2_max = ([array[[0,1,2]].max(), array[[3,4,5]].max(), array[[6,7,8]].max()])
    axis1_max = ([array[[0,3,6]].max(), array[[1,4,7]].max(), array[[2,5,8]].max()])

    axis2_min = ([array[[0,1,2]].min(), array[[3,4,5]].min(), array[[6,7,8]].min()])
    axis1_min = ([array[[0,3,6]].min(), array[[1,4,7]].min(), array[[2,5,8]].min()])

    axis2_sum = ([array[[0,1,2]].sum(), array[[3,4,5]].sum(), array[[6,7,8]].sum()])
    axis1_sum = ([array[[0,3,6]].sum(), array[[1,4,7]].sum(), array[[2,5,8]].sum()])



    calculations = {    'mean': [axis1_mean, axis2_mean, array.mean()],
                'variance': [axis1_var, axis2_var, array.var()],
                'standard deviation': [axis1_std, axis2_std, array.std()],
                'max': [axis1_max, axis2_max, array.max()],
                'min': [axis1_min, axis2_min, array.min()],
                'sum': [axis1_sum, axis2_sum, array.sum()]
            }


    return calculations