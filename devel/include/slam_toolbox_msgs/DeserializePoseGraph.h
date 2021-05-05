// Generated by gencpp from file slam_toolbox_msgs/DeserializePoseGraph.msg
// DO NOT EDIT!


#ifndef SLAM_TOOLBOX_MSGS_MESSAGE_DESERIALIZEPOSEGRAPH_H
#define SLAM_TOOLBOX_MSGS_MESSAGE_DESERIALIZEPOSEGRAPH_H

#include <ros/service_traits.h>


#include <slam_toolbox_msgs/DeserializePoseGraphRequest.h>
#include <slam_toolbox_msgs/DeserializePoseGraphResponse.h>


namespace slam_toolbox_msgs
{

struct DeserializePoseGraph
{

typedef DeserializePoseGraphRequest Request;
typedef DeserializePoseGraphResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct DeserializePoseGraph
} // namespace slam_toolbox_msgs


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::slam_toolbox_msgs::DeserializePoseGraph > {
  static const char* value()
  {
    return "29a9bb432c3daccc49d63131eece4576";
  }

  static const char* value(const ::slam_toolbox_msgs::DeserializePoseGraph&) { return value(); }
};

template<>
struct DataType< ::slam_toolbox_msgs::DeserializePoseGraph > {
  static const char* value()
  {
    return "slam_toolbox_msgs/DeserializePoseGraph";
  }

  static const char* value(const ::slam_toolbox_msgs::DeserializePoseGraph&) { return value(); }
};


// service_traits::MD5Sum< ::slam_toolbox_msgs::DeserializePoseGraphRequest> should match
// service_traits::MD5Sum< ::slam_toolbox_msgs::DeserializePoseGraph >
template<>
struct MD5Sum< ::slam_toolbox_msgs::DeserializePoseGraphRequest>
{
  static const char* value()
  {
    return MD5Sum< ::slam_toolbox_msgs::DeserializePoseGraph >::value();
  }
  static const char* value(const ::slam_toolbox_msgs::DeserializePoseGraphRequest&)
  {
    return value();
  }
};

// service_traits::DataType< ::slam_toolbox_msgs::DeserializePoseGraphRequest> should match
// service_traits::DataType< ::slam_toolbox_msgs::DeserializePoseGraph >
template<>
struct DataType< ::slam_toolbox_msgs::DeserializePoseGraphRequest>
{
  static const char* value()
  {
    return DataType< ::slam_toolbox_msgs::DeserializePoseGraph >::value();
  }
  static const char* value(const ::slam_toolbox_msgs::DeserializePoseGraphRequest&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::slam_toolbox_msgs::DeserializePoseGraphResponse> should match
// service_traits::MD5Sum< ::slam_toolbox_msgs::DeserializePoseGraph >
template<>
struct MD5Sum< ::slam_toolbox_msgs::DeserializePoseGraphResponse>
{
  static const char* value()
  {
    return MD5Sum< ::slam_toolbox_msgs::DeserializePoseGraph >::value();
  }
  static const char* value(const ::slam_toolbox_msgs::DeserializePoseGraphResponse&)
  {
    return value();
  }
};

// service_traits::DataType< ::slam_toolbox_msgs::DeserializePoseGraphResponse> should match
// service_traits::DataType< ::slam_toolbox_msgs::DeserializePoseGraph >
template<>
struct DataType< ::slam_toolbox_msgs::DeserializePoseGraphResponse>
{
  static const char* value()
  {
    return DataType< ::slam_toolbox_msgs::DeserializePoseGraph >::value();
  }
  static const char* value(const ::slam_toolbox_msgs::DeserializePoseGraphResponse&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // SLAM_TOOLBOX_MSGS_MESSAGE_DESERIALIZEPOSEGRAPH_H
