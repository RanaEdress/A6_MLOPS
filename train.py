import time

def main():
    print("Starting training")

    for i in range(3):
        print(f"Epoch {i+1}")
        time.sleep(1)

    raise Exception("Intentional failure")

if __name__ == "__main__":
    main()