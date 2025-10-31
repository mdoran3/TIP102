def find_shallowest_point(depths):
    if len(depths) == 1:
        return depths[0]
    
    mid = len(depths) // 2

    ######### VISUALIZE #########
    left = depths[:mid]
    right = depths[mid:]
    print(f"LEFT: {left}")
    print(f"RIGHT: {right} \n")
    #############################
    
    left_min_depth = find_shallowest_point(depths[:mid])
    right_min_depth = find_shallowest_point(depths[mid:])
    

    return left_min_depth if left_min_depth < right_min_depth else right_min_depth

print(find_shallowest_point([5, 7, 2, 8, 3]))
print(find_shallowest_point([12, 15, 10, 21]))