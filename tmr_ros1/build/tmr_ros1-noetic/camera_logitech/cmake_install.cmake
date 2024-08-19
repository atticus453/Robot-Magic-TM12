# Install script for directory: /home/jiayulin/robot_magic_tm12/tmr_ros1/src/tmr_ros1-noetic/camera_logitech

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/jiayulin/robot_magic_tm12/tmr_ros1/install")
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
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/jiayulin/robot_magic_tm12/tmr_ros1/build/tmr_ros1-noetic/camera_logitech/catkin_generated/installspace/camera_logitech.pc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/camera_logitech/cmake" TYPE FILE FILES
    "/home/jiayulin/robot_magic_tm12/tmr_ros1/build/tmr_ros1-noetic/camera_logitech/catkin_generated/installspace/camera_logitechConfig.cmake"
    "/home/jiayulin/robot_magic_tm12/tmr_ros1/build/tmr_ros1-noetic/camera_logitech/catkin_generated/installspace/camera_logitechConfig-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/camera_logitech" TYPE FILE FILES "/home/jiayulin/robot_magic_tm12/tmr_ros1/src/tmr_ros1-noetic/camera_logitech/package.xml")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/camera_logitech" TYPE PROGRAM FILES "/home/jiayulin/robot_magic_tm12/tmr_ros1/build/tmr_ros1-noetic/camera_logitech/catkin_generated/installspace/image_publisher.py")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/camera_logitech" TYPE PROGRAM FILES "/home/jiayulin/robot_magic_tm12/tmr_ros1/build/tmr_ros1-noetic/camera_logitech/catkin_generated/installspace/image_publisher_ffmpeg.py")
endif()

