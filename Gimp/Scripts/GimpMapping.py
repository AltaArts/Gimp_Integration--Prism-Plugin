# -*- coding: utf-8 -*-
#
####################################################
#
# PRISM - Pipeline for animation and VFX projects
#
# www.prism-pipeline.com
#
# contact: contact@prism-pipeline.com
#
####################################################
#
#
# Copyright (C) 2016-2023 Richard Frangenberg
# Copyright (C) 2023 Prism Software GmbH
#
# Licensed under GNU LGPL-3.0-or-later
#
# This file is part of Prism.
#
# Prism is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Prism is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with Prism.  If not, see <https://www.gnu.org/licenses/>.
###########################################################################
###########################################################################
#
#                    Gimp Integration for Prism2
#
#       https://github.com/AltaArts/Gimp_Integration--Prism-Plugin
#
#
#                           Joshua Breckeen
#                              Alta Arts
#                          josh@alta-arts.com
#
###########################################################################
###########################################################################
#                                                                         #
#    This is a Collection of Gimp Mapping Options for use with Prism      #
#                                                                         #


#   Gimp image precision enum value -> UI display metadata
IMAGEPRECISIONDATA = {
    100: {"display": "8-bit Integer", "gamma": "Linear"},
    150: {"display": "8-bit Integer", "gamma": "sRGB"},
    200: {"display": "16-bit Integer", "gamma": "Linear"},
    250: {"display": "16-bit Integer", "gamma": "sRGB"},
    300: {"display": "32-bit Integer", "gamma": "Linear"},
    350: {"display": "32-bit Integer", "gamma": "sRGB"},
    500: {"display": "16-bit Half Float", "gamma": "Linear"},
    550: {"display": "16-bit Half Float", "gamma": "sRGB"},
    600: {"display": "32-bit Float", "gamma": "Linear"},
    650: {"display": "32-bit Float", "gamma": "sRGB"},
}


INPUT_FORMATS = [".png", ".exr", ".jpg", "bmp"]

#   Output formats supported by the Prism Gimp render state UI
OUTPUT_FORMATS = [".png", ".exr", ".jpg", ".tif", ".pdf", ".psd"]

#   Export gamma options displayed in the render state UI
OUTPUT_GAMMA_OPTIONS = ["sRGB", "Linear"]

#   Scale percentage options for render export
SCALE_OPTIONS = ["10", "25", "50", "100", "150", "200", "300"]

#   PNG lossless compression level (1 = least, 10 = most)
PNG_COMPRESS_OPTIONS = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

#   JPEG quality and smoothing values (0.0 - 1.0)
JPEG_QUALITY_OPTIONS = ["0", ".1", ".2", ".3", ".4", ".5", ".6", ".7", ".8", ".9", "1"]
JPEG_SMOOTHING_OPTIONS = ["0", ".1", ".2", ".3", ".4", ".5", ".6", ".7", ".8", ".9", "1"]

#   JPEG chroma subsampling labels as presented in the UI
JPEG_SUBSAMPLING_LABELS = ["4:2:0", "4:2:2", "4:4:4"]

#   TIFF compression labels as presented in the UI
TIFF_COMPRESSION_LABELS = [
    "None",
    "LZW (lossless)",
    "Pack Bits (lossless)",
    "Deflate (lossless)",
    "JPEG (lossy)",
]

#   File extension -> format-specific Gimp exporter procedure name
EXPORTER_PROCEDURE_MAP = {
    ".png": "file-png-export",
    ".jpg": "file-jpeg-export",
    ".jpeg": "file-jpeg-export",
    ".tif": "file-tiff-export",
    ".tiff": "file-tiff-export",
    ".pdf": "file-pdf-export",
    ".psd": "file-psd-export",
    ".exr": "file-exr-export",
}

#   UI color mode/bit depth -> file-png-export "format" choice nick
PNG_FORMAT_MAP = {
    ("RGB", "8"): "rgb8",
    ("RGBA", "8"): "rgba8",
    ("GRAY", "8"): "gray8",
    ("GRAYA", "8"): "graya8",
    ("RGB", "16"): "rgb16",
    ("RGBA", "16"): "rgba16",
    ("GRAY", "16"): "gray16",
    ("GRAYA", "16"): "graya16",
}

#   UI JPEG subsampling label -> file-jpeg-export "sub-sampling" choice nick
JPEG_SUBSAMPLING_MAP = {
    "4:2:0": "sub-sampling-2x2",
    "4:2:2": "sub-sampling-2x1",
    "4:4:4": "sub-sampling-1x1",
}

#   UI TIFF compression label -> file-tiff-export "compression" choice nick
TIFF_COMPRESSION_MAP = {
    "None": "none",
    "LZW (lossless)": "lzw",
    "Pack Bits (lossless)": "packbits",
    "Deflate (lossless)": "adobe_deflate",
    "JPEG (lossy)": "jpeg",
}

#   Per-format allowed output color modes
FORMAT_COLOR_MODES = {
    ".png": ["RGB", "RGBA", "GRAY", "GRAYA"],
    ".exr": ["RGB", "RGBA", "GRAY", "GRAYA"],
    ".jpg": ["RGB", "GRAY"],
    ".tif": ["RGB", "RGBA", "GRAY", "GRAYA"],
    ".pdf": ["RGB", "GRAY"],
    ".psd": ["RGB", "RGBA", "GRAY", "GRAYA"],
}

#   Per-format allowed output bit depths
FORMAT_BIT_DEPTHS = {
    ".png": ["8", "16"],
    ".exr": ["16", "32"],
    ".jpg": ["8"],
    ".tif": ["8", "16"],
    ".pdf": ["8"],
    ".psd": ["8", "16", "32"],
}

#   Default bit-depth combo index when a previous value is unavailable
FORMAT_BIT_DEPTH_DEFAULT_INDEX = {
    ".png": 1,
    ".exr": 1,
    ".jpg": 0,
    ".tif": 1,
    ".pdf": 0,
    ".psd": 1,
}

