def solve(N, M, A):
    events = []

    for show in A:
        duration = show[0]
        for start in show[1:]:
            events.append((start, 'start'))
            events.append((start + duration, 'end'))

    events.sort(key=lambda x: (x[0], x[1] == 'start'))

    current_active = 0

    for time, event_type in events:
        if event_type == 'start':
            current_active += 1
            if current_active > M: 
                print("NO")
                return
        else:
            current_active -= 1

    print("YES")

# Main function to handle multiple test cases
if __name__ == "__main__":
    test_cases = [
        (4, 120, [(60, 10, 60, 100), (30, 0, 50, 90), (20, 0, 20, 40), (50, 50, 70, 110)]),
        (4, 120, [(50, 30, 60, 100), (30, 40, 50, 90), (20, 0, 20, 40), (50, 50, 70, 110)]),
        (5, 180, [(50, 10, 60, 100), (30, 40, 50, 90), (20, 0, 20, 40), (50, 50, 70, 110), (60, 60, 120, 150)])
    ]

    for N, M, A in test_cases:
        solve(N, M, A)