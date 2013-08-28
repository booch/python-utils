# From http://rightfootin.blogspot.com/2006/09/more-on-python-flatten.html
def flatten(l):
    result = []
    for item in l:
        if isinstance(item, (list, tuple)):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

# Alternate (simpler/slower) implementation.
#def flatten(l):
#    if l:
#        return reduce(lambda x,y: x+y, l)
#    else:
#        return []

# From http://www.peterbe.com/plog/uniqifiers-benchmark; preserves order of original list.
def unique(seq, idfun=None):
    if idfun is None:
        def idfun(x): return x
    seen = {}
    result = []
    for item in seq:
        marker = idfun(item)
        if marker in seen: continue
        seen[marker] = 1
        result.append(item)
    return result
