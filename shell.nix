{ target ? "default", pkgs ? import <nixpkgs> {} }:
let
  PROJECT_ROOT = builtins.toString ./.;
in pkgs.mkShell rec {
  venvDir = "${PROJECT_ROOT}/.venv";
  buildInputs = with pkgs; [
    python3Packages.python
    python3Packages.venvShellHook

    stdenv.cc.cc.lib
    zlib

    cairo
    ninja
    gobject-introspection
    gtk3
  ];

  nativeBuildInputs = with pkgs; [
    pkg-config
  ];

  postShellHook = ''
    unset SOURCE_DATE_EPOCH
    pip install -r ${PROJECT_ROOT}/visualization/requirements.txt

    export LD_LIBRARY_PATH=${pkgs.lib.makeLibraryPath [
      pkgs.stdenv.cc.cc
      pkgs.zlib
    ]}
  '';
}
