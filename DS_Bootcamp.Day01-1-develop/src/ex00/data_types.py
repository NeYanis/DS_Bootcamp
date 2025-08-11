def data_types():
    type1 = 1 #int
    type2 = 'abc' #str
    type3 = 4.123 #float
    type4 = True #bool
    type5 = ['asd','123'] #list
    type6 = {"Country":"Russia","City":"Moscow"} #dict
    type7 = (1,2) #tuple
    type8 = {1,2,3,3} #set
    print([type(types).__name__ for types in (type1, type2, type3, type4, type5, type6, type7, type8)])

if __name__ == '__main__':
    data_types()