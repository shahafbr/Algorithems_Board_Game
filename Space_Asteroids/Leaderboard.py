import pygame

class Leaderboard:
    def __init__(self):
        pygame.init()
        self.scores = []  # List to hold scores in the format [(name, score), ...]
        self.font = pygame.font.Font(None, 36)  
        self.title_font = 'Space_Asteroids/Assets/Sprites/Font.ttf'  
        self.screen = pygame.display.set_mode((800, 600))
        self.background = pygame.image.load('Space_Asteroids/Assets/Sprites/Leaderboard.png')  # Load the background image
        self.new_score = ("", 0)
    def add_score(self, name, score):
        self.scores.append((name, score))
        self.sort_by_score()
    
    def merge_sort(self, array):
        if len(array) > 1:
            mid = len(array) // 2  
            L = array[:mid]  
            R = array[mid:]
            self.merge_sort(L)  
            self.merge_sort(R)  

            i = j = k = 0
            # Copy data to temp arrays L[] and R[]
            while i < len(L) and j < len(R):
                if L[i][1] < R[j][1]:
                    array[k] = L[i]
                    i += 1
                else:
                    array[k] = R[j]
                    j += 1
                k += 1
            # Checking if any element was left
            while i < len(L):
                array[k] = L[i]
                i += 1
                k += 1
            while j < len(R):
                array[k] = R[j]
                j += 1
                k += 1

    def sort_by_score(self):
        self.merge_sort(self.scores)  # Use merge_sort instead of sort
        self.scores.reverse()  # Since merge_sort sorts in ascending order, reverse for descending
        self.scores = self.scores[:10]  # Keep only top 10 scores

    def sort_alphabetically(self):
        self.scores.sort(key=lambda x: x[0])

    def display(self, x, y):
        # Display the background
        self.screen.blit(self.background, (0, 0))

        # Load a custom TTF font for the title
        custom_title_font = pygame.font.Font(self.title_font, 48)

        # Display the title (centered at the top)
        title_surface = custom_title_font.render("Leader Board", True, (255, 255, 255))
        title_rect = title_surface.get_rect(center=(self.screen.get_width() // 2, 50))  # Adjust y to place the title accordingly
        self.screen.blit(title_surface, title_rect)

        # Calculate the starting y position of the list so it's centered vertically
        list_start_y = (self.screen.get_height() - len(self.scores) * 40) // 2  # Adjust 40 to match the line height

        # Display the top 10 scores (centered)
        for index, (name, score) in enumerate(self.scores):
            score_text = self.font.render(f"{index + 1}. {name} - {score}", True, (255, 255, 255))
            text_rect = score_text.get_rect(center=(self.screen.get_width() // 2, list_start_y + index * 40))  # 40 is line height

            # Draw a rectangle around the name
            pygame.draw.rect(self.screen, (255, 255, 255), text_rect.inflate(20, 10), 2)

            # Blit the score text (centered on the screen)
            self.screen.blit(score_text, text_rect)

    # Button interaction methods to be implemented
    def draw_button(self, text, x, y, width, height):
        """Draw a button and return its rect for click detection."""
        button_rect = pygame.Rect(x, y, width, height)
        pygame.draw.rect(self.screen, (50, 50, 50), button_rect)  # Blue button
        text_surface = self.font.render(text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=button_rect.center)
        self.screen.blit(text_surface, text_rect)
        return button_rect

    def handle_button_click(self, button_rect, mouse_pos):
        """Check if a button is clicked and return True or False."""
        if button_rect.collidepoint(mouse_pos):
            return True
        return False
    
    def read_scores_from_file(self, filename):
        scores = []
        with open(filename, 'r') as file:
            for line in file:
                name, score = line.strip().split(',')
                scores.append((name, int(score)))
        return scores

    def write_scores_to_file(self, filename, scores):
        with open(filename, 'w') as file:
            for name, score in scores:
                file.write(f"{name},{score}\n")

    def run_leaderb(self, new_score):
        screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Leaderboard")
        
        # Create a Leaderboard instance
        # Replace 'path_to_background_image.jpg' with the actual path to your background image
        leaderboard = Leaderboard()

        # Example scores
        scores = leaderboard.read_scores_from_file("Score_Storing.txt")
        print(scores)
        scores.append(new_score)
        scores.sort(key=lambda x: x[1], reverse=True)  # Assuming the score is the second element of the tuple

        # Keep only the top 10 scores
        scores = scores[:10]
        for name, score in scores:
            leaderboard.add_score(name, score)

        # Define button dimensions and positions
        button_width, button_height = 150, 50
        alpha_button_rect = pygame.Rect(100, 550, button_width, button_height)
        score_button_rect = pygame.Rect(550, 550, button_width, button_height)

        # Game loop
        running = True
        
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Check if either button is clicked
                    if leaderboard.handle_button_click(alpha_button_rect, event.pos):
                        leaderboard.sort_alphabetically()
                    elif leaderboard.handle_button_click(score_button_rect, event.pos):
                        leaderboard.sort_by_score()

            # Clear screen
            screen.fill((0, 0, 0))

            # Display leaderboard
            leaderboard.display(100, 50)

            # Draw buttons
            button_width, button_height = 150, 50
            alpha_button_rect = leaderboard.draw_button("Alphabet", 100, 550, button_width, button_height)
            score_button_rect = leaderboard.draw_button("Score", 550, 550, button_width, button_height)

            # Update display
            pygame.display.flip()
            updated_scores = scores[:10]
            self.write_scores_to_file("Score_Storing.txt", updated_scores)
          
"""
if __name__ == "__main__":
    leaderboard = Leaderboard()
    leaderboard.run_leaderb(("Rapi", 100))
    pygame.quit()
"""
