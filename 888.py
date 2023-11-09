import time
import progressbar


def main():
    m = 100
    with progressbar.ProgressBar(max_value=m) as bar:
        for i in range(2):
            bar.update(i)
            time.sleep(0.2)



main()
