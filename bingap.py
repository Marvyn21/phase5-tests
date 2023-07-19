def solution(N):
    # Implement your solution here
    binum = bin(N)[2:]
    max_gap = 0
    current_gap = 0

    for digit in binum:
        if digit == '0':
            current_gap += 1
        else:
            max_gap = max(max_gap, current_gap)
            current_gap = 0
    return max_gap