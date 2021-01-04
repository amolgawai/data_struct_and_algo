def combinations(lst):
    if len(lst) == 0:
        return [[]]
        
    first_ele = lst[0]
    combi_without_fst = combinations(lst[1:])
    
    combi_with_first = list()
    for a_combi in combi_without_fst:
        combi_with_first.append(a_combi + [first_ele])
        
    return  combi_without_fst + combi_with_first
    
    
def permutations(lst):
    if len(lst) == 0:
        return [[]]
        
    first_ele = lst[0]
    perm_without_first = permutations(lst[1:])
    
    perms = list()
    for a_perm in perm_without_first:
        for indx in range(len(a_perm) + 1):
            perm = a_perm[:indx] + [first_ele] + a_perm[indx:]
            perms.append(perm)
            
    return perms
    
    
def main():
    print(combinations(['a', 'b', 'c']))
    print(permutations(['a', 'b', 'c']))
    
    
if __name__ == "__main__":
    main()
