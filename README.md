# Checkers AI Project

This project aims to create an intelligent agent that learns to play Checkers, capable of competing against human players. It uses a combination of game theory, artificial intelligence (AI), and graphical user interface (GUI) programming to create an engaging and interactive experience. The initial version of the AI uses an expert system, with plans to incorporate machine learning for improved decision-making over time.

## Getting Started

These instructions will guide you through setting up the project on your local machine for development and testing purposes.

### Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.8 or higher

#### Installing Python

If you don't have Python installed, download and install it from the [Python official website](https://www.python.org/downloads/). Ensure you select the version that corresponds to your operating system. During installation, remember to check the option that says 'Add Python to PATH' to make Python accessible from the command line.

### Installing

Follow these steps to get your development environment up and running:

1. **Clone the repository:**
   
   ```
   git clone https://github.com/yourusername/checkers-ai.git
   ```

2. **Navigate to the project directory:**
   
   ```
   cd checkers-ai
   ```

3. **Create a virtual environment:**
   
   ```
   python -m venv venv
   ```

4. **Activate the virtual environment:**
   
   - On Windows:
     
     ```
     .\venv\Scripts\activate
     ```
   
   - On MacOS/Linux:
     
     ```
     source venv/bin/activate
     ```

5. **Install the required packages:**
   
   ```
   pip install -r requirements.txt
   ```

   Note: To exit the virtual environment, simply type `deactivate` in the command line.

## Usage

To run the project:

1. Ensure the virtual environment is activated.
2. Execute the main script in the root folder:
   
   ```
   python main.py
   ```

This will start the game, allowing a human player to compete against the AI or observe the AI play against itself.

## Contributing

If you wish to contribute to this project, please feel free to fork the repository and submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to everyone who contributed to the development of the AI algorithms and game strategies.

## Model Development Process

In the initial phase, we implemented an expert system for the AI to make decisions based on predefined rules. The focus was on creating a solid game logic that supports all basic checkers rules, including jumping and kinging, as well as developing a user-friendly GUI for gameplay. Future plans include integrating machine learning to enhance the AI's decision-making capabilities, aiming for a system that learns from each game and continuously improves its strategy against human players.