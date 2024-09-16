from machine import Pin
from time import sleep
from seven_segment import SevenSegment as seg

class Main:   
    def main():            
        A = seg(0, 1, 2, 3)
        A.clear_data()
        B = seg(4, 5, 6, 7)
        B.clear_data()

        counter = 0   

        A.display_number(15)

        while counter <= 11:
            if counter == 11:
                counter = 0
            print(f'number{[counter]}')
            A.display_number(counter)
            B.display_number(counter)
            sleep(0.5)
            counter += 1
    
    if __name__ == "__main__":
        main()
