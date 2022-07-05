from grbl_ros._command import command
from grbl_ros._configure import configure
from grbl_ros._control import control
from grbl_ros._logging import logging


class grbl(control, command, configure, logging):
    """Initializes the base grbl device class."""

    def __init__(self, node):
        self.mode = self.MODE.NORMAL
        self.state = self.STATE.ALARM  # initalize to alarm state for safety
        self.node = node  # so we can pass info to ROS
        self.s = None  # serial port object
        self.abs_move = None  # GRBL has 2 movement modes: relative and absolute
        self.machine_id = "cnc_000"
        self.baudrate = 0
        self.port = ""
        self.acceleration = 0
        self.x_max = 0
        self.y_max = 0
        self.z_max = 0
        self.defaultSpeed = 0
        self.x_max_speed = 0
        self.y_max_speed = 0
        self.z_max_speed = 0
        self.x_steps_mm = 0  # number of steps per centimeter
        self.y_steps_mm = 0  # number of steps per centimeter
        self.z_steps_mm = 0  # number of steps per centimeter
        self.idle = True  # machine is idle
        self.pos = [0.0, 0.0, 0.0]  # current position     [X, Y, Z]
        self.angular = [0.0, 0.0, 0.0, 0.0]  # quaterion  [X, Y, Z, W]
        self.origin = [0.0, 0.0, 0.0]  # minimum coordinates  [X, Y, Z]
        self.limits = [0.0, 0.0, 0.0]  # maximum coordinates  [X, Y, Z]
