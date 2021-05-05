# Install script for directory: /home/ikiwi/ikiwi_abila_new/src/cartographer_ros/cartographer_ros_msgs

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/ikiwi/ikiwi_abila_new/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/cartographer_ros_msgs/msg" TYPE FILE FILES
    "/home/ikiwi/ikiwi_abila_new/src/cartographer_ros/cartographer_ros_msgs/msg/BagfileProgress.msg"
    "/home/ikiwi/ikiwi_abila_new/src/cartographer_ros/cartographer_ros_msgs/msg/HistogramBucket.msg"
    "/home/ikiwi/ikiwi_abila_new/src/cartographer_ros/cartographer_ros_msgs/msg/LandmarkEntry.msg"
    "/home/ikiwi/ikiwi_abila_new/src/cartographer_ros/cartographer_ros_msgs/msg/LandmarkList.msg"
    "/home/ikiwi/ikiwi_abila_new/src/cartographer_ros/cartographer_ros_msgs/msg/MetricFamily.msg"
    "/home/ikiwi/ikiwi_abila_new/src/cartographer_ros/cartographer_ros_msgs/msg/MetricLabel.msg"
    "/home/ikiwi/ikiwi_abila_new/src/cartographer_ros/cartographer_ros_msgs/msg/Metric.msg"
    "/home/ikiwi/ikiwi_abila_new/src/cartographer_ros/cartographer_ros_msgs/msg/StatusCode.msg"
    "/home/ikiwi/ikiwi_abila_new/src/cartographer_ros/cartographer_ros_msgs/msg/StatusResponse.msg"
    "/home/ikiwi/ikiwi_abila_new/src/cartographer_ros/cartographer_ros_msgs/msg/SubmapEntry.msg"
    "/home/ikiwi/ikiwi_abila_new/src/cartographer_ros/cartographer_ros_msgs/msg/SubmapList.msg"
    "/home/ikiwi/ikiwi_abila_new/src/cartographer_ros/cartographer_ros_msgs/msg/SubmapTexture.msg"
    "/home/ikiwi/ikiwi_abila_new/src/cartographer_ros/cartographer_ros_msgs/msg/TrajectoryStates.msg"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/cartographer_ros_msgs/srv" TYPE FILE FILES
    "/home/ikiwi/ikiwi_abila_new/src/cartographer_ros/cartographer_ros_msgs/srv/FinishTrajectory.srv"
    "/home/ikiwi/ikiwi_abila_new/src/cartographer_ros/cartographer_ros_msgs/srv/GetTrajectoryStates.srv"
    "/home/ikiwi/ikiwi_abila_new/src/cartographer_ros/cartographer_ros_msgs/srv/ReadMetrics.srv"
    "/home/ikiwi/ikiwi_abila_new/src/cartographer_ros/cartographer_ros_msgs/srv/StartTrajectory.srv"
    "/home/ikiwi/ikiwi_abila_new/src/cartographer_ros/cartographer_ros_msgs/srv/SubmapQuery.srv"
    "/home/ikiwi/ikiwi_abila_new/src/cartographer_ros/cartographer_ros_msgs/srv/TrajectoryQuery.srv"
    "/home/ikiwi/ikiwi_abila_new/src/cartographer_ros/cartographer_ros_msgs/srv/WriteState.srv"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/cartographer_ros_msgs/cmake" TYPE FILE FILES "/home/ikiwi/ikiwi_abila_new/build/cartographer_ros/cartographer_ros_msgs/catkin_generated/installspace/cartographer_ros_msgs-msg-paths.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include" TYPE DIRECTORY FILES "/home/ikiwi/ikiwi_abila_new/devel/include/cartographer_ros_msgs")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/roseus/ros" TYPE DIRECTORY FILES "/home/ikiwi/ikiwi_abila_new/devel/share/roseus/ros/cartographer_ros_msgs")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/common-lisp/ros" TYPE DIRECTORY FILES "/home/ikiwi/ikiwi_abila_new/devel/share/common-lisp/ros/cartographer_ros_msgs")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gennodejs/ros" TYPE DIRECTORY FILES "/home/ikiwi/ikiwi_abila_new/devel/share/gennodejs/ros/cartographer_ros_msgs")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  execute_process(COMMAND "/usr/bin/python2" -m compileall "/home/ikiwi/ikiwi_abila_new/devel/lib/python2.7/dist-packages/cartographer_ros_msgs")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages" TYPE DIRECTORY FILES "/home/ikiwi/ikiwi_abila_new/devel/lib/python2.7/dist-packages/cartographer_ros_msgs")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/ikiwi/ikiwi_abila_new/build/cartographer_ros/cartographer_ros_msgs/catkin_generated/installspace/cartographer_ros_msgs.pc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/cartographer_ros_msgs/cmake" TYPE FILE FILES "/home/ikiwi/ikiwi_abila_new/build/cartographer_ros/cartographer_ros_msgs/catkin_generated/installspace/cartographer_ros_msgs-msg-extras.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/cartographer_ros_msgs/cmake" TYPE FILE FILES
    "/home/ikiwi/ikiwi_abila_new/build/cartographer_ros/cartographer_ros_msgs/catkin_generated/installspace/cartographer_ros_msgsConfig.cmake"
    "/home/ikiwi/ikiwi_abila_new/build/cartographer_ros/cartographer_ros_msgs/catkin_generated/installspace/cartographer_ros_msgsConfig-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/cartographer_ros_msgs" TYPE FILE FILES "/home/ikiwi/ikiwi_abila_new/src/cartographer_ros/cartographer_ros_msgs/package.xml")
endif()

