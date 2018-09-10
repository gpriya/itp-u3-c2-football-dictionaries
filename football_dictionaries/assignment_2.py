from pprint import pprint

def create_player_dictionary(player):
    
    return {
        'number': player[0],
        'position': player[1],
        'name': player[2],
        'date_of_birth': player[3],
        'caps': player[4],
        'club': player[5],
        'country': player[6],
        'club_country': player[7],
        'year': player[8],
    }
    
def players_by_position(squads_list):
    
    dictionary_of_players = {}
    list_of_players = []
    
    for player in squads_list:
        
        player_dict = create_player_dictionary(player)
        list_of_players.append(player_dict)
        
    
    for i in range(0, len(list_of_players)):
        
        dictionary_of_players.setdefault(list_of_players[i]["position"], [])
        
        dictionary_of_players[list_of_players[i]["position"]].append(list_of_players[i])
        
    return dictionary_of_players
