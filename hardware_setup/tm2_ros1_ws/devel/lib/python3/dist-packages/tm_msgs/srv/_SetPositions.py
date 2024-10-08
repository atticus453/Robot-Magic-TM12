# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from tm_msgs/SetPositionsRequest.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class SetPositionsRequest(genpy.Message):
  _md5sum = "1ee7b78a3830b551c6ac669ff4972d51"
  _type = "tm_msgs/SetPositionsRequest"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """#motion_type :  PTP_J , PTP_T , LINE_T ,
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
"""
  # Pseudo-constants
  PTP_J = 1
  PTP_T = 2
  LINE_T = 4

  __slots__ = ['motion_type','positions','velocity','acc_time','blend_percentage','fine_goal']
  _slot_types = ['int8','float64[]','float64','float64','int32','bool']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       motion_type,positions,velocity,acc_time,blend_percentage,fine_goal

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(SetPositionsRequest, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.motion_type is None:
        self.motion_type = 0
      if self.positions is None:
        self.positions = []
      if self.velocity is None:
        self.velocity = 0.
      if self.acc_time is None:
        self.acc_time = 0.
      if self.blend_percentage is None:
        self.blend_percentage = 0
      if self.fine_goal is None:
        self.fine_goal = False
    else:
      self.motion_type = 0
      self.positions = []
      self.velocity = 0.
      self.acc_time = 0.
      self.blend_percentage = 0
      self.fine_goal = False

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self.motion_type
      buff.write(_get_struct_b().pack(_x))
      length = len(self.positions)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(struct.Struct(pattern).pack(*self.positions))
      _x = self
      buff.write(_get_struct_2diB().pack(_x.velocity, _x.acc_time, _x.blend_percentage, _x.fine_goal))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      start = end
      end += 1
      (self.motion_type,) = _get_struct_b().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.positions = s.unpack(str[start:end])
      _x = self
      start = end
      end += 21
      (_x.velocity, _x.acc_time, _x.blend_percentage, _x.fine_goal,) = _get_struct_2diB().unpack(str[start:end])
      self.fine_goal = bool(self.fine_goal)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self.motion_type
      buff.write(_get_struct_b().pack(_x))
      length = len(self.positions)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(self.positions.tostring())
      _x = self
      buff.write(_get_struct_2diB().pack(_x.velocity, _x.acc_time, _x.blend_percentage, _x.fine_goal))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      start = end
      end += 1
      (self.motion_type,) = _get_struct_b().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.positions = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
      _x = self
      start = end
      end += 21
      (_x.velocity, _x.acc_time, _x.blend_percentage, _x.fine_goal,) = _get_struct_2diB().unpack(str[start:end])
      self.fine_goal = bool(self.fine_goal)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_2diB = None
def _get_struct_2diB():
    global _struct_2diB
    if _struct_2diB is None:
        _struct_2diB = struct.Struct("<2diB")
    return _struct_2diB
_struct_b = None
def _get_struct_b():
    global _struct_b
    if _struct_b is None:
        _struct_b = struct.Struct("<b")
    return _struct_b
# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from tm_msgs/SetPositionsResponse.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class SetPositionsResponse(genpy.Message):
  _md5sum = "6f6da3883749771fac40d6deb24a8c02"
  _type = "tm_msgs/SetPositionsResponse"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """# ok :  set motion status 
bool ok

"""
  __slots__ = ['ok']
  _slot_types = ['bool']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       ok

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(SetPositionsResponse, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.ok is None:
        self.ok = False
    else:
      self.ok = False

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self.ok
      buff.write(_get_struct_B().pack(_x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      start = end
      end += 1
      (self.ok,) = _get_struct_B().unpack(str[start:end])
      self.ok = bool(self.ok)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self.ok
      buff.write(_get_struct_B().pack(_x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      start = end
      end += 1
      (self.ok,) = _get_struct_B().unpack(str[start:end])
      self.ok = bool(self.ok)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_B = None
def _get_struct_B():
    global _struct_B
    if _struct_B is None:
        _struct_B = struct.Struct("<B")
    return _struct_B
class SetPositions(object):
  _type          = 'tm_msgs/SetPositions'
  _md5sum = 'b40b99326e48ac323581c59a790d263f'
  _request_class  = SetPositionsRequest
  _response_class = SetPositionsResponse
