from main import add

def testadd():
    assert add(2,3)==5
    print("Successful")

if __name__ == '__main__':
    testadd()