# Catcher Game - User Guide

## Getting Started

### Installation Requirements
- Python 3.7 or higher
- Pygame library (`pip install pygame`)

### Running the Game
```bash
python catcher.py
```

## Game Overview
Catcher is a fast-paced arcade game where you control a catcher at the bottom of the screen to catch falling objects. The goal is to catch as many objects as possible to earn points while avoiding letting them fall off the screen.

## Controls

### Mouse Control
- **Move Mouse Left/Right**: Move the catcher horizontally
- The catcher follows your mouse cursor's X position within the game window

### Keyboard Control
- **A Key**: Move catcher left
- **D Key**: Move catcher right
- **ESC Key**: Pause/Resume game
- **Q Key**: Quit game

### Combined Control
- You can use both mouse and keyboard controls simultaneously
- Keyboard input overrides mouse when both are active

## Gameplay Mechanics

### Objective
- Catch falling objects with your catcher
- Each caught object earns points
- Don't let objects fall past your catcher

### Falling Objects
- Objects spawn randomly from the top of the screen
- Different object types may have different point values
- Objects fall at varying speeds
- Spawn rate increases as you progress

### Scoring System
- **Basic Objects**: 10 points each
- **Bonus Objects**: 25 points each (rarer spawns)
- **Combo Multiplier**: Catching objects in quick succession increases multiplier
- **Perfect Catch**: Bonus points for catching objects in the center of the catcher

### Difficulty Progression
- Game speed increases gradually over time
- More objects spawn simultaneously at higher levels
- Special challenge objects appear at higher scores

### Game Over
- Game ends when you miss too many objects (3 misses)
- Final score is displayed with your best score
- Press SPACE to restart or Q to quit

## Tips and Strategies

### Movement Tips
- Use smooth mouse movements for precise positioning
- Keyboard controls are good for quick adjustments
- Anticipate object trajectories - position yourself early

### Scoring Tips
- Focus on consistency over risky catches
- Use the combo multiplier by catching objects quickly
- Center catches give bonus points
- Don't chase every object - sometimes it's better to let one go

### Advanced Techniques
- **Prediction**: Watch spawn patterns to predict where objects will fall
- **Positioning**: Stay centered when possible for better reaction time
- **Risk Management**: Know when to go for difficult catches vs. playing safe

## Troubleshooting

### Performance Issues
- Close other applications to free up system resources
- Lower screen resolution if the game runs slowly
- Update your graphics drivers

### Control Problems
- Ensure your mouse is properly connected and calibrated
- Check that no other applications are capturing mouse input
- Try using keyboard controls if mouse feels unresponsive

### Audio Issues
- Check system volume settings
- Verify Pygame audio initialization in console output
- Some systems may require audio driver updates

## Accessibility Features
- High contrast mode available in settings
- Adjustable game speed for different skill levels
- Visual indicators for audio cues
- Colorblind-friendly object designs

## System Requirements
- **Minimum**: Python 3.7, 512MB RAM, 50MB storage
- **Recommended**: Python 3.9+, 1GB RAM, dedicated graphics
- **Screen**: 800x600 minimum resolution
- **Input**: Mouse and keyboard support