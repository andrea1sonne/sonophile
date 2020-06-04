import sys

def run():
    # command line parser goes here
    print("This is sonophile!")

    if len(sys.argv) > 1:
        print("We have command line arguments")

if __name__ == "__main__":
    run()
