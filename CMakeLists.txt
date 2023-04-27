project(CHEESE_ENGINE)
cmake_minimum_required(VERSION 3.5.1)


file(GLOB_RECURSE SRCs src/*.cpp)
add_executable(${PROJECT_NAME} ${SRCs})
target_include_directories(${PROJECT_NAME} PUBLIC include)

