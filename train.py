import time

def main():
    print("Starting training")

    for i in range(5):
        print(f"Epoch {i+1}/5 ")
        time.sleep(1)

    print("Training is completed")

if __name__ == "__main__":
    main()

# run training