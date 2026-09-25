def group_anagrams(strs):
    groups = {}
    for s in strs:
        key = ''.join(sorted(s))   # sorted characters form the key
        if key not in groups:
            groups[key] = []
        groups[key].append(s)
    return list(groups.values())


strs = input("Enter strings").split()
result = group_anagrams(strs)
print("Grouped anagrams:", result)

