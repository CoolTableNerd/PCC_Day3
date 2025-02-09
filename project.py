# Create a list of players
players = ["LeBron", "Luka", "Austin", "Jaxon", "Jared"]

# Create a list of positions
positions = ["SF", "PG", "SG", "PF", "SF"]

# Extract the starting lineup (first 3 players) and bench players (last 2).
starters  = players[:3]
bench = players[3:]

print(starters)
print(bench)

print("\n")

# Pair players with their positions using `zip()`.
for player, position in zip(players,positions):
    print(f"Player: {player}\t Position: {position}")

# Calculate average points per game (PPG) for a list of stats.
averagePoints = sum(ppg) / len(ppg)

# Store player-team pairs as immutable tuples (e.g., `("LeBron", "Lakers")`).
team = "Lakers"
playerPairs = [(player, team) for player in players]