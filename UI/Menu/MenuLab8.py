import json
import os
from UI.MenuBuilder.MenuBuilder import MenuBuilder


class MenuLab8:
    # Constructor method for the MenuLab8 class
    def __init__(self, data_processor, validator, reader_writer):
        self.data_processor = data_processor
        self.validator = validator
        self.reader_writer = reader_writer

    # Method to display the menu options
    def display_options(self):
        # Get the current file directory and the relative path to the config file
        current_file_directory = os.path.dirname(os.path.abspath(__file__))
        relative_config_path = os.path.join('..', '..', 'Config', 'init.json')
        config_path = os.path.abspath(os.path.join(current_file_directory, relative_config_path))

        # Open the config file and load the JSON data
        with open(config_path, 'r') as file:
            config = json.load(file)

        # Get the menu configuration and create a MenuBuilder object
        menu_config = config['menu8']
        menu_builder = MenuBuilder(menu_config)

        # Display the menu
        menu_builder.display()

    # Method to run the menu
    def run(self):
        # Define the valid options
        valid_options = ['1', '2', '3', '4']

        # Loop until the user chooses to exit
        while True:
            # Display the menu options
            self.display_options()

            # Get the user's choice and validate it
            choice = self.validator.validate_input("Choose an option (1/2/3/4): ", valid_options)

            # Perform the action corresponding to the user's choice
            if choice == '1':
                # If the user chooses to explore data, ask for confirmation and then explore data
                if self.validator.validate_input("Explore data? (yes/no): ", ['yes', 'no']) == 'yes':
                    print("Exploring data...")
                    self.data_processor.explore_data()
            elif choice == '2':
                # If the user chooses to generate visualizations, ask for confirmation and then generate visualizations
                if self.validator.validate_input("Generate visualizations? (yes/no): ", ['yes', 'no']) == 'yes':
                    print("Generating visualizations...")
                    self.data_processor.visualize_data()
            elif choice == '3':
                # If the user chooses to save visualizations, ask for confirmation and then save visualizations
                if self.validator.validate_input("Save visualizations? (yes/no): ", ['yes', 'no']) == 'yes':
                    print("Saving visualizations...")
                    self.data_processor.visualize_data(save=True)
            elif choice == '4':
                # If the user chooses to exit, print a goodbye message and break the loop
                print("Goodbye!")
                break




