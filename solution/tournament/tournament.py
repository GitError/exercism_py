def tally(rows):
    """
    Process football tournament results and generate a formatted standings table.
    
    Args:
        rows (list): A list of strings representing match results in the format
                    "Team1;Team2;result" where result is one of "win", "loss", or "draw".
                    The result refers to the first team listed.
    
    Returns:
        list: A list of strings formatted as a standings table with columns for:
              Team, MP (Matches Played), W (Wins), D (Draws), L (Losses), and P (Points).
              Teams are sorted by points (descending) and then alphabetically by name.
    
    Example:
        >>> tally(["Team A;Team B;win", "Team C;Team A;draw"])
        ['Team                           | MP |  W |  D |  L |  P',
         'Team A                         |  2 |  1 |  1 |  0 |  4',
         'Team C                         |  1 |  0 |  1 |  0 |  1',
         'Team B                         |  1 |  0 |  0 |  1 |  0']
    """
    # Initialize the team stats dictionary with defaultdict-like behavior
    teams = {}
    
    # Process each row of input
    for row in rows:
        if not row.strip():
            continue
        
        try:
            team1, team2, result = row.strip().split(';')
            
            # Initialize teams with default values only when needed
            for team in (team1, team2):
                if team not in teams:
                    teams[team] = {"MP": 0, "W": 0, "D": 0, "L": 0, "P": 0}
            
            # All matches increment MP for both teams
            teams[team1]["MP"] += 1
            teams[team2]["MP"] += 1
            
            # Update stats based on result (combined logic)
            if result == "win":
                teams[team1]["W"] += 1
                teams[team1]["P"] += 3
                teams[team2]["L"] += 1
            elif result == "loss":
                teams[team1]["L"] += 1
                teams[team2]["W"] += 1
                teams[team2]["P"] += 3
            elif result == "draw":
                teams[team1]["D"] += 1
                teams[team1]["P"] += 1
                teams[team2]["D"] += 1
                teams[team2]["P"] += 1
        except ValueError:
            # Skip malformed rows
            continue
    
    # Format the output table with header
    result = ["Team                           | MP |  W |  D |  L |  P"]
    
    # Sort and format in one pass
    for team_name, stats in sorted(teams.items(), key=lambda x: (-x[1]["P"], x[0])):
        result.append(f"{team_name}{' ' * (31 - len(team_name))}|  {stats['MP']} |  {stats['W']} |  {stats['D']} |  {stats['L']} | {stats['P']:2d}")
    
    return result
