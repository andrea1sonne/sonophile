import sys

def run():
    # command line parser goes here
    print("This is sonophile!")

    if len(sys.argv) > 1:
        print("We have command line arguments")

        if sys.argv[1] == "foo":
            print("This will be a foo simulation.")

if __name__ == "__main__":
    run()
