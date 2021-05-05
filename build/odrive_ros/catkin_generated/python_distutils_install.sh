#!/bin/sh

if [ -n "$DESTDIR" ] ; then
    case $DESTDIR in
        /*) # ok
            ;;
        *)
            /bin/echo "DESTDIR argument must be absolute... "
            /bin/echo "otherwise python's distutils will bork things."
            exit 1
    esac
fi

echo_and_run() { echo "+ $@" ; "$@" ; }

echo_and_run cd "/home/ikiwi/ikiwi_abila_new/src/odrive_ros"

# ensure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/home/ikiwi/ikiwi_abila_new/install/lib/python2.7/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/home/ikiwi/ikiwi_abila_new/install/lib/python2.7/dist-packages:/home/ikiwi/ikiwi_abila_new/build/lib/python2.7/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/ikiwi/ikiwi_abila_new/build" \
    "/usr/bin/python2" \
    "/home/ikiwi/ikiwi_abila_new/src/odrive_ros/setup.py" \
     \
    build --build-base "/home/ikiwi/ikiwi_abila_new/build/odrive_ros" \
    install \
    --root="${DESTDIR-/}" \
    --install-layout=deb --prefix="/home/ikiwi/ikiwi_abila_new/install" --install-scripts="/home/ikiwi/ikiwi_abila_new/install/bin"
