;; Auto-generated. Do not edit!


(when (boundp 'tm_msgs::SetPositions)
  (if (not (find-package "TM_MSGS"))
    (make-package "TM_MSGS"))
  (shadow 'SetPositions (find-package "TM_MSGS")))
(unless (find-package "TM_MSGS::SETPOSITIONS")
  (make-package "TM_MSGS::SETPOSITIONS"))
(unless (find-package "TM_MSGS::SETPOSITIONSREQUEST")
  (make-package "TM_MSGS::SETPOSITIONSREQUEST"))
(unless (find-package "TM_MSGS::SETPOSITIONSRESPONSE")
  (make-package "TM_MSGS::SETPOSITIONSRESPONSE"))

(in-package "ROS")





(intern "*PTP_J*" (find-package "TM_MSGS::SETPOSITIONSREQUEST"))
(shadow '*PTP_J* (find-package "TM_MSGS::SETPOSITIONSREQUEST"))
(defconstant tm_msgs::SetPositionsRequest::*PTP_J* 1)
(intern "*PTP_T*" (find-package "TM_MSGS::SETPOSITIONSREQUEST"))
(shadow '*PTP_T* (find-package "TM_MSGS::SETPOSITIONSREQUEST"))
(defconstant tm_msgs::SetPositionsRequest::*PTP_T* 2)
(intern "*LINE_T*" (find-package "TM_MSGS::SETPOSITIONSREQUEST"))
(shadow '*LINE_T* (find-package "TM_MSGS::SETPOSITIONSREQUEST"))
(defconstant tm_msgs::SetPositionsRequest::*LINE_T* 4)

(defun tm_msgs::SetPositionsRequest-to-symbol (const)
  (cond
        ((= const 1) 'tm_msgs::SetPositionsRequest::*PTP_J*)
        ((= const 2) 'tm_msgs::SetPositionsRequest::*PTP_T*)
        ((= const 4) 'tm_msgs::SetPositionsRequest::*LINE_T*)
        (t nil)))

(defclass tm_msgs::SetPositionsRequest
  :super ros::object
  :slots (_motion_type _positions _velocity _acc_time _blend_percentage _fine_goal ))

(defmethod tm_msgs::SetPositionsRequest
  (:init
   (&key
    ((:motion_type __motion_type) 0)
    ((:positions __positions) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:velocity __velocity) 0.0)
    ((:acc_time __acc_time) 0.0)
    ((:blend_percentage __blend_percentage) 0)
    ((:fine_goal __fine_goal) nil)
    )
   (send-super :init)
   (setq _motion_type (round __motion_type))
   (setq _positions __positions)
   (setq _velocity (float __velocity))
   (setq _acc_time (float __acc_time))
   (setq _blend_percentage (round __blend_percentage))
   (setq _fine_goal __fine_goal)
   self)
  (:motion_type
   (&optional __motion_type)
   (if __motion_type (setq _motion_type __motion_type)) _motion_type)
  (:positions
   (&optional __positions)
   (if __positions (setq _positions __positions)) _positions)
  (:velocity
   (&optional __velocity)
   (if __velocity (setq _velocity __velocity)) _velocity)
  (:acc_time
   (&optional __acc_time)
   (if __acc_time (setq _acc_time __acc_time)) _acc_time)
  (:blend_percentage
   (&optional __blend_percentage)
   (if __blend_percentage (setq _blend_percentage __blend_percentage)) _blend_percentage)
  (:fine_goal
   (&optional (__fine_goal :null))
   (if (not (eq __fine_goal :null)) (setq _fine_goal __fine_goal)) _fine_goal)
  (:serialization-length
   ()
   (+
    ;; int8 _motion_type
    1
    ;; float64[] _positions
    (* 8    (length _positions)) 4
    ;; float64 _velocity
    8
    ;; float64 _acc_time
    8
    ;; int32 _blend_percentage
    4
    ;; bool _fine_goal
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int8 _motion_type
       (write-byte _motion_type s)
     ;; float64[] _positions
     (write-long (length _positions) s)
     (dotimes (i (length _positions))
       (sys::poke (elt _positions i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
       )
     ;; float64 _velocity
       (sys::poke _velocity (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _acc_time
       (sys::poke _acc_time (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; int32 _blend_percentage
       (write-long _blend_percentage s)
     ;; bool _fine_goal
       (if _fine_goal (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int8 _motion_type
     (setq _motion_type (sys::peek buf ptr- :char)) (incf ptr- 1)
     (if (> _motion_type 127) (setq _motion_type (- _motion_type 256)))
   ;; float64[] _positions
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _positions (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _positions i) (sys::peek buf ptr- :double)) (incf ptr- 8)
     ))
   ;; float64 _velocity
     (setq _velocity (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _acc_time
     (setq _acc_time (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; int32 _blend_percentage
     (setq _blend_percentage (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; bool _fine_goal
     (setq _fine_goal (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(defclass tm_msgs::SetPositionsResponse
  :super ros::object
  :slots (_ok ))

(defmethod tm_msgs::SetPositionsResponse
  (:init
   (&key
    ((:ok __ok) nil)
    )
   (send-super :init)
   (setq _ok __ok)
   self)
  (:ok
   (&optional (__ok :null))
   (if (not (eq __ok :null)) (setq _ok __ok)) _ok)
  (:serialization-length
   ()
   (+
    ;; bool _ok
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _ok
       (if _ok (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _ok
     (setq _ok (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(defclass tm_msgs::SetPositions
  :super ros::object
  :slots ())

(setf (get tm_msgs::SetPositions :md5sum-) "b40b99326e48ac323581c59a790d263f")
(setf (get tm_msgs::SetPositions :datatype-) "tm_msgs/SetPositions")
(setf (get tm_msgs::SetPositions :request) tm_msgs::SetPositionsRequest)
(setf (get tm_msgs::SetPositions :response) tm_msgs::SetPositionsResponse)

(defmethod tm_msgs::SetPositionsRequest
  (:response () (instance tm_msgs::SetPositionsResponse :init)))

(setf (get tm_msgs::SetPositionsRequest :md5sum-) "b40b99326e48ac323581c59a790d263f")
(setf (get tm_msgs::SetPositionsRequest :datatype-) "tm_msgs/SetPositionsRequest")
(setf (get tm_msgs::SetPositionsRequest :definition-)
      "#motion_type :  PTP_J , PTP_T , LINE_T ,
#               LINE_J , CIRC_J ,CIRC_T , PLINE_J ,PLINE_T 
# More details please refer to the TM Expression Editor Manual(2.12 rev1.00) Chapter 12.6-12.9
int8 PTP_J = 1
int8 PTP_T = 2
#int8 LINE_J = 3
int8 LINE_T = 4
#int8 CIRC_J = 5
#int8 CIRC_T = 6
#int8 PLINE_J = 7
#int8 PLINE_T = 8

int8 motion_type
float64[] positions
float64 velocity       # motion velocity: if expressed in Cartesian coordinate (unit: m/s) , if expressed in joint velocity (unit: rad/s, and the maximum value is limited to pi )
float64 acc_time       # time to reach maximum speed (unit: ms)
int32 blend_percentage # blending value: expressed as a percentage (unit: %, and the minimum value of 0 means no blending)
bool fine_goal         # precise position mode : If activated, the amount of error in the final position will converge more.
---
# ok :  set motion status 
bool ok

")

(setf (get tm_msgs::SetPositionsResponse :md5sum-) "b40b99326e48ac323581c59a790d263f")
(setf (get tm_msgs::SetPositionsResponse :datatype-) "tm_msgs/SetPositionsResponse")
(setf (get tm_msgs::SetPositionsResponse :definition-)
      "#motion_type :  PTP_J , PTP_T , LINE_T ,
#               LINE_J , CIRC_J ,CIRC_T , PLINE_J ,PLINE_T 
# More details please refer to the TM Expression Editor Manual(2.12 rev1.00) Chapter 12.6-12.9
int8 PTP_J = 1
int8 PTP_T = 2
#int8 LINE_J = 3
int8 LINE_T = 4
#int8 CIRC_J = 5
#int8 CIRC_T = 6
#int8 PLINE_J = 7
#int8 PLINE_T = 8

int8 motion_type
float64[] positions
float64 velocity       # motion velocity: if expressed in Cartesian coordinate (unit: m/s) , if expressed in joint velocity (unit: rad/s, and the maximum value is limited to pi )
float64 acc_time       # time to reach maximum speed (unit: ms)
int32 blend_percentage # blending value: expressed as a percentage (unit: %, and the minimum value of 0 means no blending)
bool fine_goal         # precise position mode : If activated, the amount of error in the final position will converge more.
---
# ok :  set motion status 
bool ok

")



(provide :tm_msgs/SetPositions "b40b99326e48ac323581c59a790d263f")


