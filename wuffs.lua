project "wuffs"

dofile(_BUILD_DIR .. "/static_library.lua")

configuration { "*" }

uuid "f8863658-8c27-4929-b879-b21d74748b4a"

defines {
  "WUFFS_IMPLEMENTATION",
}

files {
  "release/c/wuffs-v0.3.c",
}
