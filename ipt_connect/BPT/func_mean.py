# All functions for calculating mean value are independent of other models, so don't use import


def mean(vec):
    if len(vec) != 0:
        return float(sum(vec)) / len(vec)
    else:
        return 0.0


def ipt_mean(vec):
    if len(vec) in [5, 6]:
        nreject = 1
    else:
        nreject = (len(vec) + 5) // 4

    # TODO: the following code looks messy, but it works.
    # There was an unsuccessful attempt to refactor it.
    # The code should be refactored and tested.

    nhigh = nreject // 2
    nlow = nreject - nhigh
    weight = 1 - divmod(((len(vec) - 1)/4), 1)[1]

    if nhigh == 0:
        vec = vec[nlow:]
    else:
        vec = vec[nlow:-nhigh]
    
    vec[0] = vec[0]  * weight
    vec[len(vec) - 1] = vec[len(vec) - 1]  * weight
    return float(sum(vec)) / (len(vec) - 2 + (2*weight))
    # return mean(vec)


def iypt_mean(vec):
    if len(vec) > 1:
        vec.append((vec.pop(0) + vec.pop()) / 2.0)
        return mean(vec)
    return mean(vec)


def ttn_mean(vec):
    if len(vec) <= 4:
        return mean(vec)
    return iypt_mean(vec)
