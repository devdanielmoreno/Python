'''
m2e3.py
Dani Moreno
20221011
'''
p=0; q=0
    
print("p: %d\t q: %d\t!(%d||%d): %d\t!%d&&!%d: %d\n",
                (p,q,p,q,not (p or q),p,q,not p and not q))
print("p: %d\t q: %d\t!(%d&&%d): %d\t!%d||!%d: %d\n",
                (p,q,p,q,not (p and q),p,q, not p or not q))
p=1; q=0
    
print("p: %d\t q: %d\t!(%d||%d): %d\t!%d&&!%d: %d\n",
                (p,q,p,q,not (p or q),p,q,not p and not q))
print("p: %d\t q: %d\t!(%d&&%d): %d\t!%d||!%d: %d\n",
                (p,q,p,q,not (p and q),p,q, not p or not q))

p=0; q=1
    
print("p: %d\t q: %d\t!(%d||%d): %d\t!%d&&!%d: %d\n",
                (p,q,p,q,not (p or q),p,q,not p and not q))
print("p: %d\t q: %d\t!(%d&&%d): %d\t!%d||!%d: %d\n",
                (p,q,p,q,not (p and q),p,q, not p or not q))

p=1; q=1
    
print("p: %d\t q: %d\t!(%d||%d): %d\t!%d&&!%d: %d\n",
                (p,q,p,q,not (p or q),p,q,not p and not q))
print("p: %d\t q: %d\t!(%d&&%d): %d\t!%d||!%d: %d\n",
                (p,q,p,q,not (p and q),p,q, not p or not q))
    