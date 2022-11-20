import constants
from game.casting.actor import Actor
from game.shared.point import Point

class Cycle(Actor):
    """
    A one man vehicle you ride on.
    
    The responsibility of Cycle is to move itself.
    
    Attributes:
        _points (int): The number of points
    """
    def __init__(self, color):
        super().__init__()
        self._cycle_color = color
        self._segments = []
        self._prepare_body()
        
    def get_segments(self):
        return self._segments
    
    def move_next(self):
        # move all segments
        for segment in self._segments:
            segment.move_next()
        # update velocities
        for i in range(len(self._segments) -1, 0, -1):
            trailing = self._segments[i]
            previous = self._segments[i - 1]
            velocity = previous.get_velocity()
            trailing.set_velocity(velocity)
            # self.grow_trail(1) ---------------- Taking this out to see how to shorten the two snake as we watch them grow
            
    def get_head(self):
        return self._segments[0]
    
    def grow_trail(self, number_of_segments):
        for i in range(number_of_segments):
            tail = self._segments[-1]
            velocity = tail.get_velocity()
            offset = velocity.reverse()
            position = tail.get_position().add(offset)
            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text("#")
            segment.set_color(self._cycle_color)
            self._segments.append(segment)
            
    def turn_head(self, velocity):
        self._segments[0].set_velocity(velocity)
        
    def _prepare_body(self):
        x = 0.0
        y = 0.0
        
        if self._cycle_color == constants.RED: #made an adjustment to this, i removed it from the bracket to see if it does affect anything
      
            x = int(-20)
            y = int(constants.MAX_Y / 4)
        else:
            x = int(20)
            y = int(constants.MAX_Y / 2)
        
        for i in range(constants.CYCLE_LENGTH):
            position = Point(x - i * constants.CELL_SIZE, y)
            velocity = Point(1 * constants.CELL_SIZE, 0)
            text = "8" if i == 0 else "#"
            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text(text)
            segment.set_color(self._cycle_color)
            self._segments.append(segment)


              #     x = int(constants.MAX_X / 1)
        #     y = int(constants.MAX_Y / 10)
        # else:
        #     x = int(constants.MAX_X // 1)
        #     y = int(constants.MAX_Y // 4)

        # for i in range(constants.CYCLE_LENGTH):
        #     position = Point(x - i * constants.CELL_SIZE, y)
        #     velocity = Point(1 * constants.CELL_SIZE, 0)
        #     text = "8" if i == 0 else "#"

        #     segment = Actor()
        #     segment.set_position(position)
        #     segment.set_velocity(velocity)
        #     segment.set_text(text)
        #     segment.set_color(self._cycle_color)
        #     self._segments.append(segment)
