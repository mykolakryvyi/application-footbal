from API_requests import Requests
from team import Team


class Analysis:
    APIkey = '3f561cce229d17fa05f23e5fa9f1ce750c39652d1aa8fed1ae58464da66706a4'

    def __init__(self, team_id, start_date, end_date):
        self.team = Team(team_id, start_date, end_date)

    def choose_team(self):
        teams = {}
        teams_names = []
        league_id = 148  # EPL id in our API
        print('Downloading the info about teams...')

        teams_info = Requests.get_teams_by_league_id(league_id)
        print(teams_info)

        for team in teams_info:
            teams[team['team_name']] = team['team_key']
        for team in teams_info:
            teams_names.append(team['team_name'])

        for i in range(len(teams_names)):
            print(f'{i+1}. {teams_names[i]}')

        chosen_team = input(
            'Choose the team which statistics analysis you want to see: ')
        while chosen_team not in teams_names:
            for i in range(len(teams_names)):
                print(f'{i+1}. {teams_names[i]}')

            print('You typed a wrong team, try one more time...')
            chosen_team = input(
                'Choose the team which statistics analysis you want to see: ')

        self.team = Team(teams[chosen_team])

    def get_info(self, criterion):
        if criterion == 'scheme':
            return self.analyze_team_schemas()
        elif criterion == 'possesion':
            return self.analyze_team_ball_possesion()
        elif criterion == 'fouls':
            return self.analyze_team_fouls()
        else:
            return self.analyze_team_shots()

    def analyze_team_schemas(self):
        if self.team:
            return self.team.get_schemas_info()
        else:
            return "You haven't chosen a team yet."

    def analyze_team_ball_possesion(self):
        if self.team:
            return self.team.get_ball_possesion_info()
        else:
            return "You haven't chosen a team yet."

    def analyze_team_fouls(self):
        if self.team:
            return self.team.get_fouls_info()
        else:
            return "You haven't chosen a team yet."

    def analyze_team_shots(self):
        if self.team:
            return self.team.get_shots_info()
        else:
            return "You haven't chosen a team yet."
