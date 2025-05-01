from abc import ABC, abstractmethod

# State Interface
class MediaPlayerState(ABC):
    @abstractmethod
    def play(self, player):
        pass
    
    @abstractmethod
    def pause(self, player):
        pass
    
    @abstractmethod
    def stop(self, player):
        pass
    
    @abstractmethod
    def fast_forward(self, player):
        pass

# Concrete States
class StoppedState(MediaPlayerState):
    def play(self, player):
        print("Starting playback...")
        player.set_state(PlayingState())
    
    def pause(self, player):
        print("Cannot pause - player is stopped.")
    
    def stop(self, player):
        print("Player is already stopped.")
    
    def fast_forward(self, player):
        print("Cannot fast forward - player is stopped.")

class PlayingState(MediaPlayerState):
    def play(self, player):
        print("Player is already playing.")
    
    def pause(self, player):
        print("Pausing playback...")
        player.set_state(PausedState())
    
    def stop(self, player):
        print("Stopping playback...")
        player.set_state(StoppedState())
    
    def fast_forward(self, player):
        print("Entering fast forward mode...")
        player.set_state(FastForwardState())

class PausedState(MediaPlayerState):
    def play(self, player):
        print("Resuming playback...")
        player.set_state(PlayingState())
    
    def pause(self, player):
        print("Player is already paused.")
    
    def stop(self, player):
        print("Stopping playback...")
        player.set_state(StoppedState())
    
    def fast_forward(self, player):
        print("Cannot fast forward from pause - resume playback first.")

class FastForwardState(MediaPlayerState):
    def play(self, player):
        print("Returning to normal playback...")
        player.set_state(PlayingState())
    
    def pause(self, player):
        print("Pausing fast forward...")
        player.set_state(PausedState())
    
    def stop(self, player):
        print("Stopping playback...")
        player.set_state(StoppedState())
    
    def fast_forward(self, player):
        print("Already in fast forward mode.")

# Context
class MediaPlayer:
    def __init__(self):
        self.state = StoppedState()
    
    def set_state(self, state):
        self.state = state
    
    def play(self):
        self.state.play(self)
    
    def pause(self):
        self.state.pause(self)
    
    def stop(self):
        self.state.stop(self)
    
    def fast_forward(self):
        self.state.fast_forward(self)

# Usage example
if __name__ == "__main__":
    player = MediaPlayer()
    
    player.play()     # Starts playback
    player.pause()    # Pauses playback
    player.play()     # Resumes playback
    player.fast_forward()  # Enters fast forward
    player.play()     # Returns to normal playback
    player.stop()     # Stops playback
    player.pause()    # Attempt to pause when stopped
