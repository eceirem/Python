kumeler = {
 "A": ["B", "C", "D"],
 "B": ["E", "F"],
 "D": ["G", "H"],
 "G": ["I", "J"],
 "H": ["K"]
}

def inside_folder(dict, alt_kume, ust_kume):
    if alt_kume in dict[ust_kume] or alt_kume == ust_kume:
        return True
    else:
        return False

print(inside_folder(kumeler, "B", "D"))