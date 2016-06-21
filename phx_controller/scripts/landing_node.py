#!/usr/bin/env python
import numpy as np
import rospy
from phx_uart_msp_bridge.msg import Altitude
from phx_uart_msp_bridge.msg import RemoteControl
from sensor_msgs.msg import Imu

#If we want our code to work properly we have to run another class: AltitudeHoldNode()
#It should be working before our device reaches the altitude of 1m


class LandingNode():
    def __init__(self):
        rospy.init_node('landing_controller')
        self.input_rc = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000]
        self.sub_imu = rospy.Subscriber('/phx/imu', Imu, self.imuCallback)
        self.sub = rospy.Subscriber('/phx/marvicAltitude/altitude', Altitude, self.altitudeCallback)

        self.pub = rospy.Publisher('/phx/rc_computer', RemoteControl, queue_size=1)
        self.enabled = False
        self.p = 1
        self.d = 5
        self.setPoint_d = 9.81
        self.setPoint = 1


        self.freq = 100  # Hz
        self.r = rospy.Rate(self.freq)

        self.altitude_start = 1
        self.altitude = 0.0
        self.linear_acceleration_z = 0.0

        self.controlCommand = 1500

    def altitudeCallback(self, altitude_msg):
        self.altitude = altitude_msg.estimated_altitude

    def imuCallback(self, imu_msg):
        self.linear_acceleration_z = imu_msg.linear_acceleration.z

    def enableCallback(self, enable):
        self.enabled = enable

    def run(self):
        while not rospy.is_shutdown():
            if self.enabled:
                controlCommand_p = (self.setPoint - self.altitude) * self.p
                controlCommand_d = (self.setPoint_d - self.linear_acceleration_z) * self.d

                un_cliped = self.controlCommand + controlCommand_p + controlCommand_d
                self.controlCommand = np.clip(un_cliped, 1000, 2000)

                print(self.controlCommand, self.altitude, self.linear_acceleration_z)
            self.r.sleep()
        '''
        if(self.altitude < self.altitude_start):
                if(self.linear_acceleration_z > 0.1):
                    self.throttle += 2
            else:
                self.throttle -= 10
        '''



if __name__ == '__main__':
    try:
        controller_node = LandingNode()
        controller_node.enabled = True;
        controller_node.run()
    except rospy.ROSInterruptException:
        pass
