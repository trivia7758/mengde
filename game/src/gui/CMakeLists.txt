project(gui)

file(GLOB SOURCES app/*.cc
                  foundation/*.cc
                  uifw/*.cc)
file(GLOB HEADERS app/*.h
                  foundation/*.h
                  uifw/*.h)

if(WIN32)
    set(MENGDE_LIB_TYPE STATIC)
else()
    set(MENGDE_LIB_TYPE SHARED)
endif()

add_library(gui ${MENGDE_LIB_TYPE} ${SOURCES} ${HEADERS})

target_include_directories(gui PUBLIC ${SDL2_INCLUDE_DIR})
target_include_directories(gui PUBLIC ${SDL2_TTF_INCLUDE_DIR})
target_link_libraries(gui core util)
target_link_libraries(gui ${SDL2_LIBRARY})
target_link_libraries(gui ${SDL2_TTF_LIBRARIES})
target_link_libraries(gui Boost::filesystem Boost::system)
if(TARGET Boost::format)
    target_link_libraries(gui Boost::format)
endif()

install(TARGETS gui DESTINATION install)
