---
sidebar_position: 3
title: ROS 2 Fundamentals
---

# ROS 2 Fundamentals

## Introduction to ROS 2

The Robot Operating System 2 (ROS 2) is not an operating system but rather a flexible framework for writing robot software. It is a collection of tools, libraries, and conventions that aim to simplify the task of creating complex and robust robot behavior across a wide variety of robot platforms.

ROS 2 is the next generation of the Robot Operating System, addressing many limitations of the original ROS including:

- Better support for real-time systems
- Improved security features
- Enhanced multi-robot systems support
- Deterministic Quality of Service (QoS) policies
- Better cross-platform support (Windows, macOS, Linux)

## Architecture Overview

### Nodes
In ROS 2, processes are called nodes. A node is an executable that uses ROS 2 client libraries to communicate with other nodes. Nodes are designed to be simple and modular, with each node performing a single function.

### Topics and Messages
ROS 2 uses a publish-subscribe communication pattern where nodes communicate by passing messages over topics:

- **Messages**: Data structures that contain information sent between nodes
- **Topics**: Named buses over which messages are sent
- **Publishers**: Nodes that send messages to a topic
- **Subscribers**: Nodes that receive messages from a topic

### Services
For request-response communication, ROS 2 provides services:

- **Services**: Allow nodes to send a request and receive a response
- **Service Servers**: Nodes that provide a service
- **Service Clients**: Nodes that use a service

### Actions
For longer running tasks with feedback, ROS 2 provides actions:

- **Actions**: Similar to services but allow feedback during execution
- **Action Servers**: Process action requests and send feedback
- **Action Clients**: Send action requests and receive feedback

## Key Concepts and Features

### DDS (Data Distribution Service)
ROS 2 uses DDS as its underlying middleware for communication:

- Provides discovery mechanisms
- Handles Quality of Service (QoS) policies
- Enables real-time performance
- Supports reliable and best-effort communication

### Quality of Service (QoS)
QoS policies allow fine-tuning of communication behavior:

- **Reliability**: Reliable vs. best-effort delivery
- **Durability**: Volatile vs. persistent data
- **History**: Keep-all vs. keep-last data
- **Deadline**: Time constraints for data delivery
- **Liveliness**: Monitoring participant availability

### Composition
ROS 2 supports composition of nodes to optimize performance:

- Components: Libraries that can be combined into a single process
- Composition: Combining multiple components into a single executable
- Benefits: Reduced communication overhead and improved performance

### Lifecycle Nodes
For managing complex system states:

- Lifecycle nodes have explicit state transitions
- Enable better resource management
- Support for initialization and shutdown procedures

## Setting Up ROS 2

### Installation
ROS 2 can be installed on multiple platforms:

1. **Ubuntu (recommended for development)**
2. **Windows** (through binaries or WSL2)
3. **macOS** (through binaries or Docker)
4. **Raspberry Pi OS** (for embedded systems)

### Environment Setup
After installation, you need to source the ROS 2 environment:

```bash
source /opt/ros/<distro>/setup.bash
```

## Practical Examples

### Creating a Node

Basic ROS 2 node in Python:

```python
import rclpy
from rclpy.node import Node

class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher_ = self.create_publisher(String, 'topic', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = String()
        msg.data = 'Hello World: %d' % self.i
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)
        self.i += 1
```

### Working with Parameters
ROS 2 includes a built-in parameter system:

```python
self.declare_parameter('param_name', 'default_value')
param_value = self.get_parameter('param_name').value
```

## ROS 2 Ecosystem

### Available Distributions
ROS 2 has different distributions released approximately every year:

- **Foxy Fitzroy** (June 2020) - LTS, supported until May 2025
- **Galactic Geochelone** (May 2021) - EOL May 2022
- **Humble Hawksbill** (May 2022) - LTS, supported until May 2027
- **Iron Irwini** (May 2023) - EOL November 2024
- **Jazzy Jalisco** (May 2024) - LTS, supported until May 2029

### Popular Packages
The ROS 2 ecosystem includes thousands of packages:

- **Navigation2**: Path planning and navigation stack
- **MoveIt2**: Motion planning for robotic arms
- **Robot State Publisher**: Publishes transforms for robot kinematics
- **TF2**: Transform library for coordinate systems
- **Gazebo**: 3D simulation environment
- **OpenCV**: Computer vision library integration

## ROS 2 vs. ROS 1

| Feature | ROS 1 | ROS 2 |
|---------|-------|-------|
| Communication | Custom | DDS-based |
| Middleware | Master-based | DDS-based |
| Platforms | Linux | Multi-platform |
| Real-time | Limited | Better support |
| Security | None | Built-in support |
| Multi-robot | Complex | Better support |

## Best Practices

### Node Design
- Keep nodes focused on a single purpose
- Use composition for performance-critical applications
- Implement proper error handling
- Log appropriately

### Messaging
- Design messages for efficiency
- Use appropriate QoS settings
- Consider message size and frequency
- Plan for backward compatibility

### Testing
- Use launch files for easy testing
- Implement unit tests for components
- Use system tests for integration
- Consider using ros_testing tools

## Conclusion

ROS 2 provides a powerful and flexible framework for developing complex robotic systems. Its modern architecture addresses many of the limitations of ROS 1 while maintaining the core philosophy of modular, distributed systems.

The next chapter will explore Digital Twin Simulation using Gazebo and Isaac, which are essential tools for testing and developing robotics applications before deploying them on real hardware.