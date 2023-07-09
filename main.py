import random

class Player:
    def __init__(self, name, bowling, batting, fielding, running, experience):
        self.name = name
        self.bowling = bowling
        self.batting = batting
        self.fielding = fielding
        self.running = running
        self.experience = experience

    def get_bowling_ability(self):
        return self.bowling

    def get_batting_ability(self):
        return self.batting

    def get_fielding_ability(self):
        return self.fielding

    def get_running_ability(self):
        return self.running

    def get_experience(self):
        return self.experience


class Team:
    def __init__(self, name, players):
        self.name = name
        self.players = players
        self.captain = None
        self.bowlers = []  # List to store players who can bowl

    def select_captain(self):
        self.captain = random.choice(self.players)

    def send_next_player(self):
        return random.choice(self.players)

    def choose_bowler(self):
        return random.choice(self.bowlers)

    def decide_batting_order(self):
        random.shuffle(self.players)
        self.bowlers = [player for player in self.players if player.get_bowling_ability() > 0]  # Select players who can bowl


class Field:
    def __init__(self, size, fan_ratio, pitch_conditions, home_advantage):
        self.size = size
        self.fan_ratio = fan_ratio
        self.pitch_conditions = pitch_conditions
        self.home_advantage = home_advantage


class Umpire:
    def __init__(self, team1, team2, field):
        self.team1 = team1
        self.team2 = team2
        self.field = field
        self.score = {team1.name: 0, team2.name: 0}
        self.wickets = {team1.name: 0, team2.name: 0}
        self.overs = 0
        self.current_bowler = None
        self.current_batsman = None

    def simulate_ball(self):
        bowler = self.current_bowler
        batsman = self.current_batsman
        bowling_ability = bowler.get_bowling_ability()
        batting_ability = batsman.get_batting_ability()
        
        # Simulate ball outcome based on probabilities
        if random.random() < batting_ability:
            runs_scored = random.randint(0, 6)
            self.score[self.current_team.name] += runs_scored
            self.current_batsman = self.current_team.send_next_player()
            self.commentator.umpire_signal(runs_scored)
        else:
            self.wickets[self.current_team.name] += 1
            self.current_batsman = self.current_team.send_next_player()
            self.commentator.umpire_out()

        # Update overs, change bowler if necessary, and check for innings end
        self.overs += 0.1
        if self.overs % 1 == 0:
            self.change_bowler()
        if self.overs >= 50 or self.wickets[self.current_team.name] >= 10:
            self.change_innings()

    def change_bowler(self):
        self.current_bowler = self.current_team.choose_bowler()

    def change_innings(self):
        self.current_team, self.opposing_team = self.opposing_team, self.current_team
        self.current_bowler = self.current_team.choose_bowler()
        self.overs = 0
        self.commentator.umpire_innings(self.opposing_team)

    def simulate_match(self):
        self.current_team = self.team1
        self.opposing_team = self.team2
        self.current_batsman = self.current_team.send_next_player()
        self.current_bowler = self.current_team.choose_bowler()

        print("Match starts!")
        while self.overs < 50 and self.wickets[self.current_team.name] < 10:
            self.simulate_ball()

        self.end_match()

    def end_match(self):
        print("Match ended!")
        print(f"{self.team1.name} Score: {self.score[self.team1.name]}/{self.wickets[self.team1.name]}")
        print(f"{self.team2.name} Score: {self.score[self.team2.name]}/{self.wickets[self.team2.name]}")
        
        if self.score[self.team1.name] > self.score[self.team2.name]:
            print(f"{self.team1.name} won the match!")
        elif self.score[self.team1.name] < self.score[self.team2.name]:
            print(f"{self.team2.name} won the match!")
        else:
            print("The match ended in a draw.")


class Commentator:
    def __init__(self, umpire):
        self.umpire = umpire

    def announce_weather(self):
        weather_conditions = ["Sunny", "Cloudy", "Rainy", "Windy"]
        weather = random.choice(weather_conditions)
        print(f"The weather conditions today are {weather}.")

    def provide_commentary(self):
        print(f"{self.umpire.current_team.name} is batting against {self.umpire.opposing_team.name}.")
        print(f"Bowler: {self.umpire.current_bowler.name}")
        print(f"Batsman: {self.umpire.current_batsman.name}")
        print(f"Score: {self.umpire.score[self.umpire.current_team.name]}/{self.umpire.wickets[self.umpire.current_team.name]}")
        print(f"Overs: {self.umpire.overs}")

    def umpire_signal(self, runs):
        if runs == 0:
            print("Umpire: No run.")
        elif runs == 1:
            print("Umpire: One run.")
        elif runs == 2:
            print("Umpire: Two runs.")
        elif runs == 3:
            print("Umpire: Three runs.")
        elif runs == 4:
            print("Umpire: Boundary! Four runs.")
        elif runs == 6:
            print("Umpire: Six runs.")
        elif runs > 6:
            print(f"Umpire: {runs} runs!")
        else:
            print("Umpire: Invalid runs.")

    def umpire_out(self):
        print("Umpire: Out!")
        
    def umpire_innings(self, team):
        print(f"Umpire: Innings change. {team.name} is now batting.")

# Example usage
player1 = Player("MS Dhoni", 0.2, 0.8, 0.99, 0.8, 0.9)
player2 = Player("Virat Kohli", 0.1, 0.9, 0.95, 0.7, 0.8)
team1 = Team("Team 1", [player1, player2])
team1.select_captain()
team1.decide_batting_order()

player3 = Player("Kane Williamson", 0.1, 0.7, 0.9, 0.8, 0.9)
player4 = Player("Steve Smith", 0.2, 0.8, 0.85, 0.7, 0.8)
team2 = Team("Team 2", [player3, player4])
team2.select_captain()
team2.decide_batting_order()

field = Field("Large", 0.9, "Dry", 0.1)

umpire = Umpire(team1, team2, field)
commentator = Commentator(umpire)

commentator.announce_weather()
umpire.commentator = commentator  # Assign the commentator to the umpire
umpire.simulate_match()
