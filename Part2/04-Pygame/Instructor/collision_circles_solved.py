def check_collision(x1, y1, r1, x2, y2, r2):
    # Calculate the distance between the centers of the two circles
    distance_centers = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    
    # Calculate the sum of the radii
    sum_radii = r1 + r2
    
    # Check for collision
    if distance_centers <= sum_radii:
        return True
    else:
        return False

# Example usage
print(check_collision(3, 5, 2, 7, 5, 3))  # This should print True
