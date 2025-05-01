def solve(N, D, P, S):
    ants = sorted(zip(P, S), reverse=True)  # Sort by position in descending order
    colonies = 0
    min_speed = float('inf')
    
    for pos, speed in ants:
        time = (D - pos) / speed  # Compute time to reach sugar
        
        if speed < min_speed:
            colonies += 1  # New colony formed
            min_speed = speed  # Update min speed of colony
    
    print(colonies)

solve(4, 10, [2,4,5,6], [3,1,2,3])