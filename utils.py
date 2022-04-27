import collections

def flatten(d, parent_key='', sep='_'):
    items = []
    for k, v in d.items():
        new_key = parent_key + sep + k if parent_key else k
        if isinstance(v, list):
            #print("test")
            items.extend(flatten(v[0], new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)
