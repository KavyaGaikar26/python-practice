def tower_of_hanoi(n, source, auxiliary, destination):

    # Base case
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return

    # Step 1: Move n-1 disks from source to auxiliary
    tower_of_hanoi(n - 1, source, destination, auxiliary)

    # Step 2: Move the largest disk from source to destination
    print(f"Move disk {n} from {source} to {destination}")

    # Step 3: Move n-1 disks from auxiliary to destination
    tower_of_hanoi(n - 1, auxiliary, source, destination)


tower_of_hanoi(3, "A", "B", "C")