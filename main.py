import winsound as ws
import scales
import random
import time

class Melody:
    def __init__(self):
        self.notes = [None] * 8
        self.fit = 0

def generate_random_melody():
    melody = Melody()
    notes = [0, 1, 2, 3, 4, 5, 6, 7]
    for i in range(8):
        melody.notes[i] = random.choice(notes)
    return melody

def modify_melody(melody):
    # Modify the melody here (e.g., change a random note)
    index_to_change = random.randint(0, 7)
    melody.notes[index_to_change] = random.randint(0, 7)  # Randomly modify a note
    return melody


if __name__ == "__main__":
    melodies = [generate_random_melody() for _ in range(10)]
    ssss = int(input("Input scale to use(0 = c, 1 = cm, 2 = d, etc.): "))
    while True:
        for index, melody in enumerate(melodies, 1):
            print(f"Melody {index}:")
            for note in melody.notes:
                ws.Beep(scales.scale[ssss][note], 350)
            melody.fit = int(input("rate out of 100: "))
            time.sleep(0.5)
        # Sort melodies based on fit value
        sorted_melodies = sorted(melodies, key=lambda melody: melody.fit, reverse=True)
        
        valllll = input("Continue? y/n")
        if valllll == "y":
            pass
        elif valllll == "n":
            print(sorted_melodies[0])
            exit()
        else:
            print("ARE YOU STUPID??? IT'S Y OR N. THATS NOT THAT HARD TO TYPE!!!")
        # Modify the best melody slightly and add it to the melodies array
        best_melody = sorted_melodies[0]
        melodies = melodies[:1]  # Keep the first melody

        # Create a set to store unique melodies
        unique_melodies = set()

        # Add the first melody to the set
        unique_melodies.add(tuple(best_melody.notes))

        for _ in range(9):
            # Continue generating new melodies until a unique one is found
            while True:
                new_melody = modify_melody(best_melody)
                melody_tuple = tuple(new_melody.notes)
                if melody_tuple not in unique_melodies:
                    melodies.append(new_melody)
                    unique_melodies.add(melody_tuple)
                    break

        
        print("--------------------------------------------------")
        print("|                Next Generation                 |")
        print("--------------------------------------------------")
