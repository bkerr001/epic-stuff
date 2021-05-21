# weight from flowsheet data
pt_weight_kg = 100
target_volume = pt_weight_kg*30
# query database, results reutrn as list or tuple? [volume, completed_time]
infusions = [[1000, 1429], [1000, 1545], [800, 1555], [500, 1557], [500, 1605]]


def fluidcounter(inf):
    v_infused = 0
    for i in inf:
        v_infused = v_infused + i[0]
        if v_infused > target_volume:
            return print(f'{i[1]} is when the 30ml/kg was met')


# can be run with each mar action
fluidcounter(infusions)
