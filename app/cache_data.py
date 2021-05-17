from API_requests import Requests


def get_all_teams():
    all_teams = []
    teams_names = []

    available_leagues = Requests.get_available_leagues()
    for league in available_leagues:
        teams = Requests.get_teams_by_league_id(league['league_id'])

        for team in teams:
            if not team['team_name'] in teams_names:
                teams_names.append(team['team_name'])
                all_teams.append(
                    (team['team_name'], team['team_key'], team['team_badge'], league['league_id']))

    return all_teams


def write_to_file(file_path, data):
    with open(file_path, 'w', encoding='utf-8') as file:
        for line in data:
            print(line[0])
            file.write(f'{line[0]}, {line[1]}, {line[2]}, {line[3]}\n')


def read_all_teams(file_path):
    all_teams = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            team_info = line.split(', ')
            team_object = {
                'team_name': team_info[0],
                'team_id': team_info[1],
                'team_badge': team_info[2],
                'league_id': team_info[3][:-1]
            }

            all_teams.append(team_object)

    return all_teams


if __name__ == '__main__':
    write_to_file('all_teams.txt', get_all_teams())
