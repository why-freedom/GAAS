#encoding=utf-8

'''
To make the UAV move to track the trace of a certain object manually selected or find by algorithm.

The position of object is generated by object_tracking algorithm.result is published via ROS msg.
'''


def generate_trace_by_target_3d_relative_position(object_p,uav_cam_current_q):# input the cam rotation and object relative position.
    x,y,z = object_p
    pass
    return uav_vx,uav_vy,uav_vz,uav_target_yaw,uav_cam_target_pitch

def publish_next_move_with_collision_avoidance(obstacle_map,next_target):
    #call the function in tutoral1.


def main():
    #init rospy node.
    #subscribe object tracking result,that is the 3d position of object and the rotation of camera.
    #subscribe obstacle info in octree.
    #publish next move generated by generate_trace_by_target_3d_relative_position() and publish_next_move_with_collision_avoidance().
    #publish rviz info to debug.
    

if __name__ == '__main__':
    main()


