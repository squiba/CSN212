import numpy
def qhull(sample):
    link = lambda a,b: numpy.concatenate((a,b[1:]))
    edge = lambda a,b: numpy.concatenate(([a],[b]))

    def dome(sample,base): 
        h, t = base
        dists = numpy.dot(sample-h, numpy.dot(((0,-1),(1,0)),(t-h)))
        outer = numpy.repeat(sample, dists>0, axis=0)
        
        if len(outer):
            pivot = sample[numpy.argmax(dists)]
            return link(dome(outer, edge(h, pivot)),
                        dome(outer, edge(pivot, t)))
        else:
            return base

    if len(sample) > 2:
        axis = sample[:,0]
        base = numpy.take(sample, [numpy.argmin(axis), numpy.argmax(axis)], axis=0)
        return link(dome(sample, base),
                    dome(sample, base[::-1]))
    else:
        return sample

# MAIN
if __name__ == "__main__":
    from pylab import plot
    import pylab as plt

    sample = 100*numpy.random.random((32,2))
    hull = qhull(sample)
     
    for s in sample:
        plot([s[0]], [s[1]], 'b.')

    i = 0
    while i < len(hull)-1:
        plot([hull[i][0], hull[i+1][0]], [hull[i][1], hull[i+1][1]], color='k')
        i = i + 1

    plot([hull[-1][0], hull[0][0]], [hull[-1][1], hull[0][1]], color='k')
    plt.savefig("qh.png")
