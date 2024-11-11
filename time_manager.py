import ntptime
import time
from machine import RTC
import netman

class TimeManager:
    def __init__(self, ssid, password, country='GB'):
        """Initialize TimeManager with WiFi credentials."""
        self._ssid = ssid
        self._password = password
        self._country = country
        self._rtc = RTC()
        self._is_connected = False
        self._network_status = None

    def connect_and_sync(self):
        """Establish WiFi connection and sync time with NTP server."""
        try:
            self._network_status = netman.connectWiFi(
                self._ssid,
                self._password,
                self._country
            )
            self._is_connected = True
            self._sync_time()
        except Exception as e:
            print(f"Connection failed: {e}")
            self._is_connected = False
            raise

    def _sync_time(self):
        """Synchronize with NTP server."""
        try:
            ntptime.settime()
        except Exception as e:
            print(f"Time sync failed: {e}")
            raise

    def get_time(self):
        """Return current time as tuple (hour, minute, second)."""
        current_time = self._rtc.datetime()
        return (current_time[4], current_time[5], current_time[6])

    def get_formatted_time(self):
        """Return time as formatted string HH:MM:SS."""
        hour, minute, second = self.get_time()
        return f"{hour:02d}:{minute:02d}:{second:02d}"

    @property
    def is_connected(self):
        """Return WiFi connection status."""
        return self._is_connected