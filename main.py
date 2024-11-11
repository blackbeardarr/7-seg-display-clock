from machine import Pin
from time import sleep
import network
import rp2
import ntptime
from seven_segment import SevenSegment as seg
from time_manager import TimeManager
from wifi_config import WIFI_CREDENTIALS  # Import credentials from config file

class Main:   
    def main():
        print("Initializing...")
        
        # Initialize displays
        try:
            D = seg(0, 1, 2, 3)
            C = seg(4, 5, 6, 7)
            B = seg(8, 9, 10, 11)
            A = seg(12, 13, 14, 15)
            
            # Clear all displays
            for display in [A, B, C, D]:
                display.clear_data()
                
            print("Displays initialized")
            
            # Initialize time manager with credentials from config
            time_mgr = TimeManager(
                WIFI_CREDENTIALS["ssid"],
                WIFI_CREDENTIALS["password"],
                WIFI_CREDENTIALS["country"]
            )
            print("Connecting to WiFi...")
            
            # Connect and sync - this might take a few seconds
            time_mgr.connect_and_sync()
            print("Time synced successfully")
            
            while True:
                try:
                    # Get current time
                    hour, minute, second = time_mgr.get_time()
                    
                    print(f"Current time: {hour:02d}:{minute:02d}:{second:02d}")
                    
                    # Display hour and minute on segments
                    A.display_number(hour // 10)
                    B.display_number(hour % 10)
                    C.display_number(minute // 10)
                    D.display_number(minute % 10)
                    
                    sleep(1)
                    
                except Exception as e:
                    print(f"Error in main loop: {e}")
                    sleep(1)
                    
        except Exception as e:
            print(f"Initialization error: {e}")
            if 'A' in locals():
                for display in [A, B, C, D]:
                    display.display_number(44)  # Error display
            sleep(5)
    
    if __name__ == "__main__":
        main()