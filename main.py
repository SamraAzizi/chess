import pygame 

pygame.init()
WIDTH = 1000
HEIGHT = 900

screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Two Player Pygame Chess")
font = pygame.font.Font('freesansbold.ttf', 20)
big_font = pygame.font.Font('freesansbold.ttf', 50)
timer = pygame.time.Clock()
fps = 60


#game variable and images

white_pieces = ['knight','bishop','king','queen','bishop','knight','rook'
                ,'pawn' ,'pawn' ,'pawn' ,'pawn' ,'pawn' ,'pawn' ,'pawn' ,'pawn' ]



white_location = [(0,0),(1.0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0)
                  ,(0,1),(1.1),(2,1),(3,1),(4,1),(5,1),(6,1),(7,1)]






black_pieces = ['knight','bishop','king','queen','bishop','knight','rook'
                ,'pawn' ,'pawn' ,'pawn' ,'pawn' ,'pawn' ,'pawn' ,'pawn' ,'pawn' ]

black_location = [(0,7),(1,7),(2,7),(3,7),(4,7),(5,7),(6,7),(7,7)
                  ,(0,6),(1,6),(2,6),(3,6),(4,6),(5,6),(6,6),(7,6)]

captured_pieces_white = []
captured_pieces_black = []

turn_step = 0
selection = 100
valid_moves = []



#load in game piece image (queen , king, rook, kinght, pawn)
black_queen = pygame.image.load("assets/images/black queen.png")
black_queen = pygame.transform.scale(black_queen,(80,80))
black_queen_small = pygame.transform.scale(black_queen,(45,45))



black_king = pygame.image.load("assets/images/black king.png")
black_king = pygame.transform.scale(black_king,(80,80))
black_king_small = pygame.transform.scale(black_king,(45,45))




black_rook = pygame.image.load("assets/images/black rook.png")
black_rook = pygame.transform.scale(black_rook,(80,80))
black_rook_small = pygame.transform.scale(black_rook,(45,45))




black_bishop = pygame.image.load("assets/images/black bishop.png")
black_bishop = pygame.transform.scale(black_bishop,(80,80))
black_bishop_small = pygame.transform.scale(black_bishop,(45,45))




black_knight = pygame.image.load("assets/images/black knight.png")
black_knight = pygame.transform.scale(black_knight,(80,80))
black_knight_small = pygame.transform.scale(black_knight,(45,45))




black_pawn = pygame.image.load("assets/images/black pawn.png")
black_pawn = pygame.transform.scale(black_pawn,(65,65))
black_pawn_small = pygame.transform.scale(black_pawn,(45,45))



white_queen = pygame.image.load("assets/images/white queen.png")
white_queen = pygame.transform.scale(white_queen,(80,80))
white_queen_small = pygame.transform.scale(white_queen,(45,45))




white_king = pygame.image.load("assets/images/white king.png")
white_king = pygame.transform.scale(white_king,(80,80))
white_king_small = pygame.transform.scale(white_king,(45,45))



white_rook = pygame.image.load("assets/images/white rook.png")
white_rook = pygame.transform.scale(white_rook,(80,80))
white_rook_small = pygame.transform.scale(white_rook,(45,45))




white_bishop = pygame.image.load("assets/images/white bishop.png")
white_bishop = pygame.transform.scale(white_bishop,(80,80))
white_bishop_small = pygame.transform.scale(white_bishop,(45,45))



white_knight = pygame.image.load("assets/images/white knight.png")
white_knight = pygame.transform.scale(white_knight,(80,80))
white_knight_small = pygame.transform.scale(white_knight,(45,45))



white_pawn = pygame.image.load("assets/images/white pawn.png")
white_pawn = pygame.transform.scale(white_pawn,(65,65))
white_pawn_small = pygame.transform.scale(white_pawn,(45,45))

white_images = [white_pawn, white_queen, white_king, white_knight, white_rook, white_bishop ]
small_white_images = [white_pawn_small, white_queen_small, white_king_small, white_knight_small, white_rook_small, white_bishop_small ]



black_images = [black_pawn, black_queen, black_king, black_knight, black_rook, black_bishop ]
small_black_images = [black_pawn_small, black_queen_small, black_king_small, black_knight_small, black_rook_small, black_bishop_small ]



piece_list = ['pawn','queen','king','bishop','rook','knight']

#check variable/flashing counter

#draw main game board

def draw_board():
    for i in range(32): 
        column = i % 4
        row = i // 4
        if row %2 == 0:
            pygame.draw.rect(screen, 'light gray' , [600 - (column * 200 ), row * 100, 100, 100])
            
        else:
               
            pygame.draw.rect(screen, 'light gray', [700 - (column * 200), row *100, 100 , 100])

        pygame.draw.rect(screen,"gray",[0, 800,WIDTH, 100 ] )
        pygame.draw.rect(screen,"gold",[0, 800,WIDTH, 100 ],5 )
        pygame.draw.rect(screen,"gold",[800, 0,200, HEIGHT  ],5 )
        status_text = ['White : Select a Piece To Move','White : Select a Destination'
                       ,'Black : Select a Piece To Move','Black : Select a Destination']


        screen.blit(big_font.render(status_text[turn_step], True, 'black'),(20,820))

        for i in range(9):
            pygame.draw.line(screen, 'black', (0,100 * i), (800, 100 *i),2)
            pygame.draw.line(screen, 'black', (100 * i , 0), (100 * i , 800),2)

#draw pieces onto boad

def draw_pieces():
    for i in range(len(white_pieces)):
        index = piece_list.index(white_pieces[i])
        if white_pieces[i] == 'pawn':
            screen.blit(white_pawn, (white_location[i][0] * 100 + 22 , white_location[i][1] * 100 +30))


        else:
            screen.blit(white_images[index], (white_location[i][0] * 100 + 10 , white_location[i][1] * 100 +10))   

        if turn_step < 2:
            if selection == i:
                pygame.draw.rect(screen, 'red', [white_location[i][0] * 100 +1 , white_location[i][1] * 100 +1 , 100, 100], 2)

    for i in range(len(black_pieces)):
        index = piece_list.index(black_pieces[i])
        if black_pieces[i] == 'pawn':
            screen.blit(black_pawn, (black_location[i][0] * 100 + 22 , black_location[i][1] * 100 +30))


        else:
            screen.blit(black_images[index], (black_location[i][0] * 100 + 10 , black_location[i][1] * 100 +10))

        if turn_step >= 2:
            if selection == i:
                pygame.draw.rect(screen, 'blue', [black_location[i][0] * 100 +1 , black_location[i][1] * 100 +1 , 100, 100], 2)

#function to check all pieces valid option of board

def check_options(pieces, location, turn):

    moves_list = []
    all_moves_list = []

    for i in range((len(pieces))):
        locations = location[i]
        piece = pieces[i]
        if piece == 'pawn':
            moves_list = check_pawn(location, turn)
        
        elif piece == 'rook':
            moves_list = check_rook(location, turn)

        elif piece == 'knight':
            moves_list = check_knight(location, turn)

        elif piece == 'bishop':
            moves_list = check_bishop(location, turn)

        elif piece == 'king':
            moves_list = check_king(location, turn)


        elif piece == 'queen':
            moves_list = check_queen(location, turn)


        all_moves_list.append(moves_list)

    return all_moves_list


# check valid king moves

def check_king(position, color):
    moves_list = []

    if color == "white":
        enemies_list = black_location
        friends_list = white_location

    else:
        friends_list = black_location
        enemies_list = white_location


         # 8 squars to check for kings, they can go one square any direction
        targets = [(1,2),(1,1),(1,-1),(-1,0),(-1,0),(-1, -1),(-2,-1),(0,1),(0,-1)]

        for i  in range(8):
            target = (position[0] + target[i][0], position[1] + target[i][1])
            if target not in friends_list and 0 <= target[0] <= 7 and 0 <= target[1] <= 7:
                moves_list.append(target)



    return moves_list


# check valid queen moves

def check_queen(position, color): 

    moves_list = check_bishop(position, color)
    second_list = check_rook(position, color)

    for i in range(len(second_list)):
        moves_list.append(second_list[i])

    
    return moves_list



# check bishop moves

def check_bishop(position, color):
    moves_list = []
    if color == "white":
        enemies_list = black_location
        friends_list = white_location

    else:
        friends_list = black_location
        enemies_list = white_location

    for i in range(4):  # up-right, up-left, down-right, down-left
        path = True
        chain  = 1
        if i == 0:
            x = 1
            y = -1

        elif i == 1:
            x = -1
            y = -1
        elif i == 2:
            x = 1
            y = 1
        else:
            x = -1
            y = 1
        while path:
            if (position[0] + (chain * x), position[1] + (chain * y)) not in friends_list and \
            0 <= position[0] + (chain  * x) <= 7 and 0 <= position[1] + (chain * y) <= 7:
                moves_list.append((position[0] + (chain * x),position[1] + (chain * y)))
                if(position[0] * (chain * x), position[1] + (chain * y)) in enemies_list:
                    path = False
                    chain += 1
                
            else:
                path = False







    return moves_list


#check rook moves

def check_rook(position, color):
    moves_list = []
    if color == "white":
        enemies_list = black_location
        friends_list = white_location

    else:
        friends_list = black_location
        enemies_list = white_location

    for i in range(4):  # up, down , right, left
        path = True
        chain  = 1
        if i == 0:
            x = 0
            y = 1

        elif i == 1:
            x = 0
            y = -1
        elif i == 2:
            x = 1
            y = 0
        else:
            x = -1
            y = 0

        while path:
            if (position[0] + (chain * x), position[1] + (chain * y)) not in friends_list and \
            0 <= position[0] + (chain  * x) <= 7 and 0 <= position[1] + (chain * y) <= 7:
                moves_list.append((position[0] + (chain * x),position[1] + (chain * y)))
                if(position[0] * (chain * x), position[1] + (chain * y)) in enemies_list:
                    path = False
                    chain += 1
                
            else:
                path = False


    return moves_list

   
#check valid pawn moves

def check_pawn(position, color): 
    moves_list = []
    if color == 'white':
        if (position[0], position[1] + 1) not in white_location and \
            (position[0], position[1] + 1) not in black_location and position[1] < 7:
            moves_list.append((position[0], position[1] + 1))


        if (position[0], position[1] + 2) not in white_location and \
            (position[0], position[1] + 1) not in black_location and position[1] ==1:
            moves_list.append((position[0], position[1] + 2))

        if (position[0] +1 , position[1] + 1) in black_location:
            moves_list.append((position[0] +1 , position[1] +1 ))

        if (position[0] -1 , position[1] + 1) in black_location:
            moves_list.append((position[0] -1, position[1] +1 ))




    else:

        if (position[0], position[1] - 1) not in white_location and \
            (position[0], position[1] - 1) not in black_location and position[1] >0:
            moves_list.append((position[0], position[1] - 1))


        if (position[0], position[1] - 2) not in white_location and \
            (position[0], position[1] + 1) not in black_location and position[1] ==6:
            moves_list.append((position[0], position[1] + 2))

        if (position[0] +1 , position[1] - 1) in white_location:
            moves_list.append((position[0] +1 , position[1] -1 ))

        if (position[0] -1 , position[1] - 1) in white_location:
            moves_list.append((position[0] -1, position[1] -1 ))

    return moves_list

#check valid knight moves

def check_knight(position, color):
    moves_list = []

    if color == "white":
        enemies_list = black_location
        friends_list = white_location

    else:
        friends_list = black_location
        enemies_list = white_location

        # 8 squars to check for knights, they can go two squares in one direction and one in another
        targets = [(1,2),(1,-2),(2,1),(2,-1),(-1,2),(-1, -2),(-2,-1),(-2,1),(-2,-1)]

        for i  in range(8):
            target = (position[0] + target[i][0], position[1] + target[i][1])
            if target not in friends_list and 0 <= target[0] <= 7 and 0 <= target[1] <= 7:
                moves_list.append(target)


    return moves_list




# check for valid moves for just selected piece

def check_valid_moves():
    if turn_step < 2:
        option_list = white_option
    else:
        option_list = black_options
    valid_option = option_list[selection]
    return valid_option

#draw valid moves on screen
def draw_valid(moves):
    if turn_step <2:
        color = 'red'
    else:
        color = 'blue'
    for i in range(len(moves)):
        pygame.draw.cirlce(screen, color, (moves[i][0] * 100 +50, moves[i][1] *100+ 500),5)


# draw captured pieces on side of screen

def draw_captured():

    for i in range(len(captured_pieces_white)):
        captured_piece = captured_pieces_white[i]
        index = piece_list.index(captured_piece)
        screen.blit(small_black_images)


#main game loop

black_options = check_options(black_pieces, black_location, 'black')
white_option = check_options(white_pieces, white_location, 'white')
run = True
while run:
    timer.tick(fps)
    screen.fill('dark gray')

    draw_board()
    draw_pieces()
    draw_captured()
    if selection != 100:
        valid_moves = check_valid_moves()
        draw_valid(valid_moves)
    
    #event handling 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x_coord == event.pos[0] // 100
            y_coord == event.pos[1] // 100
            click_coords = (x_coord, y_coord)

            if turn_step <= 1:
                if click_coords in white_location:
                    selection = white_location.index(click_coords)
                    if turn_step == 0:
                        turn_step = 1

            if click_coords in valid_moves and selection != 100:
                white_location[selection] = click_coords
                if click_coords in black_location:
                    black_pieces = black_location.index(click_coords)
                    captured_pieces_white.append(black_pieces[black_pieces])
                    black_pieces.pop(black_pieces)
                    black_location.pop(black_pieces)

                
                black_options = check_options(black_pieces, black_location)
                white_options = check_options(white_pieces, white_location)
    
                turn_step = 2
                selection = 100
                valid_moves = []



            if turn_step > 1:
                if click_coords in black_location:
                    selection = black_location.index(click_coords)
                    if turn_step == 2:
                        turn_step = 3

            if click_coords in valid_moves and selection != 100:
                black_location[selection] = click_coords
                if click_coords in white_location:
                    white_pieces = white_location.index(click_coords)
                    captured_pieces_white.append(white_pieces[white_pieces])
                    white_pieces.pop(white_pieces)
                    white_location.pop(white_pieces)

                
                black_options = check_options(black_pieces, black_location)
                white_options = check_options(white_pieces, white_location)
    
                turn_step = 0
                selection = 100
                valid_moves = []



    pygame.display.flip()


pygame.quit()