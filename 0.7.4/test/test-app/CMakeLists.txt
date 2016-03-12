project(HTTPTimeServer)
cmake_minimum_required(VERSION 2.8.11)

include(conanbuildinfo.cmake)
conan_basic_setup()

add_executable(server src/HTTPTimeServer.cpp)
target_link_libraries(server ${CONAN_LIBS})
