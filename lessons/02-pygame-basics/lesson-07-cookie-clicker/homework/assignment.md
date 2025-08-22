# Practice Exercise: Cookie Clicker Game Enhancements

## Overview
This practice exercise will help you practice and expand your Pygame skills by enhancing the Cookie Clicker game with new features, better user experience, and more complex game mechanics.

## Practice Tasks

### Task 1: Upgrade System Implementation
Enhance the basic cookie clicker with an upgrade system.

**What to do:**
- Add an "Auto-Clicker" upgrade that costs 50 cookies and gives 1 cookie per second
- Add a "Cookie Factory" upgrade that costs 100 cookies and gives 5 cookies per second
- Display current cookies per second on screen
- Implement automatic cookie generation using delta time
- Show upgrade costs and current ownership
- Update costs after each purchase (increase by 20%)

**Example Features:**
```
Auto-Clickers: 2 (Cost: 72 cookies)
Factories: 1 (Cost: 120 cookies)
Cookies per second: 7
```

### Task 2: Audio System Enhancement
Add comprehensive audio features to the game.

**What to do:**
- Add click sound effect when clicking the cookie
- Add purchase sound effect when buying upgrades
- Add background music that loops continuously
- Implement volume controls (0.0 to 1.0)
- Add a mute/unmute toggle (press 'M' key)
- Ensure sounds don't overlap or cause audio issues

**Audio Features:**
- Click sound: Short, satisfying sound
- Purchase sound: Different sound for upgrades
- Background music: Looping ambient music
- Volume control: Adjustable levels

### Task 3: Save/Load System
Implement a persistent save/load system for the game.

**What to do:**
- Save game state when pressing 'S' key
- Load game state when pressing 'L' key
- Save all game variables: cookies, upgrades, costs, etc.
- Use JSON format for data storage
- Display save/load confirmation messages
- Handle file errors gracefully (create new save if none exists)

**Save Data Structure:**
```json
{
    "cookies": 150,
    "auto_clickers": 2,
    "factories": 1,
    "auto_clicker_cost": 72,
    "factory_cost": 120,
    "total_cookies_earned": 500
}
```

### Task 4: Visual Effects and Animations
Add engaging visual effects to make the game more interactive.

**What to do:**
- Make the cookie scale up/down when clicked (bounce effect)
- Add floating numbers that appear when earning cookies
- Change background color based on total cookies earned
- Add sparkle effects around the cookie when you have many upgrades
- Implement smooth button hover effects
- Add particle effects when buying upgrades

**Visual Enhancements:**
- Cookie animation: Scale from 1.0 to 1.2 and back
- Floating text: Show "+1" or "+5" when earning cookies
- Background progression: Different colors for different milestones
- Sparkle system: Visual feedback for high upgrade counts

### Task 5: Achievement System
Create an achievement system to reward player progress.

**What to do:**
- Implement at least 5 achievements with different triggers
- Display achievement notifications when earned
- Track achievement progress and completion
- Save achievements to the save file
- Show achievement list in a separate screen (press 'A' key)

**Achievement Examples:**
- "First Click": Click the cookie for the first time
- "Cookie Collector": Reach 100 cookies
- "Auto-Clicker Master": Own 10 auto-clickers
- "Factory Owner": Own 5 factories
- "Millionaire": Reach 1000 cookies

## Code Guidelines

1. **File Name**: `cookie_clicker_enhanced.py`
2. **Code Quality**: 
   - Use clear variable names and functions
   - Add comprehensive comments explaining your code
   - Use proper formatting and indentation
   - Organize code into logical sections
3. **Assets**: Include all necessary image and audio files
4. **Documentation**: Add a README file explaining how to run the game
5. **Testing**: Ensure all features work correctly and don't conflict

## Technical Requirements

### Required Imports
```python
import pygame
import sys
import os
import json
import math
import time
```

### File Structure
```
cookie_clicker_enhanced.py
assets/
    cookie.png
    bg.png
    click.wav
    purchase.wav
    background_music.mp3
README.md
```

### Key Functions to Implement
- `save_game()`: Save current game state to JSON file
- `load_game()`: Load game state from JSON file
- `update_animations()`: Handle all visual animations
- `check_achievements()`: Check and award achievements
- `play_sound()`: Play sound effects with volume control
- `draw_upgrades()`: Display upgrade buttons and info

## Tips

- Start with Task 1 and build incrementally
- Test each feature individually before combining
- Use delta time for smooth animations and consistent timing
- Handle edge cases (file errors, missing assets, etc.)
- Keep the game loop running at 60 FPS for smooth performance
- Use constants for magic numbers and configuration

## Extra Challenges

### Extra Challenge 1: Prestige System
Add a prestige system where players can reset progress for permanent bonuses:
- Prestige button appears at 1000 cookies
- Reset cookies to 0 but give permanent multiplier
- Show prestige level and bonus on screen

### Extra Challenge 2: Statistics Screen
Create a comprehensive statistics screen:
- Track total cookies earned, clicks, time played
- Show highest cookies per second achieved
- Display average cookies per click
- Press 'T' key to view statistics

### Extra Challenge 3: Mini-Game Integration
Add a simple mini-game that appears randomly:
- "Catch the falling cookie" mini-game
- Award bonus cookies for successful catches
- Appears every 30 seconds of gameplay

## Controls Reference

- **Mouse Click**: Click cookie to earn cookies
- **Mouse Click**: Click upgrade buttons to purchase
- **S Key**: Save game
- **L Key**: Load game
- **M Key**: Mute/unmute audio
- **A Key**: View achievements
- **T Key**: View statistics (extra challenge)
- **ESC Key**: Quit game

Have fun creating your enhanced Cookie Clicker game!
