# for this project used chatgpt 
import random

def generate_names():
    first_names = {
        "ladies": ["Alice", "Emma", "Sophia", "Isabella", "Olivia", "Ava", "Mia", "Charlotte", "Amelia", "Harper"],
        "gentlemen": ["Liam", "Noah", "William", "James", "Oliver", "Benjamin", "Elijah", "Lucas", "Mason", "Logan"]
    }
    last_names = ["Smith", "Johnson", "Brown", "Williams", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez"]
    
    category = input("Would you like ladies' names or gentlemen's names? (ladies/gentlemen): ").strip().lower()
    while category not in first_names:
        category = input("Invalid choice. Please enter 'ladies' or 'gentlemen': ").strip().lower()
    
    available_first_names = first_names[category][:]
    available_last_names = last_names[:]
    random.shuffle(available_first_names)
    random.shuffle(available_last_names)
    
    for _ in range(10):
        if not available_first_names or not available_last_names:
            print("No more unique names available.")
            break
        
        first_name = available_first_names.pop()
        last_name = available_last_names.pop()
        print(f"{first_name} {last_name}")
        
generate_names()
    
   