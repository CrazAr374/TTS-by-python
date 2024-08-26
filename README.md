# Robo-Speaker

Robo-Speaker is a simple Python-based text-to-speech application that allows users to input text and have it spoken aloud by the computer. This project uses the `pyttsx3` library to convert text into speech.

## Features

- Convert text to speech in real-time.
- Simple and easy-to-use command-line interface.
- Repeats the process until the user types "exit" to stop.

## Requirements

- Python 3.x
- `pyttsx3` library

## Installation

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/your-username/robo-speaker.git
    ```

2. **Navigate to the Project Directory:**

    ```bash
    cd robo-speaker
    ```

3. **Install the Required Python Libraries:**

    Make sure you have `pip` installed. Then, install the required library:

    ```bash
    pip install pyttsx3
    ```

## Usage

1. **Run the Application:**

    Run the Python script using the command:

    ```bash
    python robo_speaker.py
    ```

2. **Enter Text:**

    After running the script, you will be prompted to enter text. Type in any text you want to be spoken aloud by the computer.

3. **Exit the Application:**

    To exit the application, type "exit" and press Enter.


## Troubleshooting

- **No sound output**: Make sure your speakers are turned on and the volume is up. Also, ensure your audio drivers are correctly installed.
- **Module not found**: If you get an error saying `ModuleNotFoundError: No module named 'pyttsx3'`, ensure that `pyttsx3` is installed by running `pip install pyttsx3`.

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request. We appreciate any contributions, whether it be improving the documentation, adding features, or fixing bugs.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [pyttsx3](https://pyttsx3.readthedocs.io/en/latest/) - Text-to-speech library for Python.

