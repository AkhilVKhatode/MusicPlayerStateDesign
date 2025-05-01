# Media Player State Design Pattern Implementation

A Python implementation of a media player using the State design pattern to handle different playback states.

## 🎯 Features

- Implements common media player states: Playing, Paused, Stopped, and Fast Forwarding
- Clean separation of state-specific behavior
- Easy to extend with new states
- Demonstrates proper state transitions
- Clear feedback for invalid operations

## 🛠️ Design Pattern

This project demonstrates the **State behavioral design pattern**, which:

- Allows an object to alter its behavior when its internal state changes
- Encapsulates state-specific behavior in separate classes
- Makes state transitions explicit
- Eliminates large conditional statements

## 💻 Usage
```python
from media_player import MediaPlayer

player = MediaPlayer()

player.play()      # Starts playback
player.pause()     # Pauses playback
player.play()      # Resumes playback
player.fast_forward()  # Enters fast forward mode
player.stop()      # Stops playback
```

## 📝 Example Output
```
Starting playback...
Pausing playback...
Resuming playback...
Entering fast forward mode...
Stopping playback...
```
