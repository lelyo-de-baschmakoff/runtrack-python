def draw_rectangle(width, height):
    horizontal_line = '-' * width

    print(horizontal_line)

    for _ in range(height - 2):
        print('|' + ' ' * (width - 2) + '|')

    if height > 1:
        print(horizontal_line)

draw_rectangle(45, 23)
