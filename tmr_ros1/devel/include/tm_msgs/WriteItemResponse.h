// Generated by gencpp from file tm_msgs/WriteItemResponse.msg
// DO NOT EDIT!


#ifndef TM_MSGS_MESSAGE_WRITEITEMRESPONSE_H
#define TM_MSGS_MESSAGE_WRITEITEMRESPONSE_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace tm_msgs
{
template <class ContainerAllocator>
struct WriteItemResponse_
{
  typedef WriteItemResponse_<ContainerAllocator> Type;

  WriteItemResponse_()
    : ok(false)  {
    }
  WriteItemResponse_(const ContainerAllocator& _alloc)
    : ok(false)  {
  (void)_alloc;
    }



   typedef uint8_t _ok_type;
  _ok_type ok;





  typedef boost::shared_ptr< ::tm_msgs::WriteItemResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::tm_msgs::WriteItemResponse_<ContainerAllocator> const> ConstPtr;

}; // struct WriteItemResponse_

typedef ::tm_msgs::WriteItemResponse_<std::allocator<void> > WriteItemResponse;

typedef boost::shared_ptr< ::tm_msgs::WriteItemResponse > WriteItemResponsePtr;
typedef boost::shared_ptr< ::tm_msgs::WriteItemResponse const> WriteItemResponseConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::tm_msgs::WriteItemResponse_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::tm_msgs::WriteItemResponse_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::tm_msgs::WriteItemResponse_<ContainerAllocator1> & lhs, const ::tm_msgs::WriteItemResponse_<ContainerAllocator2> & rhs)
{
  return lhs.ok == rhs.ok;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::tm_msgs::WriteItemResponse_<ContainerAllocator1> & lhs, const ::tm_msgs::WriteItemResponse_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace tm_msgs

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::tm_msgs::WriteItemResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::tm_msgs::WriteItemResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::tm_msgs::WriteItemResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::tm_msgs::WriteItemResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::tm_msgs::WriteItemResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::tm_msgs::WriteItemResponse_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::tm_msgs::WriteItemResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "6f6da3883749771fac40d6deb24a8c02";
  }

  static const char* value(const ::tm_msgs::WriteItemResponse_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x6f6da3883749771fULL;
  static const uint64_t static_value2 = 0xac40d6deb24a8c02ULL;
};

template<class ContainerAllocator>
struct DataType< ::tm_msgs::WriteItemResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "tm_msgs/WriteItemResponse";
  }

  static const char* value(const ::tm_msgs::WriteItemResponse_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::tm_msgs::WriteItemResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "#ok =   write status\n"
"bool ok\n"
;
  }

  static const char* value(const ::tm_msgs::WriteItemResponse_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::tm_msgs::WriteItemResponse_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.ok);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct WriteItemResponse_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::tm_msgs::WriteItemResponse_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::tm_msgs::WriteItemResponse_<ContainerAllocator>& v)
  {
    s << indent << "ok: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.ok);
  }
};

} // namespace message_operations
} // namespace ros

#endif // TM_MSGS_MESSAGE_WRITEITEMRESPONSE_H
