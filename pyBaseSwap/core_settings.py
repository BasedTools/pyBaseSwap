import json
import logging

class CoreSettings:
    
    # Default settings for the application
    DEFAULT_SETTINGS = {
        "address": "",  # User's wallet address, only needed for transactions
        "private_key": "",  # Private key, required for transactions like swap, approve, etc.
        "RPC": "https://mainnet.base.org",  # RPC URL for connecting to Binance Smart Chain (BSC)
        "MaxTXFeeETH": 0.0001,  # Maximum transaction fee in ETH to avoid excessive gas costs
        "Slippage": 3,  # Maximum allowed slippage percentage for swap transactions
        "timeout": 60  # Timeout in seconds for web3 requests
    }

    def __init__(self, settings_file_path: str = "Settings.json", saveSetting: bool = False):
        """
        Initializes the CoreSettings class.
        - `settings_file_path`: Path to the JSON file where settings are stored.
        - `saveSetting`: If True, changes in settings will be saved to the file.
        """
        self.saveSetting = saveSetting  # Whether to save changes to settings or not
        self.settings_file_path = settings_file_path  # Path to the settings JSON file
        self.settings = self.DEFAULT_SETTINGS.copy()  # Start with default settings
        self.load_settings()  # Load settings from the file, if available

    def reinit_settings(self):
        """
        Resets settings to default and reloads from the settings file.
        """
        self.settings = self.DEFAULT_SETTINGS.copy()  # Reset to default settings
        self.load_settings()  # Load user settings from file, if they exist

    def load_settings(self):
        """
        Loads the settings from the JSON file.
        If the file doesn't exist or there's an error, it creates a new file with default settings.
        """
        try:
            # Try to open and read settings from file
            with open(self.settings_file_path, "r") as f:
                user_settings = json.load(f)  # Load user settings from JSON file
            self.settings.update(user_settings)  # Update the default settings with user-defined ones
        except Exception as e:
            # If file not found or error occurs, optionally create the file with default settings
            if self.saveSetting:
                logging.info("Settings file not found, creating with default settings.")
                self.save_settings_to_file()

    def save_settings_to_file(self):
        """
        Saves the current settings to the JSON file.
        """
        try:
            print(self.settings_file_path)  # Print the file path to verify the location
            # Open the file in write mode and save the settings as a JSON object
            with open(self.settings_file_path, "w") as f:
                json.dump(self.settings, f, indent=4)
            logging.info(f"Settings saved to {self.settings_file_path}")
        except Exception as e:
            logging.error(f"Failed to save settings: {e}")  # Log error if unable to save

    def change_settings(self, key: str, new_value):
        """
        Changes a specific setting by its key and saves it to the file if required.
        - `key`: The setting to be changed.
        - `new_value`: The new value for the setting.
        """
        if key in self.settings:
            self.settings[key] = new_value  # Update the setting with the new value
            if self.saveSetting:
                self.save_settings_to_file()  # Save settings if the saveSetting flag is True
        else:
            logging.error(f"Setting key '{key}' not found in settings.")  # Log an error if the key doesn't exist
