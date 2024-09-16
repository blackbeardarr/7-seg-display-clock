from machine import Pin

class SevenSegment:
    def __init__(self, data_pin, clock_pin, latch_pin, clear_pin):
        self.data = Pin(data_pin, Pin.OUT)
        self.clock = Pin(clock_pin, Pin.OUT)
        self.latch = Pin(latch_pin, Pin.OUT)
        self.clear = Pin(clear_pin, Pin.OUT)
    
    def clear_data(self):
        self.clear.low()
        self.clear.high()

    def tick(self):
        self.clock.low()
        self.clock.high()

    def latch_data(self):
        self.latch.high()
        self.latch.low()

    '''
    Write a given binary value to a shift register (SN74HC595N).
    '''
    def write(self, value):
        for i in range(8):            
            # Takes the value of the binary number avaliable at position 'i'
            # and applies the AND operator to pass on either high or low.
            self.new_data = value >> i & 1
            if self.new_data == 0:
                self.data.high()
            else:
                self.data.low()
            self.tick()
    '''
    Reads in an interger value and returns the corresponding binary value
    for the shift register (SN74HC595N).
    Note: This is for a Common Anode 7-Segment-Display. Reverse each binary value
    for the more ubiquitous Common Cathode type.
    '''
    def get_bit_value(self, value):
        number = {}
        # Binary - '0b'; null, A, B, C, D, E, F, G
        # Only 7 segments to a display so position 1 on shift register
        # is unneeded.
        number[0] = 0b10000001
        number[1] = 0b11001111
        number[2] = 0b10010010
        number[3] = 0b10000110
        number[4] = 0b11001100
        number[5] = 0b10100100
        number[6] = 0b10100000
        number[7] = 0b10001111
        number[8] = 0b10000000
        number[9] = 0b10000100
        number[10] = 0b11111111 # Clears 7-seg display
        number[44] = 0b10100111 # Returns F for error
        try:
            return number[value]
        except KeyError as err:
            print("Error - Number out of bounds:", err)
            return number[44]

    '''
    Writes the binary data to a shift register, then 
    latches out the data and clears the shift register's buffer.
    '''
    def display_number(self, value):
        self.write(self.get_bit_value(value))
        self.latch_data()
        self.clear_data()