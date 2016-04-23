import pandas


def merge_series_summing_values(series_a, series_b):
    '''This method merges two series summing columns.'''

    if series_a is None or series_b is None:
        if series_a is not None:  # only b is None
            return series_a.copy()
        elif series_b is not None:  # only a is None
            return series_b.copy()
        else:  # both are None
            return None

    else:  # Neither is None, Must merge
        temp_a = series_a
        temp_b = series_b
        if type(series_a) is pandas.Series: temp_a = pandas.DataFrame(series_a, columns=['count']).reset_index();
        if type(series_b) is pandas.Series: temp_b = pandas.DataFrame(series_b, columns=['count']).reset_index();
        merged = pandas.concat([temp_a, temp_b]).groupby('index').sum()['count']

# print '----------------------'
#    print 'len(a) = ', len(a)
#    print 'len(b) = ', len(b)
#    print 'len(merged) = ', len(merged)
#    inter = set(a.keys()).intersection(set(b.keys()))
#    print 'a /\ b = ',  len(inter), ' :: ', list(inter)[:1]
#    print 'a U b = ',  len(set(a.keys()).union(set(b.keys())))
#    print 'a - b = ',  len(set(a.keys()) - set(b.keys()))
#    print 'b - a = ',  len(set(b.keys()) - set(a.keys()))
#    print '----------------------'
#    if len(inter)>0:
#        i = list(inter)[0]
#        print 'a[{0}]={1}'.format(i, a[i])
#        print 'b[{0}]={1}'.format(i, b[i])
#        print 'merged[{0}]={1}'.format(i, merged[i])
#        print '----------------------'

    return merged