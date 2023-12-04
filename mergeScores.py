import pygame 

class Leaderboard:
    def __init__(self):
        self.scores = {}  # Dictionary for scores
        self.username = set()  # Set for unique usernames

    def add_score(self, username, score):
        if username not in self.username:
            self.username.add(username)
        self.scores[username] = score

    def merge_sort(self, items):
        if len(items) > 1:
            mid = len(items) // 2
            left = items[:mid]
            right = items[mid:]

            self.merge_sort(left)
            self.merge_sort(right)

            i = j = k = 0

            while i < len(left) and j < len(right):
                
                if left[i][1] > right[j][1]:
                    items[k] = left[i]
                    i += 1

                else:
                    
                    items[k] = right[j]
                    j += 1
                k += 1

            while i < len(left):
                items[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                items[k] = right[j]
                j += 1
                k += 1

    def get_sorted_scores(self):
        sorted_items = list(self.scores.items())
        self.merge_sort(sorted_items)
        return sorted_items
