import pandas as pd

class Mission:
    def __init__(self, references, cave_heights, cave_depths):
        self.references = references
        self.cave_heights = cave_heights
        self.cave_depths = cave_depths

    @classmethod
    def from_csv(cls, file_path):
        data = pd.read_csv(file_path)
        references = data['reference'].tolist()
        cave_heights = data['cave_height'].tolist()
        cave_depths = data['cave_depth'].tolist()
        return cls(references, cave_heights, cave_depths)

# Example usage:
mission = Mission.from_csv('/Users/jelenazlataric/Desktop/ENGINEERING SCIENCE/B1 practical 1/b1-coding-practical-mt24/data/mission.csv')
print(mission.references)
print(mission.cave_heights)
print(mission.cave_depths)
