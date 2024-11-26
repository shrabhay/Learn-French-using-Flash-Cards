# Learn French using Flash Cards
## Description
A user-friendly Flash Card App built with Python and Tkinter, designed to help you learn French vocabulary efficiently. This interactive app displays French words with their English translations and allows you to track and revisit words you’ve learned or need to practice more.

---

## Features
* **Flash Card Interface**:
  * Displays a French word on one side of the card.
  * Automatically flips the card after 3 seconds to reveal the English translation.

* **Learn and Track Progress**:
  * Mark words as "known" to remove them from the practice list.
  * Saves progress by tracking words left to learn in a separate file.

* **Interactive Design**:
  * Intuitive buttons for marking words as "known" or moving to the next word.
  * Engaging graphics for the flashcards and buttons.

---

## Project Structure
```
Flash Card App
├── flash_card_app.py              # Main application file with GUI and functionality.
├── data
│   ├── french_words.csv           # Original dataset of French words and their English translations.
│   └── words_left_to_learn.csv    # Auto-generated file to track words left to learn.
├── images
│   ├── card_front.png             # Image for the front of the flashcard.
│   ├── card_back.png              # Image for the back of the flashcard.
│   ├── wrong.png                  # Image for the "unknown" button.
│   └── right.png                  # Image for the "known" button.
```

---

## Setup Instructions

### Prerequisites
* Python 3.8 or higher installed on your system.
* Required Python libraries:
  * `pandas`
  * `tkinter` (comes pre-installed with Python on most systems)

### Installation
1. Clone this repository:
    ```commandline
    git clone https://github.com/shrabhay/Learn-French-using-Flash-Cards.git
    cd flash-card-app
    ```

2. Install dependencies:
    ```commandline
    pip3 install pandas
    ```

3. Run the application:
    ```commandline
    python3 flash_card_app.py
    ```

---

## How to Use
### 1. Start the App
* Launch the application to see the first flash card with a French word displayed.

### 2. Mark Words
* If you know the word, click the green checkmark button to mark it as "known."
* If you don’t know the word, click the red cross button to move to the next word.

### 3. Learn at Your Own Pace
* The app automatically tracks your progress and saves words you need to practice in a `words_left_to_learn.csv` file.

### 4. Continue Learning
* When you restart the app, it picks up where you left off, using the words_left_to_learn.csv file.

---

## File Details
### 1. `flash_card_app.py`
* The main application file that:
  * Reads the word data from a CSV file.
  * Tracks progress and updates the dataset dynamically.
  * Sets up the Tkinter-based GUI.

### 2. `data/french_words.csv`
* Original dataset containing French words and their English translations in a CSV format.

### 3. `data/words_left_to_learn.csv`
* Auto-generated file that stores the remaining words to learn. Created after marking words as "known."

### 4. Images
* `card_front.png`: The design for the front of the flash card.
* `card_back.png`: The design for the back of the flash card.
* `wrong.png`: The image for the "unknown" button.
* `right.png`: The image for the "known" button.

---

## Future Enhancements
* Add additional datasets for other languages or subjects.
* Introduce user accounts to manage individual progress.
* Enhance the UI with animations and sound effects.
* Provide statistics on learning progress.

---

## Screenshots
### Flash Card Front:
![flash card front](https://github.com/shrabhay/Learn-French-using-Flash-Cards/blob/main/screenshots/flash_card_front.png)

### Flash Card Back:
![flash card back](https://github.com/shrabhay/Learn-French-using-Flash-Cards/blob/main/screenshots/flash_card_back.png)

---

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

---

## Contributing
Contributions are welcome! If you have suggestions or feature requests, feel free to open an issue or submit a pull request.
