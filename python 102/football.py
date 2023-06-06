from random import choice

teamA = []
teamB = []    # Create two empty lists for teams A and B

players = ['Harry', 'Hermione', 'Neville', 'Ginny']

def add_player_to_team(team):
	player_picked = choice(players)
	team.append(player_picked)
	players.remove(player_picked)
	
# Add a player to each team
add_player_to_team(teamA)
add_player_to_team(teamB)


