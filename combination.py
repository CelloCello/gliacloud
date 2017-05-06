# -*- coding: utf-8 -*-

def combcount(n,r):
    f = lambda n, r: n * f(n-1, r) if n>r else 1
    return f(n, n-r)/f(r, 0)


def com(n, r):
    if r == 1:
        return n

    if r == n:
        return 1

    #h = 0
    #if n > r:
    #    h = n - r + 1

    #top = h
    #bottom = 1
    #return (top+bottom) * h / 2
    rst = com(n-1, r) + com(n-1, r-1)
    #= [com(n-1-1, r)+com(n-1-1, r-1)] + [com(n-1-1, r-1)+com(n-1-1, r-1-1)]
    #rst = com(n-1-1, r) + 2*com(n-1-1, r-1) + com(n-1-1, r-1-1)
    #rst = com(n-N, r) + 2*(N-1)*com(n-N, r-N) + com(n-N, r-N)
    #c(3, 2) = c(2, 2) + c(2, 1)
    #= 1 + 2
    #= 3
    #c(5, 2) = c(4, 2) + c(4, 1)
    #= c(3, 2) + 3 + 4
    #= c(2, 2) + c(2, 1) + 3 + 4
    #= 1 + 2 + 3 + 4
    #c(10, 4) = c(9, 4) + c(9, 3)
    #= c(8, 4) + c(8, 3) + c(8, 3) + c(8, 2)
    #= c(7, 4) + c(7, 3) + c(7, 3) + c(7, 2) + c(7, 3) + c(7, 2) + c(7, 2) + c(7, 1)
    #= c(7, 4) + c(7, 3) + c(7, 3) + c(7, 2) + c(7, 3) + c(7, 2) + c(7, 2) + 7
    #c(990, 33) = c(989, 33) + c(989, 32)
    
    return rst


def com1(n, r):
    calc_list = {(n, r):1}

    rst = 0
    times = 0
    while (len(calc_list) > 0):
        #print len(calc_list)
        new_list = {}
        #rst = 0
        for k, v in calc_list.iteritems():
            nn = k[0]
            rr = k[1]
            #print 'v: ' + str(v) + str(k)
            if nn == rr:
                rst += (1 * v)
                continue
            if rr == 1:
                rst += (nn * v)
                continue

            try:
                nnn = nn - 1
                rrr = rr - 1
                kk = (nnn, rr)
                if kk in new_list:
                    new_list[kk] += v
                else:
                    new_list[kk] = v

                kk = (nnn, rrr)
                if kk in new_list:
                    new_list[kk] += v
                else:
                    new_list[kk] = v

                continue

                
                nnn = nn - 1
                rrr = rr - 1
                if nnn == rr:
                    rst += 1 * v
                else:
                    kk = (nnn, rr)
                    if kk in new_list:
                        new_list[kk] += 1
                    else:
                        new_list[kk] = 1
                    #new_list.append((nn-1, rr))
                    
                if nnn == rrr:
                    rst += 1 * v
                elif rrr == 1:
                    rst += nnn * v
                else:
                    kk = (nnn, rrr)
                    if kk in new_list:
                        new_list[kk] += 1
                    else:
                        new_list[kk] = 1
                    #new_list.append((nn-1, rr-1))
            except:
                print "cc: " + str(len(new_list))
                print "ll: " + str(len(new_list))
                raise
        #print '---------' + str(rst)
        calc_list = new_list
        times += 1

    print "times: " + str(times)
    return rst



print combcount(990, 33)
#print combcount(3, 2) #3
print com1(990, 33)
#print com(990, 33)

