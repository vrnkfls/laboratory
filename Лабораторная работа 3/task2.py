def find_common_participants(participants1, participants2, s=','):
    p_list1 = participants1.split(s)
    p_list2 = participants2.split(s)
    participants = list(set(p_list1).intersection(p_list2))
    participants.sort()
    return participants

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

participants = find_common_participants(participants_first_group, participants_second_group, s ='|')
print("Общие участники:", participants)