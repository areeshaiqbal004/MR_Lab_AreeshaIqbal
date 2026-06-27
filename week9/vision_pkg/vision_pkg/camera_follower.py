import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image  
from geometry_msgs.msg import Twist  
from cv_bridge import CvBridge     
import cv2                        
import numpy as np                 

class CameraFollower(Node):
    def __init__(self):
        super().__init__('camera_follower')
        
        # Task 1: Camera Subscription
        self.subscription = self.create_subscription(
            Image,
            '/camera/image_raw',
            self.image_callback,
            10)
            
        # Motion Command Publisher
        self.publisher = self.create_publisher(Twist, '/cmd_vel', 10)
        self.bridge = CvBridge()
        
        # --- Strict Demo Parameters ---
        self.kp = 0.0012                # UNTOUCHED: Your working alignment gain
        self.center_deadband = 40       # UNTOUCHED: Your working pixel deadband
        self.forward_speed = 0.12       # UNTOUCHED: Your working linear approach speed

        self.get_logger().info("Demo Pipeline Armed. Real-time Telemetry Terminal Logs active.")

    def image_callback(self, msg):
        try:
            cv_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8') 
        except Exception as e:
            self.get_logger().error(f'CvBridge Error: {e}')
            return

        # Get horizontal frame layout dimensions
        height, width, _ = cv_image.shape
        image_center_x = width // 2

        # Task 2: Segment Green Colorspace
        hsv_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2HSV)
        lower_green = np.array([35, 100, 40])
        upper_green = np.array([85, 255, 255])
        mask = cv2.inRange(hsv_image, lower_green, upper_green)

        # Task 3: Compute Centroid
        moments = cv2.moments(mask)
        twist = Twist()

        # STEP 1: Detection Check
        if moments["m00"] > 800: 
            cx = int(moments["m10"] / moments["m00"])
            cy = int(moments["m01"] / moments["m00"])
            
            # Crosshair telemetry overlays
            cv2.circle(cv_image, (cx, cy), 10, (0, 0, 255), -1)
            cv2.line(cv_image, (image_center_x, 0), (image_center_x, cv_image.shape[0]), (255, 0, 0), 1)

            # Find how low the green shape goes on screen using the image mask rows
            green_pixels_y = np.where(mask > 0)[0]
            lowest_pixel_y = np.max(green_pixels_y) if len(green_pixels_y) > 0 else 0

            # Task 4: Calculate Error
            error_x = image_center_x - cx
            
            # STEP 2: Alignment Check (Focus only on turning if out of bounds)
            if abs(error_x) > self.center_deadband:
                twist.linear.x = 0.0
                twist.angular.z = self.kp * error_x
                self.get_logger().info(
                    f"[ALIGNING] Error: {error_x:4d} px | "
                    f"Cmd Vel -> Linear: {twist.linear.x:.2f} m/s, Angular: {twist.angular.z:.3f} rad/s"
                )
            
            # STEP 3: Centered -> Evaluate Distance dynamically using frame height boundaries
            else:
                if lowest_pixel_y >= (height - 150):
                    # Task 5: Arrived safely with an earlier brake gap
                    twist.linear.x = 0.0
                    twist.angular.z = 0.0
                    self.get_logger().info(
                        f"[ARRIVED]  Error: {error_x:4d} px | Pos: {lowest_pixel_y}/{height}px | "
                        f"Cmd Vel -> Linear: {twist.linear.x:.2f} m/s, Angular: {twist.angular.z:.3f} rad/s"
                    )
                else:
                    # Task 5: Move Forward toward target since there is open space below it
                    twist.linear.x = self.forward_speed
                    twist.angular.z = self.kp * error_x # Minor adjustments while driving
                    self.get_logger().info(
                        f"[APPROACH] Error: {error_x:4d} px | Pos: {lowest_pixel_y}/{height}px | "
                        f"Cmd Vel -> Linear: {twist.linear.x:.2f} m/s, Angular: {twist.angular.z:.3f} rad/s"
                    )
                
        # STEP 4: Safety Stop / Search Loop
        else:
            twist.linear.x = 0.0
            twist.angular.z = 0.15 
            self.get_logger().info(
                f"[SEARCHING] Target Lost | "
                f"Cmd Vel -> Linear: {twist.linear.x:.2f} m/s, Angular: {twist.angular.z:.3f} rad/s"
            )

        # Publish commands to wheels
        self.publisher.publish(twist)

        # Show feeds
        cv2.imshow("Tracking View", cv_image)
        cv2.imshow("Green Isolation Mask", mask)
        cv2.waitKey(1)

def main(args=None):
    rclpy.init(args=args)
    camera_follower = CameraFollower()
    try:
        rclpy.spin(camera_follower)
    except KeyboardInterrupt:
        pass
    camera_follower.destroy_node()
    rclpy.shutdown()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
