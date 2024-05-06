def print_reverse(n):
    # Base case: if n is 0, do nothing and return
    if n == 0:
        return 
    
    # Recursively call print_reverse with a reduced value of n
    print_reverse(n-1)
    
    # Print the disk number
    print("Disk no", n)

def tower_of_hanoi(n, src_rod, aux_rod, dest_rod):
    # Base case: if n is 0, do nothing and return
    if n == 0:
        return
    
    # Move (n-1) disks from source to auxiliary rod
    tower_of_hanoi(n-1, src_rod, dest_rod, aux_rod)
    
    # Print the movement of the nth disk from source to destination rod
    print("Disk", n, "moved from", src_rod, "to", dest_rod)
    
    # Move (n-1) disks from auxiliary rod to destination rod
    tower_of_hanoi(n-1, aux_rod, src_rod, dest_rod)

# Input: Get the number of disks from the user
n = int(input("Enter the number of disks : "))

# Output: Display the order of disks in reverse
print("\nThe order of disks will be :")
print_reverse(n)

# Output: Display the towers and the number of steps
print("\nTower A acts as source\nTower B acts as aux\nTower C acts as destination\n")
tower_of_hanoi(n, "A", "B", "C")
moves = (2**n) - 1
print(f"\nNo of steps : {moves}")
