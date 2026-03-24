def has_common_friends(fg1: frozenset[str], fg2: frozenset[str]) -> bool:
    return not fg1.isdisjoint(fg2)


def friend_groups(f_groups: list[tuple[str, str]]) -> list[list[str]]:
    fgs: set[frozenset[str]] = set(frozenset((*fg,)) for fg in (friend_group for friend_group in f_groups))
    
    while True:
        initial_length_of_fgs: int = len(fgs)
        cont: bool = True
        for fg in list(fgs):
            if not cont:
                break
            for other_fg in list(fgs):
                if fg == other_fg:
                    continue
                
                if has_common_friends(fg, other_fg):
                    common_fg: frozenset[str] = fg | other_fg
                    fgs.remove(fg)
                    fgs.remove(other_fg)
                    fgs.add(common_fg)
                    
                    cont = False
                    break
                    
        final_length_of_fgs: int = len(fgs)
        
        if initial_length_of_fgs == final_length_of_fgs:
            break
        
        
    return [sorted(list(fg)) for fg in fgs]


relations2 = [("Virgilia", "Beatrice")]
print(friend_groups(relations2))
assert friend_groups(relations2) == [["Beatrice", "Virgilia"]]

relations3 = [("Virgilia", "Beatrice"), ("Ronove", "Beatrice")]
print(friend_groups(relations3))
assert friend_groups(relations3) == [["Beatrice", "Ronove", "Virgilia"]]

relations4 = [("Will", "Lion"), ("Zepar", "Furfur"), ("Lion", "Erika")]
print(friend_groups(relations4))
assert sorted(friend_groups(relations4)) == [
    ["Erika", "Lion", "Will"],
    ["Furfur", "Zepar"],
]

relations5 = [
    ("Jessica", "Krauss"),
    ("Rudolf", "Kyrie"),
    ("Ange", "Battler"),
    ("Eva", "George"),
    ("Eva", "Hideyoshi"),
    ("Krauss", "Natsuhi"),
    ("Kyrie", "Ange"),
    ("Rosa", "Maria"),
    ("Jessica", "Natsuhi"),
]
assert sorted(friend_groups(relations5)) == [
    ["Ange", "Battler", "Kyrie", "Rudolf"],
    ["Eva", "George", "Hideyoshi"],
    ["Jessica", "Krauss", "Natsuhi"],
    ["Maria", "Rosa"],
]
