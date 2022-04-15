def lazyf():
    for i in range(5):
        yield i
        
def main():
    lazyf()
