# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from cartographer_ros_msgs/StartTrajectoryRequest.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import geometry_msgs.msg

class StartTrajectoryRequest(genpy.Message):
  _md5sum = "555a1aa894dfd093eaa13b245b423df8"
  _type = "cartographer_ros_msgs/StartTrajectoryRequest"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """# Copyright 2016 The Cartographer Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

string configuration_directory
string configuration_basename
bool use_initial_pose
geometry_msgs/Pose initial_pose
int32 relative_to_trajectory_id

================================================================================
MSG: geometry_msgs/Pose
# A representation of pose in free space, composed of position and orientation. 
Point position
Quaternion orientation

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

================================================================================
MSG: geometry_msgs/Quaternion
# This represents an orientation in free space in quaternion form.

float64 x
float64 y
float64 z
float64 w
"""
  __slots__ = ['configuration_directory','configuration_basename','use_initial_pose','initial_pose','relative_to_trajectory_id']
  _slot_types = ['string','string','bool','geometry_msgs/Pose','int32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       configuration_directory,configuration_basename,use_initial_pose,initial_pose,relative_to_trajectory_id

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(StartTrajectoryRequest, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.configuration_directory is None:
        self.configuration_directory = ''
      if self.configuration_basename is None:
        self.configuration_basename = ''
      if self.use_initial_pose is None:
        self.use_initial_pose = False
      if self.initial_pose is None:
        self.initial_pose = geometry_msgs.msg.Pose()
      if self.relative_to_trajectory_id is None:
        self.relative_to_trajectory_id = 0
    else:
      self.configuration_directory = ''
      self.configuration_basename = ''
      self.use_initial_pose = False
      self.initial_pose = geometry_msgs.msg.Pose()
      self.relative_to_trajectory_id = 0

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
      _x = self.configuration_directory
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.configuration_basename
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_B7di().pack(_x.use_initial_pose, _x.initial_pose.position.x, _x.initial_pose.position.y, _x.initial_pose.position.z, _x.initial_pose.orientation.x, _x.initial_pose.orientation.y, _x.initial_pose.orientation.z, _x.initial_pose.orientation.w, _x.relative_to_trajectory_id))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.initial_pose is None:
        self.initial_pose = geometry_msgs.msg.Pose()
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.configuration_directory = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.configuration_directory = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.configuration_basename = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.configuration_basename = str[start:end]
      _x = self
      start = end
      end += 61
      (_x.use_initial_pose, _x.initial_pose.position.x, _x.initial_pose.position.y, _x.initial_pose.position.z, _x.initial_pose.orientation.x, _x.initial_pose.orientation.y, _x.initial_pose.orientation.z, _x.initial_pose.orientation.w, _x.relative_to_trajectory_id,) = _get_struct_B7di().unpack(str[start:end])
      self.use_initial_pose = bool(self.use_initial_pose)
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
      _x = self.configuration_directory
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.configuration_basename
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_B7di().pack(_x.use_initial_pose, _x.initial_pose.position.x, _x.initial_pose.position.y, _x.initial_pose.position.z, _x.initial_pose.orientation.x, _x.initial_pose.orientation.y, _x.initial_pose.orientation.z, _x.initial_pose.orientation.w, _x.relative_to_trajectory_id))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.initial_pose is None:
        self.initial_pose = geometry_msgs.msg.Pose()
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.configuration_directory = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.configuration_directory = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.configuration_basename = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.configuration_basename = str[start:end]
      _x = self
      start = end
      end += 61
      (_x.use_initial_pose, _x.initial_pose.position.x, _x.initial_pose.position.y, _x.initial_pose.position.z, _x.initial_pose.orientation.x, _x.initial_pose.orientation.y, _x.initial_pose.orientation.z, _x.initial_pose.orientation.w, _x.relative_to_trajectory_id,) = _get_struct_B7di().unpack(str[start:end])
      self.use_initial_pose = bool(self.use_initial_pose)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_B7di = None
def _get_struct_B7di():
    global _struct_B7di
    if _struct_B7di is None:
        _struct_B7di = struct.Struct("<B7di")
    return _struct_B7di
# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from cartographer_ros_msgs/StartTrajectoryResponse.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import cartographer_ros_msgs.msg

class StartTrajectoryResponse(genpy.Message):
  _md5sum = "a14602d76d9b734b374a25be319cdbe9"
  _type = "cartographer_ros_msgs/StartTrajectoryResponse"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """cartographer_ros_msgs/StatusResponse status
int32 trajectory_id


================================================================================
MSG: cartographer_ros_msgs/StatusResponse
# Copyright 2018 The Cartographer Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# A common message type to indicate the outcome of a service call.
uint8 code
string message
"""
  __slots__ = ['status','trajectory_id']
  _slot_types = ['cartographer_ros_msgs/StatusResponse','int32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       status,trajectory_id

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(StartTrajectoryResponse, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.status is None:
        self.status = cartographer_ros_msgs.msg.StatusResponse()
      if self.trajectory_id is None:
        self.trajectory_id = 0
    else:
      self.status = cartographer_ros_msgs.msg.StatusResponse()
      self.trajectory_id = 0

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
      _x = self.status.code
      buff.write(_get_struct_B().pack(_x))
      _x = self.status.message
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.trajectory_id
      buff.write(_get_struct_i().pack(_x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.status is None:
        self.status = cartographer_ros_msgs.msg.StatusResponse()
      end = 0
      start = end
      end += 1
      (self.status.code,) = _get_struct_B().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.status.message = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.status.message = str[start:end]
      start = end
      end += 4
      (self.trajectory_id,) = _get_struct_i().unpack(str[start:end])
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
      _x = self.status.code
      buff.write(_get_struct_B().pack(_x))
      _x = self.status.message
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.trajectory_id
      buff.write(_get_struct_i().pack(_x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.status is None:
        self.status = cartographer_ros_msgs.msg.StatusResponse()
      end = 0
      start = end
      end += 1
      (self.status.code,) = _get_struct_B().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.status.message = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.status.message = str[start:end]
      start = end
      end += 4
      (self.trajectory_id,) = _get_struct_i().unpack(str[start:end])
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
_struct_i = None
def _get_struct_i():
    global _struct_i
    if _struct_i is None:
        _struct_i = struct.Struct("<i")
    return _struct_i
class StartTrajectory(object):
  _type          = 'cartographer_ros_msgs/StartTrajectory'
  _md5sum = 'dcc000df748d283ba7bf678a47ffa491'
  _request_class  = StartTrajectoryRequest
  _response_class = StartTrajectoryResponse
