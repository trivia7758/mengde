project(core)

file(GLOB SOURCES *.cc)
file(GLOB HEADERS *.h)

if(WIN32)
    set(MENGDE_LIB_TYPE STATIC)
else()
    set(MENGDE_LIB_TYPE SHARED)
endif()

add_library(core ${MENGDE_LIB_TYPE} ${SOURCES} ${HEADERS})

target_include_directories(core SYSTEM PUBLIC ${LUA_INCLUDE_DIR} ${FLATBUFFERS_INCLUDE_DIR})
target_link_libraries(core util)
target_link_libraries(core ${LUA_LIBRARIES})

install(TARGETS core DESTINATION install)
