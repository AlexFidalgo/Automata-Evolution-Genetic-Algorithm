import pygame
import textwrap
from config import Config
from initialization import *

def get_total_number_of_cells(r): 

    return 2*r + 1

def get_number_of_combination_of_bits(total_number_of_cells):
    
    return 2**total_number_of_cells

def get_total_number_of_possible_rules(r):

    number_of_considered_cells = get_total_number_of_cells(r)

    return 2**(2**number_of_considered_cells)

def get_rule_table(r, rule):

    number_of_considered_cells = get_total_number_of_cells(r)
    total_number_of_bits = get_number_of_combination_of_bits(number_of_considered_cells)
    
    binary_string = bin(rule)[2:]
    bits_rule = format(int(binary_string, 2), f'0{total_number_of_bits}b')
    
    rule_dict = {}
    for i in range(total_number_of_bits):
        binary_representation = format(i, f'0{number_of_considered_cells}b')
        rule_dict[binary_representation] = int(bits_rule[total_number_of_bits -1 - i])
    
    return rule_dict

def render_text_with_border(screen, t, width):

    border_color = (0, 0, 0)
    text = pygame.font.Font(None, 36).render(f"t = {t}", True, (255, 255, 0))
    border_text = pygame.font.Font(None, 36).render(f"t = {t}", True, border_color)
    text_position = (width * 10 - 80, 10)
    screen.blit(border_text, (text_position[0] - 1, text_position[1] - 1))
    screen.blit(border_text, (text_position[0] + 1, text_position[1] - 1))
    screen.blit(border_text, (text_position[0] - 1, text_position[1] + 1))
    screen.blit(border_text, (text_position[0] + 1, text_position[1] + 1))
    screen.blit(text, (width * 10 - 80, 10))

def draw_cells(screen, cells_on_screen):

    for i, row in enumerate(cells_on_screen):
        for j, cell in enumerate(row):
            if cell == -1:
                color = (220, 220, 220)
            else:
                color = (255, 255, 255) if cell == 0 else (0, 0, 0)
            pygame.draw.rect(screen, color, (j * 10, i * 10, 10, 10))

def get_new_cells(rule_dict, current_cells, r):

    N = len(current_cells)

    new_cells = []
    
    for c in range(N):
        
        input_str = ''
        
        for i in range(-r, r+1):
            
            corrected_index = (c+i)%len(current_cells)
            
            input_str += str(current_cells[corrected_index])
            
        new_cells.append(rule_dict[input_str])
        
    return new_cells

def get_rule_dict_from_rule_list(rule_list):
    rule_dict = {format(i, '0' + str(round(math.log(len(rule_list))/math.log(2))) + 'b'): v
                for i,v in enumerate(rule_list)}
    return rule_dict

def user_option(p, use_pred_color=True):

    option = 1

    while option != 0:
        
        s = textwrap.dedent("""
            Type q to quit.
            Type e to evolve.
            Type s to simulate the best chromosome.
            Type a to automatically evolve from now on.
            Type an integer n to evolve n generations.
            Type here: """)
        option = input(s).lower()

        if option == 's':
            p.population[0].simulate(Config.height, get_uniformly_distributed_ic(p.population[0].N, predominant_color=1),show_time = False, stop = 30)

        elif option == 'q':
            ret = 'q'
            return ret

        elif option =='a':
            ret = 'c'
            return ret

        else:
            if option == 'e':
                option = '1'
            try:
                generations_to_evolve = int(option)
            except:
                print("Invalid Entry")
                continue
            for i in range(generations_to_evolve):
                p.evolve(use_pred_color = use_pred_color)
                print(f"\nCurrent generation: {p.generations}")
                print(f"Current fitness: --------> {p.get_max_fitness()}")

def get_pred_color(ic):

    if sum(ic) > len(ic)/2:
        return 1
    return 0


if __name__ == '__main__':

# last rule
#   radius = 0: 2**(2**1) - 1 = 3
#   radius = 1: 2**(2**3) - 1 = 255
#   radius = 2: 2**(2**5) - 1 = 4294967295

    print(get_total_number_of_cells(2))