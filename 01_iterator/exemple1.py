class MazeIterator:

    def __init__(self, maze):
        self._maze = maze
        self._current = (0, 0)

    def __next__(self):
        x, y = self._current

        while x < self._maze.height:
            while y < self._maze.width:
                self._current = x, y = x, y+1
                if self._maze[x, y-1]:
                    return x, y-1
            self._current = x, y = x+1, 0

        raise StopIteration("L'itération à travers le labyrinthe est terminée")

    def __iter__(self):
        return self
        

class Maze:

    def __init__(self, structure):
        self._structure = structure
        self.height = len(structure)
        self.width = len(structure[0])

    def __getitem__(self, key):
        x, y = key
        return (
            (0 <= x < self.height) and
            (0 <= y < self.width) and
            self._structure[x][y] == '.'
        )

    @classmethod
    def load_from_file(cls, filename):
        structure = None
        with open(filename) as f:
            structure = [list(line[:-1]) for line in f.readlines()]
        return cls(structure)

    def __repr__(self):
        s = ''
        for line in self._structure:
            s += "".join(line) + "\n"
        return s

    def __iter__(self):
        return MazeIterator(self)
    
def main():
    maze = Maze.load_from_file("exemple1.txt")
    for position in maze:
        print(position)

if __name__ == "__main__":
    main()