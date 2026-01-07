teams = {
    "Alpha": [101, 102, 103],
    "Beta":  [103, 104, 105],
    "Gamma": [106, 107],      
    "Delta": [102, 108]      
}
def analyze_teams(teams):
    seen = set()
    duplicates = set()
    all_students = set()

    for members in teams.values():
        for student in members:
            if student in seen:
                duplicates.add(student)
            else:
                seen.add(student)
            all_students.add(student)

    valid_teams = []
    for team, members in teams.items():
        if not duplicates.intersection(members):
            valid_teams.append(team)

    return duplicates, valid_teams, len(all_students)

disqualified, valid_teams, total_unique = analyze_teams(teams)

print("Disqualified Students:", disqualified)
print("Valid Teams:", valid_teams)
print("Total Unique Participants:", total_unique)
