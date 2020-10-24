n0 = frozenset()
Nat = set([n0])

def pretty_pure_set(s):
    return '{%s}' % ' ,'.join([pretty(x) for x in s])

def pretty_set_of_predecessors(s):
    return '{%s}' % ' ,'.join([str(x) for x in range(len(s))])

def pretty_number(s):
    return(str(len(s)))

def pretty(s):
    assert s in Nat
    return pretty_number(s)

def suc(n):
    assert n in Nat
    s = frozenset(n | frozenset([n]))
    Nat.add(s)
    return s

def dec(n):
    assert n in Nat
    res = set()
    for k in n:
        res = res.union(k)
    return frozenset(res)

def less_than(m, n):
    assert m in Nat and n in Nat
    return m.issubset(n)

def less_than_or_equal_to(m, n):
    assert m in Nat and n in Nat
    return m == n or less_than(m,n)

def add(m, n, verbose=' '):
    assert m in Nat and n in Nat

    if verbose:
        print(verbose + "add(%s, %s)" %(pretty(m), pretty(n)))

    if n == n0:
        return m
    
    res = suc(add(m, dec(n), verbose=verbose + ' '))

    if verbose:
        print(verbose + "add(%s, %s) = %s" %(pretty(m), pretty(n), pretty(res)))
    return res

def mul(m, n, verbose=' '):
    assert m in Nat and n in Nat
    
    if verbose:
        print(verbose + "mul(%s, %s)" % (pretty(m), pretty(n)))

    if n == n0:
        return n0

    res = add(mul(m, dec(n), verbose=verbose + ' '), m, verbose= verbose + ' ')
    if verbose:
        print(verbose + "mul(%s, %s) = %s" %(pretty(m), pretty(n), pretty(res)))

    return res

#Aufgabe 2.5, Exponentialfunktion nur mit Multiplikation
# n ist der Exponent, verbose kann auf false gesetzt werden um nicht jeden Schritt gezeigt zu bekommen 
def exp(m, n, verbose=' '):
    assert m in Nat and n in Nat

    n1 = suc(n0)

    if verbose:
        print(verbose + "exp(%s, %s)" %(pretty(m), pretty(n)))

    if n == n0:
        return n1

    res = mul(exp(m, dec(n), verbose=verbose + ' '), m, verbose=verbose + ' ')
    if verbose:
        print(verbose + "exp(%s, %s) = %s" %(pretty(m), pretty(n), pretty(res)))
    
    return res

def examples():
    n1 = suc(n0)
    n2 = suc(n1)
    n3 = suc(n2)

    print(pretty(dec(n0)))
    print(pretty(dec(n1)))
    print(pretty(dec(n2)))
    print(pretty(dec(n3)))

    print(pretty(add(n3, n2)))
    print(pretty(mul(n3, n2)))

    print(pretty(exp(n2, n2)))

    m = n2 #2
    n = n3 #3
    k = n2 #2

    #solution1 = pretty(exp(m, exp(n, k))) #Dauert sehr, sehr lange
    #solution2 = pretty(exp(exp(m, n), k))
    solution3 = pretty(exp(m, mul(n, k))) #Auch sehr langsam

    #print("exp(%s,exp(%s, %s)) = %s" %(pretty(m), pretty(n), pretty(k), solution1))
    #print("exp(exp(%s, %s),%s) = %s" %(pretty(m), pretty(n), pretty(k), solution2))
    print("exp(%s, mul(%s, %s)) = %s" %(pretty(m), pretty(n), pretty(k), solution3))

    return

if __name__ == "__main__":
    examples()
    exit(0)