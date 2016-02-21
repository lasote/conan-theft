PROJECT(Theft)
cmake_minimum_required(VERSION 3.0)
include(../conanbuildinfo.cmake)
CONAN_BASIC_SETUP()

ADD_LIBRARY(theft theft.c theft_bloom.c theft_hash.c theft_mt.c)
TARGET_LINK_LIBRARIES(theft ${CONAN_LIBS})

set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -std=c99")