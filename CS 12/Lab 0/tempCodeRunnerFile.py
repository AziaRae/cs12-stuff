
relations1 = []
assert friend_groups(relations1) == []

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
