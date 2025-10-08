# 🎲 Daily Basis

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![Pygame](https://img.shields.io/badge/Pygame-2.x-green.svg)](https://www.pygame.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)]()

A fun and engaging board game built with Python and Pygame where players race to collect gold while managing their coins through various events and challenges!

## 📹 Video Demo
[Watch the Demo on YouTube](https://youtu.be/MX1eX4aTDz8)

## 📖 About

**Daily Basis** is a 2-player turn-based board game inspired by classic board games. Players move across a 50-space board, landing on different types of spaces that affect their coins and gold. The objective is simple but challenging: be the first player to reach the goal amount of gold!

### 🎯 Game Objective

Be the first player to collect the target amount of **gold** (default: 5 gold) to win the game!

## ✨ Features

### 🎮 Game Mechanics
- **Turn-based gameplay** for 2 players
- **Dice rolling** system (1-6)
- **50-space board** with multiple paths
- **Multiple space types** with unique effects:
  - 🔵 **Blue Spaces** - Earn +3 coins
  - 🎲 **Chance Spaces** - Draw random chance cards (27 different events)
  - 🎰 **Gacha Spaces** - Try your luck with random rewards
  - 💀 **Bad Luck Spaces** - Face unfortunate events
  - 💰 **Gold Spaces** - Purchase gold with coins

### 🎴 Event System
- **27 unique Chance cards** with various effects:
  - Gain or lose coins
  - Move forward or backward on the board
  - Earn gold
  - Interest on coins
  - And many more surprises!

### ⚙️ Customization
- Adjustable **goal gold** amount (1-100)
- Custom starting **coins** for each player
- Custom starting **gold** for each player
- **Music volume** control
- Background music toggle (on/off)

### 🎨 User Interface
- Colorful and intuitive game board
- Visual dice animations
- Event card displays
- Real-time stats tracking for both players
- Main menu with settings

## 🛠️ Installation

### Prerequisites
- Python 3.x
- Pygame library

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/DNeilson67/DailyBasis-main.git
   cd DailyBasis-main
   ```

2. **Install Pygame**
   ```bash
   pip install pygame
   ```

3. **Run the game**
   ```bash
   python main.py
   ```

## 🎮 How to Play

1. **Start the Game**
   - Launch the game and click the "Start" button
   - The game randomly determines which player goes first

2. **Taking Turns**
   - Click the dice to roll (1-6)
   - Your player piece automatically moves to the new position
   - Land on different spaces for various effects

3. **Space Types**
   - **Blue Spaces**: Automatically gain 3 coins
   - **Chance Spaces**: Draw a random chance card
   - **Gacha Spaces**: Trigger gacha event
   - **Bad Luck Spaces**: Face a random unfortunate event
   - **Gold Spaces**: Opportunity to convert coins to gold

4. **Winning**
   - First player to reach the goal gold amount wins!

## 📁 Project Structure

```
DailyBasis-main/
├── main.py              # Main game loop and initialization
├── gamefunctions.py     # Core game functions and logic
├── event.py            # Event system (chance, gacha, bad luck)
├── movement.py         # Board movement and position data
├── player1.py          # Player 1 class and properties
├── player2.py          # Player 2 class and properties
├── dice.py             # Dice rolling mechanics
├── bg.py               # Background and board graphics
├── inputs.py           # Button inputs and UI interactions
├── msg.py              # Message display system
├── settings.py         # Game settings and configuration
├── images/             # Game graphics and sprites
│   ├── board.png
│   ├── dice1-6.png
│   ├── chances/        # 27 chance card images
│   ├── badluck/        # Bad luck card images
│   └── gacha/          # Gacha card images
└── sound/              # Game audio files
    ├── BGM.wav
    ├── chance.wav
    ├── coin.wav
    └── ...
```

## 🎵 Audio Credits

The game features background music and sound effects for:
- Background music (BGM)
- Dice rolling
- Coin collection
- Gold acquisition
- Event triggers
- Button clicks

## 🎓 Academic Project

This project was developed as a **Final Project** for the **Algorithm and Programming** course at BINUS University.

**Developer**: Davin Neilson (2602119133)

## 🎯 Game Statistics

- **Board Spaces**: 50
- **Chance Cards**: 27 unique events
- **Bad Luck Cards**: 15 unique events
- **Gacha Options**: 5 different outcomes
- **Maximum Coins/Gold**: 100 each
- **Default Starting Coins**: 10 per player
- **Default Starting Gold**: 0 per player
- **Default Goal Gold**: 5

## 🤝 Contributing

This is an academic project, but suggestions and feedback are welcome! Feel free to open an issue or submit a pull request.

## 📄 License

This project is created for educational purposes.

## 📧 Contact

For questions or feedback, please reach out through the GitHub repository.

---

**Enjoy playing Daily Basis! 🎲🎮**
