
seven = 7

def helloBasic():
    print("Hello from basicmodule.py")

def helloNumber():
    print(f"Hello, {seven}")

if not('runningFromMain' in globals()): 
    print("This is not running from the command line")


helloBasic()

if __name__ == "__main__":
    runningFromMain = True
    print("You're running this from the command line")