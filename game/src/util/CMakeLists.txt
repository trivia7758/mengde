project(util)

file(GLOB_RECURSE SOURCES *.cc)
file(GLOB_RECURSE HEADERS *.h)

if(WIN32)
    set(MENGDE_LIB_TYPE STATIC)
else()
    set(MENGDE_LIB_TYPE SHARED)
endif()

add_library(util ${MENGDE_LIB_TYPE} ${SOURCES} ${HEADERS})

target_include_directories(util PUBLIC ${SDL2_INCLUDE_DIR})
target_link_libraries(util ${SDL2_LIBRARY})
target_link_libraries(util Boost::filesystem Boost::system)

install(TARGETS util DESTINATION install)
