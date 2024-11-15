def find_common_participants(group1, group2, splitter=','):

    participants1 = group1.split(splitter)
    participants2 = group2.split(splitter)
    common_participants = []
    for i in participants1:
        for j in participants2:
            if i == j:
                common_participants.append(i)

    return sorted(common_participants)


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group, splitter='|'))

