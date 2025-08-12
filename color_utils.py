from color_codes import MAJOR_COLORS, MINOR_COLORS, get_color_from_pair_number

def generate_color_code_reference():
    output = []
    total_pairs = len(MAJOR_COLORS) * len(MINOR_COLORS)
    for pair_number in range(1, total_pairs + 1):
        major, minor = get_color_from_pair_number(pair_number)
        output.append(f'{pair_number:2}: {major:<6} | {minor}')
    return "\n".join(output)
