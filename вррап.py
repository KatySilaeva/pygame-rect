import pygame


class Board:

    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.board = [[0] * w for _ in range(h)]
        self.left = 10
        self.top = 10
        self.cell_size = 30

    def set_veiw(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        color = [pygame.Color('black'), pygame.Color('white')]
        for y in range(self.h):
            for x in range(self.w):
                pygame.draw.rect(screen, color[self.board[y][x]],
                                 (x * self.cell_size + self.left, y * self.cell_size + self.top, self.cell_size,
                                  self.cell_size))
                pygame.draw.rect(screen, color[1],
                                 (x * self.cell_size + self.left, y * self.cell_size + self.top, self.cell_size,
                                  self.cell_size), 1)

    def get_click(self, mous_pos):
        cell = self.get_cell(mous_pos)
        self.on_click(cell)

    def get_cell(self, mous_pos):
        cell_x = (mous_pos[0] - self.left) // self.cell_size
        cell_y = (mous_pos[1] - self.top) // self.cell_size
        if cell_x < 0 or cell_x >= self.w or cell_y < 0 or cell_y >= self.h:
            return None
        return cell_x, cell_y

    def on_click(self, cell_coords):
        for i in range(self.w):
            self.board[cell_coords[1]][i] = (self.board[cell_coords[1]][i] + 1) % 2
        for i in range(self.h):
            if i == cell_coords[1]:
                continue
            self.board[i][cell_coords[0]] = (self.board[i][cell_coords[0]] + 1) % 2


def main():
    pygame.init()
    size = we, he = 800, 600
    screen = pygame.display.set_mode(size)

    running = True

    board = Board(5, 7)
    board.set_veiw(100, 100, 50)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                board.get_click(event.pos)
        screen.fill(pygame.Color('black'))
        board.render(screen)
        pygame.display.flip()


if __name__ == '__main__':
    main()
