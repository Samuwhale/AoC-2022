with open('input.txt', 'r') as input_file:
    input_data = input_file.readlines()
    input_data = [line.strip().title() for line in input_data]

# dictionaries to go from ABC/XYZ to the right condition or hand
input_to_hand = {
    'A': 'rock',
    'B': 'paper',
    'C': 'scissors',
    'X': 'rock',
    'Y': 'paper',
    'Z': 'scissors',
}
input_to_condition = {
    'X': 'loose',
    'Y': 'tie',
    'Z': 'win',
}
score_list = {
    'rock': 1,
    'paper': 2,
    'scissors': 3,
}


def get_player_outcome(enemy_hand, player_hand):
    '''returns appropriate amount of points given what was played'''
    if enemy_hand == player_hand:
        return 3

    if player_hand == 'rock':
        if enemy_hand == 'scissors':
            return 6
        else:
            return 0
    elif player_hand == 'paper':
        if enemy_hand == 'rock':
            return 6
        else:
            return 0
    else:  # player hand = scissors
        if enemy_hand == 'paper':
            return 6
        else:
            return 0


# dict where each value is defeated by its key
what_beats_what = {
    'rock': 'scissors', 'paper': 'rock', 'scissors': 'paper'
}


def calculate_round_score(enemy_hand, player_hand):
    hand_score = score_list[player_hand]
    outcome_score = get_player_outcome(enemy_hand, player_hand)
    print(f"Hand: {hand_score}, outcome: {outcome_score}, round_score: {hand_score + outcome_score}")
    return hand_score + outcome_score


def caclculate_play(enemy_hand, condition):
    print(enemy_hand)
    print(f"This round needs to end in a: {condition}")
    if condition == 'tie':
        return enemy_hand
    elif condition == 'win':
        # returns what hand wins if the enemy hand has to be the losing hand
        for win_hand, lose_hand in what_beats_what.items():
            if lose_hand == enemy_hand:
                return win_hand
    else:
        # returns what hand loses against the hand the enemy has
        return what_beats_what[enemy_hand]


# Runs the strategy from step 1
def xyz_to_hand_strategy():
    total_score = 0
    for round in input_data:
        enemy_hand = input_to_hand[round[0]]
        player_hand = input_to_hand[round[-1]]
        round_score = calculate_round_score(enemy_hand, player_hand)
        total_score += round_score
    return total_score


# Runs the strategy from step 2
def xyz_to_condition_strategy():
    total_score = 0
    for round in input_data:
        enemy_hand = input_to_hand[round[0]]
        round_condition = input_to_condition[round[-1]]
        player_hand = caclculate_play(enemy_hand, round_condition)
        round_score = calculate_round_score(enemy_hand, player_hand)
        total_score += round_score
    return total_score


print(xyz_to_hand_strategy())
print(xyz_to_condition_strategy())
