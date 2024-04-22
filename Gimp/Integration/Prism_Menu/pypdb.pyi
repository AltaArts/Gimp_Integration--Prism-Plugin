from typing import List, Tuple
from gi.repository import Gegl
from gi.repository import GLib
from gi.repository import Gio
from gi.repository import GObject
'Wrapper of ``Gimp.get_pdb()`` to simplify invoking GIMP PDB procedures.'
import gi
gi.require_version('Gimp', '3.0')
from gi.repository import Gimp
__all__ = ['pdb', 'PyPDBProcedure', 'PDBProcedureError']

class _PyPDB:

    def __init__(self):
        pass

    @property
    def last_status(self):
        pass

    @property
    def last_error(self):
        pass

    def __getattr__(self, name):
        pass

    def __getitem__(self, name):
        pass

    def __contains__(self, name):
        pass

    def remove_from_cache(self, name):
        pass

    def _get_proc_by_name(self, proc_name):
        pass

    @staticmethod
    def _procedure_exists(proc_name):
        pass

    def extension_gimp_help(self, domain_names: List[str]=None, domain_uris: List[str]=None):
        """Parameters:
        
        * domain_names - Domain names.
        
        * domain_uris - Domain URIs.
        """
        pass

    def extension_script_fu(self):
        """A scheme interpreter for scripting GIMP operations.
        
        More help here later.
        """
        pass

    def file_aa_save(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, file: Gio.File=None, file_type: int=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Saves grayscale image in various text formats.
        
        Image types: *
        Menu label: ASCII art
        
        This plug-in uses aalib to save grayscale image as ascii art into a
        variety of text formats.
        
        Parameters:
        
        * image - The image to save.
        
        * num_drawables (default: 1) - Number of drawables to be saved.
        
        * drawables - The drawables to save.
        
        * file - The file to save to.
        
        * file_type (default: 0) - File type to use.
        """
        pass

    def file_ani_load(self, file: Gio.File=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE) -> Gimp.Image:
        """Loads files of Windows ANI file format.
        
        Menu label: Microsoft Windows animated cursor
        
        Loads files of Windows ANI file format.
        
        Parameters:
        
        * file - The file to load.
        
        Returns:
        
        * image - Output image.
        """
        pass

    def file_ani_load_thumb(self, file: Gio.File=None, thumb_size: int=None) -> Tuple[Gimp.Image, int, int, Gimp.ImageType, int]:
        """Loads a preview from a Windows ANI files.
        
        Parameters:
        
        * file - The file to load the thumbnail from.
        
        * thumb_size (default: 256) - Preferred thumbnail size.
        
        Returns:
        
        * image - Thumbnail image.
        
        * image_width (default: 0) - Width of the full-sized image (0 for
          unknown).
        
        * image_height (default: 0) - Height of the full-sized image (0 for
          unknown).
        
        * image_type (default: <enum GIMP_RGB_IMAGE of type Gimp.ImageType>) -
          Type of the image.
        
        * num_layers (default: 1) - Number of layers in the image.
        """
        pass

    def file_ani_save(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, file: Gio.File=None, cursor_name: str=None, author_name: str=None, default_delay: int=None, n_hot_spot_x: int=None, hot_spot_x: Gimp.Int32Array=None, n_hot_spot_y: int=None, hot_spot_y: Gimp.Int32Array=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Saves files in Windows ANI file format.
        
        Image types: *
        Menu label: Microsoft Windows animated cursor
        
        Saves files in Windows ANI file format.
        
        Parameters:
        
        * image - The image to save.
        
        * num_drawables (default: 1) - Number of drawables to be saved.
        
        * drawables - The drawables to save.
        
        * file - The file to save to.
        
        * cursor_name - Cursor Name (Optional).
        
        * author_name - Cursor Author (Optional).
        
        * default_delay (default: 8) - Default delay between frames in jiffies
          (1/60 of a second).
        
        * n_hot_spot_x (default: 0) - Number of hot spot's X coordinates.
        
        * hot_spot_x - X coordinates of hot spot (one per layer).
        
        * n_hot_spot_y (default: 0) - Number of hot spot's Y coordinates.
        
        * hot_spot_y - Y coordinates of hot spot (one per layer).
        """
        pass

    def file_bmp_load(self, file: Gio.File=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE) -> Gimp.Image:
        """Loads files of Windows BMP file format.
        
        Menu label: Windows BMP image
        
        Loads files of Windows BMP file format.
        
        Parameters:
        
        * file - The file to load.
        
        Returns:
        
        * image - Output image.
        """
        pass

    def file_bmp_save(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, file: Gio.File=None, use_rle: bool=None, write_color_space: bool=None, rgb_format: int=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Saves files in Windows BMP file format.
        
        Image types: INDEXED, GRAY, RGB*
        Menu label: Windows BMP image
        
        Saves files in Windows BMP file format.
        
        Parameters:
        
        * image - The image to save.
        
        * num_drawables (default: 1) - Number of drawables to be saved.
        
        * drawables - The drawables to save.
        
        * file - The file to save to.
        
        * use_rle (default: False) - Use run-length-encoding compression (only
          valid for 4 and 8-bit indexed images).
        
        * write_color_space (default: True) - Whether or not to write
          BITMAPV5HEADER color space data.
        
        * rgb_format (default: 3) - Export format for RGB images (0=RGB_565,
          1=RGBA_5551, 2=RGB_555, 3=RGB_888, 4=RGBA_8888,
          5=RGBX_8888).
        """
        pass

    def file_bz2_load(self, file: Gio.File=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE) -> Gimp.Image:
        """Loads files compressed with bzip2.
        
        Menu label: bzip archive
        
        This procedure loads files in the bzip2 compressed format.
        
        Parameters:
        
        * file - The file to load.
        
        Returns:
        
        * image - Output image.
        """
        pass

    def file_bz2_save(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, file: Gio.File=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Saves files compressed with bzip2.
        
        Image types: RGB*, GRAY*, INDEXED*
        Menu label: bzip archive
        
        This procedure saves files in the bzip2 compressed format.
        
        Parameters:
        
        * image - The image to save.
        
        * num_drawables (default: 1) - Number of drawables to be saved.
        
        * drawables - The drawables to save.
        
        * file - The file to save to.
        """
        pass

    def file_cel_load(self, file: Gio.File=None, palette_file: Gio.File=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE) -> Gimp.Image:
        """Loads files in KISS CEL file format.
        
        Menu label: KISS CEL
        
        This plug-in loads individual KISS cell files.
        
        Parameters:
        
        * file - The file to load.
        
        * palette_file - KCF file to load palette from.
        
        Returns:
        
        * image - Output image.
        """
        pass

    def file_cel_save(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, file: Gio.File=None, palette_file: Gio.File=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Exports files in KISS CEL file format.
        
        Image types: RGB*, INDEXED*
        Menu label: KISS CEL
        
        This plug-in exports individual KISS cell files.
        
        Parameters:
        
        * image - The image to save.
        
        * num_drawables (default: 1) - Number of drawables to be saved.
        
        * drawables - The drawables to save.
        
        * file - The file to save to.
        
        * palette_file - File to save palette to.
        """
        pass

    def file_colorxhtml_save(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, file: Gio.File=None, source_file: bool=None, characters: str=None, font_size: int=None, separate: bool=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Save as colored HTML text.
        
        Image types: RGB
        Menu label: Colored HTML text
        
        Saves the image as colored XHTML text (based on Perl version by Marc
        Lehmann).
        
        Parameters:
        
        * image - The image to save.
        
        * num_drawables (default: 1) - Number of drawables to be saved.
        
        * drawables - The drawables to save.
        
        * file - The file to save to.
        
        * source_file (default: False) - _Read characters from file, if true,
          or use text entry.
        
        * characters (default: foo) - _File to read or characters to use.
        
        * font_size (default: 10) - Fo_nt size in pixels.
        
        * separate (default: False) - _Write a separate CSS file.
        """
        pass

    def file_csource_save(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, file: Gio.File=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Dump image data in RGB(A) format for C source.
        
        Image types: *
        Menu label: C source code
        
        CSource cannot be run non-interactively.
        
        Parameters:
        
        * image - The image to save.
        
        * num_drawables (default: 1) - Number of drawables to be saved.
        
        * drawables - The drawables to save.
        
        * file - The file to save to.
        """
        pass

    def file_cur_load(self, file: Gio.File=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE) -> Gimp.Image:
        """Loads files of Windows CUR file format.
        
        Menu label: Microsoft Windows cursor
        
        Loads files of Windows CUR file format.
        
        Parameters:
        
        * file - The file to load.
        
        Returns:
        
        * image - Output image.
        """
        pass

    def file_cur_save(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, file: Gio.File=None, n_hot_spot_x: int=None, hot_spot_x: Gimp.Int32Array=None, n_hot_spot_y: int=None, hot_spot_y: Gimp.Int32Array=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Saves files in Windows CUR file format.
        
        Image types: *
        Menu label: Microsoft Windows cursor
        
        Saves files in Windows CUR file format.
        
        Parameters:
        
        * image - The image to save.
        
        * num_drawables (default: 1) - Number of drawables to be saved.
        
        * drawables - The drawables to save.
        
        * file - The file to save to.
        
        * n_hot_spot_x (default: 0) - Number of hot spot's X coordinates.
        
        * hot_spot_x - X coordinates of hot spot (one per layer).
        
        * n_hot_spot_y (default: 0) - Number of hot spot's Y coordinates.
        
        * hot_spot_y - Y coordinates of hot spot (one per layer).
        """
        pass

    def file_darktable_ari_load(self, file: Gio.File=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE) -> Gimp.Image:
        """Load files in the ARI raw format via darktable.
        
        This plug-in loads files in Arriflex' raw ARI format by calling
        darktable.
        
        Parameters:
        
        * file - The file to load.
        
        Returns:
        
        * image - Output image.
        """
        pass

    def file_darktable_bay_load(self, file: Gio.File=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE) -> Gimp.Image:
        """Load files in the BAY raw format via darktable.
        
        This plug-in loads files in Casio's raw BAY format by calling darktable.
        
        Parameters:
        
        * file - The file to load.
        
        Returns:
        
        * image - Output image.
        """
        pass

    def file_darktable_canon_load(self, file: Gio.File=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE) -> Gimp.Image:
        """Load files in the Canon raw formats via darktable.
        
        This plug-in loads files in Canon's raw formats by calling darktable.
        
        Parameters:
        
        * file - The file to load.
        
        Returns:
        
        * image - Output image.
        """
        pass

    def file_darktable_cine_load(self, file: Gio.File=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE) -> Gimp.Image:
        """Load files in the CINE raw format via darktable.
        
        This plug-in loads files in Phantom Software's raw CINE format by
        calling darktable.
        
        Parameters:
        
        * file - The file to load.
        
        Returns:
        
        * image - Output image.
        """
        pass

    def file_darktable_dng_load(self, file: Gio.File=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE) -> Gimp.Image:
        """Load files in the DNG raw format via darktable.
        
        This plug-in loads files in the Adobe Digital Negative DNG format by
        calling darktable.
        
        Parameters:
        
        * file - The file to load.
        
        Returns:
        
        * image - Output image.
        """
        pass

    def file_darktable_erf_load(self, file: Gio.File=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE) -> Gimp.Image:
        """Load files in the ERF raw format via darktable.
        
        This plug-in loads files in Epson's raw ERF format by calling darktable.
        
        Parameters:
        
        * file - The file to load.
        
        Returns:
        
        * image - Output image.
        """
        pass

    def file_darktable_hasselblad_load(self, file: Gio.File=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE) -> Gimp.Image:
        """Load files in the Hasselblad raw formats via darktable.
        
        This plug-in loads files in Hasselblad's raw formats by calling
        darktable.
        
        Parameters:
        
        * file - The file to load.
        
        Returns:
        
        * image - Output image.
        """
        pass

    def file_darktable_kodak_load(self, file: Gio.File=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE) -> Gimp.Image:
        """Load files in the Kodak raw formats via darktable.
        
        This plug-in loads files in Kodak's raw formats by calling darktable.
        
        Parameters:
        
        * file - The file to load.
        
        Returns:
        
        * image - Output image.
        """
        pass

    def file_darktable_load_thumb(self, file: Gio.File=None, thumb_size: int=None) -> Tuple[Gimp.Image, int, int, Gimp.ImageType, int]:
        """Load thumbnail from a raw image via darktable.
        
        This plug-in loads a thumbnail from a raw image by calling
        darktable-cli.
        
        Parameters:
        
        * file - The file to load the thumbnail from.
        
        * thumb_size (default: 256) - Preferred thumbnail size.
        
        Returns:
        
        * image - Thumbnail image.
        
        * image_width (default: 0) - Width of the full-sized image (0 for
          unknown).
        
        * image_height (default: 0) - Height of the full-sized image (0 for
          unknown).
        
        * image_type (default: <enum GIMP_RGB_IMAGE of type Gimp.ImageType>) -
          Type of the image.
        
        * num_layers (default: 1) - Number of layers in the image.
        """
        pass

    def file_darktable_mef_load(self, file: Gio.File=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE) -> Gimp.Image:
        """Load files in the MEF raw format via darktable.
        
        This plug-in loads files in Mamiya's raw MEF format by calling
        darktable.
        
        Parameters:
        
        * file - The file to load.
        
        Returns:
        
        * image - Output image.
        """
        pass

    def file_darktable_minolta_load(self, file: Gio.File=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE) -> Gimp.Image:
        """Load files in the Minolta raw formats via darktable.
        
        This plug-in loads files in Minolta's raw formats by calling darktable.
        
        Parameters:
        
        * file - The file to load.
        
        Returns:
        
        * image - Output image.
        """
        pass

    def file_darktable_mos_load(self, file: Gio.File=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE) -> Gimp.Image:
        """Load files in the MOS raw format via darktable.
        
        This plug-in loads files in Leaf's raw MOS format by calling darktable.
        
        Parameters:
        
        * file - The file to load.
        
        Returns:
        
        * image - Output image.
        """
        pass

    def file_darktable_nikon_load(self, file: Gio.File=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE) -> Gimp.Image:
        """Load files in the Nikon raw formats via darktable.
        
        This plug-in loads files in Nikon's raw formats by calling darktable.
        
        Parameters:
        
        * file - The file to load.
        
        Returns:
        
        * image - Output image.
        """
        pass

    def file_darktable_orf_load(self, file: Gio.File=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE) -> Gimp.Image:
        """Load files in the ORF raw format via darktable.
        
        This plug-in loads files in Olympus' raw ORF format by calling
        darktable.
        
        Parameters:
        
        * file - The file to load.
        
        Returns:
        
        * image - Output image.
        """
        pass

    def file_darktable_panasonic_load(self, file: Gio.File=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE) -> Gimp.Image:
        """Load files in the Panasonic raw formats via darktable.
        
        This plug-in loads files in Panasonic's raw formats by calling
        darktable.
        
        Parameters:
        
        * file - The file to load.
        
        Returns:
        
        * image - Output image.
        """
        pass

    def file_darktable_pef_load(self, file: Gio.File=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE) -> Gimp.Image:
        """Load files in the PEF raw format via darktable.
        
        This plug-in loads files in Pentax' raw PEF format by calling darktable.
        
        Parameters:
        
        * file - The file to load.
        
        Returns:
        
        * image - Output image.
        """
        pass

    def file_darktable_phaseone_load(self, file: Gio.File=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE) -> Gimp.Image:
        """Load files in the Phase One raw formats via darktable.
        
        This plug-in loads files in Phase One's raw formats by calling
        darktable.
        
        Parameters:
        
        * file - The file to load.
        
        Returns:
        
        * image - Output image.
        """
        pass

    def file_darktable_pxn_load(self, file: Gio.File=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE) -> Gimp.Image:
        """Load files in the PXN raw format via darktable.
        
        This plug-in loads files in Logitech's raw PXN format by calling
        darktable.
        
        Parameters:
        
        * file - The file to load.
        
        Returns:
        
        * image - Output image.
        """
        pass

    def file_darktable_qtk_load(self, file: Gio.File=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE) -> Gimp.Image:
        """Load files in the QTK raw format via darktable.
        
        This plug-in loads files in Apple's QuickTake QTK raw format by calling
        darktable.
        
        Parameters:
        
        * file - The file to load.
        
        Returns:
        
        * image - Output image.
        """
        pass

    def file_darktable_raf_load(self, file: Gio.File=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE) -> Gimp.Image:
        """Load files in the RAF raw format via darktable.
        
        This plug-in loads files in Fujifilm's raw RAF format by calling
        darktable.
        
        Parameters:
        
        * file - The file to load.
        
        Returns:
        
        * image - Output image.
        """
        pass

    def file_darktable_rdc_load(self, file: Gio.File=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE) -> Gimp.Image:
        """Load files in the RDC raw format via darktable.
        
        This plug-in loads files in Digital Foto Maker's raw RDC format by
        calling darktable.
        
        Parameters:
        
        * file - The file to load.
        
        Returns:
        
        * image - Output image.
        """
        pass

    def file_darktable_rwl_load(self, file: Gio.File=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE) -> Gimp.Image:
        """Load files in the RWL raw format via darktable.
        
        This plug-in loads files in Leica's raw RWL format by calling darktable.
        
        Parameters:
        
        * file - The file to load.
        
        Returns:
        
        * image - Output image.
        """
        pass

    def file_darktable_sinar_load(self, file: Gio.File=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE) -> Gimp.Image:
        """Load files in the Sinar raw formats via darktable.
        
        This plug-in loads files in Sinar's raw formats by calling darktable.
        
        Parameters:
        
        * file - The file to load.
        
        Returns:
        
        * image - Output image.
        """
        pass

    def file_darktable_sony_load(self, file: Gio.File=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE) -> Gimp.Image:
        """Load files in the Sony raw formats via darktable.
        
        This plug-in loads files in Sony's raw formats by calling darktable.
        
        Parameters:
        
        * file - The file to load.
        
        Returns:
        
        * image - Output image.
        """
        pass

    def file_darktable_srw_load(self, file: Gio.File=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE) -> Gimp.Image:
        """Load files in the SRW raw format via darktable.
        
        This plug-in loads files in Samsung's raw SRW format by calling
        darktable.
        
        Parameters:
        
        * file - The file to load.
        
        Returns:
        
        * image - Output image.
        """
        pass

    def file_darktable_x3f_load(self, file: Gio.File=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE) -> Gimp.Image:
        """Load files in the X3F raw format via darktable.
        
        This plug-in loads files in Sigma's raw X3F format by calling darktable.
        
        Parameters:
        
        * file - The file to load.
        
        Returns:
        
        * image - Output image.
        """
        pass

    def file_dcx_load(self, file: Gio.File=None, override_palette: int=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE) -> Gimp.Image:
        """Loads files in Zsoft DCX file format.
        
        Menu label: ZSoft DCX image
        
        FIXME: write help for dcx_load.
        
        Parameters:
        
        * file - The file to load.
        
        * override_palette (default: 0) - Use built-in palette (0) or override
          with black/white (1).
        
        Returns:
        
        * image - Output image.
        """
        pass

    def file_dds_load(self, file: Gio.File=None, load_mipmaps: bool=None, flip_image: bool=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE) -> Gimp.Image:
        """Loads files in DDS image format.
        
        Menu label: DDS image
        
        Loads files in DDS image format.
        
        Parameters:
        
        * file - The file to load.
        
        * load_mipmaps (default: True) - Load mipmaps if present.
        
        * flip_image (default: False) - Flip the image vertically on import.
        
        Returns:
        
        * image - Output image.
        """
        pass

    def file_dds_save(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, file: Gio.File=None, compression_format: str=None, perceptual_metric: bool=None, format: str=None, save_type: str=None, flip_image: bool=None, transparent_color: bool=None, transparent_index: int=None, mipmaps: str=None, mipmap_filter: str=None, mipmap_wrap: str=None, gamma_correct: bool=None, srgb: bool=None, gamma: float=None, preserve_alpha_coverage: bool=None, alpha_test_threshold: float=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Saves files in DDS image format.
        
        Image types: INDEXED, GRAY, RGB
        Menu label: DDS image
        
        Saves files in DDS image format.
        
        Parameters:
        
        * image - The image to save.
        
        * num_drawables (default: 1) - Number of drawables to be saved.
        
        * drawables - The drawables to save.
        
        * file - The file to save to.
        
        * compression_format - Compression format.
        
        * perceptual_metric (default: False) - Use a perceptual error metric
          during compression.
        
        * format - Pixel format.
        
        * save_type - How to save the image.
        
        * flip_image (default: False) - Flip the image vertically on export.
        
        * transparent_color (default: False) - Make an indexed color
          transparent.
        
        * transparent_index (default: 0) - Index of transparent color or -1 to
          disable (for indexed images only).
        
        * mipmaps - How to handle mipmaps.
        
        * mipmap_filter - Filtering to use when generating mipmaps.
        
        * mipmap_wrap - Wrap mode to use when generating mipmaps.
        
        * gamma_correct (default: False) - Use gamma correct mipmap filtering.
        
        * srgb (default: False) - Use sRGB colorspace for gamma correction.
        
        * gamma (default: 0.0) - Gamma value to use for gamma correction (e.g.
          2.2).
        
        * preserve_alpha_coverage (default: False) - Preserve alpha test
          coverage for alpha channel maps.
        
        * alpha_test_threshold (default: 0.5) - Alpha test threshold value for
          which alpha test coverage should be preserved.
        """
        pass

    def file_desktop_link_load(self, file: Gio.File=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE) -> Gimp.Image:
        """Follows a link to an image in a .desktop file.
        
        Menu label: Desktop Link
        
        Opens a .desktop file and if it is a link, it asks GIMP to open the file
        the link points to.
        
        Parameters:
        
        * file - The file to load.
        
        Returns:
        
        * image - Output image.
        """
        pass

    def file_dicom_load(self, file: Gio.File=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE) -> Gimp.Image:
        """Loads files of the dicom file format.
        
        Menu label: DICOM image
        
        Load a file in the DICOM standard format. The standard is defined at
        http://medical.nema.org/. The plug-in currently only supports
        reading images with uncompressed pixel sections.
        
        Parameters:
        
        * file - The file to load.
        
        Returns:
        
        * image - Output image.
        """
        pass

    def file_dicom_save(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, file: Gio.File=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Save file in the DICOM file format.
        
        Image types: RGB, GRAY
        Menu label: Digital Imaging and Communications in Medicine image
        
        Save an image in the medical standard DICOM image formats. The standard
        is defined at http://medical.nema.org/. The file format is
        defined in section 10 of the standard. The files are saved
        uncompressed and the compulsory DICOM tags are filled with
        default dummy values.
        
        Parameters:
        
        * image - The image to save.
        
        * num_drawables (default: 1) - Number of drawables to be saved.
        
        * drawables - The drawables to save.
        
        * file - The file to save to.
        """
        pass

    def file_eps_load(self, file: Gio.File=None, resolution: int=None, width: int=None, height: int=None, check_bbox: bool=None, pages: str=None, coloring: int=None, text_alpha_bits: int=None, graphoc_alpha_bits: int=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE) -> Gimp.Image:
        """Load Encapsulated PostScript images.
        
        Menu label: Encapsulated PostScript image
        
        Load Encapsulated PostScript images.
        
        Parameters:
        
        * file - The file to load.
        
        * resolution (default: 100) - Resolution to interpret image (dpi).
        
        * width (default: 826) - Desired width.
        
        * height (default: 1170) - Desired height.
        
        * check_bbox (default: True) - FALSE: Use width/height, TRUE: Use
          BoundingBox.
        
        * pages (default: 1) - Pages to load (e.g.: 1,3,5-7).
        
        * coloring (default: 6) - 4: b/w, 5: grey, 6: color image, 7:
          automatic.
        
        * text_alpha_bits (default: 1) - 1, 2 or 4.
        
        * graphoc_alpha_bits (default: 1) - 1, 2 or 4.
        
        Returns:
        
        * image - Output image.
        """
        pass

    def file_eps_save(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, file: Gio.File=None, width: float=None, height: float=None, x_offset: float=None, y_offset: float=None, unit: int=None, keep_ratio: bool=None, rotation: int=None, level: bool=None, eps_flag: bool=None, show_preview: bool=None, preview: int=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Export image as Encapsulated PostScript image.
        
        Image types: RGB, GRAY, INDEXED
        Menu label: Encapsulated PostScript
        
        PostScript exporting handles all image types except those with alpha
        channels.
        
        Parameters:
        
        * image - The image to save.
        
        * num_drawables (default: 1) - Number of drawables to be saved.
        
        * drawables - The drawables to save.
        
        * file - The file to save to.
        
        * width (default: 287.0) - Width of the image in PostScript file (0:
          use input image size).
        
        * height (default: 200.0) - Height of the image in PostScript file (0:
          use input image size).
        
        * x_offset (default: 5.0) - X-offset to image from lower left corner.
        
        * y_offset (default: 5.0) - Y-offset to image from lower left corner.
        
        * unit (default: 1) - Unit for width/height/offset. 0: inches, 1:
          millimeters.
        
        * keep_ratio (default: True) - FALSE: use width/height, TRUE: keep
          aspect ratio.
        
        * rotation (default: 0) - 0, 90, 180, 270.
        
        * level (default: True) - FALSE: PostScript Level 1, TRUE: PostScript
          Level 2.
        
        * eps_flag (default: False) - FALSE: PostScript, TRUE: Encapsulated
          PostScript.
        
        * show_preview (default: False) - Show Preview.
        
        * preview (default: 256) - 0: no preview, >0: max. size of preview.
        """
        pass

    def file_exr_load(self, file: Gio.File=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE) -> Gimp.Image:
        """Loads files in the OpenEXR file format.
        
        Menu label: OpenEXR image
        
        This plug-in loads OpenEXR files.
        
        Parameters:
        
        * file - The file to load.
        
        Returns:
        
        * image - Output image.
        """
        pass

    def file_exr_save(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, file: Gio.File=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Saves files in the OpenEXR file format.
        
        Image types: *
        Menu label: OpenEXR image
        
        This procedure saves images in the OpenEXR format, using gegl:exr-save.
        
        Parameters:
        
        * image - The image to save.
        
        * num_drawables (default: 1) - Number of drawables to be saved.
        
        * drawables - The drawables to save.
        
        * file - The file to save to.
        """
        pass

    def file_farbfeld_load(self, file: Gio.File=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE) -> Gimp.Image:
        """Load file in the Farbfeld file format.
        
        Menu label: Farbfeld
        
        Load file in the Farbfeld file format.
        
        Parameters:
        
        * file - The file to load.
        
        Returns:
        
        * image - Output image.
        """
        pass

    def file_farbfeld_save(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, file: Gio.File=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Export image in the Farbfeld file format.
        
        Image types: *
        Menu label: Farbfeld
        
        Export image in the Farbfeld file format.
        
        Parameters:
        
        * image - The image to save.
        
        * num_drawables (default: 1) - Number of drawables to be saved.
        
        * drawables - The drawables to save.
        
        * file - The file to save to.
        """
        pass

    def file_faxg3_load(self, file: Gio.File=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE) -> Gimp.Image:
        """Loads g3 fax files.
        
        Menu label: G3 fax image
        
        This plug-in loads Fax G3 Image files.
        
        Parameters:
        
        * file - The file to load.
        
        Returns:
        
        * image - Output image.
        """
        pass

    def file_fits_load(self, file: Gio.File=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE) -> Gimp.Image:
        """Load file of the FITS file format.
        
        Menu label: Flexible Image Transport System
        
        Load file of the FITS file format (Flexible Image Transport System).
        
        Parameters:
        
        * file - The file to load.
        
        Returns:
        
        * image - Output image.
        """
        pass

    def file_fits_save(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, file: Gio.File=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Export file in the FITS file format.
        
        Image types: RGB, GRAY, INDEXED
        Menu label: Flexible Image Transport System
        
        FITS exporting handles all image types except those with alpha channels.
        
        Parameters:
        
        * image - The image to save.
        
        * num_drawables (default: 1) - Number of drawables to be saved.
        
        * drawables - The drawables to save.
        
        * file - The file to save to.
        """
        pass

    def file_fli_info(self, file: Gio.File=None) -> Tuple[int, int, int]:
        """Get information about a Fli movie.
        
        This is an experimental plug-in to handle FLI movies.
        
        Parameters:
        
        * file - The local file to get info about.
        
        Returns:
        
        * width (default: 0) - Width of one frame.
        
        * height (default: 0) - Height of one frame.
        
        * frames (default: 0) - Number of frames.
        """
        pass

    def file_fli_load(self, file: Gio.File=None, from_frame: int=None, to_frame: int=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE) -> Gimp.Image:
        """Load FLI-movies.
        
        Menu label: AutoDesk FLIC animation
        
        This is an experimental plug-in to handle FLI movies.
        
        Parameters:
        
        * file - The file to load.
        
        * from_frame (default: -1) - Load beginning from this frame.
        
        * to_frame (default: -1) - End loading with this frame.
        
        Returns:
        
        * image - Output image.
        """
        pass

    def file_fli_save(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, file: Gio.File=None, from_frame: int=None, to_frame: int=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Export FLI-movies.
        
        Image types: INDEXED, GRAY
        Menu label: AutoDesk FLIC animation
        
        This is an experimental plug-in to handle FLI movies.
        
        Parameters:
        
        * image - The image to save.
        
        * num_drawables (default: 1) - Number of drawables to be saved.
        
        * drawables - The drawables to save.
        
        * file - The file to save to.
        
        * from_frame (default: -1) - Export beginning from this frame.
        
        * to_frame (default: -1) - End exporting with this frame (or -1 for
          all frames).
        """
        pass

    def file_gbr_load(self, file: Gio.File=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE) -> Gimp.Image:
        """Loads GIMP brushes.
        
        Loads GIMP brushes (1 or 4 bpp and old .gpb format).
        
        Parameters:
        
        * file - The file to load.
        
        Returns:
        
        * image - Output image.
        """
        pass

    def file_gbr_save(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, file: Gio.File=None, spacing: int=None, description: str=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Exports files in the GIMP brush file format.
        
        Image types: *
        Menu label: GIMP brush
        
        Exports files in the GIMP brush file format.
        
        Parameters:
        
        * image - The image to save.
        
        * num_drawables (default: 1) - Number of drawables to be saved.
        
        * drawables - The drawables to save.
        
        * file - The file to save to.
        
        * spacing (default: 10) - Spacing of the brush.
        
        * description (default: GIMP Brush) - Short description of the brush.
        """
        pass

    def file_gbr_save_internal(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, file: Gio.File=None, spacing: int=None, name: str=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Exports Gimp brush file (.GBR).
        
        Exports Gimp brush file (.GBR).
        
        Parameters:
        
        * image - Input image.
        
        * num_drawables (default: 1) - Number of drawables.
        
        * drawables - Selected drawables.
        
        * file - The file to export.
        
        * spacing (default: 10) - Spacing of the brush.
        
        * name (default: GIMP Brush) - The name of the brush.
        """
        pass

    def file_gex_load(self, file: Gio.File=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE) -> str:
        """Loads GIMP extension.
        
        Loads GIMP extension.
        
        Parameters:
        
        * file - The file to load.
        
        Returns:
        
        * extension_id - Identifier of the newly installed extension.
        """
        pass

    def file_gif_load(self, file: Gio.File=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE) -> Gimp.Image:
        """Loads files of Compuserve GIF file format.
        
        Menu label: GIF image
        
        Parameters:
        
        * file - The file to load.
        
        Returns:
        
        * image - Output image.
        """
        pass

    def file_gif_load_thumb(self, file: Gio.File=None, thumb_size: int=None) -> Tuple[Gimp.Image, int, int, Gimp.ImageType, int]:
        """Loads only the first frame of a GIF image, to be used as a thumbnail.
        
        Parameters:
        
        * file - The file to load the thumbnail from.
        
        * thumb_size (default: 256) - Preferred thumbnail size.
        
        Returns:
        
        * image - Thumbnail image.
        
        * image_width (default: 0) - Width of the full-sized image (0 for
          unknown).
        
        * image_height (default: 0) - Height of the full-sized image (0 for
          unknown).
        
        * image_type (default: <enum GIMP_RGB_IMAGE of type Gimp.ImageType>) -
          Type of the image.
        
        * num_layers (default: 1) - Number of layers in the image.
        """
        pass

    def file_gif_save(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, file: Gio.File=None, interlace: bool=None, loop: bool=None, number_of_repeats: int=None, default_delay: int=None, default_dispose: int=None, as_animation: bool=None, force_delay: bool=None, force_dispose: bool=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Exports files in GIF file format.
        
        Image types: INDEXED*, GRAY*
        Menu label: GIF image
        
        Export a file in GIF format, with possible animation, transparency, and
        comment. To export an animation, operate on a multi-layer file
        and give the 'as-animation' parameter as TRUE. The plug-in will
        interpret <50% alpha as transparent. When run non-interactively,
        the value for the comment is taken from the 'gimp-comment'
        parasite.
        
        Parameters:
        
        * image - The image to save.
        
        * num_drawables (default: 1) - Number of drawables to be saved.
        
        * drawables - The drawables to save.
        
        * file - The file to save to.
        
        * interlace (default: False) - Try to export as interlaced.
        
        * loop (default: True) - (animated gif) Loop infinitely.
        
        * number_of_repeats (default: 0) - (animated gif) Number of repeats
          (Ignored if 'loop' is TRUE).
        
        * default_delay (default: 100) - (animated gif) Default delay between
          frames in milliseconds.
        
        * default_dispose (default: 0) - (animated gif) Default disposal type
          (0=`don't care`, 1=combine, 2=replace).
        
        * as_animation (default: False) - Export GIF as animation?.
        
        * force_delay (default: False) - (animated gif) Use specified delay
          for all frames.
        
        * force_dispose (default: False) - (animated gif) Use specified
          disposal for all frames.
        """
        pass

    def file_gih_load(self, file: Gio.File=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE) -> Gimp.Image:
        """Loads GIMP animated brushes.
        
        This procedure loads a GIMP brush pipe as an image.
        
        Parameters:
        
        * file - The file to load.
        
        Returns:
        
        * image - Output image.
        """
        pass

    def file_gih_save(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, file: Gio.File=None, spacing: int=None, description: str=None, cell_width: int=None, cell_height: int=None, num_cells: int=None, ranks: GLib.Bytes=None, selection_modes: List[str]=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Exports images in GIMP brush pipe format.
        
        Image types: RGB*, GRAY*
        Menu label: GIMP brush (animated)
        
        This plug-in exports an image in the GIMP brush pipe format. For a
        colored brush pipe, RGBA layers are used, otherwise the layers
        should be grayscale masks. The image can be multi-layered, and
        additionally the layers can be divided into a rectangular array
        of brushes.
        
        Parameters:
        
        * image - The image to save.
        
        * num_drawables (default: 1) - Number of drawables to be saved.
        
        * drawables - The drawables to save.
        
        * file - The file to save to.
        
        * spacing (default: 20) - Spacing of the brush.
        
        * description (default: GIMP Brush Pipe) - Short description of the
          GIH brush pipe.
        
        * cell_width (default: 1) - Width of the brush cells in pixels.
        
        * cell_height (default: 1) - Height of the brush cells in pixels.
        
        * num_cells (default: 1) - Number of cells to cut up.
        
        * ranks - Ranks of the dimensions.
        
        * selection_modes - Selection modes.
        """
        pass

    def file_gih_save_internal(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, file: Gio.File=None, spacing: int=None, name: str=None, params: str=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Exports Gimp animated brush file (.gih).
        
        Exports Gimp animated brush file (.gih).
        
        Parameters:
        
        * image - Input image.
        
        * num_drawables (default: 1) - The number of drawables to save.
        
        * drawables - Drawables to save.
        
        * file - The file to export.
        
        * spacing (default: 10) - Spacing of the brush.
        
        * name (default: GIMP Brush) - The name of the brush.
        
        * params - The pipe's parameters.
        """
        pass

    def file_glob(self, pattern: str=None, filename_encoding: bool=None) -> List[str]:
        """Returns a list of matching filenames.
        
        This can be useful in scripts and other plug-ins (e.g.,
        batch-conversion). See the glob(7) manpage for more info. Note
        however that this isn't a full-featured glob implementation. It
        only handles simple patterns like "/home/foo/bar/*.jpg".
        
        Parameters:
        
        * pattern - The glob pattern (in UTF-8 encoding).
        
        * filename_encoding (default: False) - FALSE to return UTF-8 strings,
          TRUE to return strings in filename encoding.
        
        Returns:
        
        * files - The list of matching filenames.
        """
        pass

    def file_gz_load(self, file: Gio.File=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE) -> Gimp.Image:
        """Loads files compressed with gzip.
        
        Menu label: gzip archive
        
        This procedure loads files in the gzip compressed format.
        
        Parameters:
        
        * file - The file to load.
        
        Returns:
        
        * image - Output image.
        """
        pass

    def file_gz_save(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, file: Gio.File=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Saves files compressed with gzip.
        
        Image types: RGB*, GRAY*, INDEXED*
        Menu label: gzip archive
        
        This procedure saves files in the gzip compressed format.
        
        Parameters:
        
        * image - The image to save.
        
        * num_drawables (default: 1) - Number of drawables to be saved.
        
        * drawables - The drawables to save.
        
        * file - The file to save to.
        """
        pass

    def file_header_save(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, file: Gio.File=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Saves files as C unsigned character array.
        
        Image types: INDEXED, RGB
        Menu label: C source code header
        
        FIXME: write help.
        
        Parameters:
        
        * image - The image to save.
        
        * num_drawables (default: 1) - Number of drawables to be saved.
        
        * drawables - The drawables to save.
        
        * file - The file to save to.
        """
        pass

    def file_heif_av1_load(self, file: Gio.File=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE) -> Gimp.Image:
        """Loads AVIF images.
        
        Menu label: HEIF/AVIF
        
        Load image stored in AV1 Image File Format (AVIF).
        
        Parameters:
        
        * file - The file to load.
        
        Returns:
        
        * image - Output image.
        """
        pass

    def file_heif_av1_save(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, file: Gio.File=None, quality: int=None, lossless: bool=None, save_bit_depth: int=None, pixel_format: int=None, encoder_speed: int=None, save_exif: bool=None, save_xmp: bool=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Exports AVIF images.
        
        Image types: RGB*
        Menu label: HEIF/AVIF
        
        Save image in AV1 Image File Format (AVIF).
        
        Parameters:
        
        * image - The image to save.
        
        * num_drawables (default: 1) - Number of drawables to be saved.
        
        * drawables - The drawables to save.
        
        * file - The file to save to.
        
        * quality (default: 50) - Quality factor (0 = worst, 100 = best).
        
        * lossless (default: False) - Use lossless compression.
        
        * save_bit_depth (default: 8) - Bit depth of exported image.
        
        * pixel_format (default: 3) - Format of color sub-sampling.
        
        * encoder_speed (default: 1) - Tradeoff between speed and compression.
        
        * save_exif (default: False) - Toggle saving Exif data.
        
        * save_xmp (default: False) - Toggle saving XMP data.
        """
        pass

    def file_heif_hej2_load(self, file: Gio.File=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE) -> Gimp.Image:
        """Loads HEJ2 images.
        
        Menu label: JPEG 2000 encapsulated in HEIF
        
        Load JPEG 2000 image encapsulated in HEIF (HEJ2).
        
        Parameters:
        
        * file - The file to load.
        
        Returns:
        
        * image - Output image.
        """
        pass

    def file_heif_load(self, file: Gio.File=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE) -> Gimp.Image:
        """Loads HEIF images.
        
        Menu label: HEIF/HEIC
        
        Load image stored in HEIF format (High Efficiency Image File Format).
        Typical suffices for HEIF files are .heif, .heic.
        
        Parameters:
        
        * file - The file to load.
        
        Returns:
        
        * image - Output image.
        """
        pass

    def file_heif_save(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, file: Gio.File=None, quality: int=None, lossless: bool=None, save_bit_depth: int=None, pixel_format: int=None, encoder_speed: int=None, save_exif: bool=None, save_xmp: bool=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Exports HEIF images.
        
        Image types: RGB*
        Menu label: HEIF/HEIC
        
        Save image in HEIF format (High Efficiency Image File Format).
        
        Parameters:
        
        * image - The image to save.
        
        * num_drawables (default: 1) - Number of drawables to be saved.
        
        * drawables - The drawables to save.
        
        * file - The file to save to.
        
        * quality (default: 50) - Quality factor (0 = worst, 100 = best).
        
        * lossless (default: False) - Use lossless compression.
        
        * save_bit_depth (default: 8) - Bit depth of exported image.
        
        * pixel_format (default: 3) - Format of color sub-sampling.
        
        * encoder_speed (default: 1) - Tradeoff between speed and compression.
        
        * save_exif (default: False) - Toggle saving Exif data.
        
        * save_xmp (default: False) - Toggle saving XMP data.
        """
        pass

    def file_hgt_load(self, file: Gio.File=None, sample_spacing: int=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE) -> Gimp.Image:
        """Load HGT data as images.
        
        Menu label: Digital Elevation Model data
        
        Load Digital Elevation Model data in HGT format from the Shuttle Radar
        Topography Mission as images. Though the output image will be
        RGB, all colors are grayscale by default and the contrast will
        be quite low on most earth relief. Therefore You will likely
        want to remap elevation to colors as a second step, for instance
        with the "Gradient Map" plug-in.
        
        Parameters:
        
        * file - The file to load.
        
        * sample_spacing (default: 0) - The sample spacing of the data. (0:
          auto-detect, 1: SRTM-1, 2: SRTM-3 data).
        
        Returns:
        
        * image - Output image.
        """
        pass

    def file_html_table_save(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, file: Gio.File=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """GIMP Table Magic.
        
        Image types: *
        Menu label: HTML table
        
        Allows you to draw an HTML table in GIMP. See help for more info.
        
        Parameters:
        
        * image - The image to save.
        
        * num_drawables (default: 1) - Number of drawables to be saved.
        
        * drawables - The drawables to save.
        
        * file - The file to save to.
        """
        pass

    def file_icns_load(self, file: Gio.File=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE) -> Gimp.Image:
        """Loads files in Apple Icon Image format.
        
        Menu label: Icns
        
        Loads Apple Icon Image files.
        
        Parameters:
        
        * file - The file to load.
        
        Returns:
        
        * image - Output image.
        """
        pass

    def file_icns_load_thumb(self, file: Gio.File=None, thumb_size: int=None) -> Tuple[Gimp.Image, int, int, Gimp.ImageType, int]:
        """Loads a preview from an Apple Icon Image file.
        
        Parameters:
        
        * file - The file to load the thumbnail from.
        
        * thumb_size (default: 256) - Preferred thumbnail size.
        
        Returns:
        
        * image - Thumbnail image.
        
        * image_width (default: 0) - Width of the full-sized image (0 for
          unknown).
        
        * image_height (default: 0) - Height of the full-sized image (0 for
          unknown).
        
        * image_type (default: <enum GIMP_RGB_IMAGE of type Gimp.ImageType>) -
          Type of the image.
        
        * num_layers (default: 1) - Number of layers in the image.
        """
        pass

    def file_icns_save(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, file: Gio.File=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Saves files in Apple Icon Image file format.
        
        Image types: *
        Menu label: Apple Icon Image
        
        Saves files in Apple Icon Image file format.
        
        Parameters:
        
        * image - The image to save.
        
        * num_drawables (default: 1) - Number of drawables to be saved.
        
        * drawables - The drawables to save.
        
        * file - The file to save to.
        """
        pass

    def file_ico_load(self, file: Gio.File=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE) -> Gimp.Image:
        """Loads files of Windows ICO file format.
        
        Menu label: Microsoft Windows icon
        
        Loads files of Windows ICO file format.
        
        Parameters:
        
        * file - The file to load.
        
        Returns:
        
        * image - Output image.
        """
        pass

    def file_ico_load_thumb(self, file: Gio.File=None, thumb_size: int=None) -> Tuple[Gimp.Image, int, int, Gimp.ImageType, int]:
        """Loads a preview from a Windows ICO or CUR files.
        
        Parameters:
        
        * file - The file to load the thumbnail from.
        
        * thumb_size (default: 256) - Preferred thumbnail size.
        
        Returns:
        
        * image - Thumbnail image.
        
        * image_width (default: 0) - Width of the full-sized image (0 for
          unknown).
        
        * image_height (default: 0) - Height of the full-sized image (0 for
          unknown).
        
        * image_type (default: <enum GIMP_RGB_IMAGE of type Gimp.ImageType>) -
          Type of the image.
        
        * num_layers (default: 1) - Number of layers in the image.
        """
        pass

    def file_ico_save(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, file: Gio.File=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Saves files in Windows ICO file format.
        
        Image types: *
        Menu label: Microsoft Windows icon
        
        Saves files in Windows ICO file format.
        
        Parameters:
        
        * image - The image to save.
        
        * num_drawables (default: 1) - Number of drawables to be saved.
        
        * drawables - The drawables to save.
        
        * file - The file to save to.
        """
        pass

    def file_iff_load(self, file: Gio.File=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE) -> Gimp.Image:
        """Load file in the IFF file format.
        
        Menu label: Amiga IFF
        
        Load file in the IFF file format.
        
        Parameters:
        
        * file - The file to load.
        
        Returns:
        
        * image - Output image.
        """
        pass

    def file_j2k_load(self, file: Gio.File=None, colorspace: int=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE) -> Gimp.Image:
        """Loads JPEG 2000 codestream.
        
        Menu label: JPEG 2000 codestream
        
        Loads JPEG 2000 codestream. If the color space is set to UNKNOWN (0), we
        will try to guess, which is only possible for few spaces (such
        as grayscale). Most such calls will fail. You are rather
        expected to know the color space of your data.
        
        Parameters:
        
        * file - The file to load.
        
        * colorspace (default: 0) - Color space { UNKNOWN (0), GRAYSCALE (1),
          RGB (2), CMYK (3), YCbCr (4), xvYCC (5) }.
        
        Returns:
        
        * image - Output image.
        """
        pass

    def file_jp2_load(self, file: Gio.File=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE) -> Gimp.Image:
        """Loads JPEG 2000 images.
        
        Menu label: JPEG 2000 image
        
        The JPEG 2000 image loader.
        
        Parameters:
        
        * file - The file to load.
        
        Returns:
        
        * image - Output image.
        """
        pass

    def file_jpeg_load(self, file: Gio.File=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE) -> Gimp.Image:
        """Loads files in the JPEG file format.
        
        Menu label: JPEG image
        
        Loads files in the JPEG file format.
        
        Parameters:
        
        * file - The file to load.
        
        Returns:
        
        * image - Output image.
        """
        pass

    def file_jpeg_load_thumb(self, file: Gio.File=None, thumb_size: int=None) -> Tuple[Gimp.Image, int, int, Gimp.ImageType, int]:
        """Loads a thumbnail from a JPEG image.
        
        Loads a thumbnail from a JPEG image, if one exists.
        
        Parameters:
        
        * file - The file to load the thumbnail from.
        
        * thumb_size (default: 256) - Preferred thumbnail size.
        
        Returns:
        
        * image - Thumbnail image.
        
        * image_width (default: 0) - Width of the full-sized image (0 for
          unknown).
        
        * image_height (default: 0) - Height of the full-sized image (0 for
          unknown).
        
        * image_type (default: <enum GIMP_RGB_IMAGE of type Gimp.ImageType>) -
          Type of the image.
        
        * num_layers (default: 1) - Number of layers in the image.
        """
        pass

    def file_jpeg_save(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, file: Gio.File=None, quality: float=None, smoothing: float=None, optimize: bool=None, progressive: bool=None, cmyk: bool=None, sub_sampling: int=None, baseline: bool=None, restart: int=None, dct: int=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Saves files in the JPEG file format.
        
        Image types: RGB*, GRAY*
        Menu label: JPEG image
        
        Saves files in the lossy, widely supported JPEG format.
        
        Parameters:
        
        * image - The image to save.
        
        * num_drawables (default: 1) - Number of drawables to be saved.
        
        * drawables - The drawables to save.
        
        * file - The file to save to.
        
        * quality (default: 0.9) - Quality of exported image.
        
        * smoothing (default: 0.0) - Smoothing factor for exported image.
        
        * optimize (default: True) - Use optimized tables during Huffman
          coding.
        
        * progressive (default: True) - Create progressive JPEG images.
        
        * cmyk (default: False) - Create a CMYK JPEG image using the
          soft-proofing color profile.
        
        * sub_sampling (default: 2) - Sub-sampling type { 0 == 4:2:0 (chroma
          quartered), 1 == 4:2:2 (chroma halved horizontally), 2 ==
          4:4:4 (best quality), 3 == 4:4:0 (chroma halved vertically).
        
        * baseline (default: True) - Force creation of a baseline JPEG
          (non-baseline JPEGs can't be read by all decoders).
        
        * restart (default: 0) - Interval of restart markers (in MCU rows, 0 =
          no restart markers).
        
        * dct (default: 0) - DCT method to use { INTEGER (0), FIXED (1), FLOAT
          (2) }.
        """
        pass

    def file_jpegxl_load(self, file: Gio.File=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE) -> Gimp.Image:
        """Loads files in the JPEG XL file format.
        
        Menu label: JPEG XL image
        
        Loads files in the JPEG XL file format.
        
        Parameters:
        
        * file - The file to load.
        
        Returns:
        
        * image - Output image.
        """
        pass

    def file_jpegxl_save(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, file: Gio.File=None, lossless: bool=None, compression: float=None, save_bit_depth: int=None, speed: int=None, uses_original_profile: bool=None, cmyk: bool=None, save_exif: bool=None, save_xmp: bool=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Saves files in the JPEG XL file format.
        
        Image types: RGB*, GRAY*
        Menu label: JPEG XL image
        
        Saves files in the JPEG XL file format.
        
        Parameters:
        
        * image - The image to save.
        
        * num_drawables (default: 1) - Number of drawables to be saved.
        
        * drawables - The drawables to save.
        
        * file - The file to save to.
        
        * lossless (default: False) - Use lossless compression.
        
        * compression (default: 1.0) - Max. butteraugli distance, lower =
          higher quality. Range: 0 .. 15. 1.0 = visually lossless.
        
        * save_bit_depth (default: 8) - Bit depth of exported image.
        
        * speed (default: 7) - Encoder effort setting.
        
        * uses_original_profile (default: False) - Store ICC profile to
          exported JXL file.
        
        * cmyk (default: False) - Create a CMYK JPEG XL image using the
          soft-proofing color profile.
        
        * save_exif (default: False) - Toggle saving Exif data.
        
        * save_xmp (default: False) - Toggle saving XMP data.
        """
        pass

    def file_load_rgbe(self, file: Gio.File=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE) -> Gimp.Image:
        """Load files in the RGBE file format.
        
        Menu label: Radiance RGBE
        
        This procedure loads images in the RGBE format, using gegl:rgbe-load.
        
        Parameters:
        
        * file - The file to load.
        
        Returns:
        
        * image - Output image.
        """
        pass

    def file_mng_save(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, file: Gio.File=None, interlaced: bool=None, png_compression: int=None, jpeg_quality: float=None, jpeg_smoothing: float=None, loop: bool=None, default_delay: int=None, default_chunks: int=None, default_dispose: int=None, bkgd: bool=None, gama: bool=None, phys: bool=None, time: bool=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Saves images in the MNG file format.
        
        Image types: *
        Menu label: MNG animation
        
        This plug-in saves images in the Multiple-image Network Graphics (MNG)
        format which can be used as a replacement for animated GIFs, and
        more.
        
        Parameters:
        
        * image - The image to save.
        
        * num_drawables (default: 1) - Number of drawables to be saved.
        
        * drawables - The drawables to save.
        
        * file - The file to save to.
        
        * interlaced (default: False) - Use interlacing.
        
        * png_compression (default: 9) - PNG compression level, choose a high
          compression level for small file size.
        
        * jpeg_quality (default: 0.75) - JPEG quality factor.
        
        * jpeg_smoothing (default: 0.0) - JPEG smoothing factor.
        
        * loop (default: True) - (ANIMATED MNG) Loop infinitely.
        
        * default_delay (default: 100) - (ANIMATED MNG) Default delay between
          frames in milliseconds.
        
        * default_chunks (default: 0) - (ANIMATED MNG) Default chunks type (0
          = PNG + Delta PNG; 1 = JNG + Delta PNG; 2 = All PNG; 3 = All
          JNG).
        
        * default_dispose (default: 0) - (ANIMATED MNG) Default dispose type
          (0 = combine; 1 = replace).
        
        * bkgd (default: False) - Write bKGd (background color) chunk.
        
        * gama (default: False) - Write gAMA (gamma) chunk.
        
        * phys (default: True) - Write pHYs (image resolution) chunk.
        
        * time (default: True) - Write tIME (creation time) chunk.
        """
        pass

    def file_openraster_load(self, file: Gio.File=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE) -> Gimp.Image:
        """Load an OpenRaster (.ora) file.
        
        Menu label: OpenRaster
        
        Load an OpenRaster (.ora) file.
        
        Parameters:
        
        * file - The file to load.
        
        Returns:
        
        * image - Output image.
        """
        pass

    def file_openraster_load_thumb(self, file: Gio.File=None, thumb_size: int=None) -> Tuple[Gimp.Image, int, int, Gimp.ImageType, int]:
        """Loads a thumbnail from an OpenRaster (.ora) file.
        
        Loads a thumbnail from an OpenRaster (.ora) file.
        
        Parameters:
        
        * file - The file to load the thumbnail from.
        
        * thumb_size (default: 256) - Preferred thumbnail size.
        
        Returns:
        
        * image - Thumbnail image.
        
        * image_width (default: 0) - Width of the full-sized image (0 for
          unknown).
        
        * image_height (default: 0) - Height of the full-sized image (0 for
          unknown).
        
        * image_type (default: <enum GIMP_RGB_IMAGE of type Gimp.ImageType>) -
          Type of the image.
        
        * num_layers (default: 1) - Number of layers in the image.
        """
        pass

    def file_openraster_save(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, file: Gio.File=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Save an OpenRaster (.ora) file.
        
        Image types: *
        Menu label: OpenRaster
        
        Save an OpenRaster (.ora) file.
        
        Parameters:
        
        * image - The image to save.
        
        * num_drawables (default: 1) - Number of drawables to be saved.
        
        * drawables - The drawables to save.
        
        * file - The file to save to.
        """
        pass

    def file_pam_save(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, file: Gio.File=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Exports files in the PAM file format.
        
        Image types: RGB*, GRAY*, INDEXED*
        Menu label: PAM image
        
        PAM export handles RGB images with or without transparency.
        
        Parameters:
        
        * image - The image to save.
        
        * num_drawables (default: 1) - Number of drawables to be saved.
        
        * drawables - The drawables to save.
        
        * file - The file to save to.
        """
        pass

    def file_pat_load(self, file: Gio.File=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE) -> Gimp.Image:
        """Loads GIMP patterns.
        
        Loads GIMP patterns.
        
        Parameters:
        
        * file - The file to load.
        
        Returns:
        
        * image - Output image.
        """
        pass

    def file_pat_save(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, file: Gio.File=None, description: str=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Exports GIMP pattern file (.PAT).
        
        Image types: *
        Menu label: GIMP pattern
        
        New GIMP patterns can be created by exporting them in the appropriate
        place with this plug-in.
        
        Parameters:
        
        * image - The image to save.
        
        * num_drawables (default: 1) - Number of drawables to be saved.
        
        * drawables - The drawables to save.
        
        * file - The file to save to.
        
        * description (default: GIMP Pattern) - Short description of the
          pattern.
        """
        pass

    def file_pat_save_internal(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, file: Gio.File=None, name: str=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Exports Gimp pattern file (.PAT).
        
        Exports Gimp pattern file (.PAT).
        
        Parameters:
        
        * image - Input image.
        
        * num_drawables (default: 1) - Number of drawables.
        
        * drawables - Selected drawables.
        
        * file - The file to export.
        
        * name (default: GIMP Pattern) - The name of the pattern.
        """
        pass

    def file_pbm_save(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, file: Gio.File=None, raw: int=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Exports files in the PBM file format.
        
        Image types: RGB, GRAY, INDEXED
        Menu label: PBM image
        
        PBM exporting produces mono images without transparency.
        
        Parameters:
        
        * image - The image to save.
        
        * num_drawables (default: 1) - Number of drawables to be saved.
        
        * drawables - The drawables to save.
        
        * file - The file to save to.
        
        * raw (default: 1) - TRUE for raw output, FALSE for ascii output.
        """
        pass

    def file_pcx_load(self, file: Gio.File=None, override_palette: int=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE) -> Gimp.Image:
        """Loads files in Zsoft PCX file format.
        
        Menu label: ZSoft PCX image
        
        FIXME: write help for pcx_load.
        
        Parameters:
        
        * file - The file to load.
        
        * override_palette (default: 0) - Use built-in palette (0) or override
          with black/white (1).
        
        Returns:
        
        * image - Output image.
        """
        pass

    def file_pcx_save(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, file: Gio.File=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Exports files in ZSoft PCX file format.
        
        Image types: INDEXED, RGB, GRAY
        Menu label: ZSoft PCX image
        
        FIXME: write help for pcx_save.
        
        Parameters:
        
        * image - The image to save.
        
        * num_drawables (default: 1) - Number of drawables to be saved.
        
        * drawables - The drawables to save.
        
        * file - The file to save to.
        """
        pass

    def file_pdf_load(self, file: Gio.File=None, password: str=None, reverse_order: bool=None, n_pages: int=None, pages: Gimp.Int32Array=None, antialias: bool=None, white_background: bool=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE) -> Gimp.Image:
        """Load file in PDF format.
        
        Menu label: Portable Document Format
        
        Loads files in Adobe's Portable Document Format. PDF is designed to be
        easily processed by a variety of different platforms, and is a
        distant cousin of PostScript.
        
        Parameters:
        
        * file - The file to load.
        
        * password - The password to decrypt the encrypted PDF file.
        
        * reverse_order (default: False) - Load PDF pages in reverse order.
        
        * n_pages (default: 0) - Number of pages to load (0 for all).
        
        * pages - The pages to load in the expected order.
        
        * antialias (default: True) - Render texts with anti-aliasing.
        
        * white_background (default: True) - Render all pages as opaque by
          filling the background in white.
        
        Returns:
        
        * image - Output image.
        """
        pass

    def file_pdf_load_thumb(self, file: Gio.File=None, thumb_size: int=None) -> Tuple[Gimp.Image, int, int, Gimp.ImageType, int]:
        """Loads a preview from a PDF file.
        
        Loads a small preview of the first page of the PDF format file. Uses the
        embedded thumbnail if present.
        
        Parameters:
        
        * file - The file to load the thumbnail from.
        
        * thumb_size (default: 256) - Preferred thumbnail size.
        
        Returns:
        
        * image - Thumbnail image.
        
        * image_width (default: 0) - Width of the full-sized image (0 for
          unknown).
        
        * image_height (default: 0) - Height of the full-sized image (0 for
          unknown).
        
        * image_type (default: <enum GIMP_RGB_IMAGE of type Gimp.ImageType>) -
          Type of the image.
        
        * num_layers (default: 1) - Number of layers in the image.
        """
        pass

    def file_pdf_save(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, file: Gio.File=None, vectorize: bool=None, ignore_hidden: bool=None, apply_masks: bool=None, layers_as_pages: bool=None, reverse_order: bool=None, root_layers_only: bool=None, convert_text_layers: bool=None, fill_background_color: bool=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Save files in PDF format.
        
        Image types: *
        Menu label: Portable Document Format
        
        Saves files in Adobe's Portable Document Format. PDF is designed to be
        easily processed by a variety of different platforms, and is a
        distant cousin of PostScript.
        
        Parameters:
        
        * image - The image to save.
        
        * num_drawables (default: 1) - Number of drawables to be saved.
        
        * drawables - The drawables to save.
        
        * file - The file to save to.
        
        * vectorize (default: True) - Convert bitmaps to vector graphics where
          possible.
        
        * ignore_hidden (default: True) - Non-visible layers will not be
          exported.
        
        * apply_masks (default: True) - Apply layer masks before saving
          (Keeping the mask will not change the output, only the PDF
          structure).
        
        * layers_as_pages (default: False) - Layers as pages (bottom layers
          first).
        
        * reverse_order (default: False) - Reverse the pages order (top layers
          first).
        
        * root_layers_only (default: True) - Only the root layers are
          considered pages.
        
        * convert_text_layers (default: False) - Convert text layers to raster
          graphics.
        
        * fill_background_color (default: True) - Fill transparent areas with
          background color if layer has an alpha channel.
        """
        pass

    def file_pdf_save_multi(self, count: int=None, images: Gimp.Int32Array=None, vectorize: bool=None, ignore_hidden: bool=None, apply_masks: bool=None, fill_background_color: bool=None, uri: str=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Save files in PDF format.
        
        Image types: *
        Menu label: _Create multipage PDF...
        
        Saves files in Adobe's Portable Document Format. PDF is designed to be
        easily processed by a variety of different platforms, and is a
        distant cousin of PostScript.
        
        Parameters:
        
        * count (default: 1) - The number of images entered (This will be the
          number of pages).
        
        * images - Input image for each page (An image can appear more than
          once).
        
        * vectorize (default: True) - Convert bitmaps to vector graphics where
          possible.
        
        * ignore_hidden (default: True) - Omit hidden layers and layers with
          zero opacity.
        
        * apply_masks (default: True) - Apply layer masks before saving
          (Keeping them will not change the output),.
        
        * fill_background_color (default: True) - Fill transparent areas with
          background color if layer has an alpha channel.
        
        * uri - The URI of the file to save to.
        """
        pass

    def file_pfm_save(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, file: Gio.File=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Exports files in the PFM file format.
        
        Image types: RGB, GRAY, INDEXED
        Menu label: PFM image
        
        PFM export handles all images without transparency.
        
        Parameters:
        
        * image - The image to save.
        
        * num_drawables (default: 1) - Number of drawables to be saved.
        
        * drawables - The drawables to save.
        
        * file - The file to save to.
        """
        pass

    def file_pgm_save(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, file: Gio.File=None, raw: int=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Exports files in the PGM file format.
        
        Image types: RGB, GRAY, INDEXED
        Menu label: PGM image
        
        PGM exporting produces grayscale images without transparency.
        
        Parameters:
        
        * image - The image to save.
        
        * num_drawables (default: 1) - Number of drawables to be saved.
        
        * drawables - The drawables to save.
        
        * file - The file to save to.
        
        * raw (default: 1) - TRUE for raw output, FALSE for ascii output.
        """
        pass

    def file_pix_load(self, file: Gio.File=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE) -> Gimp.Image:
        """Loads files of the Alias|Wavefront or Esm Software Pix file format.
        
        Menu label: Alias Pix image
        
        Loads files of the Alias|Wavefront or Esm Software Pix file format.
        
        Parameters:
        
        * file - The file to load.
        
        Returns:
        
        * image - Output image.
        """
        pass

    def file_pix_save(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, file: Gio.File=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Export file in the Alias|Wavefront pix/matte file format.
        
        Image types: *
        Menu label: Alias Pix image
        
        Export file in the Alias|Wavefront pix/matte file format.
        
        Parameters:
        
        * image - The image to save.
        
        * num_drawables (default: 1) - Number of drawables to be saved.
        
        * drawables - The drawables to save.
        
        * file - The file to save to.
        """
        pass

    def file_png_load(self, file: Gio.File=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE) -> Gimp.Image:
        """Loads files in PNG file format.
        
        Menu label: PNG image
        
        This plug-in loads Portable Network Graphics (PNG) files.
        
        Parameters:
        
        * file - The file to load.
        
        Returns:
        
        * image - Output image.
        """
        pass

    def file_png_save(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, file: Gio.File=None, interlaced: bool=None, compression: int=None, bkgd: bool=None, offs: bool=None, phys: bool=None, time: bool=None, save_transparent: bool=None, optimize_palette: bool=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Exports files in PNG file format.
        
        Image types: *
        Menu label: PNG image
        
        This plug-in exports Portable Network Graphics (PNG) files.
        
        Parameters:
        
        * image - The image to save.
        
        * num_drawables (default: 1) - Number of drawables to be saved.
        
        * drawables - The drawables to save.
        
        * file - The file to save to.
        
        * interlaced (default: False) - Use Adam7 interlacing.
        
        * compression (default: 9) - Deflate Compression factor (0..9).
        
        * bkgd (default: True) - Write bKGD chunk (PNG metadata).
        
        * offs (default: False) - Write oFFs chunk (PNG metadata).
        
        * phys (default: True) - Write pHYs chunk (PNG metadata).
        
        * time (default: True) - Write tIME chunk (PNG metadata).
        
        * save_transparent (default: False) - Preserve color of completely
          transparent pixels.
        
        * optimize_palette (default: False) - When checked, save as 1, 2, 4,
          or 8-bit depending on number of colors used. When unchecked,
          always save as 8-bit.
        """
        pass

    def file_pnm_load(self, file: Gio.File=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE) -> Gimp.Image:
        """Loads files in the PNM file format.
        
        Menu label: PNM Image
        
        This plug-in loads files in the various Netpbm portable file formats.
        
        Parameters:
        
        * file - The file to load.
        
        Returns:
        
        * image - Output image.
        """
        pass

    def file_pnm_save(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, file: Gio.File=None, raw: int=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Exports files in the PNM file format.
        
        Image types: RGB, GRAY, INDEXED
        Menu label: PNM image
        
        PNM export handles all image types without transparency.
        
        Parameters:
        
        * image - The image to save.
        
        * num_drawables (default: 1) - Number of drawables to be saved.
        
        * drawables - The drawables to save.
        
        * file - The file to save to.
        
        * raw (default: 1) - TRUE for raw output, FALSE for ascii output.
        """
        pass

    def file_ppm_save(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, file: Gio.File=None, raw: int=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Exports files in the PPM file format.
        
        Image types: RGB, GRAY, INDEXED
        Menu label: PPM image
        
        PPM export handles RGB images without transparency.
        
        Parameters:
        
        * image - The image to save.
        
        * num_drawables (default: 1) - Number of drawables to be saved.
        
        * drawables - The drawables to save.
        
        * file - The file to save to.
        
        * raw (default: 1) - TRUE for raw output, FALSE for ascii output.
        """
        pass

    def file_print_gtk(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Print the image.
        
        Image types: *
        Menu label: _Print...
        Menu path: <Image>/File/[Send]
        
        Print the image using the GTK+ Print API.
        
        Parameters:
        
        * image - The input image.
        
        * num_drawables (default: 1) - Number of input drawables.
        
        * drawables - The input drawables.
        """
        pass

    def file_print_gtk_page_setup(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Adjust page size and orientation for printing.
        
        Image types: *
        Menu label: Page Set_up...
        Menu path: <Image>/File/[Send]
        
        Adjust page size and orientation for printing the image using the GTK+
        Print API.
        
        Parameters:
        
        * image - The input image.
        
        * num_drawables (default: 1) - Number of input drawables.
        
        * drawables - The input drawables.
        """
        pass

    def file_ps_load(self, file: Gio.File=None, resolution: int=None, width: int=None, height: int=None, check_bbox: bool=None, pages: str=None, coloring: int=None, text_alpha_bits: int=None, graphoc_alpha_bits: int=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE) -> Gimp.Image:
        """Load PostScript documents.
        
        Menu label: PostScript document
        
        Load PostScript documents.
        
        Parameters:
        
        * file - The file to load.
        
        * resolution (default: 100) - Resolution to interpret image (dpi).
        
        * width (default: 826) - Desired width.
        
        * height (default: 1170) - Desired height.
        
        * check_bbox (default: True) - FALSE: Use width/height, TRUE: Use
          BoundingBox.
        
        * pages (default: 1) - Pages to load (e.g.: 1,3,5-7).
        
        * coloring (default: 6) - 4: b/w, 5: grey, 6: color image, 7:
          automatic.
        
        * text_alpha_bits (default: 1) - 1, 2 or 4.
        
        * graphoc_alpha_bits (default: 1) - 1, 2 or 4.
        
        Returns:
        
        * image - Output image.
        """
        pass

    def file_ps_load_thumb(self, file: Gio.File=None, thumb_size: int=None) -> Tuple[Gimp.Image, int, int, Gimp.ImageType, int]:
        """Loads a small preview from a PostScript or PDF document.
        
        Parameters:
        
        * file - The file to load the thumbnail from.
        
        * thumb_size (default: 256) - Preferred thumbnail size.
        
        Returns:
        
        * image - Thumbnail image.
        
        * image_width (default: 0) - Width of the full-sized image (0 for
          unknown).
        
        * image_height (default: 0) - Height of the full-sized image (0 for
          unknown).
        
        * image_type (default: <enum GIMP_RGB_IMAGE of type Gimp.ImageType>) -
          Type of the image.
        
        * num_layers (default: 1) - Number of layers in the image.
        """
        pass

    def file_ps_save(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, file: Gio.File=None, width: float=None, height: float=None, x_offset: float=None, y_offset: float=None, unit: int=None, keep_ratio: bool=None, rotation: int=None, level: bool=None, eps_flag: bool=None, show_preview: bool=None, preview: int=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Export image as PostScript document.
        
        Image types: RGB, GRAY, INDEXED
        Menu label: PostScript document
        
        PostScript exporting handles all image types except those with alpha
        channels.
        
        Parameters:
        
        * image - The image to save.
        
        * num_drawables (default: 1) - Number of drawables to be saved.
        
        * drawables - The drawables to save.
        
        * file - The file to save to.
        
        * width (default: 287.0) - Width of the image in PostScript file (0:
          use input image size).
        
        * height (default: 200.0) - Height of the image in PostScript file (0:
          use input image size).
        
        * x_offset (default: 5.0) - X-offset to image from lower left corner.
        
        * y_offset (default: 5.0) - Y-offset to image from lower left corner.
        
        * unit (default: 1) - Unit for width/height/offset. 0: inches, 1:
          millimeters.
        
        * keep_ratio (default: True) - FALSE: use width/height, TRUE: keep
          aspect ratio.
        
        * rotation (default: 0) - 0, 90, 180, 270.
        
        * level (default: True) - FALSE: PostScript Level 1, TRUE: PostScript
          Level 2.
        
        * eps_flag (default: False) - FALSE: PostScript, TRUE: Encapsulated
          PostScript.
        
        * show_preview (default: False) - Show Preview.
        
        * preview (default: 256) - 0: no preview, >0: max. size of preview.
        """
        pass

    def file_psd_load(self, file: Gio.File=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE) -> Gimp.Image:
        """Loads images from the Photoshop PSD and PSB file formats.
        
        Menu label: Photoshop image
        
        This plug-in loads images in Adobe Photoshop (TM) native PSD and PSB
        format.
        
        Parameters:
        
        * file - The file to load.
        
        Returns:
        
        * image - Output image.
        """
        pass

    def file_psd_load_merged(self, file: Gio.File=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE) -> Gimp.Image:
        """Loads images from the Photoshop PSD and PSB file formats.
        
        Menu label: Photoshop image (merged)
        
        This plug-in loads the merged image data in Adobe Photoshop (TM) native
        PSD and PSB format.
        
        Parameters:
        
        * file - The file to load.
        
        Returns:
        
        * image - Output image.
        """
        pass

    def file_psd_load_metadata(self, file: Gio.File=None, size: int=None, image: Gimp.Image=None, metadata_type: bool=None, cmyk: bool=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE) -> Gimp.Image:
        """Loads Photoshop-format metadata from other file formats.
        
        Loads Photoshop-format metadata from other file formats.
        
        Parameters:
        
        * file - The file to load.
        
        * size (default: 0) -
        
        * image - The image.
        
        * metadata_type (default: False) - If the metadata contains image or
          layer PSD resources.
        
        * cmyk (default: False) - If the layer metadata needs to be converted
          from CMYK colorspace.
        
        Returns:
        
        * image - Output image.
        """
        pass

    def file_psd_load_thumb(self, file: Gio.File=None, thumb_size: int=None) -> Tuple[Gimp.Image, int, int, Gimp.ImageType, int]:
        """Loads thumbnails from the Photoshop PSD file format.
        
        This plug-in loads thumbnail images from Adobe Photoshop (TM) native PSD
        format files.
        
        Parameters:
        
        * file - The file to load the thumbnail from.
        
        * thumb_size (default: 256) - Preferred thumbnail size.
        
        Returns:
        
        * image - Thumbnail image.
        
        * image_width (default: 0) - Width of the full-sized image (0 for
          unknown).
        
        * image_height (default: 0) - Height of the full-sized image (0 for
          unknown).
        
        * image_type (default: <enum GIMP_RGB_IMAGE of type Gimp.ImageType>) -
          Type of the image.
        
        * num_layers (default: 1) - Number of layers in the image.
        """
        pass

    def file_psd_save(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, file: Gio.File=None, clippingpath: bool=None, clippingpathname: str=None, clippingpathflatness: float=None, cmyk: bool=None, duotone: bool=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Saves files in the Photoshop(tm) PSD file format.
        
        Image types: *
        Menu label: Photoshop image
        
        This filter saves files of Adobe Photoshop(tm) native PSD format. These
        files may be of any image type supported by GIMP, with or
        without layers, layer masks, aux channels and guides.
        
        Parameters:
        
        * image - The image to save.
        
        * num_drawables (default: 1) - Number of drawables to be saved.
        
        * drawables - The drawables to save.
        
        * file - The file to save to.
        
        * clippingpath (default: False) - Select a path to be the clipping
          path.
        
        * clippingpathname - Clipping path name (ignored if no clipping path).
        
        * clippingpathflatness (default: 0.2) - Clipping path flatness in
          device pixels (ignored if no clipping path).
        
        * cmyk (default: False) - Export a CMYK PSD image using the
          soft-proofing color profile.
        
        * duotone (default: False) - Export as a Duotone PSD file if Duotone
          color space information was attached to the image when
          originally imported.
        """
        pass

    def file_psp_load(self, file: Gio.File=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE) -> Gimp.Image:
        """Loads images from the Paint Shop Pro PSP file format.
        
        Menu label: Paint Shop Pro image
        
        This plug-in loads and exports images in Paint Shop Pro's native PSP
        format. Vector layers aren't handled. Exporting isn't yet
        implemented.
        
        Parameters:
        
        * file - The file to load.
        
        Returns:
        
        * image - Output image.
        """
        pass

    def file_qoi_load(self, file: Gio.File=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE) -> Gimp.Image:
        """Load file in the QOI file format.
        
        Menu label: Quite OK Image
        
        Load file in the QOI file format (Quite OK Image).
        
        Parameters:
        
        * file - The file to load.
        
        Returns:
        
        * image - Output image.
        """
        pass

    def file_qoi_save(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, file: Gio.File=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Export image in the QOI file format.
        
        Image types: *
        Menu label: Quite OK Image
        
        Export image in the QOI file format (Quite OK Image).
        
        Parameters:
        
        * image - The image to save.
        
        * num_drawables (default: 1) - Number of drawables to be saved.
        
        * drawables - The drawables to save.
        
        * file - The file to save to.
        """
        pass

    def file_raw_load(self, file: Gio.File=None, width: int=None, height: int=None, offset: int=None, pixel_format: int=None, data_type: int=None, endianness: int=None, planar_configuration: int=None, palette_offset: int=None, palette_type: int=None, palette_file: Gio.File=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE) -> Gimp.Image:
        """Load raw images, specifying image information.
        
        Menu label: Raw image data
        
        Load raw images, specifying image information.
        
        Parameters:
        
        * file - The file to load.
        
        * width (default: 350) - Image width in number of pixels.
        
        * height (default: 350) - Image height in number of pixels.
        
        * offset (default: 0) - Offset to beginning of image in raw data.
        
        * pixel_format (default: 0) - The layout of pixel data, such as
          components and their order.
        
        * data_type (default: 0) - Data type used to represent pixel values {
          RAW_ENCODING_UNSIGNED (0), RAW_ENCODING_SIGNED (1),
          RAW_ENCODING_FLOAT (2) }.
        
        * endianness (default: 0) - Order of sequences of bytes {
          RAW_LITTLE_ENDIAN (0), RAW_BIG_ENDIAN (1) }.
        
        * planar_configuration (default: 0) - How color pixel data are stored
          { RAW_PLANAR_CONTIGUOUS (0), RAW_PLANAR_SEPARATE (1) }.
        
        * palette_offset (default: 0) - Offset to beginning of data in the
          palette file.
        
        * palette_type (default: 0) - The layout for the palette's color
          channels { RAW_PALETTE_RGB (0), RAW_PALETTE_BGR (1) }.
        
        * palette_file - The file containing palette data.
        
        Returns:
        
        * image - Output image.
        """
        pass

    def file_raw_placeholder_ari_load(self, file: Gio.File=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE) -> Gimp.Image:
        """Load files in the ARI raw format via placeholder.
        
        This plug-in loads files in Arriflex' raw ARI format by calling
        placeholder.
        
        Parameters:
        
        * file - The file to load.
        
        Returns:
        
        * image - Output image.
        """
        pass

    def file_raw_placeholder_bay_load(self, file: Gio.File=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE) -> Gimp.Image:
        """Load files in the BAY raw format via placeholder.
        
        This plug-in loads files in Casio's raw BAY format by calling
        placeholder.
        
        Parameters:
        
        * file - The file to load.
        
        Returns:
        
        * image - Output image.
        """
        pass

    def file_raw_placeholder_canon_load(self, file: Gio.File=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE) -> Gimp.Image:
        """Load files in the Canon raw formats via placeholder.
        
        This plug-in loads files in Canon's raw formats by calling placeholder.
        
        Parameters:
        
        * file - The file to load.
        
        Returns:
        
        * image - Output image.
        """
        pass

    def file_raw_placeholder_cine_load(self, file: Gio.File=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE) -> Gimp.Image:
        """Load files in the CINE raw format via placeholder.
        
        This plug-in loads files in Phantom Software's raw CINE format by
        calling placeholder.
        
        Parameters:
        
        * file - The file to load.
        
        Returns:
        
        * image - Output image.
        """
        pass

    def file_raw_placeholder_dng_load(self, file: Gio.File=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE) -> Gimp.Image:
        """Load files in the DNG raw format via placeholder.
        
        This plug-in loads files in the Adobe Digital Negative DNG format by
        calling placeholder.
        
        Parameters:
        
        * file - The file to load.
        
        Returns:
        
        * image - Output image.
        """
        pass

    def file_raw_placeholder_erf_load(self, file: Gio.File=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE) -> Gimp.Image:
        """Load files in the ERF raw format via placeholder.
        
        This plug-in loads files in Epson's raw ERF format by calling
        placeholder.
        
        Parameters:
        
        * file - The file to load.
        
        Returns:
        
        * image - Output image.
        """
        pass

    def file_raw_placeholder_hasselblad_load(self, file: Gio.File=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE) -> Gimp.Image:
        """Load files in the Hasselblad raw formats via placeholder.
        
        This plug-in loads files in Hasselblad's raw formats by calling
        placeholder.
        
        Parameters:
        
        * file - The file to load.
        
        Returns:
        
        * image - Output image.
        """
        pass

    def file_raw_placeholder_kodak_load(self, file: Gio.File=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE) -> Gimp.Image:
        """Load files in the Kodak raw formats via placeholder.
        
        This plug-in loads files in Kodak's raw formats by calling placeholder.
        
        Parameters:
        
        * file - The file to load.
        
        Returns:
        
        * image - Output image.
        """
        pass

    def file_raw_placeholder_mef_load(self, file: Gio.File=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE) -> Gimp.Image:
        """Load files in the MEF raw format via placeholder.
        
        This plug-in loads files in Mamiya's raw MEF format by calling
        placeholder.
        
        Parameters:
        
        * file - The file to load.
        
        Returns:
        
        * image - Output image.
        """
        pass

    def file_raw_placeholder_minolta_load(self, file: Gio.File=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE) -> Gimp.Image:
        """Load files in the Minolta raw formats via placeholder.
        
        This plug-in loads files in Minolta's raw formats by calling
        placeholder.
        
        Parameters:
        
        * file - The file to load.
        
        Returns:
        
        * image - Output image.
        """
        pass

    def file_raw_placeholder_mos_load(self, file: Gio.File=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE) -> Gimp.Image:
        """Load files in the MOS raw format via placeholder.
        
        This plug-in loads files in Leaf's raw MOS format by calling
        placeholder.
        
        Parameters:
        
        * file - The file to load.
        
        Returns:
        
        * image - Output image.
        """
        pass

    def file_raw_placeholder_nikon_load(self, file: Gio.File=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE) -> Gimp.Image:
        """Load files in the Nikon raw formats via placeholder.
        
        This plug-in loads files in Nikon's raw formats by calling placeholder.
        
        Parameters:
        
        * file - The file to load.
        
        Returns:
        
        * image - Output image.
        """
        pass

    def file_raw_placeholder_orf_load(self, file: Gio.File=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE) -> Gimp.Image:
        """Load files in the ORF raw format via placeholder.
        
        This plug-in loads files in Olympus' raw ORF format by calling
        placeholder.
        
        Parameters:
        
        * file - The file to load.
        
        Returns:
        
        * image - Output image.
        """
        pass

    def file_raw_placeholder_panasonic_load(self, file: Gio.File=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE) -> Gimp.Image:
        """Load files in the Panasonic raw formats via placeholder.
        
        This plug-in loads files in Panasonic's raw formats by calling
        placeholder.
        
        Parameters:
        
        * file - The file to load.
        
        Returns:
        
        * image - Output image.
        """
        pass

    def file_raw_placeholder_pef_load(self, file: Gio.File=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE) -> Gimp.Image:
        """Load files in the PEF raw format via placeholder.
        
        This plug-in loads files in Pentax' raw PEF format by calling
        placeholder.
        
        Parameters:
        
        * file - The file to load.
        
        Returns:
        
        * image - Output image.
        """
        pass

    def file_raw_placeholder_phaseone_load(self, file: Gio.File=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE) -> Gimp.Image:
        """Load files in the Phase One raw formats via placeholder.
        
        This plug-in loads files in Phase One's raw formats by calling
        placeholder.
        
        Parameters:
        
        * file - The file to load.
        
        Returns:
        
        * image - Output image.
        """
        pass

    def file_raw_placeholder_pxn_load(self, file: Gio.File=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE) -> Gimp.Image:
        """Load files in the PXN raw format via placeholder.
        
        This plug-in loads files in Logitech's raw PXN format by calling
        placeholder.
        
        Parameters:
        
        * file - The file to load.
        
        Returns:
        
        * image - Output image.
        """
        pass

    def file_raw_placeholder_qtk_load(self, file: Gio.File=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE) -> Gimp.Image:
        """Load files in the QTK raw format via placeholder.
        
        This plug-in loads files in Apple's QuickTake QTK raw format by calling
        placeholder.
        
        Parameters:
        
        * file - The file to load.
        
        Returns:
        
        * image - Output image.
        """
        pass

    def file_raw_placeholder_raf_load(self, file: Gio.File=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE) -> Gimp.Image:
        """Load files in the RAF raw format via placeholder.
        
        This plug-in loads files in Fujifilm's raw RAF format by calling
        placeholder.
        
        Parameters:
        
        * file - The file to load.
        
        Returns:
        
        * image - Output image.
        """
        pass

    def file_raw_placeholder_rdc_load(self, file: Gio.File=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE) -> Gimp.Image:
        """Load files in the RDC raw format via placeholder.
        
        This plug-in loads files in Digital Foto Maker's raw RDC format by
        calling placeholder.
        
        Parameters:
        
        * file - The file to load.
        
        Returns:
        
        * image - Output image.
        """
        pass

    def file_raw_placeholder_rwl_load(self, file: Gio.File=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE) -> Gimp.Image:
        """Load files in the RWL raw format via placeholder.
        
        This plug-in loads files in Leica's raw RWL format by calling
        placeholder.
        
        Parameters:
        
        * file - The file to load.
        
        Returns:
        
        * image - Output image.
        """
        pass

    def file_raw_placeholder_sinar_load(self, file: Gio.File=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE) -> Gimp.Image:
        """Load files in the Sinar raw formats via placeholder.
        
        This plug-in loads files in Sinar's raw formats by calling placeholder.
        
        Parameters:
        
        * file - The file to load.
        
        Returns:
        
        * image - Output image.
        """
        pass

    def file_raw_placeholder_sony_load(self, file: Gio.File=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE) -> Gimp.Image:
        """Load files in the Sony raw formats via placeholder.
        
        This plug-in loads files in Sony's raw formats by calling placeholder.
        
        Parameters:
        
        * file - The file to load.
        
        Returns:
        
        * image - Output image.
        """
        pass

    def file_raw_placeholder_srw_load(self, file: Gio.File=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE) -> Gimp.Image:
        """Load files in the SRW raw format via placeholder.
        
        This plug-in loads files in Samsung's raw SRW format by calling
        placeholder.
        
        Parameters:
        
        * file - The file to load.
        
        Returns:
        
        * image - Output image.
        """
        pass

    def file_raw_placeholder_x3f_load(self, file: Gio.File=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE) -> Gimp.Image:
        """Load files in the X3F raw format via placeholder.
        
        This plug-in loads files in Sigma's raw X3F format by calling
        placeholder.
        
        Parameters:
        
        * file - The file to load.
        
        Returns:
        
        * image - Output image.
        """
        pass

    def file_raw_save(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, file: Gio.File=None, planar_configuration: int=None, palette_type: int=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Dump images to disk in raw format.
        
        Image types: INDEXED, GRAY, RGB, RGBA
        Menu label: Raw image data
        
        Dump images to disk in raw format.
        
        Parameters:
        
        * image - The image to save.
        
        * num_drawables (default: 1) - Number of drawables to be saved.
        
        * drawables - The drawables to save.
        
        * file - The file to save to.
        
        * planar_configuration (default: 0) - How color pixel data are stored
          { RAW_PLANAR_CONTIGUOUS (0), RAW_PLANAR_SEPARATE (1) }.
        
        * palette_type (default: 0) - The layout for the palette's color
          channels { RAW_PALETTE_RGB (0), RAW_PALETTE_BGR (1) }.
        """
        pass

    def file_save_rgbe(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, file: Gio.File=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Saves files in the RGBE file format.
        
        Image types: *
        Menu label: Radiance RGBE
        
        This procedure exports images in the RGBE format, using gegl:rgbe-save.
        
        Parameters:
        
        * image - The image to save.
        
        * num_drawables (default: 1) - Number of drawables to be saved.
        
        * drawables - The drawables to save.
        
        * file - The file to save to.
        """
        pass

    def file_sgi_load(self, file: Gio.File=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE) -> Gimp.Image:
        """Loads files in SGI image file format.
        
        Menu label: Silicon Graphics IRIS image
        
        This plug-in loads SGI image files.
        
        Parameters:
        
        * file - The file to load.
        
        Returns:
        
        * image - Output image.
        """
        pass

    def file_sgi_save(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, file: Gio.File=None, compression: int=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Exports files in SGI image file format.
        
        Image types: *
        Menu label: Silicon Graphics IRIS image
        
        This plug-in exports SGI image files.
        
        Parameters:
        
        * image - The image to save.
        
        * num_drawables (default: 1) - Number of drawables to be saved.
        
        * drawables - The drawables to save.
        
        * file - The file to save to.
        
        * compression (default: 1) - Compression level (0 = none, 1 = RLE, 2 =
          ARLE).
        """
        pass

    def file_sunras_load(self, file: Gio.File=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE) -> Gimp.Image:
        """Load file of the SunRaster file format.
        
        Menu label: SUN Rasterfile image
        
        Load file of the SunRaster file format.
        
        Parameters:
        
        * file - The file to load.
        
        Returns:
        
        * image - Output image.
        """
        pass

    def file_sunras_save(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, file: Gio.File=None, rle: int=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Export file in the SunRaster file format.
        
        Image types: RGB, GRAY, INDEXED
        Menu label: SUN Rasterfile image
        
        SUNRAS exporting handles all image types except those with alpha
        channels.
        
        Parameters:
        
        * image - The image to save.
        
        * num_drawables (default: 1) - Number of drawables to be saved.
        
        * drawables - The drawables to save.
        
        * file - The file to save to.
        
        * rle (default: 1) - Use standard (0) or Run-Length Encoded (1)
          output.
        """
        pass

    def file_svg_load(self, file: Gio.File=None, resolution: float=None, width: int=None, height: int=None, paths: str=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE) -> Gimp.Image:
        """Loads files in the SVG file format.
        
        Menu label: SVG image
        
        Renders SVG files to raster graphics using librsvg.
        
        Parameters:
        
        * file - The file to load.
        
        * resolution (default: 300.0) - Resolution to use for rendering the
          SVG.
        
        * width (default: 0) - Width (in pixels) to load the SVG in. (0 for
          original width, a negative width to specify a maximum
          width).
        
        * height (default: 0) - Height (in pixels) to load the SVG in. (0 for
          original height, a negative height to specify a maximum
          height).
        
        * paths - Whether and how to import paths so that they can be used
          with the path tool.
        
        Returns:
        
        * image - Output image.
        """
        pass

    def file_svg_load_thumb(self, file: Gio.File=None, thumb_size: int=None) -> Tuple[Gimp.Image, int, int, Gimp.ImageType, int]:
        """Generates a thumbnail of an SVG image.
        
        Renders a thumbnail of an SVG file using librsvg.
        
        Parameters:
        
        * file - The file to load the thumbnail from.
        
        * thumb_size (default: 256) - Preferred thumbnail size.
        
        Returns:
        
        * image - Thumbnail image.
        
        * image_width (default: 0) - Width of the full-sized image (0 for
          unknown).
        
        * image_height (default: 0) - Height of the full-sized image (0 for
          unknown).
        
        * image_type (default: <enum GIMP_RGB_IMAGE of type Gimp.ImageType>) -
          Type of the image.
        
        * num_layers (default: 1) - Number of layers in the image.
        """
        pass

    def file_tga_load(self, file: Gio.File=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE) -> Gimp.Image:
        """Loads files of Targa file format.
        
        Menu label: TarGA image
        
        FIXME: write help for tga_load.
        
        Parameters:
        
        * file - The file to load.
        
        Returns:
        
        * image - Output image.
        """
        pass

    def file_tga_save(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, file: Gio.File=None, rle: bool=None, origin: int=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Exports files in the Targa file format.
        
        Image types: *
        Menu label: TarGA image
        
        FIXME: write help for tga_save.
        
        Parameters:
        
        * image - The image to save.
        
        * num_drawables (default: 1) - Number of drawables to be saved.
        
        * drawables - The drawables to save.
        
        * file - The file to save to.
        
        * rle (default: True) - Use RLE compression.
        
        * origin (default: 1) - Image origin (0 = top-left, 1 = bottom-left).
        """
        pass

    def file_tiff_load(self, file: Gio.File=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE) -> Gimp.Image:
        """Loads files of the TIFF and BigTIFF file formats.
        
        Menu label: TIFF or BigTIFF image
        
        Loads files of the Tag Image File Format (TIFF) and its 64-bit offsets
        variant (BigTIFF).
        
        Parameters:
        
        * file - The file to load.
        
        Returns:
        
        * image - Output image.
        """
        pass

    def file_tiff_save(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, file: Gio.File=None, bigtiff: bool=None, compression: str=None, save_transparent_pixels: bool=None, cmyk: bool=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Exports files in the TIFF or BigTIFF file formats.
        
        Image types: *
        Menu label: TIFF or BigTIFF image
        
        Exports files in the Tag Image File Format (TIFF) or its 64-bit offsets
        variant (BigTIFF) able to support much bigger file sizes.
        
        Parameters:
        
        * image - The image to save.
        
        * num_drawables (default: 1) - Number of drawables to be saved.
        
        * drawables - The drawables to save.
        
        * file - The file to save to.
        
        * bigtiff (default: False) - The BigTIFF variant file format uses
          64-bit offsets, hence supporting over 4GiB files and bigger.
        
        * compression - Compression type.
        
        * save_transparent_pixels (default: True) - Keep the color data masked
          by an alpha channel intact (do not store premultiplied
          components).
        
        * cmyk (default: False) - Create a CMYK TIFF image using the
          soft-proofing color profile.
        """
        pass

    def file_wbmp_load(self, file: Gio.File=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE) -> Gimp.Image:
        """Loads files of Wireless BMP file format.
        
        Menu label: Wireless BMP image
        
        Loads files of Wireless BMP file format.
        
        Parameters:
        
        * file - The file to load.
        
        Returns:
        
        * image - Output image.
        """
        pass

    def file_webp_load(self, file: Gio.File=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE) -> Gimp.Image:
        """Loads images in the WebP file format.
        
        Menu label: WebP image
        
        Loads images in the WebP file format.
        
        Parameters:
        
        * file - The file to load.
        
        Returns:
        
        * image - Output image.
        """
        pass

    def file_webp_save(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, file: Gio.File=None, preset: int=None, lossless: bool=None, quality: float=None, alpha_quality: float=None, use_sharp_yuv: bool=None, animation_loop: bool=None, minimize_size: bool=None, keyframe_distance: int=None, default_delay: int=None, force_delay: bool=None, animation: bool=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Saves files in the WebP image format.
        
        Image types: *
        Menu label: WebP image
        
        Saves files in the WebP image format.
        
        Parameters:
        
        * image - The image to save.
        
        * num_drawables (default: 1) - Number of drawables to be saved.
        
        * drawables - The drawables to save.
        
        * file - The file to save to.
        
        * preset (default: 0) - WebP encoder preset (Default=0, Picture=1,
          Photo=2, Drawing=3, Icon=4, Text=5).
        
        * lossless (default: False) - Use lossless encoding.
        
        * quality (default: 90.0) - Quality of the image.
        
        * alpha_quality (default: 100.0) - Quality of the image's alpha
          channel.
        
        * use_sharp_yuv (default: False) - Use sharper (but slower) RGB→YUV
          conversion.
        
        * animation_loop (default: True) - Loop animation infinitely.
        
        * minimize_size (default: True) - Minimize output file size.
        
        * keyframe_distance (default: 50) - Maximum distance between
          keyframes.
        
        * default_delay (default: 200) - Default delay (in milliseconds) to
          use when timestamps for frames are not available or forced.
        
        * force_delay (default: False) - Force default delay on all frames.
        
        * animation (default: False) - Use layers for animation.
        """
        pass

    def file_wmf_load(self, file: Gio.File=None, resolution: float=None, width: int=None, height: int=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE) -> Gimp.Image:
        """Loads files in the WMF file format.
        
        Menu label: Microsoft WMF file
        
        Loads files in the WMF file format.
        
        Parameters:
        
        * file - The file to load.
        
        * resolution (default: 300.0) - Resolution to use for rendering the
          WMF.
        
        * width (default: 0) - Width (in pixels) to load the WMF in, 0 for
          original width.
        
        * height (default: 0) - Height (in pixels) to load the WMF in, 0 for
          original height.
        
        Returns:
        
        * image - Output image.
        """
        pass

    def file_wmf_load_thumb(self, file: Gio.File=None, thumb_size: int=None) -> Tuple[Gimp.Image, int, int, Gimp.ImageType, int]:
        """Loads a small preview from a WMF image.
        
        Parameters:
        
        * file - The file to load the thumbnail from.
        
        * thumb_size (default: 256) - Preferred thumbnail size.
        
        Returns:
        
        * image - Thumbnail image.
        
        * image_width (default: 0) - Width of the full-sized image (0 for
          unknown).
        
        * image_height (default: 0) - Height of the full-sized image (0 for
          unknown).
        
        * image_type (default: <enum GIMP_RGB_IMAGE of type Gimp.ImageType>) -
          Type of the image.
        
        * num_layers (default: 1) - Number of layers in the image.
        """
        pass

    def file_xbm_load(self, file: Gio.File=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE) -> Gimp.Image:
        """Load a file in X10 or X11 bitmap (XBM) file format.
        
        Menu label: X BitMap image
        
        Load a file in X10 or X11 bitmap (XBM) file format. XBM is a lossless
        format for flat black-and-white (two color indexed) images.
        
        Parameters:
        
        * file - The file to load.
        
        Returns:
        
        * image - Output image.
        """
        pass

    def file_xbm_save(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, file: Gio.File=None, save_comment: bool=None, gimp_comment: str=None, x10_format: bool=None, use_hot_spot: bool=None, hot_spot_x: int=None, hot_spot_y: int=None, prefix: str=None, write_mask: bool=None, mask_suffix: str=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Export a file in X10 or X11 bitmap (XBM) file format.
        
        Image types: INDEXED
        Menu label: X BitMap image
        
        X10 or X11 bitmap (XBM) file format. XBM is a lossless format for flat
        black-and-white (two color indexed) images.
        
        Parameters:
        
        * image - The image to save.
        
        * num_drawables (default: 1) - Number of drawables to be saved.
        
        * drawables - The drawables to save.
        
        * file - The file to save to.
        
        * save_comment (default: False) - Write a comment at the beginning of
          the file.
        
        * gimp_comment (default: Created with GIMP) - Image description
          (maximum 72 bytes).
        
        * x10_format (default: False) - Export in X10 format.
        
        * use_hot_spot (default: False) - Write hotspot information.
        
        * hot_spot_x (default: 0) - X coordinate of hotspot.
        
        * hot_spot_y (default: 0) - Y coordinate of hotspot.
        
        * prefix (default: bitmap) - Identifier prefix [determined from
          filename].
        
        * write_mask (default: False) - Write extra mask file.
        
        * mask_suffix (default: -mask) - Suffix of the mask file.
        """
        pass

    def file_xpm_load(self, file: Gio.File=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE) -> Gimp.Image:
        """Load files in XPM (X11 Pixmap) format.
        
        Menu label: X PixMap image
        
        Load files in XPM (X11 Pixmap) format. XPM is a portable image format
        designed to be included in C source code. XLib provides utility
        functions to read this format. Newer code should however be
        using gdk-pixbuf-csource instead. XPM supports colored images,
        unlike the XBM format which XPM was designed to replace.
        
        Parameters:
        
        * file - The file to load.
        
        Returns:
        
        * image - Output image.
        """
        pass

    def file_xpm_save(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, file: Gio.File=None, threshold: int=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Export files in XPM (X11 Pixmap) format.
        
        Image types: *
        Menu label: X PixMap image
        
        Export files in XPM (X11 Pixmap) format. XPM is a portable image format
        designed to be included in C source code. XLib provides utility
        functions to read this format. Newer code should however be
        using gdk-pixbuf-csource instead. XPM supports colored images,
        unlike the XBM format which XPM was designed to replace.
        
        Parameters:
        
        * image - The image to save.
        
        * num_drawables (default: 1) - Number of drawables to be saved.
        
        * drawables - The drawables to save.
        
        * file - The file to save to.
        
        * threshold (default: 127) - Alpha threshold.
        """
        pass

    def file_xwd_load(self, file: Gio.File=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE) -> Gimp.Image:
        """Loads files in the XWD (X Window Dump) format.
        
        Menu label: X window dump
        
        Loads files in the XWD (X Window Dump) format. XWD image files are
        produced by the program xwd. Xwd is an X Window System window
        dumping utility.
        
        Parameters:
        
        * file - The file to load.
        
        Returns:
        
        * image - Output image.
        """
        pass

    def file_xwd_save(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, file: Gio.File=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Exports files in the XWD (X Window Dump) format.
        
        Image types: RGB, GRAY, INDEXED
        Menu label: X window dump
        
        XWD exporting handles all image types except those with alpha channels.
        
        Parameters:
        
        * image - The image to save.
        
        * num_drawables (default: 1) - Number of drawables to be saved.
        
        * drawables - The drawables to save.
        
        * file - The file to save to.
        """
        pass

    def file_xz_load(self, file: Gio.File=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE) -> Gimp.Image:
        """Loads files compressed with xz.
        
        Menu label: xz archive
        
        This procedure loads files in the xz compressed format.
        
        Parameters:
        
        * file - The file to load.
        
        Returns:
        
        * image - Output image.
        """
        pass

    def file_xz_save(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, file: Gio.File=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Saves files compressed with xz.
        
        Image types: RGB*, GRAY*, INDEXED*
        Menu label: xz archive
        
        This procedure saves files in the xz compressed format.
        
        Parameters:
        
        * image - The image to save.
        
        * num_drawables (default: 1) - Number of drawables to be saved.
        
        * drawables - The drawables to save.
        
        * file - The file to save to.
        """
        pass

    def generate_pdb_stubs(self, output_dirpath: str=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Generates a stub file for the GIMP procedural database (PDB) for
        Python plug-ins named "pypdb.pyi".
        
        Menu label: Generate GIMP PDB Stubs for Python
        Menu path: <Image>/Filters/Development/Python-Fu
        
        The "pypdb.py" file provides a convenience wrapper to simplify calls to
        GIMP PDB procedures from Python plug-ins. The generated
        "pypdb.pyi" stub file can then be used in integrated development
        environments (IDEs) to display code completion suggestions for
        GIMP PDB procedures.
        
        Parameters:
        
        * output_dirpath (default: C:\\Users\\Joshua
          Breckeen\\AppData\\Roaming\\GIMP\\2.99\\plug-ins\\generate-pdb-stu
          bs) - Output directory path (default: "C:\\Users\\Joshua Breck
          een\\AppData\\Roaming\\GIMP\\2.99\\plug-ins\\generate-pdb-stubs").
        """
        pass

    def gimp_airbrush(self, drawable: Gimp.Drawable=None, pressure: float=None, num_strokes: int=None, strokes: Gimp.FloatArray=None):
        """Paint in the current brush with varying pressure. Paint application
        is time-dependent.
        
        This tool simulates the use of an airbrush. Paint pressure represents
        the relative intensity of the paint application. High pressure
        results in a thicker layer of paint while low pressure results
        in a thinner layer.
        
        Parameters:
        
        * drawable - The affected drawable.
        
        * pressure (default: 0.0) - The pressure of the airbrush strokes.
        
        * num_strokes (default: 2) - Number of stroke control points (count
          each coordinate as 2 points).
        
        * strokes - Array of stroke coordinates: { s1.x, s1.y, s2.x, s2.y,
          ..., sn.x, sn.y }.
        """
        pass

    def gimp_airbrush_default(self, drawable: Gimp.Drawable=None, num_strokes: int=None, strokes: Gimp.FloatArray=None):
        """Paint in the current brush with varying pressure. Paint application
        is time-dependent.
        
        This tool simulates the use of an airbrush. It is similar to
        'gimp-airbrush' except that the pressure is derived from the
        airbrush tools options box. It the option has not been set the
        default for the option will be used.
        
        Parameters:
        
        * drawable - The affected drawable.
        
        * num_strokes (default: 2) - Number of stroke control points (count
          each coordinate as 2 points).
        
        * strokes - Array of stroke coordinates: { s1.x, s1.y, s2.x, s2.y,
          ..., sn.x, sn.y }.
        """
        pass

    def gimp_attach_parasite(self, parasite: Gimp.Parasite=None):
        """Add a global parasite.
        
        This procedure attaches a global parasite. It has no return values.
        
        Parameters:
        
        * parasite - The parasite to attach.
        """
        pass

    def gimp_brush_get_angle(self, brush: Gimp.Brush=None) -> float:
        """Gets the rotation angle of a generated brush.
        
        Gets the angle of rotation for a generated brush. Returns an error when
        called for a non-parametric brush.
        
        Parameters:
        
        * brush - The brush.
        
        Returns:
        
        * angle (default: 0.0) - The rotation angle of the brush in degree.
        """
        pass

    def gimp_brush_get_aspect_ratio(self, brush: Gimp.Brush=None) -> float:
        """Gets the aspect ratio of a generated brush.
        
        Gets the aspect ratio of a generated brush. Returns an error when called
        for a non-parametric brush. The aspect ratio is a float between
        0.0 and 1000.0.
        
        Parameters:
        
        * brush - The brush.
        
        Returns:
        
        * aspect_ratio (default: 0.0) - The aspect ratio of the brush.
        """
        pass

    def gimp_brush_get_by_name(self, name: str=None) -> Gimp.Brush:
        """Returns the brush with the given name.
        
        Search and return an existing brush with the name in argument, or
        nothing if no brush has this name.
        
        Parameters:
        
        * name - The name of the brush.
        
        Returns:
        
        * brush - The brush.
        """
        pass

    def gimp_brush_get_hardness(self, brush: Gimp.Brush=None) -> float:
        """Gets the hardness of a generated brush.
        
        Gets the hardness of a generated brush. The hardness of a brush is the
        amount its intensity fades at the outside edge, as a float
        between 0.0 and 1.0. Returns an error when called for a
        non-parametric brush.
        
        Parameters:
        
        * brush - The brush.
        
        Returns:
        
        * hardness (default: 0.0) - The hardness of the brush.
        """
        pass

    def gimp_brush_get_info(self, brush: Gimp.Brush=None) -> Tuple[int, int, int, int]:
        """Gets information about the brush.
        
        Gets information about the brush: brush extents (width and height),
        color depth and mask depth (bpp). The color bpp is zero when the
        brush is parametric versus raster.
        
        Parameters:
        
        * brush - The brush.
        
        Returns:
        
        * width (default: 0) - The brush width.
        
        * height (default: 0) - The brush height.
        
        * mask_bpp (default: 0) - The brush mask bpp.
        
        * color_bpp (default: 0) - The brush color bpp.
        """
        pass

    def gimp_brush_get_pixels(self, brush: Gimp.Brush=None) -> Tuple[int, int, int, GLib.Bytes, int, GLib.Bytes]:
        """Gets information about the brush.
        
        Gets information about the brush: the brush extents (width and height)
        and its pixels data. The color bpp is zero and pixels empty when
        the brush is parametric versus raster.
        
        Parameters:
        
        * brush - The brush.
        
        Returns:
        
        * width (default: 0) - The brush width.
        
        * height (default: 0) - The brush height.
        
        * mask_bpp (default: 0) - The brush mask bpp.
        
        * mask_bytes - The brush mask data.
        
        * color_bpp (default: 0) - The brush color bpp.
        
        * color_bytes - The brush color data.
        """
        pass

    def gimp_brush_get_radius(self, brush: Gimp.Brush=None) -> float:
        """Gets the radius of a generated brush.
        
        Gets the radius of a generated brush. Returns an error when called for a
        non-parametric brush.
        
        Parameters:
        
        * brush - The brush.
        
        Returns:
        
        * radius (default: 0.0) - The radius of the brush in pixels.
        """
        pass

    def gimp_brush_get_shape(self, brush: Gimp.Brush=None) -> Gimp.BrushGeneratedShape:
        """Gets the shape of a generated brush.
        
        Gets the shape of a generated brush. Returns an error when called for a
        non-parametric brush. The choices for shape are Circle
        (GIMP_BRUSH_GENERATED_CIRCLE), Square
        (GIMP_BRUSH_GENERATED_SQUARE), and Diamond
        (GIMP_BRUSH_GENERATED_DIAMOND). Other shapes might be added in
        the future.
        
        Parameters:
        
        * brush - The brush.
        
        Returns:
        
        * shape (default: <enum GIMP_BRUSH_GENERATED_CIRCLE of type
          Gimp.BrushGeneratedShape>) - The brush shape.
        """
        pass

    def gimp_brush_get_spacing(self, brush: Gimp.Brush=None) -> int:
        """Gets the brush spacing, the stamping frequency.
        
        Returns the spacing setting for the brush. Spacing is an integer between
        0 and 1000 which represents a percentage of the maximum of the
        width and height of the mask. Both parametric and raster brushes
        have a spacing.
        
        Parameters:
        
        * brush - The brush.
        
        Returns:
        
        * spacing (default: 0) - The brush spacing.
        """
        pass

    def gimp_brush_get_spikes(self, brush: Gimp.Brush=None) -> int:
        """Gets the number of spikes for a generated brush.
        
        Gets the number of spikes for a generated brush. Returns an error when
        called for a non-parametric brush.
        
        Parameters:
        
        * brush - The brush.
        
        Returns:
        
        * spikes (default: 0) - The number of spikes on the brush.
        """
        pass

    def gimp_brush_is_generated(self, brush: Gimp.Brush=None) -> bool:
        """Whether the brush is generated (parametric versus raster).
        
        Returns TRUE when brush is parametric.
        
        Parameters:
        
        * brush - The brush.
        
        Returns:
        
        * generated (default: False) - TRUE if the brush is generated.
        """
        pass

    def gimp_brush_new(self, name: str=None) -> Gimp.Brush:
        """Create a new generated brush having default parameters.
        
        Creates a new, parametric brush.
        
        Parameters:
        
        * name - The requested name of the new brush.
        
        Returns:
        
        * brush - The brush.
        """
        pass

    def gimp_brush_set_angle(self, brush: Gimp.Brush=None, angle_in: float=None) -> float:
        """Sets the rotation angle of a generated brush.
        
        Sets the rotation angle for a generated brush. Sets the angle modulo
        180, in the range [-180.0, 180.0]. Returns the clamped value.
        Returns an error when brush is non-parametric or not editable.
        
        Parameters:
        
        * brush - The brush.
        
        * angle_in (default: 0.0) - The desired brush rotation angle in
          degrees.
        
        Returns:
        
        * angle_out (default: 0.0) - The brush rotation angle actually
          assigned.
        """
        pass

    def gimp_brush_set_aspect_ratio(self, brush: Gimp.Brush=None, aspect_ratio_in: float=None) -> float:
        """Sets the aspect ratio of a generated brush.
        
        Sets the aspect ratio for a generated brush. Clamps aspect ratio to
        [0.0, 1000.0]. Returns the clamped value. Returns an error when
        brush is non-parametric or not editable.
        
        Parameters:
        
        * brush - The brush.
        
        * aspect_ratio_in (default: 0.0) - The desired brush aspect ratio.
        
        Returns:
        
        * aspect_ratio_out (default: 0.0) - The brush aspect ratio actually
          assigned.
        """
        pass

    def gimp_brush_set_hardness(self, brush: Gimp.Brush=None, hardness_in: float=None) -> float:
        """Sets the hardness of a generated brush.
        
        Sets the hardness for a generated brush. Clamps hardness to [0.0, 1.0].
        Returns the clamped value. Returns an error when brush is
        non-parametric or not editable.
        
        Parameters:
        
        * brush - The brush.
        
        * hardness_in (default: 0.0) - The desired brush hardness.
        
        Returns:
        
        * hardness_out (default: 0.0) - The brush hardness actually assigned.
        """
        pass

    def gimp_brush_set_radius(self, brush: Gimp.Brush=None, radius_in: float=None) -> float:
        """Sets the radius of a generated brush.
        
        Sets the radius for a generated brush. Clamps radius to [0.0, 32767.0].
        Returns the clamped value. Returns an error when brush is
        non-parametric or not editable.
        
        Parameters:
        
        * brush - The brush.
        
        * radius_in (default: 0.0) - The desired brush radius in pixel.
        
        Returns:
        
        * radius_out (default: 0.0) - The brush radius actually assigned.
        """
        pass

    def gimp_brush_set_shape(self, brush: Gimp.Brush=None, shape_in: Gimp.BrushGeneratedShape=None) -> Gimp.BrushGeneratedShape:
        """Sets the shape of a generated brush.
        
        Sets the shape of a generated brush. Returns an error when brush is
        non-parametric or not editable. The choices for shape are Circle
        (GIMP_BRUSH_GENERATED_CIRCLE), Square
        (GIMP_BRUSH_GENERATED_SQUARE), and Diamond
        (GIMP_BRUSH_GENERATED_DIAMOND).
        
        Parameters:
        
        * brush - The brush.
        
        * shape_in (default: <enum GIMP_BRUSH_GENERATED_CIRCLE of type
          Gimp.BrushGeneratedShape>) - The brush shape.
        
        Returns:
        
        * shape_out (default: <enum GIMP_BRUSH_GENERATED_CIRCLE of type
          Gimp.BrushGeneratedShape>) - The brush shape actually
          assigned.
        """
        pass

    def gimp_brush_set_spacing(self, brush: Gimp.Brush=None, spacing: int=None):
        """Sets the brush spacing.
        
        Set the spacing for the brush. The spacing must be an integer between 0
        and 1000. Both parametric and raster brushes have a spacing.
        Returns an error when the brush is not editable. Create a new or
        copied brush or to get an editable brush.
        
        Parameters:
        
        * brush - The brush.
        
        * spacing (default: 0) - The brush spacing.
        """
        pass

    def gimp_brush_set_spikes(self, brush: Gimp.Brush=None, spikes_in: int=None) -> int:
        """Sets the number of spikes for a generated brush.
        
        Sets the number of spikes for a generated brush. Clamps spikes to
        [2,20]. Returns the clamped value. Returns an error when brush
        is non-parametric or not editable.
        
        Parameters:
        
        * brush - The brush.
        
        * spikes_in (default: 0) - The desired number of spikes.
        
        Returns:
        
        * spikes_out (default: 0) - The number of spikes actually assigned.
        """
        pass

    def gimp_brushes_close_popup(self, brush_callback: str=None):
        """Close the brush selection dialog.
        
        Closes an open brush selection dialog.
        
        Parameters:
        
        * brush_callback - The name of the callback registered for this
          pop-up.
        """
        pass

    def gimp_brushes_get_list(self, filter: str=None) -> List[str]:
        """Retrieve a complete listing of the available brushes.
        
        This procedure returns a complete listing of available GIMP brushes.
        Each name returned can be used as input to the
        'gimp-context-set-brush' procedure.
        
        Parameters:
        
        * filter - An optional regular expression used to filter the list.
        
        Returns:
        
        * brush_list - The list of brush names.
        """
        pass

    def gimp_brushes_get_opacity(self) -> float:
        """Get the opacity.
        
        Returns the opacity setting. The return value is a floating point number
        between 0 and 100.
        
        Returns:
        
        * opacity (default: 0.0) - The opacity.
        """
        pass

    def gimp_brushes_get_paint_mode(self) -> Gimp.LayerMode:
        """Get the paint mode.
        
        Returns the paint-mode setting. The return value is an integer which
        corresponds to the values listed in the argument description.
        
        Returns:
        
        * paint_mode (default: <enum GIMP_LAYER_MODE_NORMAL of type
          Gimp.LayerMode>) - The paint mode.
        """
        pass

    def gimp_brushes_list(self, filter: str=None) -> List[str]:
        """Retrieve a complete listing of the available brushes.
        
        This procedure returns a complete listing of available GIMP brushes.
        Each name returned can be used as input to the
        'gimp-context-set-brush' procedure.
        
        Parameters:
        
        * filter - An optional regular expression used to filter the list.
        
        Returns:
        
        * brush_list - The list of brush names.
        """
        pass

    def gimp_brushes_popup(self, brush_callback: str=None, popup_title: str=None, initial_brush: Gimp.Brush=None, parent_window: GLib.Bytes=None):
        """Invokes the GIMP brush selection dialog.
        
        Opens a dialog letting a user choose a brush.
        
        Parameters:
        
        * brush_callback - The callback PDB proc to call when user chooses a
          brush.
        
        * popup_title - Title of the brush selection dialog.
        
        * initial_brush - The brush to set as the initial choice.
        
        * parent_window - An optional parent window handle for the popup to be
          set transient to.
        """
        pass

    def gimp_brushes_refresh(self):
        """Refresh current brushes. This function always succeeds.
        
        This procedure retrieves all brushes currently in the user's brush path
        and updates the brush dialogs accordingly.
        """
        pass

    def gimp_brushes_set_brush(self, brush: Gimp.Brush=None):
        """Set the active brush.
        
        Sets the active brush in the current context. The brush will be used in
        subsequent paint and stroke operations. Returns an error when
        the brush data was uninstalled since the brush object was
        created.
        
        Parameters:
        
        * brush - The brush.
        """
        pass

    def gimp_brushes_set_opacity(self, opacity: float=None):
        """Set the opacity.
        
        Modifies the opacity setting. The value should be a floating point
        number between 0 and 100.
        
        Parameters:
        
        * opacity (default: 0.0) - The opacity.
        """
        pass

    def gimp_brushes_set_paint_mode(self, paint_mode: Gimp.LayerMode=None):
        """Set the paint mode.
        
        Modifies the paint_mode setting.
        
        Parameters:
        
        * paint_mode (default: <enum GIMP_LAYER_MODE_NORMAL of type
          Gimp.LayerMode>) - The paint mode.
        """
        pass

    def gimp_brushes_set_popup(self, brush_callback: str=None, brush: Gimp.Brush=None):
        """Sets the selected brush in a brush selection dialog.
        
        Sets the selected brush in a brush selection dialog.
        
        Parameters:
        
        * brush_callback - The name of the callback registered for this
          pop-up.
        
        * brush - The brush to set as selected.
        """
        pass

    def gimp_buffer_delete(self, buffer_name: str=None):
        """Deletes a named buffer.
        
        This procedure deletes a named buffer.
        
        Parameters:
        
        * buffer_name - The buffer name.
        """
        pass

    def gimp_buffer_get_bytes(self, buffer_name: str=None) -> int:
        """Retrieves the specified buffer's bytes.
        
        This procedure retrieves the specified named buffer's bytes.
        
        Parameters:
        
        * buffer_name - The buffer name.
        
        Returns:
        
        * bytes (default: 0) - The buffer bpp.
        """
        pass

    def gimp_buffer_get_height(self, buffer_name: str=None) -> int:
        """Retrieves the specified buffer's height.
        
        This procedure retrieves the specified named buffer's height.
        
        Parameters:
        
        * buffer_name - The buffer name.
        
        Returns:
        
        * height (default: 0) - The buffer height.
        """
        pass

    def gimp_buffer_get_image_type(self, buffer_name: str=None) -> Gimp.ImageBaseType:
        """Retrieves the specified buffer's image type.
        
        This procedure retrieves the specified named buffer's image type.
        
        Parameters:
        
        * buffer_name - The buffer name.
        
        Returns:
        
        * image_type (default: <enum GIMP_RGB of type Gimp.ImageBaseType>) -
          The buffer image type.
        """
        pass

    def gimp_buffer_get_width(self, buffer_name: str=None) -> int:
        """Retrieves the specified buffer's width.
        
        This procedure retrieves the specified named buffer's width.
        
        Parameters:
        
        * buffer_name - The buffer name.
        
        Returns:
        
        * width (default: 0) - The buffer width.
        """
        pass

    def gimp_buffer_rename(self, buffer_name: str=None, new_name: str=None) -> str:
        """Renames a named buffer.
        
        This procedure renames a named buffer.
        
        Parameters:
        
        * buffer_name - The buffer name.
        
        * new_name - The buffer's new name.
        
        Returns:
        
        * real_name - The real name given to the buffer.
        """
        pass

    def gimp_buffers_get_list(self, filter: str=None) -> List[str]:
        """Retrieve a complete listing of the available buffers.
        
        This procedure returns a complete listing of available named buffers.
        
        Parameters:
        
        * filter - An optional regular expression used to filter the list.
        
        Returns:
        
        * buffer_list - The list of buffer names.
        """
        pass

    def gimp_channel_combine_masks(self, channel1: Gimp.Channel=None, channel2: Gimp.Channel=None, operation: Gimp.ChannelOps=None, offx: int=None, offy: int=None):
        """Combine two channel masks.
        
        This procedure combines two channel masks. The result is stored in the
        first channel.
        
        Parameters:
        
        * channel1 - The channel1.
        
        * channel2 - The channel2.
        
        * operation (default: <enum GIMP_CHANNEL_OP_ADD of type
          Gimp.ChannelOps>) - The selection operation.
        
        * offx (default: 0) - x offset between upper left corner of channels:
          (second - first).
        
        * offy (default: 0) - y offset between upper left corner of channels:
          (second - first).
        """
        pass

    def gimp_channel_copy(self, channel: Gimp.Channel=None) -> Gimp.Channel:
        """Copy a channel.
        
        This procedure copies the specified channel and returns the copy. The
        new channel still needs to be added to the image, as this is not
        automatic. Add the new channel with 'gimp-image-insert-channel'.
        
        Parameters:
        
        * channel - The channel to copy.
        
        Returns:
        
        * channel_copy - The newly copied channel.
        """
        pass

    def gimp_channel_delete(self, item: Gimp.Item=None):
        """Delete a item.
        
        This procedure deletes the specified item. This must not be done if the
        image containing this item was already deleted or if the item
        was already removed from the image. The only case in which this
        procedure is useful is if you want to get rid of a item which
        has not yet been added to an image.
        
        Parameters:
        
        * item - The item to delete.
        """
        pass

    def gimp_channel_get_color(self, channel: Gimp.Channel=None) -> Gegl.Color:
        """Get the compositing color of the specified channel.
        
        This procedure returns the specified channel's compositing color.
        
        Parameters:
        
        * channel - The channel.
        
        Returns:
        
        * color - The channel compositing color.
        """
        pass

    def gimp_channel_get_name(self, item: Gimp.Item=None) -> str:
        """Get the name of the specified item.
        
        This procedure returns the specified item's name.
        
        Parameters:
        
        * item - The item.
        
        Returns:
        
        * name - The item name.
        """
        pass

    def gimp_channel_get_opacity(self, channel: Gimp.Channel=None) -> float:
        """Get the opacity of the specified channel.
        
        This procedure returns the specified channel's opacity.
        
        Parameters:
        
        * channel - The channel.
        
        Returns:
        
        * opacity (default: 0.0) - The channel opacity.
        """
        pass

    def gimp_channel_get_show_masked(self, channel: Gimp.Channel=None) -> bool:
        """Get the composite method of the specified channel.
        
        This procedure returns the specified channel's composite method. If it
        is TRUE, then the channel is composited with the image so that
        masked regions are shown. Otherwise, selected regions are shown.
        
        Parameters:
        
        * channel - The channel.
        
        Returns:
        
        * show_masked (default: False) - The channel composite method.
        """
        pass

    def gimp_channel_get_tattoo(self, item: Gimp.Item=None) -> int:
        """Get the tattoo of the specified item.
        
        This procedure returns the specified item's tattoo. A tattoo is a unique
        and permanent identifier attached to a item that can be used to
        uniquely identify a item within an image even between sessions.
        
        Parameters:
        
        * item - The item.
        
        Returns:
        
        * tattoo (default: 1) - The item tattoo.
        """
        pass

    def gimp_channel_get_visible(self, item: Gimp.Item=None) -> bool:
        """Get the visibility of the specified item.
        
        This procedure returns the specified item's visibility.
        
        Parameters:
        
        * item - The item.
        
        Returns:
        
        * visible (default: False) - The item visibility.
        """
        pass

    def gimp_channel_new(self, image: Gimp.Image=None, width: int=None, height: int=None, name: str=None, opacity: float=None, color: Gegl.Color=None) -> Gimp.Channel:
        """Create a new channel.
        
        This procedure creates a new channel with the specified width, height,
        name, opacity and color. The new channel still needs to be added
        to the image, as this is not automatic. Add the new channel with
        'gimp-image-insert-channel'. Other attributes, such as channel
        visibility, should be set with explicit procedure calls. The
        channel's contents are undefined initially.
        
        Parameters:
        
        * image - The image to which to add the channel.
        
        * width (default: 1) - The channel width.
        
        * height (default: 1) - The channel height.
        
        * name - The channel name.
        
        * opacity (default: 0.0) - The channel opacity.
        
        * color - The channel compositing color.
        
        Returns:
        
        * channel - The newly created channel.
        """
        pass

    def gimp_channel_new_from_component(self, image: Gimp.Image=None, component: Gimp.ChannelType=None, name: str=None) -> Gimp.Channel:
        """Create a new channel from a color component.
        
        This procedure creates a new channel from a color component. The new
        channel still needs to be added to the image, as this is not
        automatic. Add the new channel with 'gimp-image-insert-channel'.
        Other attributes, such as channel visibility, should be set with
        explicit procedure calls.
        
        Parameters:
        
        * image - The image to which to add the channel.
        
        * component (default: <enum GIMP_CHANNEL_RED of type
          Gimp.ChannelType>) - The image component.
        
        * name - The channel name.
        
        Returns:
        
        * channel - The newly created channel.
        """
        pass

    def gimp_channel_ops_duplicate(self, image: Gimp.Image=None) -> Gimp.Image:
        """Duplicate the specified image.
        
        This procedure duplicates the specified image, copying all layers,
        channels, and image information.
        
        Parameters:
        
        * image - The image.
        
        Returns:
        
        * new_image - The new, duplicated image.
        """
        pass

    def gimp_channel_ops_offset(self, drawable: Gimp.Drawable=None, wrap_around: bool=None, fill_type: Gimp.OffsetType=None, offset_x: int=None, offset_y: int=None):
        """Offset the drawable by the specified amounts in the X and Y
        directions.
        
        This procedure offsets the specified drawable by the amounts specified
        by 'offset_x' and 'offset_y'. If 'wrap_around' is set to TRUE,
        then portions of the drawable which are offset out of bounds are
        wrapped around. Alternatively, the undefined regions of the
        drawable can be filled with transparency or the background
        color, as specified by the 'fill-type' parameter.
        
        Parameters:
        
        * drawable - The drawable to offset.
        
        * wrap_around (default: False) - wrap image around or fill vacated
          regions.
        
        * fill_type (default: <enum GIMP_OFFSET_BACKGROUND of type
          Gimp.OffsetType>) - fill vacated regions of drawable with
          background or transparent.
        
        * offset_x (default: 0) - offset by this amount in X direction.
        
        * offset_y (default: 0) - offset by this amount in Y direction.
        """
        pass

    def gimp_channel_set_color(self, channel: Gimp.Channel=None, color: Gegl.Color=None):
        """Set the compositing color of the specified channel.
        
        This procedure sets the specified channel's compositing color.
        
        Parameters:
        
        * channel - The channel.
        
        * color - The new channel compositing color.
        """
        pass

    def gimp_channel_set_name(self, item: Gimp.Item=None, name: str=None):
        """Set the name of the specified item.
        
        This procedure sets the specified item's name.
        
        Parameters:
        
        * item - The item.
        
        * name - The new item name.
        """
        pass

    def gimp_channel_set_opacity(self, channel: Gimp.Channel=None, opacity: float=None):
        """Set the opacity of the specified channel.
        
        This procedure sets the specified channel's opacity.
        
        Parameters:
        
        * channel - The channel.
        
        * opacity (default: 0.0) - The new channel opacity.
        """
        pass

    def gimp_channel_set_show_masked(self, channel: Gimp.Channel=None, show_masked: bool=None):
        """Set the composite method of the specified channel.
        
        This procedure sets the specified channel's composite method. If it is
        TRUE, then the channel is composited with the image so that
        masked regions are shown. Otherwise, selected regions are shown.
        
        Parameters:
        
        * channel - The channel.
        
        * show_masked (default: False) - The new channel composite method.
        """
        pass

    def gimp_channel_set_tattoo(self, item: Gimp.Item=None, tattoo: int=None):
        """Set the tattoo of the specified item.
        
        This procedure sets the specified item's tattoo. A tattoo is a unique
        and permanent identifier attached to a item that can be used to
        uniquely identify a item within an image even between sessions.
        
        Parameters:
        
        * item - The item.
        
        * tattoo (default: 1) - The new item tattoo.
        """
        pass

    def gimp_channel_set_visible(self, item: Gimp.Item=None, visible: bool=None):
        """Set the visibility of the specified item.
        
        This procedure sets the specified item's visibility.
        
        Parameters:
        
        * item - The item.
        
        * visible (default: False) - The new item visibility.
        """
        pass

    def gimp_clone(self, drawable: Gimp.Drawable=None, src_drawable: Gimp.Drawable=None, clone_type: Gimp.CloneType=None, src_x: float=None, src_y: float=None, num_strokes: int=None, strokes: Gimp.FloatArray=None):
        """Clone from the source to the dest drawable using the current brush.
        
        This tool clones (copies) from the source drawable starting at the
        specified source coordinates to the dest drawable. If the
        "clone_type" argument is set to PATTERN-CLONE, then the current
        pattern is used as the source and the "src_drawable" argument is
        ignored. Pattern cloning assumes a tileable pattern and mods the
        sum of the src coordinates and subsequent stroke offsets with
        the width and height of the pattern. For image cloning, if the
        sum of the src coordinates and subsequent stroke offsets exceeds
        the extents of the src drawable, then no paint is transferred.
        The clone tool is capable of transforming between any image
        types including RGB->Indexed--although converting from any type
        to indexed is significantly slower.
        
        Parameters:
        
        * drawable - The affected drawable.
        
        * src_drawable - The source drawable.
        
        * clone_type (default: <enum GIMP_CLONE_IMAGE of type Gimp.CloneType>)
          - The type of clone.
        
        * src_x (default: 0.0) - The x coordinate in the source image.
        
        * src_y (default: 0.0) - The y coordinate in the source image.
        
        * num_strokes (default: 2) - Number of stroke control points (count
          each coordinate as 2 points).
        
        * strokes - Array of stroke coordinates: { s1.x, s1.y, s2.x, s2.y,
          ..., sn.x, sn.y }.
        """
        pass

    def gimp_clone_default(self, drawable: Gimp.Drawable=None, num_strokes: int=None, strokes: Gimp.FloatArray=None):
        """Clone from the source to the dest drawable using the current brush.
        
        This tool clones (copies) from the source drawable starting at the
        specified source coordinates to the dest drawable. This function
        performs exactly the same as the 'gimp-clone' function except
        that the tools arguments are obtained from the clones option
        dialog. It this dialog has not been activated then the dialogs
        default values will be used.
        
        Parameters:
        
        * drawable - The affected drawable.
        
        * num_strokes (default: 2) - Number of stroke control points (count
          each coordinate as 2 points).
        
        * strokes - Array of stroke coordinates: { s1.x, s1.y, s2.x, s2.y,
          ..., sn.x, sn.y }.
        """
        pass

    def gimp_color_picker(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, x: float=None, y: float=None, sample_merged: bool=None, sample_average: bool=None, average_radius: float=None) -> Gegl.Color:
        """Determine the color at the given coordinates.
        
        This tool determines the color at the specified coordinates. The
        returned color is an RGB triplet even for grayscale and indexed
        drawables. If the coordinates lie outside of the extents of the
        specified drawables, then an error is returned. All drawables
        must belong to the image and be of the same type. If only one
        drawable is given and it has an alpha channel, the algorithm
        examines the alpha value of the drawable at the coordinates. If
        the alpha value is completely transparent (0), then an error is
        returned. With several drawables specified, the composite image
        with only these drawables is used. If the sample_merged
        parameter is TRUE, the data of the composite image will be used
        instead of that for the specified drawables. This is equivalent
        to sampling for colors after merging all visible layers. In the
        case of a merged sampling, the supplied drawables are ignored.
        
        Parameters:
        
        * image - The image.
        
        * num_drawables (default: 1) - The number of drawables.
        
        * drawables - The drawables to pick from.
        
        * x (default: 0.0) - x coordinate of upper-left corner of rectangle.
        
        * y (default: 0.0) - y coordinate of upper-left corner of rectangle.
        
        * sample_merged (default: False) - Use the composite image, not the
          drawables.
        
        * sample_average (default: False) - Average the color of all the
          pixels in a specified radius.
        
        * average_radius (default: 0.0) - The radius of pixels to average.
        
        Returns:
        
        * color - The return color.
        """
        pass

    def gimp_context_are_dynamics_enabled(self) -> bool:
        """Whether the currently active paint dynamics will be applied to
        painting.
        
        Returns whether the currently active paint dynamics (as returned by
        'gimp-context-get-dynamics') is enabled.
        
        Returns:
        
        * enabled (default: False) - Whether dynamics enabled or disabled.
        """
        pass

    def gimp_context_enable_dynamics(self, enable: bool=None):
        """Enables paint dynamics using the active paint dynamics.
        
        Enables the active paint dynamics to be used in all subsequent paint
        operations.
        
        Parameters:
        
        * enable (default: False) - Whether to enable or disable dynamics.
        """
        pass

    def gimp_context_get_antialias(self) -> bool:
        """Get the antialias setting.
        
        Returns the antialias setting.
        
        Returns:
        
        * antialias (default: False) - The antialias setting.
        """
        pass

    def gimp_context_get_background(self) -> Gegl.Color:
        """Get the current GIMP background color.
        
        Returns the current GIMP background color. The background color is used
        in a variety of tools such as blending, erasing (with non-alpha
        images), and image filling.
        
        Returns:
        
        * background - The background color.
        """
        pass

    def gimp_context_get_brush(self) -> Gimp.Brush:
        """Get the currently active brush.
        
        Returns the currently active brush. All paint and stroke operations use
        this brush.
        
        Returns:
        
        * brush - The active brush.
        """
        pass

    def gimp_context_get_brush_angle(self) -> float:
        """Get brush angle in degrees.
        
        Set the angle in degrees for brush based paint tools.
        
        Returns:
        
        * angle (default: -180.0) - Angle in degrees.
        """
        pass

    def gimp_context_get_brush_aspect_ratio(self) -> float:
        """Get brush aspect ratio.
        
        Set the aspect ratio for brush based paint tools.
        
        Returns:
        
        * aspect (default: -20.0) - Aspect ratio.
        """
        pass

    def gimp_context_get_brush_force(self) -> float:
        """Get brush force in paint options.
        
        Get the brush application force for brush based paint tools.
        
        Returns:
        
        * force (default: 0.0) - Brush application force.
        """
        pass

    def gimp_context_get_brush_hardness(self) -> float:
        """Get brush hardness in paint options.
        
        Get the brush hardness for brush based paint tools.
        
        Returns:
        
        * hardness (default: 0.0) - Brush hardness.
        """
        pass

    def gimp_context_get_brush_size(self) -> float:
        """Get brush size in pixels.
        
        Get the brush size in pixels for brush based paint tools.
        
        Returns:
        
        * size (default: 0.0) - Brush size in pixels.
        """
        pass

    def gimp_context_get_brush_spacing(self) -> float:
        """Get brush spacing as percent of size.
        
        Get the brush spacing as percent of size for brush based paint tools.
        
        Returns:
        
        * spacing (default: 0.01) - Brush spacing as fraction of size.
        """
        pass

    def gimp_context_get_diagonal_neighbors(self) -> bool:
        """Get the diagonal neighbors setting.
        
        Returns the diagonal neighbors setting.
        
        Returns:
        
        * diagonal_neighbors (default: False) - The diagonal neighbors
          setting.
        """
        pass

    def gimp_context_get_distance_metric(self) -> Gegl.DistanceMetric:
        """Get the distance metric used in some computations.
        
        Returns the distance metric in the current context. See
        'gimp-context-set-distance-metric' to know more about its usage.
        
        Returns:
        
        * metric (default: <enum Euclidean of type Gegl.DistanceMetric>) - The
          distance metric.
        """
        pass

    def gimp_context_get_dynamics(self) -> str:
        """Get the currently active paint dynamics.
        
        Returns the name of the currently active paint dynamics. If enabled, all
        paint operations and stroke operations use this paint dynamics
        to control the application of paint to the image. If disabled,
        the dynamics will be ignored during paint actions. See
        'gimp-context-are-dynamics-enabled' to enquire whether dynamics
        are used or ignored.
        
        Returns:
        
        * name - The name of the active paint dynamics.
        """
        pass

    def gimp_context_get_feather(self) -> bool:
        """Get the feather setting.
        
        Returns the feather setting.
        
        Returns:
        
        * feather (default: False) - The feather setting.
        """
        pass

    def gimp_context_get_feather_radius(self) -> Tuple[float, float]:
        """Get the feather radius setting.
        
        Returns the feather radius setting.
        
        Returns:
        
        * feather_radius_x (default: 0.0) - The horizontal feather radius.
        
        * feather_radius_y (default: 0.0) - The vertical feather radius.
        """
        pass

    def gimp_context_get_font(self) -> Gimp.Font:
        """Get the currently active font.
        
        Returns the currently active font.
        
        Returns:
        
        * font - The active font.
        """
        pass

    def gimp_context_get_foreground(self) -> Gegl.Color:
        """Get the current GIMP foreground color.
        
        Returns the current GIMP foreground color. The foreground color is used
        in a variety of tools such as paint tools, blending, and bucket
        fill.
        
        Returns:
        
        * foreground - The foreground color.
        """
        pass

    def gimp_context_get_gradient(self) -> Gimp.Gradient:
        """Get the currently active gradient.
        
        Returns the currently active gradient.
        
        Returns:
        
        * gradient - The active gradient.
        """
        pass

    def gimp_context_get_gradient_blend_color_space(self) -> Gimp.GradientBlendColorSpace:
        """Get the gradient blend color space.
        
        Get the gradient blend color space for paint tools and the gradient
        tool.
        
        Returns:
        
        * blend_color_space (default: <enum GIMP_GRADIENT_BLEND_RGB_PERCEPTUAL
          of type Gimp.GradientBlendColorSpace>) - Color blend space.
        """
        pass

    def gimp_context_get_gradient_repeat_mode(self) -> Gimp.RepeatMode:
        """Get the gradient repeat mode.
        
        Get the gradient repeat mode for paint tools and the gradient tool.
        
        Returns:
        
        * repeat_mode (default: <enum GIMP_REPEAT_NONE of type
          Gimp.RepeatMode>) - Repeat mode.
        """
        pass

    def gimp_context_get_gradient_reverse(self) -> bool:
        """Get the gradient reverse setting.
        
        Get the gradient reverse setting for paint tools and the gradient tool.
        
        Returns:
        
        * reverse (default: False) - Reverse.
        """
        pass

    def gimp_context_get_ink_angle(self) -> float:
        """Get ink angle in degrees.
        
        Get the ink angle in degrees for ink tool.
        
        Returns:
        
        * angle (default: -90.0) - ink angle in degrees.
        """
        pass

    def gimp_context_get_ink_blob_angle(self) -> float:
        """Get ink blob angle in degrees.
        
        Get the ink blob angle in degrees for ink tool.
        
        Returns:
        
        * angle (default: -180.0) - ink blob angle in degrees.
        """
        pass

    def gimp_context_get_ink_blob_aspect_ratio(self) -> float:
        """Get ink blob aspect ratio.
        
        Get the ink blob aspect ratio for ink tool.
        
        Returns:
        
        * aspect (default: 1.0) - ink blob aspect ratio.
        """
        pass

    def gimp_context_get_ink_blob_type(self) -> Gimp.InkBlobType:
        """Get ink blob type.
        
        Get the ink blob type for ink tool.
        
        Returns:
        
        * type (default: <enum GIMP_INK_BLOB_TYPE_CIRCLE of type
          Gimp.InkBlobType>) - Ink blob type.
        """
        pass

    def gimp_context_get_ink_size(self) -> float:
        """Get ink blob size in pixels.
        
        Get the ink blob size in pixels for ink tool.
        
        Returns:
        
        * size (default: 0.0) - ink blob size in pixels.
        """
        pass

    def gimp_context_get_ink_size_sensitivity(self) -> float:
        """Get ink size sensitivity.
        
        Get the ink size sensitivity for ink tool.
        
        Returns:
        
        * size (default: 0.0) - ink size sensitivity.
        """
        pass

    def gimp_context_get_ink_speed_sensitivity(self) -> float:
        """Get ink speed sensitivity.
        
        Get the ink speed sensitivity for ink tool.
        
        Returns:
        
        * speed (default: 0.0) - ink speed sensitivity.
        """
        pass

    def gimp_context_get_ink_tilt_sensitivity(self) -> float:
        """Get ink tilt sensitivity.
        
        Get the ink tilt sensitivity for ink tool.
        
        Returns:
        
        * tilt (default: 0.0) - ink tilt sensitivity.
        """
        pass

    def gimp_context_get_interpolation(self) -> Gimp.InterpolationType:
        """Get the interpolation type.
        
        Returns the interpolation setting. The return value is an integer which
        corresponds to the values listed in the argument description. If
        the interpolation has not been set explicitly by
        'gimp-context-set-interpolation', the default interpolation set
        in gimprc will be used.
        
        Returns:
        
        * interpolation (default: <enum GIMP_INTERPOLATION_NONE of type
          Gimp.InterpolationType>) - The interpolation type.
        """
        pass

    def gimp_context_get_line_cap_style(self) -> Gimp.CapStyle:
        """Get the line cap style setting.
        
        Returns the line cap style setting.
        
        Returns:
        
        * cap_style (default: <enum GIMP_CAP_BUTT of type Gimp.CapStyle>) -
          The line cap style setting.
        """
        pass

    def gimp_context_get_line_dash_offset(self) -> float:
        """Get the line dash offset setting.
        
        Returns the line dash offset setting.
        
        Returns:
        
        * dash_offset (default: 0.0) - The line dash offset setting.
        """
        pass

    def gimp_context_get_line_dash_pattern(self) -> Tuple[int, Gimp.FloatArray]:
        """Get the line dash pattern setting.
        
        Returns the line dash pattern setting.
        
        Returns:
        
        * num_dashes (default: 0) - The number of dashes in the dash_pattern
          array.
        
        * dashes - The line dash pattern setting.
        """
        pass

    def gimp_context_get_line_join_style(self) -> Gimp.JoinStyle:
        """Get the line join style setting.
        
        Returns the line join style setting.
        
        Returns:
        
        * join_style (default: <enum GIMP_JOIN_MITER of type Gimp.JoinStyle>)
          - The line join style setting.
        """
        pass

    def gimp_context_get_line_miter_limit(self) -> float:
        """Get the line miter limit setting.
        
        Returns the line miter limit setting.
        
        Returns:
        
        * miter_limit (default: 0.0) - The line miter limit setting.
        """
        pass

    def gimp_context_get_line_width(self) -> float:
        """Get the line width setting.
        
        Returns the line width setting.
        
        Returns:
        
        * line_width (default: 0.0) - The line width setting.
        """
        pass

    def gimp_context_get_line_width_unit(self) -> Gimp.Unit:
        """Get the line width unit setting.
        
        Returns the line width unit setting.
        
        Returns:
        
        * line_width_unit (default: 0) - The line width unit setting.
        """
        pass

    def gimp_context_get_mypaint_brush(self) -> str:
        """Get the currently active MyPaint brush.
        
        Returns the name of the currently active MyPaint brush.
        
        Returns:
        
        * name - The name of the active MyPaint brush.
        """
        pass

    def gimp_context_get_opacity(self) -> float:
        """Get the opacity.
        
        Returns the opacity setting. The return value is a floating point number
        between 0 and 100.
        
        Returns:
        
        * opacity (default: 0.0) - The opacity.
        """
        pass

    def gimp_context_get_paint_method(self) -> str:
        """Get the currently active paint method.
        
        Returns the name of the currently active paint method.
        
        Returns:
        
        * name - The name of the active paint method.
        """
        pass

    def gimp_context_get_paint_mode(self) -> Gimp.LayerMode:
        """Get the paint mode.
        
        Returns the paint-mode setting. The return value is an integer which
        corresponds to the values listed in the argument description.
        
        Returns:
        
        * paint_mode (default: <enum GIMP_LAYER_MODE_NORMAL of type
          Gimp.LayerMode>) - The paint mode.
        """
        pass

    def gimp_context_get_palette(self) -> Gimp.Palette:
        """Get the currently active palette.
        
        Returns the currently active palette.
        
        Returns:
        
        * palette - The active palette.
        """
        pass

    def gimp_context_get_pattern(self) -> Gimp.Pattern:
        """Get the currently active pattern.
        
        Returns the active pattern in the current context. All clone and
        bucket-fill operations with patterns will use this pattern to
        control the application of paint to the image.
        
        Returns:
        
        * pattern - The active pattern.
        """
        pass

    def gimp_context_get_resource(self, type_name: str=None) -> Gimp.Resource:
        """Get the currently active resource for a type.
        
        Returns the currently active resource for the given type name.
        
        Parameters:
        
        * type_name - The name of the resource type.
        
        Returns:
        
        * resource - The active resource.
        """
        pass

    def gimp_context_get_sample_criterion(self) -> Gimp.SelectCriterion:
        """Get the sample criterion setting.
        
        Returns the sample criterion setting.
        
        Returns:
        
        * sample_criterion (default: <enum GIMP_SELECT_CRITERION_COMPOSITE of
          type Gimp.SelectCriterion>) - The sample criterion setting.
        """
        pass

    def gimp_context_get_sample_merged(self) -> bool:
        """Get the sample merged setting.
        
        Returns the sample merged setting.
        
        Returns:
        
        * sample_merged (default: False) - The sample merged setting.
        """
        pass

    def gimp_context_get_sample_threshold(self) -> float:
        """Get the sample threshold setting.
        
        Returns the sample threshold setting.
        
        Returns:
        
        * sample_threshold (default: 0.0) - The sample threshold setting.
        """
        pass

    def gimp_context_get_sample_threshold_int(self) -> int:
        """Get the sample threshold setting as an integer value.
        
        Returns the sample threshold setting as an integer value. See
        'gimp-context-get-sample-threshold'.
        
        Returns:
        
        * sample_threshold (default: 0) - The sample threshold setting.
        """
        pass

    def gimp_context_get_sample_transparent(self) -> bool:
        """Get the sample transparent setting.
        
        Returns the sample transparent setting.
        
        Returns:
        
        * sample_transparent (default: False) - The sample transparent
          setting.
        """
        pass

    def gimp_context_get_stroke_method(self) -> Gimp.StrokeMethod:
        """Get the currently active stroke method.
        
        Returns the currently active stroke method.
        
        Returns:
        
        * stroke_method (default: <enum GIMP_STROKE_LINE of type
          Gimp.StrokeMethod>) - The active stroke method.
        """
        pass

    def gimp_context_get_transform_direction(self) -> Gimp.TransformDirection:
        """Get the transform direction.
        
        Returns the transform direction. The return value is an integer which
        corresponds to the values listed in the argument description.
        
        Returns:
        
        * transform_direction (default: <enum GIMP_TRANSFORM_FORWARD of type
          Gimp.TransformDirection>) - The transform direction.
        """
        pass

    def gimp_context_get_transform_resize(self) -> Gimp.TransformResize:
        """Get the transform resize type.
        
        Returns the transform resize setting. The return value is an integer
        which corresponds to the values listed in the argument
        description.
        
        Returns:
        
        * transform_resize (default: <enum GIMP_TRANSFORM_RESIZE_ADJUST of
          type Gimp.TransformResize>) - The transform resize type.
        """
        pass

    def gimp_context_list_paint_methods(self) -> List[str]:
        """Lists the available paint methods.
        
        Lists the names of the available paint methods. Any of the names can be
        used for 'gimp-context-set-paint-method'.
        
        Returns:
        
        * paint_methods - The names of the available paint methods.
        """
        pass

    def gimp_context_pop(self):
        """Pops the topmost context from the plug-in's context stack.
        
        Removes the topmost context from the plug-in's context stack. The next
        context on the stack becomes the new current context of the
        plug-in, that is, the context that was active before the
        corresponding call to 'gimp-context-push'.
        """
        pass

    def gimp_context_push(self):
        """Pushes a context onto the top of the plug-in's context stack.
        
        Creates a new context by copying the current context. The copy becomes
        the new current context for the calling plug-in until it is
        popped again using 'gimp-context-pop'.
        """
        pass

    def gimp_context_set_antialias(self, antialias: bool=None):
        """Set the antialias setting.
        
        Modifies the antialias setting. If antialiasing is turned on, the edges
        of selected region will contain intermediate values which give
        the appearance of a sharper, less pixelized edge. This should be
        set as TRUE most of the time unless a binary-only selection is
        wanted.
        
        This setting affects the following procedures:
        'gimp-image-select-color', 'gimp-image-select-contiguous-color',
        'gimp-image-select-round-rectangle',
        'gimp-image-select-ellipse', 'gimp-image-select-polygon',
        'gimp-image-select-item', 'gimp-drawable-edit-bucket-fill',
        'gimp-drawable-edit-stroke-item',
        'gimp-drawable-edit-stroke-selection'.
        
        Parameters:
        
        * antialias (default: False) - The antialias setting.
        """
        pass

    def gimp_context_set_background(self, background: Gegl.Color=None):
        """Set the current GIMP background color.
        
        Sets the current GIMP background color. After this is set, operations
        which use background such as blending, filling images, clearing,
        and erasing (in non-alpha images) will use the new value.
        
        Parameters:
        
        * background - The background color.
        """
        pass

    def gimp_context_set_brush(self, brush: Gimp.Brush=None):
        """Set the active brush.
        
        Sets the active brush in the current context. The brush will be used in
        subsequent paint and stroke operations. Returns an error when
        the brush data was uninstalled since the brush object was
        created.
        
        Parameters:
        
        * brush - The brush.
        """
        pass

    def gimp_context_set_brush_angle(self, angle: float=None):
        """Set brush angle in degrees.
        
        Set the angle in degrees for brush based paint tools.
        
        Parameters:
        
        * angle (default: -180.0) - Angle in degrees.
        """
        pass

    def gimp_context_set_brush_aspect_ratio(self, aspect: float=None):
        """Set brush aspect ratio.
        
        Set the aspect ratio for brush based paint tools.
        
        Parameters:
        
        * aspect (default: -20.0) - Aspect ratio.
        """
        pass

    def gimp_context_set_brush_default_hardness(self):
        """Set brush spacing to its default.
        
        Set the brush spacing to the default for paintbrush, airbrush, or pencil
        tools.
        """
        pass

    def gimp_context_set_brush_default_size(self):
        """Set brush size to its default.
        
        Set the brush size to the default (max of width and height) for
        paintbrush, airbrush, or pencil tools.
        """
        pass

    def gimp_context_set_brush_default_spacing(self):
        """Set brush spacing to its default.
        
        Set the brush spacing to the default for paintbrush, airbrush, or pencil
        tools.
        """
        pass

    def gimp_context_set_brush_force(self, force: float=None):
        """Set brush application force.
        
        Set the brush application force for brush based paint tools.
        
        Parameters:
        
        * force (default: 0.0) - Brush application force.
        """
        pass

    def gimp_context_set_brush_hardness(self, hardness: float=None):
        """Set brush hardness.
        
        Set the brush hardness for brush based paint tools.
        
        Parameters:
        
        * hardness (default: 0.0) - Brush hardness.
        """
        pass

    def gimp_context_set_brush_size(self, size: float=None):
        """Set brush size in pixels.
        
        Set the brush size in pixels for brush based paint tools.
        
        Parameters:
        
        * size (default: 1.0) - Brush size in pixels.
        """
        pass

    def gimp_context_set_brush_spacing(self, spacing: float=None):
        """Set brush spacing as percent of size.
        
        Set the brush spacing as percent of size for brush based paint tools.
        
        Parameters:
        
        * spacing (default: 0.01) - Brush spacing as fraction of size.
        """
        pass

    def gimp_context_set_default_colors(self):
        """Set the current GIMP foreground and background colors to black and
        white.
        
        Sets the current GIMP foreground and background colors to their initial
        default values, black and white.
        """
        pass

    def gimp_context_set_defaults(self):
        """Reset context settings to their default values.
        
        Resets context settings used by various procedures to their default
        value. You should usually call this after a context push so that
        a script which calls procedures affected by context settings
        will not be affected by changes in the global context.
        """
        pass

    def gimp_context_set_diagonal_neighbors(self, diagonal_neighbors: bool=None):
        """Set the diagonal neighbors setting.
        
        Modifies the diagonal neighbors setting. If the affected region of an
        operation is based on a seed point, like when doing a seed fill,
        then, when this setting is TRUE, all eight neighbors of each
        pixel are considered when calculating the affected region; in
        contrast, when this setting is FALSE, only the four orthogonal
        neighbors of each pixel are considered.
        
        This setting affects the following procedures:
        'gimp-image-select-contiguous-color',
        'gimp-drawable-edit-bucket-fill'.
        
        Parameters:
        
        * diagonal_neighbors (default: False) - The diagonal neighbors
          setting.
        """
        pass

    def gimp_context_set_distance_metric(self, metric: Gegl.DistanceMetric=None):
        """Set the distance metric used in some computations.
        
        Modifies the distance metric used in some computations, such as
        'gimp-drawable-edit-gradient-fill'. In particular, it does not
        change the metric used in generic distance computation on
        canvas, as in the Measure tool.
        
        This setting affects the following procedures:
        'gimp-drawable-edit-gradient-fill'.
        
        Parameters:
        
        * metric (default: <enum Euclidean of type Gegl.DistanceMetric>) - The
          distance metric.
        """
        pass

    def gimp_context_set_dynamics(self, name: str=None):
        """Set the active paint dynamics.
        
        Sets the active paint dynamics. The paint dynamics will be used in all
        subsequent paint operations when dynamics are enabled. The name
        should be a name of an installed paint dynamics. Returns an
        error if no matching paint dynamics is found.
        
        Parameters:
        
        * name - A name of a paint dynamics.
        """
        pass

    def gimp_context_set_feather(self, feather: bool=None):
        """Set the feather setting.
        
        Modifies the feather setting. If the feather option is enabled,
        selections will be blurred before combining. The blur is a
        gaussian blur; its radii can be controlled using
        'gimp-context-set-feather-radius'.
        
        This setting affects the following procedures:
        'gimp-image-select-color', 'gimp-image-select-contiguous-color',
        'gimp-image-select-rectangle',
        'gimp-image-select-round-rectangle',
        'gimp-image-select-ellipse', 'gimp-image-select-polygon',
        'gimp-image-select-item'.
        
        Parameters:
        
        * feather (default: False) - The feather setting.
        """
        pass

    def gimp_context_set_feather_radius(self, feather_radius_x: float=None, feather_radius_y: float=None):
        """Set the feather radius setting.
        
        Modifies the feather radius setting.
        
        This setting affects all procedures that are affected by
        'gimp-context-set-feather'.
        
        Parameters:
        
        * feather_radius_x (default: 0.0) - The horizontal feather radius.
        
        * feather_radius_y (default: 0.0) - The vertical feather radius.
        """
        pass

    def gimp_context_set_font(self, font: Gimp.Font=None):
        """Set the active font.
        
        Sets the active font in the current context. The font will be used in
        subsequent text operations. Returns an error when the font data
        was uninstalled since the font object was created.
        
        Parameters:
        
        * font - The font.
        """
        pass

    def gimp_context_set_foreground(self, foreground: Gegl.Color=None):
        """Set the current GIMP foreground color.
        
        Sets the current GIMP foreground color. After this is set, operations
        which use foreground such as paint tools, blending, and bucket
        fill will use the new value.
        
        Parameters:
        
        * foreground - The foreground color.
        """
        pass

    def gimp_context_set_gradient(self, gradient: Gimp.Gradient=None):
        """Sets the active gradient.
        
        Sets the active gradient in the current context. The gradient will be
        used in subsequent gradient operations. Returns an error when
        the gradient data was uninstalled since the gradient object was
        created.
        
        Parameters:
        
        * gradient - The gradient.
        """
        pass

    def gimp_context_set_gradient_blend_color_space(self, blend_color_space: Gimp.GradientBlendColorSpace=None):
        """Set the gradient blend color space.
        
        Set the gradient blend color space for paint tools and the gradient
        tool.
        
        Parameters:
        
        * blend_color_space (default: <enum GIMP_GRADIENT_BLEND_RGB_PERCEPTUAL
          of type Gimp.GradientBlendColorSpace>) - Blend color space.
        """
        pass

    def gimp_context_set_gradient_fg_bg_hsv_ccw(self):
        """Sets the built-in FG-BG HSV (ccw) gradient as the active gradient.
        
        Sets the built-in FG-BG HSV (ccw) gradient as the active gradient. The
        gradient will be used for subsequent gradient operations.
        """
        pass

    def gimp_context_set_gradient_fg_bg_hsv_cw(self):
        """Sets the built-in FG-BG HSV (cw) gradient as the active gradient.
        
        Sets the built-in FG-BG HSV (cw) gradient as the active gradient. The
        gradient will be used for subsequent gradient operations.
        """
        pass

    def gimp_context_set_gradient_fg_bg_rgb(self):
        """Sets the built-in FG-BG RGB gradient as the active gradient.
        
        Sets the built-in FG-BG RGB gradient as the active gradient. The
        gradient will be used for subsequent gradient operations.
        """
        pass

    def gimp_context_set_gradient_fg_transparent(self):
        """Sets the built-in FG-Transparent gradient as the active gradient.
        
        Sets the built-in FG-Transparent gradient as the active gradient. The
        gradient will be used for subsequent gradient operations.
        """
        pass

    def gimp_context_set_gradient_repeat_mode(self, repeat_mode: Gimp.RepeatMode=None):
        """Set the gradient repeat mode.
        
        Set the gradient repeat mode for paint tools and the gradient tool.
        
        Parameters:
        
        * repeat_mode (default: <enum GIMP_REPEAT_NONE of type
          Gimp.RepeatMode>) - Repeat mode.
        """
        pass

    def gimp_context_set_gradient_reverse(self, reverse: bool=None):
        """Set the gradient reverse setting.
        
        Set the gradient reverse setting for paint tools and the gradient tool.
        
        Parameters:
        
        * reverse (default: False) - Reverse.
        """
        pass

    def gimp_context_set_ink_angle(self, angle: float=None):
        """Set ink angle in degrees.
        
        Set the ink angle in degrees for ink tool.
        
        Parameters:
        
        * angle (default: -90.0) - ink angle in degrees.
        """
        pass

    def gimp_context_set_ink_blob_angle(self, angle: float=None):
        """Set ink blob angle in degrees.
        
        Set the ink blob angle in degrees for ink tool.
        
        Parameters:
        
        * angle (default: -180.0) - ink blob angle in degrees.
        """
        pass

    def gimp_context_set_ink_blob_aspect_ratio(self, aspect: float=None):
        """Set ink blob aspect ratio.
        
        Set the ink blob aspect ratio for ink tool.
        
        Parameters:
        
        * aspect (default: 1.0) - ink blob aspect ratio.
        """
        pass

    def gimp_context_set_ink_blob_type(self, type: Gimp.InkBlobType=None):
        """Set ink blob type.
        
        Set the ink blob type for ink tool.
        
        Parameters:
        
        * type (default: <enum GIMP_INK_BLOB_TYPE_CIRCLE of type
          Gimp.InkBlobType>) - Ink blob type.
        """
        pass

    def gimp_context_set_ink_size(self, size: float=None):
        """Set ink blob size in pixels.
        
        Set the ink blob size in pixels for ink tool.
        
        Parameters:
        
        * size (default: 0.0) - ink blob size in pixels.
        """
        pass

    def gimp_context_set_ink_size_sensitivity(self, size: float=None):
        """Set ink size sensitivity.
        
        Set the ink size sensitivity for ink tool.
        
        Parameters:
        
        * size (default: 0.0) - ink size sensitivity.
        """
        pass

    def gimp_context_set_ink_speed_sensitivity(self, speed: float=None):
        """Set ink speed sensitivity.
        
        Set the ink speed sensitivity for ink tool.
        
        Parameters:
        
        * speed (default: 0.0) - ink speed sensitivity.
        """
        pass

    def gimp_context_set_ink_tilt_sensitivity(self, tilt: float=None):
        """Set ink tilt sensitivity.
        
        Set the ink tilt sensitivity for ink tool.
        
        Parameters:
        
        * tilt (default: 0.0) - ink tilt sensitivity.
        """
        pass

    def gimp_context_set_interpolation(self, interpolation: Gimp.InterpolationType=None):
        """Set the interpolation type.
        
        Modifies the interpolation setting.
        
        This setting affects affects the following procedures:
        'gimp-item-transform-flip', 'gimp-item-transform-perspective',
        'gimp-item-transform-rotate', 'gimp-item-transform-scale',
        'gimp-item-transform-shear', 'gimp-item-transform-2d',
        'gimp-item-transform-matrix', 'gimp-image-scale',
        'gimp-layer-scale'.
        
        Parameters:
        
        * interpolation (default: <enum GIMP_INTERPOLATION_NONE of type
          Gimp.InterpolationType>) - The interpolation type.
        """
        pass

    def gimp_context_set_line_cap_style(self, cap_style: Gimp.CapStyle=None):
        """Set the line cap style setting.
        
        Modifies the line cap style setting for stroking lines.
        
        This setting affects the following procedures:
        'gimp-drawable-edit-stroke-selection',
        'gimp-drawable-edit-stroke-item'.
        
        Parameters:
        
        * cap_style (default: <enum GIMP_CAP_BUTT of type Gimp.CapStyle>) -
          The line cap style setting.
        """
        pass

    def gimp_context_set_line_dash_offset(self, dash_offset: float=None):
        """Set the line dash offset setting.
        
        Modifies the line dash offset setting for stroking lines.
        
        This setting affects the following procedures:
        'gimp-drawable-edit-stroke-selection',
        'gimp-drawable-edit-stroke-item'.
        
        Parameters:
        
        * dash_offset (default: 0.0) - The line dash offset setting.
        """
        pass

    def gimp_context_set_line_dash_pattern(self, num_dashes: int=None, dashes: Gimp.FloatArray=None):
        """Set the line dash pattern setting.
        
        Modifies the line dash pattern setting for stroking lines.
        
        The unit of the dash pattern segments is the actual line width used for
        the stroke operation, in other words a segment length of 1.0
        results in a square segment shape (or gap shape).
        
        This setting affects the following procedures:
        'gimp-drawable-edit-stroke-selection',
        'gimp-drawable-edit-stroke-item'.
        
        Parameters:
        
        * num_dashes (default: 0) - The number of dashes in the dash_pattern
          array.
        
        * dashes - The line dash pattern setting.
        """
        pass

    def gimp_context_set_line_join_style(self, join_style: Gimp.JoinStyle=None):
        """Set the line join style setting.
        
        Modifies the line join style setting for stroking lines. This setting
        affects the following procedures:
        'gimp-drawable-edit-stroke-selection',
        'gimp-drawable-edit-stroke-item'.
        
        Parameters:
        
        * join_style (default: <enum GIMP_JOIN_MITER of type Gimp.JoinStyle>)
          - The line join style setting.
        """
        pass

    def gimp_context_set_line_miter_limit(self, miter_limit: float=None):
        """Set the line miter limit setting.
        
        Modifies the line miter limit setting for stroking lines. A mitered join
        is converted to a bevelled join if the miter would extend to a
        distance of more than (miter-limit * line-width) from the actual
        join point. This setting affects the following procedures:
        'gimp-drawable-edit-stroke-selection',
        'gimp-drawable-edit-stroke-item'.
        
        Parameters:
        
        * miter_limit (default: 0.0) - The line miter limit setting.
        """
        pass

    def gimp_context_set_line_width(self, line_width: float=None):
        """Set the line width setting.
        
        Modifies the line width setting for stroking lines.
        
        This setting affects the following procedures:
        'gimp-drawable-edit-stroke-selection',
        'gimp-drawable-edit-stroke-item'.
        
        Parameters:
        
        * line_width (default: 0.0) - The line width setting.
        """
        pass

    def gimp_context_set_line_width_unit(self, line_width_unit: Gimp.Unit=None):
        """Set the line width unit setting.
        
        Modifies the line width unit setting for stroking lines.
        
        This setting affects the following procedures:
        'gimp-drawable-edit-stroke-selection',
        'gimp-drawable-edit-stroke-item'.
        
        Parameters:
        
        * line_width_unit (default: 0) - The line width setting unit.
        """
        pass

    def gimp_context_set_mypaint_brush(self, name: str=None):
        """Set a MyPaint brush as the active MyPaint brush.
        
        Sets the active MyPaint brush to the named MyPaint brush. The brush will
        be used in all subsequent MyPaint paint operations. The name
        should be a name of an installed MyPaint brush. Returns an error
        if no matching MyPaint brush is found.
        
        Parameters:
        
        * name - A name of a MyPaint brush.
        """
        pass

    def gimp_context_set_opacity(self, opacity: float=None):
        """Set the opacity.
        
        Modifies the opacity setting. The value should be a floating point
        number between 0 and 100.
        
        Parameters:
        
        * opacity (default: 0.0) - The opacity.
        """
        pass

    def gimp_context_set_paint_method(self, name: str=None):
        """Set the active paint method.
        
        Sets the active paint method to the named paint method. The paint method
        will be used in all subsequent paint operations. The name should
        be a name of an available paint method. Returns an error if no
        matching paint method is found.
        
        Parameters:
        
        * name - The name of the paint method.
        """
        pass

    def gimp_context_set_paint_mode(self, paint_mode: Gimp.LayerMode=None):
        """Set the paint mode.
        
        Modifies the paint_mode setting.
        
        Parameters:
        
        * paint_mode (default: <enum GIMP_LAYER_MODE_NORMAL of type
          Gimp.LayerMode>) - The paint mode.
        """
        pass

    def gimp_context_set_palette(self, palette: Gimp.Palette=None):
        """Set the active palette.
        
        Sets the active palette in the current context. The palette will be used
        in subsequent paint operations. Returns an error when the
        palette data was uninstalled since the palette object was
        created.
        
        Parameters:
        
        * palette - The palette.
        """
        pass

    def gimp_context_set_pattern(self, pattern: Gimp.Pattern=None):
        """Set the active pattern.
        
        Sets the active pattern in the current context. The pattern will be used
        in subsequent fill operations using a pattern. Returns an error
        when the pattern data was uninstalled since the pattern object
        was created.
        
        Parameters:
        
        * pattern - The pattern.
        """
        pass

    def gimp_context_set_sample_criterion(self, sample_criterion: Gimp.SelectCriterion=None):
        """Set the sample criterion setting.
        
        Modifies the sample criterion setting. If an operation depends on the
        colors of the pixels present in a drawable, like when doing a
        seed fill, this setting controls how color similarity is
        determined. SELECT_CRITERION_COMPOSITE is the default value.
        
        This setting affects the following procedures:
        'gimp-image-select-color', 'gimp-image-select-contiguous-color',
        'gimp-drawable-edit-bucket-fill'.
        
        Parameters:
        
        * sample_criterion (default: <enum GIMP_SELECT_CRITERION_COMPOSITE of
          type Gimp.SelectCriterion>) - The sample criterion setting.
        """
        pass

    def gimp_context_set_sample_merged(self, sample_merged: bool=None):
        """Set the sample merged setting.
        
        Modifies the sample merged setting. If an operation depends on the
        colors of the pixels present in a drawable, like when doing a
        seed fill, this setting controls whether the pixel data from the
        given drawable is used ('sample-merged' is FALSE), or the pixel
        data from the composite image ('sample-merged' is TRUE. This is
        equivalent to sampling for colors after merging all visible
        layers).
        
        This setting affects the following procedures:
        'gimp-image-select-color', 'gimp-image-select-contiguous-color',
        'gimp-drawable-edit-bucket-fill'.
        
        Parameters:
        
        * sample_merged (default: False) - The sample merged setting.
        """
        pass

    def gimp_context_set_sample_threshold(self, sample_threshold: float=None):
        """Set the sample threshold setting.
        
        Modifies the sample threshold setting. If an operation depends on the
        colors of the pixels present in a drawable, like when doing a
        seed fill, this setting controls what is "sufficiently close" to
        be considered a similar color. If the sample threshold has not
        been set explicitly, the default threshold set in gimprc will be
        used.
        
        This setting affects the following procedures:
        'gimp-image-select-color', 'gimp-image-select-contiguous-color',
        'gimp-drawable-edit-bucket-fill'.
        
        Parameters:
        
        * sample_threshold (default: 0.0) - The sample threshold setting.
        """
        pass

    def gimp_context_set_sample_threshold_int(self, sample_threshold: int=None):
        """Set the sample threshold setting as an integer value.
        
        Modifies the sample threshold setting as an integer value. See
        'gimp-context-set-sample-threshold'.
        
        Parameters:
        
        * sample_threshold (default: 0) - The sample threshold setting.
        """
        pass

    def gimp_context_set_sample_transparent(self, sample_transparent: bool=None):
        """Set the sample transparent setting.
        
        Modifies the sample transparent setting. If an operation depends on the
        colors of the pixels present in a drawable, like when doing a
        seed fill, this setting controls whether transparency is
        considered to be a unique selectable color. When this setting is
        TRUE, transparent areas can be selected or filled.
        
        This setting affects the following procedures:
        'gimp-image-select-color', 'gimp-image-select-contiguous-color',
        'gimp-drawable-edit-bucket-fill'.
        
        Parameters:
        
        * sample_transparent (default: False) - The sample transparent
          setting.
        """
        pass

    def gimp_context_set_stroke_method(self, stroke_method: Gimp.StrokeMethod=None):
        """Set the active stroke method.
        
        Sets the active stroke method. The method will be used in all subsequent
        stroke operations.
        
        Parameters:
        
        * stroke_method (default: <enum GIMP_STROKE_LINE of type
          Gimp.StrokeMethod>) - The new stroke method.
        """
        pass

    def gimp_context_set_transform_direction(self, transform_direction: Gimp.TransformDirection=None):
        """Set the transform direction.
        
        Modifies the transform direction setting.
        
        This setting affects affects the following procedures:
        'gimp-item-transform-flip', 'gimp-item-transform-perspective',
        'gimp-item-transform-rotate', 'gimp-item-transform-scale',
        'gimp-item-transform-shear', 'gimp-item-transform-2d',
        'gimp-item-transform-matrix'.
        
        Parameters:
        
        * transform_direction (default: <enum GIMP_TRANSFORM_FORWARD of type
          Gimp.TransformDirection>) - The transform direction.
        """
        pass

    def gimp_context_set_transform_resize(self, transform_resize: Gimp.TransformResize=None):
        """Set the transform resize type.
        
        Modifies the transform resize setting. When transforming pixels, if the
        result of a transform operation has a different size than the
        original area, this setting determines how the resulting area is
        sized.
        
        This setting affects affects the following procedures:
        'gimp-item-transform-flip', 'gimp-item-transform-flip-simple',
        'gimp-item-transform-perspective', 'gimp-item-transform-rotate',
        'gimp-item-transform-rotate-simple',
        'gimp-item-transform-scale', 'gimp-item-transform-shear',
        'gimp-item-transform-2d', 'gimp-item-transform-matrix'.
        
        Parameters:
        
        * transform_resize (default: <enum GIMP_TRANSFORM_RESIZE_ADJUST of
          type Gimp.TransformResize>) - The transform resize type.
        """
        pass

    def gimp_context_swap_colors(self):
        """Swap the current GIMP foreground and background colors.
        
        Swaps the current GIMP foreground and background colors, so that the new
        foreground color becomes the old background color and vice
        versa.
        """
        pass

    def gimp_convert_grayscale(self, image: Gimp.Image=None):
        """Convert specified image to grayscale.
        
        This procedure converts the specified image to grayscale. This process
        requires an image in RGB or Indexed color mode.
        
        Parameters:
        
        * image - The image.
        """
        pass

    def gimp_convert_indexed(self, image: Gimp.Image=None, dither_type: Gimp.ConvertDitherType=None, palette_type: Gimp.ConvertPaletteType=None, num_cols: int=None, alpha_dither: bool=None, remove_unused: bool=None, palette: str=None):
        """Convert specified image to and Indexed image.
        
        This procedure converts the specified image to 'indexed' color. This
        process requires an image in RGB or Grayscale mode. The
        'palette_type' specifies what kind of palette to use, A type of
        '0' means to use an optimal palette of 'num_cols' generated from
        the colors in the image. A type of '1' means to re-use the
        previous palette (not currently implemented). A type of '2'
        means to use the so-called WWW-optimized palette. Type '3' means
        to use only black and white colors. A type of '4' means to use a
        palette from the gimp palettes directories. The 'dither type'
        specifies what kind of dithering to use. '0' means no dithering,
        '1' means standard Floyd-Steinberg error diffusion, '2' means
        Floyd-Steinberg error diffusion with reduced bleeding, '3' means
        dithering based on pixel location ('Fixed' dithering).
        
        Parameters:
        
        * image - The image.
        
        * dither_type (default: <enum GIMP_CONVERT_DITHER_NONE of type
          Gimp.ConvertDitherType>) - The dither type to use.
        
        * palette_type (default: <enum GIMP_CONVERT_PALETTE_GENERATE of type
          Gimp.ConvertPaletteType>) - The type of palette to use.
        
        * num_cols (default: 0) - The number of colors to quantize to, ignored
          unless (palette_type == GIMP_CONVERT_PALETTE_GENERATE).
        
        * alpha_dither (default: False) - Dither transparency to fake partial
          opacity.
        
        * remove_unused (default: False) - Remove unused or duplicate color
          entries from final palette, ignored if (palette_type ==
          GIMP_CONVERT_PALETTE_GENERATE).
        
        * palette - The name of the custom palette to use, ignored unless
          (palette_type == GIMP_CONVERT_PALETTE_CUSTOM).
        """
        pass

    def gimp_convert_rgb(self, image: Gimp.Image=None):
        """Convert specified image to RGB color.
        
        This procedure converts the specified image to RGB color. This process
        requires an image in Grayscale or Indexed color mode. No image
        content is lost in this process aside from the colormap for an
        indexed image.
        
        Parameters:
        
        * image - The image.
        """
        pass

    def gimp_convolve(self, drawable: Gimp.Drawable=None, pressure: float=None, convolve_type: Gimp.ConvolveType=None, num_strokes: int=None, strokes: Gimp.FloatArray=None):
        """Convolve (Blur, Sharpen) using the current brush.
        
        This tool convolves the specified drawable with either a sharpening or
        blurring kernel. The pressure parameter controls the magnitude
        of the operation. Like the paintbrush, this tool linearly
        interpolates between the specified stroke coordinates.
        
        Parameters:
        
        * drawable - The affected drawable.
        
        * pressure (default: 0.0) - The pressure.
        
        * convolve_type (default: <enum GIMP_CONVOLVE_BLUR of type
          Gimp.ConvolveType>) - Convolve type.
        
        * num_strokes (default: 2) - Number of stroke control points (count
          each coordinate as 2 points).
        
        * strokes - Array of stroke coordinates: { s1.x, s1.y, s2.x, s2.y,
          ..., sn.x, sn.y }.
        """
        pass

    def gimp_convolve_default(self, drawable: Gimp.Drawable=None, num_strokes: int=None, strokes: Gimp.FloatArray=None):
        """Convolve (Blur, Sharpen) using the current brush.
        
        This tool convolves the specified drawable with either a sharpening or
        blurring kernel. This function performs exactly the same as the
        'gimp-convolve' function except that the tools arguments are
        obtained from the convolve option dialog. It this dialog has not
        been activated then the dialogs default values will be used.
        
        Parameters:
        
        * drawable - The affected drawable.
        
        * num_strokes (default: 2) - Number of stroke control points (count
          each coordinate as 2 points).
        
        * strokes - Array of stroke coordinates: { s1.x, s1.y, s2.x, s2.y,
          ..., sn.x, sn.y }.
        """
        pass

    def gimp_crop(self, image: Gimp.Image=None, new_width: int=None, new_height: int=None, offx: int=None, offy: int=None):
        """Crop the image to the specified extents.
        
        This procedure crops the image so that it's new width and height are
        equal to the supplied parameters. Offsets are also provided
        which describe the position of the previous image's content. All
        channels and layers within the image are cropped to the new
        image extents; this includes the image selection mask. If any
        parameters are out of range, an error is returned.
        
        Parameters:
        
        * image - The image.
        
        * new_width (default: 1) - New image width: (0 < new_width <= width).
        
        * new_height (default: 1) - New image height: (0 < new_height <=
          height).
        
        * offx (default: 0) - X offset: (0 <= offx <= (width - new_width)).
        
        * offy (default: 0) - Y offset: (0 <= offy <= (height - new_height)).
        """
        pass

    def gimp_debug_timer_end(self) -> float:
        """Finishes measuring elapsed time.
        
        This procedure stops the timer started by a previous
        'gimp-debug-timer-start' call, and prints and returns the
        elapsed time. If there was already an active timer at the time
        of corresponding call to 'gimp-debug-timer-start', a dummy value
        is returned.
        
        This is a debug utility procedure. It is subject to change at any point,
        and should not be used in production.
        
        Returns:
        
        * elapsed (default: 0.0) - The elapsed time, in seconds.
        """
        pass

    def gimp_debug_timer_start(self):
        """Starts measuring elapsed time.
        
        This procedure starts a timer, measuring the elapsed time since the
        call. Each call to this procedure should be matched by a call to
        'gimp-debug-timer-end', which returns the elapsed time. If there
        is already an active timer, it is not affected by the call,
        however, a matching 'gimp-debug-timer-end' call is still
        required.
        
        This is a debug utility procedure. It is subject to change at any point,
        and should not be used in production.
        """
        pass

    def gimp_detach_parasite(self, name: str=None):
        """Removes a global parasite.
        
        This procedure detaches a global parasite from. It has no return values.
        
        Parameters:
        
        * name - The name of the parasite to detach.
        """
        pass

    def gimp_display_delete(self, display: Gimp.Display=None):
        """Delete the specified display.
        
        This procedure removes the specified display. If this is the last
        remaining display for the underlying image, then the image is
        deleted also. Note that the display is closed no matter if the
        image is dirty or not. Better save the image before calling this
        procedure.
        
        Parameters:
        
        * display - The display to delete.
        """
        pass

    def gimp_display_get_window_handle(self, display: Gimp.Display=None) -> GLib.Bytes:
        """Get a handle to the native window for an image display.
        
        This procedure returns a handle to the native window for a given image
        display. It can be different types of data depending on the
        platform you are running on. For example in the X backend of
        GDK, a native window handle is an Xlib XID whereas on Wayland,
        it is a string handle. A value of NULL is returned for an
        invalid display or if this function is unimplemented for the
        windowing system that is being used.
        
        Parameters:
        
        * display - The display to get the window handle from.
        
        Returns:
        
        * handle - The native window handle or NULL.
        """
        pass

    def gimp_display_id_is_valid(self, display_id: int=None) -> bool:
        """Returns TRUE if the display ID is valid.
        
        This procedure checks if the given display ID is valid and refers to an
        existing display.
        
        Parameters:
        
        * display_id (default: 0) - The display ID to check.
        
        Returns:
        
        * valid (default: False) - Whether the display ID is valid.
        """
        pass

    def gimp_display_new(self, image: Gimp.Image=None) -> Gimp.Display:
        """Create a new display for the specified image.
        
        Creates a new display for the specified image. If the image already has
        a display, another is added. Multiple displays are handled
        transparently by GIMP. The newly created display is returned and
        can be subsequently destroyed with a call to
        'gimp-display-delete'. This procedure only makes sense for use
        with the GIMP UI, and will result in an execution error if
        called when GIMP has no UI.
        
        Parameters:
        
        * image - The image.
        
        Returns:
        
        * display - The new display.
        """
        pass

    def gimp_display_present(self, display: Gimp.Display=None):
        """Present the specified display.
        
        This procedure presents the specified display at the top of the display
        stack.
        
        Parameters:
        
        * display - The display to present.
        """
        pass

    def gimp_displays_flush(self):
        """Flush all internal changes to the user interface.
        
        This procedure takes no arguments and returns nothing except a success
        status. Its purpose is to flush all pending updates of image
        manipulations to the user interface. It should be called
        whenever appropriate.
        """
        pass

    def gimp_displays_reconnect(self, old_image: Gimp.Image=None, new_image: Gimp.Image=None):
        """Reconnect displays from one image to another image.
        
        This procedure connects all displays of the old_image to the new_image.
        If the old_image has no display or new_image already has a
        display the reconnect is not performed and the procedure returns
        without success. You should rarely need to use this function.
        
        Parameters:
        
        * old_image - The old image (must have at least one display).
        
        * new_image - The new image (must not have a display).
        """
        pass

    def gimp_dodgeburn(self, drawable: Gimp.Drawable=None, exposure: float=None, dodgeburn_type: Gimp.DodgeBurnType=None, dodgeburn_mode: Gimp.TransferMode=None, num_strokes: int=None, strokes: Gimp.FloatArray=None):
        """Dodgeburn image with varying exposure.
        
        Dodgeburn. More details here later.
        
        Parameters:
        
        * drawable - The affected drawable.
        
        * exposure (default: 0.0) - The exposure of the strokes.
        
        * dodgeburn_type (default: <enum GIMP_DODGE_BURN_TYPE_DODGE of type
          Gimp.DodgeBurnType>) - The type either dodge or burn.
        
        * dodgeburn_mode (default: <enum GIMP_TRANSFER_SHADOWS of type
          Gimp.TransferMode>) - The mode.
        
        * num_strokes (default: 2) - Number of stroke control points (count
          each coordinate as 2 points).
        
        * strokes - Array of stroke coordinates: { s1.x, s1.y, s2.x, s2.y,
          ..., sn.x, sn.y }.
        """
        pass

    def gimp_dodgeburn_default(self, drawable: Gimp.Drawable=None, num_strokes: int=None, strokes: Gimp.FloatArray=None):
        """Dodgeburn image with varying exposure. This is the same as the
        gimp_dodgeburn() function except that the exposure, type and
        mode are taken from the tools option dialog. If the dialog
        has not been activated then the defaults as used by the
        dialog will be used.
        
        Dodgeburn. More details here later.
        
        Parameters:
        
        * drawable - The affected drawable.
        
        * num_strokes (default: 2) - Number of stroke control points (count
          each coordinate as 2 points).
        
        * strokes - Array of stroke coordinates: { s1.x, s1.y, s2.x, s2.y,
          ..., sn.x, sn.y }.
        """
        pass

    def gimp_drawable_brightness_contrast(self, drawable: Gimp.Drawable=None, brightness: float=None, contrast: float=None):
        """Modify brightness/contrast in the specified drawable.
        
        This procedures allows the brightness and contrast of the specified
        drawable to be modified. Both 'brightness' and 'contrast'
        parameters are defined between -1.0 and 1.0.
        
        Parameters:
        
        * drawable - The drawable.
        
        * brightness (default: -1.0) - Brightness adjustment.
        
        * contrast (default: -1.0) - Contrast adjustment.
        """
        pass

    def gimp_drawable_color_balance(self, drawable: Gimp.Drawable=None, transfer_mode: Gimp.TransferMode=None, preserve_lum: bool=None, cyan_red: float=None, magenta_green: float=None, yellow_blue: float=None):
        """Modify the color balance of the specified drawable.
        
        Modify the color balance of the specified drawable. There are three axis
        which can be modified: cyan-red, magenta-green, and yellow-blue.
        Negative values increase the amount of the former, positive
        values increase the amount of the latter. Color balance can be
        controlled with the 'transfer_mode' setting, which allows
        shadows, mid-tones, and highlights in an image to be affected
        differently. The 'preserve-lum' parameter, if TRUE, ensures that
        the luminosity of each pixel remains fixed.
        
        Parameters:
        
        * drawable - The drawable.
        
        * transfer_mode (default: <enum GIMP_TRANSFER_SHADOWS of type
          Gimp.TransferMode>) - Transfer mode.
        
        * preserve_lum (default: False) - Preserve luminosity values at each
          pixel.
        
        * cyan_red (default: -100.0) - Cyan-Red color balance.
        
        * magenta_green (default: -100.0) - Magenta-Green color balance.
        
        * yellow_blue (default: -100.0) - Yellow-Blue color balance.
        """
        pass

    def gimp_drawable_colorize_hsl(self, drawable: Gimp.Drawable=None, hue: float=None, saturation: float=None, lightness: float=None):
        """Render the drawable as a grayscale image seen through a colored
        glass.
        
        Desaturates the drawable, then tints it with the specified color. This
        tool is only valid on RGB color images. It will not operate on
        grayscale drawables.
        
        Parameters:
        
        * drawable - The drawable.
        
        * hue (default: 0.0) - Hue in degrees.
        
        * saturation (default: 0.0) - Saturation in percent.
        
        * lightness (default: -100.0) - Lightness in percent.
        """
        pass

    def gimp_drawable_curves_explicit(self, drawable: Gimp.Drawable=None, channel: Gimp.HistogramChannel=None, num_values: int=None, values: Gimp.FloatArray=None):
        """Modifies the intensity curve(s) for specified drawable.
        
        Modifies the intensity mapping for one channel in the specified
        drawable. The channel can be either an intensity component, or
        the value. The 'values' parameter is an array of doubles which
        explicitly defines how each pixel value in the drawable will be
        modified. Use the 'gimp-drawable-curves-spline' function to
        modify intensity levels with Catmull Rom splines.
        
        Parameters:
        
        * drawable - The drawable.
        
        * channel (default: <enum GIMP_HISTOGRAM_VALUE of type
          Gimp.HistogramChannel>) - The channel to modify.
        
        * num_values (default: 256) - The number of values in the new curve.
        
        * values - The explicit curve.
        """
        pass

    def gimp_drawable_curves_spline(self, drawable: Gimp.Drawable=None, channel: Gimp.HistogramChannel=None, num_points: int=None, points: Gimp.FloatArray=None):
        """Modifies the intensity curve(s) for specified drawable.
        
        Modifies the intensity mapping for one channel in the specified
        drawable. The channel can be either an intensity component, or
        the value. The 'points' parameter is an array of doubles which
        define a set of control points which describe a Catmull Rom
        spline which yields the final intensity curve. Use the
        'gimp-drawable-curves-explicit' function to explicitly modify
        intensity levels.
        
        Parameters:
        
        * drawable - The drawable.
        
        * channel (default: <enum GIMP_HISTOGRAM_VALUE of type
          Gimp.HistogramChannel>) - The channel to modify.
        
        * num_points (default: 4) - The number of values in the control point
          array.
        
        * points - The spline control points: { cp1.x, cp1.y, cp2.x, cp2.y,
          ... }.
        """
        pass

    def gimp_drawable_delete(self, item: Gimp.Item=None):
        """Delete a item.
        
        This procedure deletes the specified item. This must not be done if the
        image containing this item was already deleted or if the item
        was already removed from the image. The only case in which this
        procedure is useful is if you want to get rid of a item which
        has not yet been added to an image.
        
        Parameters:
        
        * item - The item to delete.
        """
        pass

    def gimp_drawable_desaturate(self, drawable: Gimp.Drawable=None, desaturate_mode: Gimp.DesaturateMode=None):
        """Desaturate the contents of the specified drawable, with the specified
        formula.
        
        This procedure desaturates the contents of the specified drawable, with
        the specified formula. This procedure only works on drawables of
        type RGB color.
        
        Parameters:
        
        * drawable - The drawable.
        
        * desaturate_mode (default: <enum GIMP_DESATURATE_LIGHTNESS of type
          Gimp.DesaturateMode>) - The formula to use to desaturate.
        """
        pass

    def gimp_drawable_edit_bucket_fill(self, drawable: Gimp.Drawable=None, fill_type: Gimp.FillType=None, x: float=None, y: float=None):
        """Fill the area by a seed fill starting at the specified coordinates.
        
        This procedure does a seed fill at the specified coordinates, using
        various parameters from the current context. In the case of
        merged sampling, the x and y coordinates are relative to the
        image's origin; otherwise, they are relative to the drawable's
        origin.
        
        This procedure is affected by the following context setters:
        'gimp-context-set-opacity', 'gimp-context-set-paint-mode',
        'gimp-context-set-foreground', 'gimp-context-set-background',
        'gimp-context-set-pattern', 'gimp-context-set-sample-threshold',
        'gimp-context-set-sample-merged',
        'gimp-context-set-sample-criterion',
        'gimp-context-set-diagonal-neighbors',
        'gimp-context-set-antialias'.
        
        Parameters:
        
        * drawable - The affected drawable.
        
        * fill_type (default: <enum GIMP_FILL_FOREGROUND of type
          Gimp.FillType>) - The type of fill.
        
        * x (default: 0.0) - The x coordinate of this bucket fill's
          application.
        
        * y (default: 0.0) - The y coordinate of this bucket fill's
          application.
        """
        pass

    def gimp_drawable_edit_clear(self, drawable: Gimp.Drawable=None):
        """Clear selected area of drawable.
        
        This procedure clears the specified drawable. If the drawable has an
        alpha channel, the cleared pixels will become transparent. If
        the drawable does not have an alpha channel, cleared pixels will
        be set to the background color. This procedure only affects
        regions within a selection if there is a selection active.
        
        This procedure is affected by the following context setters:
        'gimp-context-set-background'.
        
        Parameters:
        
        * drawable - The drawable to clear from.
        """
        pass

    def gimp_drawable_edit_fill(self, drawable: Gimp.Drawable=None, fill_type: Gimp.FillType=None):
        """Fill selected area of drawable.
        
        This procedure fills the specified drawable according to fill mode. This
        procedure only affects regions within a selection if there is a
        selection active. If you want to fill the whole drawable,
        regardless of the selection, use 'gimp-drawable-fill'.
        
        This procedure is affected by the following context setters:
        'gimp-context-set-opacity', 'gimp-context-set-paint-mode',
        'gimp-context-set-foreground', 'gimp-context-set-background',
        'gimp-context-set-pattern'.
        
        Parameters:
        
        * drawable - The drawable to fill to.
        
        * fill_type (default: <enum GIMP_FILL_FOREGROUND of type
          Gimp.FillType>) - The type of fill.
        """
        pass

    def gimp_drawable_edit_gradient_fill(self, drawable: Gimp.Drawable=None, gradient_type: Gimp.GradientType=None, offset: float=None, supersample: bool=None, supersample_max_depth: int=None, supersample_threshold: float=None, dither: bool=None, x1: float=None, y1: float=None, x2: float=None, y2: float=None):
        """Draw a gradient between the starting and ending coordinates with the
        specified gradient type.
        
        This tool requires information on the gradient type. It creates the
        specified variety of gradient using the starting and ending
        coordinates as defined for each gradient type. For shapeburst
        gradient types, the context's distance metric is also relevant
        and can be updated with 'gimp-context-set-distance-metric'.
        
        This procedure is affected by the following context setters:
        'gimp-context-set-opacity', 'gimp-context-set-paint-mode',
        'gimp-context-set-foreground', 'gimp-context-set-background',
        'gimp-context-set-gradient' and all gradient property settings,
        'gimp-context-set-distance-metric'.
        
        Parameters:
        
        * drawable - The affected drawable.
        
        * gradient_type (default: <enum GIMP_GRADIENT_LINEAR of type
          Gimp.GradientType>) - The type of gradient.
        
        * offset (default: 0.0) - Offset relates to the starting and ending
          coordinates specified for the blend. This parameter is mode
          dependent.
        
        * supersample (default: False) - Do adaptive supersampling.
        
        * supersample_max_depth (default: 1) - Maximum recursion levels for
          supersampling.
        
        * supersample_threshold (default: 0.0) - Supersampling threshold.
        
        * dither (default: False) - Use dithering to reduce banding.
        
        * x1 (default: 0.0) - The x coordinate of this gradient's starting
          point.
        
        * y1 (default: 0.0) - The y coordinate of this gradient's starting
          point.
        
        * x2 (default: 0.0) - The x coordinate of this gradient's ending
          point.
        
        * y2 (default: 0.0) - The y coordinate of this gradient's ending
          point.
        """
        pass

    def gimp_drawable_edit_stroke_item(self, drawable: Gimp.Drawable=None, item: Gimp.Item=None):
        """Stroke the specified item.
        
        This procedure strokes the specified item, painting along its outline
        (e.g. along a path, or along a channel's boundary), with the
        active paint method and brush, or using a plain line with
        configurable properties.
        
        This procedure is affected by the following context setters:
        'gimp-context-set-opacity', 'gimp-context-set-paint-mode',
        'gimp-context-set-paint-method',
        'gimp-context-set-stroke-method', 'gimp-context-set-foreground',
        'gimp-context-set-brush' and all brush property settings,
        'gimp-context-set-gradient' and all gradient property settings,
        'gimp-context-set-line-width' and all line property settings,
        'gimp-context-set-antialias'.
        
        Parameters:
        
        * drawable - The drawable to stroke to.
        
        * item - The item to stroke.
        """
        pass

    def gimp_drawable_edit_stroke_selection(self, drawable: Gimp.Drawable=None):
        """Stroke the current selection.
        
        This procedure strokes the current selection, painting along the
        selection boundary with the active paint method and brush, or
        using a plain line with configurable properties. The paint is
        applied to the specified drawable regardless of the active
        selection.
        
        This procedure is affected by the following context setters:
        'gimp-context-set-opacity', 'gimp-context-set-paint-mode',
        'gimp-context-set-paint-method',
        'gimp-context-set-stroke-method', 'gimp-context-set-foreground',
        'gimp-context-set-brush' and all brush property settings,
        'gimp-context-set-gradient' and all gradient property settings,
        'gimp-context-set-line-width' and all line property settings,
        'gimp-context-set-antialias'.
        
        Parameters:
        
        * drawable - The drawable to stroke to.
        """
        pass

    def gimp_drawable_equalize(self, drawable: Gimp.Drawable=None, mask_only: bool=None):
        """Equalize the contents of the specified drawable.
        
        This procedure equalizes the contents of the specified drawable. Each
        intensity channel is equalized independently. The equalized
        intensity is given as inten' = (255 - inten). The 'mask_only'
        option specifies whether to adjust only the area of the image
        within the selection bounds, or the entire image based on the
        histogram of the selected area. If there is no selection, the
        entire image is adjusted based on the histogram for the entire
        image.
        
        Parameters:
        
        * drawable - The drawable.
        
        * mask_only (default: False) - Equalization option.
        """
        pass

    def gimp_drawable_extract_component(self, drawable: Gimp.Drawable=None, component: int=None, invert: bool=None, linear: bool=None):
        """Extract a color model component.
        
        Extract a color model component.
        
        Parameters:
        
        * drawable - The drawable.
        
        * component (default: 0) - Component (RGB Red (0), RGB Green (1), RGB
          Blue (2), Hue (3), HSV Saturation (4), HSV Value (5), HSL
          Saturation (6), HSL Lightness (7), CMYK Cyan (8), CMYK
          Magenta (9), CMYK Yellow (10), CMYK Key (11), Y'CbCr Y'
          (12), Y'CbCr Cb (13), Y'CbCr Cr (14), LAB L (15), LAB A
          (16), LAB B (17), LCH C(ab) (18), LCH H(ab) (19), Alpha
          (20)).
        
        * invert (default: False) - Invert the extracted component.
        
        * linear (default: False) - Use linear output instead of gamma
          corrected.
        """
        pass

    def gimp_drawable_fill(self, drawable: Gimp.Drawable=None, fill_type: Gimp.FillType=None):
        """Fill the drawable with the specified fill mode.
        
        This procedure fills the drawable. If the fill mode is foreground the
        current foreground color is used. If the fill mode is
        background, the current background color is used. If the fill
        type is white, then white is used. Transparent fill only affects
        layers with an alpha channel, in which case the alpha channel is
        set to transparent. If the drawable has no alpha channel, it is
        filled to white. No fill leaves the drawable's contents
        undefined. This procedure is unlike 'gimp-drawable-edit-fill' or
        the bucket fill tool because it fills regardless of a selection.
        Its main purpose is to fill a newly created drawable before
        adding it to the image. This operation cannot be undone.
        
        Parameters:
        
        * drawable - The drawable.
        
        * fill_type (default: <enum GIMP_FILL_FOREGROUND of type
          Gimp.FillType>) - The type of fill.
        """
        pass

    def gimp_drawable_foreground_extract(self, drawable: Gimp.Drawable=None, mode: Gimp.ForegroundExtractMode=None, mask: Gimp.Drawable=None):
        """Extract the foreground of a drawable using a given trimap.
        
        Image Segmentation by Uniform Color Clustering, see
        https://www.inf.fu-berlin.de/inst/pubs/tr-b-05-07.pdf.
        
        Parameters:
        
        * drawable - The drawable.
        
        * mode (default: <enum GIMP_FOREGROUND_EXTRACT_MATTING of type
          Gimp.ForegroundExtractMode>) - The algorithm to use.
        
        * mask - Tri-Map.
        """
        pass

    def gimp_drawable_free_shadow(self, drawable: Gimp.Drawable=None):
        """Free the specified drawable's shadow data (if it exists).
        
        This procedure is intended as a memory saving device. If any shadow
        memory has been allocated, it will be freed automatically when
        the drawable is removed from the image, or when the plug-in
        procedure which allocated it returns.
        
        Parameters:
        
        * drawable - The drawable.
        """
        pass

    def gimp_drawable_get_bpp(self, drawable: Gimp.Drawable=None) -> int:
        """Returns the bytes per pixel.
        
        This procedure returns the number of bytes per pixel.
        
        Parameters:
        
        * drawable - The drawable.
        
        Returns:
        
        * bpp (default: 0) - Bytes per pixel.
        """
        pass

    def gimp_drawable_get_format(self, drawable: Gimp.Drawable=None) -> str:
        """Returns the drawable's Babl format.
        
        This procedure returns the drawable's Babl format. Note that the actual
        PDB procedure only transfers the format's encoding. In order to
        get to the real format, the libbgimp C wrapper must be used.
        
        Parameters:
        
        * drawable - The drawable.
        
        Returns:
        
        * format - The drawable's Babl format.
        """
        pass

    def gimp_drawable_get_height(self, drawable: Gimp.Drawable=None) -> int:
        """Returns the height of the drawable.
        
        This procedure returns the specified drawable's height in pixels.
        
        Parameters:
        
        * drawable - The drawable.
        
        Returns:
        
        * height (default: 0) - Height of drawable.
        """
        pass

    def gimp_drawable_get_image(self, item: Gimp.Item=None) -> Gimp.Image:
        """Returns the item's image.
        
        This procedure returns the item's image.
        
        Parameters:
        
        * item - The item.
        
        Returns:
        
        * image - The item's image.
        """
        pass

    def gimp_drawable_get_name(self, item: Gimp.Item=None) -> str:
        """Get the name of the specified item.
        
        This procedure returns the specified item's name.
        
        Parameters:
        
        * item - The item.
        
        Returns:
        
        * name - The item name.
        """
        pass

    def gimp_drawable_get_offsets(self, drawable: Gimp.Drawable=None) -> Tuple[int, int]:
        """Returns the offsets for the drawable.
        
        This procedure returns the specified drawable's offsets. This only makes
        sense if the drawable is a layer since channels are anchored.
        The offsets of a channel will be returned as 0.
        
        Parameters:
        
        * drawable - The drawable.
        
        Returns:
        
        * offset_x (default: 0) - x offset of drawable.
        
        * offset_y (default: 0) - y offset of drawable.
        """
        pass

    def gimp_drawable_get_pixel(self, drawable: Gimp.Drawable=None, x_coord: int=None, y_coord: int=None) -> Gegl.Color:
        """Gets the value of the pixel at the specified coordinates.
        
        This procedure gets the pixel value at the specified coordinates.
        
        Parameters:
        
        * drawable - The drawable.
        
        * x_coord (default: 0) - The x coordinate.
        
        * y_coord (default: 0) - The y coordinate.
        
        Returns:
        
        * color - The pixel color.
        """
        pass

    def gimp_drawable_get_tattoo(self, item: Gimp.Item=None) -> int:
        """Get the tattoo of the specified item.
        
        This procedure returns the specified item's tattoo. A tattoo is a unique
        and permanent identifier attached to a item that can be used to
        uniquely identify a item within an image even between sessions.
        
        Parameters:
        
        * item - The item.
        
        Returns:
        
        * tattoo (default: 1) - The item tattoo.
        """
        pass

    def gimp_drawable_get_thumbnail_format(self, drawable: Gimp.Drawable=None) -> str:
        """Returns the drawable's thumbnail Babl format.
        
        This procedure returns the drawable's thumbnail Babl format. Thumbnails
        are always 8-bit images, see 'gimp-drawable-thumbnail' and
        'gimp-drawable-sub-thmbnail'.
        
        Parameters:
        
        * drawable - The drawable.
        
        Returns:
        
        * format - The drawable's thumbnail Babl format.
        """
        pass

    def gimp_drawable_get_visible(self, item: Gimp.Item=None) -> bool:
        """Get the visibility of the specified item.
        
        This procedure returns the specified item's visibility.
        
        Parameters:
        
        * item - The item.
        
        Returns:
        
        * visible (default: False) - The item visibility.
        """
        pass

    def gimp_drawable_get_width(self, drawable: Gimp.Drawable=None) -> int:
        """Returns the width of the drawable.
        
        This procedure returns the specified drawable's width in pixels.
        
        Parameters:
        
        * drawable - The drawable.
        
        Returns:
        
        * width (default: 0) - Width of drawable.
        """
        pass

    def gimp_drawable_has_alpha(self, drawable: Gimp.Drawable=None) -> bool:
        """Returns TRUE if the drawable has an alpha channel.
        
        This procedure returns whether the specified drawable has an alpha
        channel. This can only be true for layers, and the associated
        type will be one of: { RGBA , GRAYA, INDEXEDA }.
        
        Parameters:
        
        * drawable - The drawable.
        
        Returns:
        
        * has_alpha (default: False) - Does the drawable have an alpha
          channel?.
        """
        pass

    def gimp_drawable_histogram(self, drawable: Gimp.Drawable=None, channel: Gimp.HistogramChannel=None, start_range: float=None, end_range: float=None) -> Tuple[float, float, float, float, float, float]:
        """Returns information on the intensity histogram for the specified
        drawable.
        
        This tool makes it possible to gather information about the intensity
        histogram of a drawable. A channel to examine is first
        specified. This can be either value, red, green, or blue,
        depending on whether the drawable is of type color or grayscale.
        Second, a range of intensities are specified. The
        'gimp-drawable-histogram' function returns statistics based on
        the pixels in the drawable that fall under this range of values.
        Mean, standard deviation, median, number of pixels, and
        percentile are all returned. Additionally, the total count of
        pixels in the image is returned. Counts of pixels are weighted
        by any associated alpha values and by the current selection
        mask. That is, pixels that lie outside an active selection mask
        will not be counted. Similarly, pixels with transparent alpha
        values will not be counted. The returned mean, std_dev and
        median are in the range (0..255) for 8-bit images or if the
        plug-in is not precision-aware, and in the range (0.0..1.0)
        otherwise.
        
        Parameters:
        
        * drawable - The drawable.
        
        * channel (default: <enum GIMP_HISTOGRAM_VALUE of type
          Gimp.HistogramChannel>) - The channel to query.
        
        * start_range (default: 0.0) - Start of the intensity measurement
          range.
        
        * end_range (default: 0.0) - End of the intensity measurement range.
        
        Returns:
        
        * mean (default: 0.0) - Mean intensity value.
        
        * std_dev (default: 0.0) - Standard deviation of intensity values.
        
        * median (default: 0.0) - Median intensity value.
        
        * pixels (default: 0.0) - Alpha-weighted pixel count for entire image.
        
        * count (default: 0.0) - Alpha-weighted pixel count for range.
        
        * percentile (default: 0.0) - Percentile that range falls under.
        """
        pass

    def gimp_drawable_hue_saturation(self, drawable: Gimp.Drawable=None, hue_range: Gimp.HueRange=None, hue_offset: float=None, lightness: float=None, saturation: float=None, overlap: float=None):
        """Modify hue, lightness, and saturation in the specified drawable.
        
        This procedure allows the hue, lightness, and saturation in the
        specified drawable to be modified. The 'hue-range' parameter
        provides the capability to limit range of affected hues. The
        'overlap' parameter provides blending into neighboring hue
        channels when rendering.
        
        Parameters:
        
        * drawable - The drawable.
        
        * hue_range (default: <enum GIMP_HUE_RANGE_ALL of type Gimp.HueRange>)
          - Range of affected hues.
        
        * hue_offset (default: -180.0) - Hue offset in degrees.
        
        * lightness (default: -100.0) - Lightness modification.
        
        * saturation (default: -100.0) - Saturation modification.
        
        * overlap (default: 0.0) - Overlap other hue channels.
        """
        pass

    def gimp_drawable_invert(self, drawable: Gimp.Drawable=None, linear: bool=None):
        """Invert the contents of the specified drawable.
        
        This procedure inverts the contents of the specified drawable. Each
        intensity channel is inverted independently. The inverted
        intensity is given as inten' = (255 - inten). If 'linear' is
        TRUE, the drawable is inverted in linear space.
        
        Parameters:
        
        * drawable - The drawable.
        
        * linear (default: False) - Whether to invert in linear space.
        """
        pass

    def gimp_drawable_is_gray(self, drawable: Gimp.Drawable=None) -> bool:
        """Returns whether the drawable is a grayscale type.
        
        This procedure returns TRUE if the specified drawable is of type { Gray,
        GrayA }.
        
        Parameters:
        
        * drawable - The drawable.
        
        Returns:
        
        * is_gray (default: False) - TRUE if the drawable is a grayscale type.
        """
        pass

    def gimp_drawable_is_indexed(self, drawable: Gimp.Drawable=None) -> bool:
        """Returns whether the drawable is an indexed type.
        
        This procedure returns TRUE if the specified drawable is of type {
        Indexed, IndexedA }.
        
        Parameters:
        
        * drawable - The drawable.
        
        Returns:
        
        * is_indexed (default: False) - TRUE if the drawable is an indexed
          type.
        """
        pass

    def gimp_drawable_is_rgb(self, drawable: Gimp.Drawable=None) -> bool:
        """Returns whether the drawable is an RGB type.
        
        This procedure returns TRUE if the specified drawable is of type { RGB,
        RGBA }.
        
        Parameters:
        
        * drawable - The drawable.
        
        Returns:
        
        * is_rgb (default: False) - TRUE if the drawable is an RGB type.
        """
        pass

    def gimp_drawable_levels(self, drawable: Gimp.Drawable=None, channel: Gimp.HistogramChannel=None, low_input: float=None, high_input: float=None, clamp_input: bool=None, gamma: float=None, low_output: float=None, high_output: float=None, clamp_output: bool=None):
        """Modifies intensity levels in the specified drawable.
        
        This tool allows intensity levels in the specified drawable to be
        remapped according to a set of parameters. The low/high input
        levels specify an initial mapping from the source intensities.
        The gamma value determines how intensities between the low and
        high input intensities are interpolated. A gamma value of 1.0
        results in a linear interpolation. Higher gamma values result in
        more high-level intensities. Lower gamma values result in more
        low-level intensities. The low/high output levels constrain the
        final intensity mapping--that is, no final intensity will be
        lower than the low output level and no final intensity will be
        higher than the high output level. This tool is only valid on
        RGB color and grayscale images.
        
        Parameters:
        
        * drawable - The drawable.
        
        * channel (default: <enum GIMP_HISTOGRAM_VALUE of type
          Gimp.HistogramChannel>) - The channel to modify.
        
        * low_input (default: 0.0) - Intensity of lowest input.
        
        * high_input (default: 0.0) - Intensity of highest input.
        
        * clamp_input (default: False) - Clamp input values before applying
          output levels.
        
        * gamma (default: 0.1) - Gamma adjustment factor.
        
        * low_output (default: 0.0) - Intensity of lowest output.
        
        * high_output (default: 0.0) - Intensity of highest output.
        
        * clamp_output (default: False) - Clamp final output values.
        """
        pass

    def gimp_drawable_levels_stretch(self, drawable: Gimp.Drawable=None):
        """Automatically modifies intensity levels in the specified drawable.
        
        This procedure allows intensity levels in the specified drawable to be
        remapped according to a set of guessed parameters. It is
        equivalent to clicking the "Auto" button in the Levels tool.
        
        Parameters:
        
        * drawable - The drawable.
        """
        pass

    def gimp_drawable_mask_bounds(self, drawable: Gimp.Drawable=None) -> Tuple[bool, int, int, int, int]:
        """Find the bounding box of the current selection in relation to the
        specified drawable.
        
        This procedure returns whether there is a selection. If there is one,
        the upper left and lower right-hand corners of its bounding box
        are returned. These coordinates are specified relative to the
        drawable's origin, and bounded by the drawable's extents. Please
        note that the pixel specified by the lower right-hand coordinate
        of the bounding box is not part of the selection. The selection
        ends at the upper left corner of this pixel. This means the
        width of the selection can be calculated as (x2 - x1), its
        height as (y2 - y1). Note that the returned boolean does NOT
        correspond with the returned region being empty or not, it
        always returns whether the selection is non_empty. See
        'gimp-drawable-mask-intersect' for a boolean return value which
        is more useful in most cases.
        
        Parameters:
        
        * drawable - The drawable.
        
        Returns:
        
        * non_empty (default: False) - TRUE if there is a selection.
        
        * x1 (default: 0) - x coordinate of the upper left corner of selection
          bounds.
        
        * y1 (default: 0) - y coordinate of the upper left corner of selection
          bounds.
        
        * x2 (default: 0) - x coordinate of the lower right corner of
          selection bounds.
        
        * y2 (default: 0) - y coordinate of the lower right corner of
          selection bounds.
        """
        pass

    def gimp_drawable_mask_intersect(self, drawable: Gimp.Drawable=None) -> Tuple[bool, int, int, int, int]:
        """Find the bounding box of the current selection in relation to the
        specified drawable.
        
        This procedure returns whether there is an intersection between the
        drawable and the selection. Unlike 'gimp-drawable-mask-bounds',
        the intersection's bounds are returned as x, y, width, height.
        If there is no selection this function returns TRUE and the
        returned bounds are the extents of the whole drawable.
        
        Parameters:
        
        * drawable - The drawable.
        
        Returns:
        
        * non_empty (default: False) - TRUE if the returned area is not empty.
        
        * x (default: 0) - x coordinate of the upper left corner of the
          intersection.
        
        * y (default: 0) - y coordinate of the upper left corner of the
          intersection.
        
        * width (default: 0) - width of the intersection.
        
        * height (default: 0) - height of the intersection.
        """
        pass

    def gimp_drawable_merge_filters(self, drawable: Gimp.Drawable=None):
        """Merge the layer effect filters to the specified drawable.
        
        This procedure combines the contents of the drawable's filter stack (for
        export) with the specified drawable.
        
        Parameters:
        
        * drawable - The drawable.
        """
        pass

    def gimp_drawable_merge_shadow(self, drawable: Gimp.Drawable=None, undo: bool=None):
        """Merge the shadow buffer with the specified drawable.
        
        This procedure combines the contents of the drawable's shadow buffer
        (for temporary processing) with the specified drawable. The
        'undo' parameter specifies whether to add an undo step for the
        operation. Requesting no undo is useful for such applications as
        'auto-apply'.
        
        Parameters:
        
        * drawable - The drawable.
        
        * undo (default: False) - Push merge to undo stack?.
        """
        pass

    def gimp_drawable_offset(self, drawable: Gimp.Drawable=None, wrap_around: bool=None, fill_type: Gimp.OffsetType=None, offset_x: int=None, offset_y: int=None):
        """Offset the drawable by the specified amounts in the X and Y
        directions.
        
        This procedure offsets the specified drawable by the amounts specified
        by 'offset_x' and 'offset_y'. If 'wrap_around' is set to TRUE,
        then portions of the drawable which are offset out of bounds are
        wrapped around. Alternatively, the undefined regions of the
        drawable can be filled with transparency or the background
        color, as specified by the 'fill-type' parameter.
        
        Parameters:
        
        * drawable - The drawable to offset.
        
        * wrap_around (default: False) - wrap image around or fill vacated
          regions.
        
        * fill_type (default: <enum GIMP_OFFSET_BACKGROUND of type
          Gimp.OffsetType>) - fill vacated regions of drawable with
          background or transparent.
        
        * offset_x (default: 0) - offset by this amount in X direction.
        
        * offset_y (default: 0) - offset by this amount in Y direction.
        """
        pass

    def gimp_drawable_parasite_attach(self, item: Gimp.Item=None, parasite: Gimp.Parasite=None):
        """Add a parasite to an item.
        
        This procedure attaches a parasite to an item. It has no return values.
        
        Parameters:
        
        * item - The item.
        
        * parasite - The parasite to attach to the item.
        """
        pass

    def gimp_drawable_parasite_detach(self, item: Gimp.Item=None, name: str=None):
        """Removes a parasite from an item.
        
        This procedure detaches a parasite from an item. It has no return
        values.
        
        Parameters:
        
        * item - The item.
        
        * name - The name of the parasite to detach from the item.
        """
        pass

    def gimp_drawable_parasite_find(self, item: Gimp.Item=None, name: str=None) -> Gimp.Parasite:
        """Look up a parasite in an item.
        
        Finds and returns the parasite that is attached to an item.
        
        Parameters:
        
        * item - The item.
        
        * name - The name of the parasite to find.
        
        Returns:
        
        * parasite - The found parasite.
        """
        pass

    def gimp_drawable_parasite_list(self, item: Gimp.Item=None) -> List[str]:
        """List all parasites.
        
        Returns a list of all parasites currently attached the an item.
        
        Parameters:
        
        * item - The item.
        
        Returns:
        
        * parasites - The names of currently attached parasites.
        """
        pass

    def gimp_drawable_posterize(self, drawable: Gimp.Drawable=None, levels: int=None):
        """Posterize the specified drawable.
        
        This procedures reduces the number of shades allows in each intensity
        channel to the specified 'levels' parameter.
        
        Parameters:
        
        * drawable - The drawable.
        
        * levels (default: 2) - Levels of posterization.
        """
        pass

    def gimp_drawable_set_name(self, item: Gimp.Item=None, name: str=None):
        """Set the name of the specified item.
        
        This procedure sets the specified item's name.
        
        Parameters:
        
        * item - The item.
        
        * name - The new item name.
        """
        pass

    def gimp_drawable_set_pixel(self, drawable: Gimp.Drawable=None, x_coord: int=None, y_coord: int=None, color: Gegl.Color=None):
        """Sets the value of the pixel at the specified coordinates.
        
        This procedure sets the pixel value at the specified coordinates. Note
        that this function is not undoable, you should use it only on
        drawables you just created yourself.
        
        Parameters:
        
        * drawable - The drawable.
        
        * x_coord (default: 0) - The x coordinate.
        
        * y_coord (default: 0) - The y coordinate.
        
        * color - The pixel color.
        """
        pass

    def gimp_drawable_set_tattoo(self, item: Gimp.Item=None, tattoo: int=None):
        """Set the tattoo of the specified item.
        
        This procedure sets the specified item's tattoo. A tattoo is a unique
        and permanent identifier attached to a item that can be used to
        uniquely identify a item within an image even between sessions.
        
        Parameters:
        
        * item - The item.
        
        * tattoo (default: 1) - The new item tattoo.
        """
        pass

    def gimp_drawable_set_visible(self, item: Gimp.Item=None, visible: bool=None):
        """Set the visibility of the specified item.
        
        This procedure sets the specified item's visibility.
        
        Parameters:
        
        * item - The item.
        
        * visible (default: False) - The new item visibility.
        """
        pass

    def gimp_drawable_shadows_highlights(self, drawable: Gimp.Drawable=None, shadows: float=None, highlights: float=None, whitepoint: float=None, radius: float=None, compress: float=None, shadows_ccorrect: float=None, highlights_ccorrect: float=None):
        """Perform shadows and highlights correction.
        
        This filter allows adjusting shadows and highlights in the image
        separately. The implementation closely follow its counterpart in
        the Darktable photography software.
        
        Parameters:
        
        * drawable - The drawable.
        
        * shadows (default: -100.0) - Adjust exposure of shadows.
        
        * highlights (default: -100.0) - Adjust exposure of highlights.
        
        * whitepoint (default: -10.0) - Shift white point.
        
        * radius (default: 0.1) - Spatial extent.
        
        * compress (default: 0.0) - Compress the effect on shadows/highlights
          and preserve midtones.
        
        * shadows_ccorrect (default: 0.0) - Adjust saturation of shadows.
        
        * highlights_ccorrect (default: 0.0) - Adjust saturation of
          highlights.
        """
        pass

    def gimp_drawable_sub_thumbnail(self, drawable: Gimp.Drawable=None, src_x: int=None, src_y: int=None, src_width: int=None, src_height: int=None, dest_width: int=None, dest_height: int=None) -> Tuple[int, int, int, GLib.Bytes]:
        """Get a thumbnail of a sub-area of a drawable drawable.
        
        This function gets data from which a thumbnail of a drawable preview can
        be created. Maximum x or y dimension is 1024 pixels. The pixels
        are returned in RGB[A] or GRAY[A] format. The bpp return value
        gives the number of bytes in the image.
        
        Parameters:
        
        * drawable - The drawable.
        
        * src_x (default: 0) - The x coordinate of the area.
        
        * src_y (default: 0) - The y coordinate of the area.
        
        * src_width (default: 1) - The width of the area.
        
        * src_height (default: 1) - The height of the area.
        
        * dest_width (default: 1) - The thumbnail width.
        
        * dest_height (default: 1) - The thumbnail height.
        
        Returns:
        
        * width (default: 0) - The previews width.
        
        * height (default: 0) - The previews height.
        
        * bpp (default: 0) - The previews bpp.
        
        * thumbnail_data - The thumbnail data.
        """
        pass

    def gimp_drawable_threshold(self, drawable: Gimp.Drawable=None, channel: Gimp.HistogramChannel=None, low_threshold: float=None, high_threshold: float=None):
        """Threshold the specified drawable.
        
        This procedures generates a threshold map of the specified drawable. All
        pixels between the values of 'low_threshold' and
        'high_threshold', on the scale of 'channel' are replaced with
        white, and all other pixels with black.
        
        Parameters:
        
        * drawable - The drawable.
        
        * channel (default: <enum GIMP_HISTOGRAM_VALUE of type
          Gimp.HistogramChannel>) - The channel to base the threshold
          on.
        
        * low_threshold (default: 0.0) - The low threshold value.
        
        * high_threshold (default: 0.0) - The high threshold value.
        """
        pass

    def gimp_drawable_thumbnail(self, drawable: Gimp.Drawable=None, width: int=None, height: int=None) -> Tuple[int, int, int, GLib.Bytes]:
        """Get a thumbnail of a drawable.
        
        This function gets data from which a thumbnail of a drawable preview can
        be created. Maximum x or y dimension is 1024 pixels. The pixels
        are returned in RGB[A] or GRAY[A] format. The bpp return value
        gives the number of bytes in the image.
        
        Parameters:
        
        * drawable - The drawable.
        
        * width (default: 1) - The requested thumbnail width.
        
        * height (default: 1) - The requested thumbnail height.
        
        Returns:
        
        * actual_width (default: 0) - The previews width.
        
        * actual_height (default: 0) - The previews height.
        
        * bpp (default: 0) - The previews bpp.
        
        * thumbnail_data - The thumbnail data.
        """
        pass

    def gimp_drawable_type(self, drawable: Gimp.Drawable=None) -> Gimp.ImageType:
        """Returns the drawable's type.
        
        This procedure returns the drawable's type.
        
        Parameters:
        
        * drawable - The drawable.
        
        Returns:
        
        * type (default: <enum GIMP_RGB_IMAGE of type Gimp.ImageType>) - The
          drawable's type.
        """
        pass

    def gimp_drawable_type_with_alpha(self, drawable: Gimp.Drawable=None) -> Gimp.ImageType:
        """Returns the drawable's type with alpha.
        
        This procedure returns the drawable's type as if had an alpha channel.
        If the type is currently Gray, for instance, the returned type
        would be GrayA. If the drawable already has an alpha channel,
        the drawable's type is simply returned.
        
        Parameters:
        
        * drawable - The drawable.
        
        Returns:
        
        * type_with_alpha (default: <enum GIMP_RGB_IMAGE of type
          Gimp.ImageType>) - The drawable's type with alpha.
        """
        pass

    def gimp_drawable_update(self, drawable: Gimp.Drawable=None, x: int=None, y: int=None, width: int=None, height: int=None):
        """Update the specified region of the drawable.
        
        This procedure updates the specified region of the drawable. The (x, y)
        coordinate pair is relative to the drawable's origin, not to the
        image origin. Therefore, the entire drawable can be updated
        using (0, 0, width, height).
        
        Parameters:
        
        * drawable - The drawable.
        
        * x (default: 0) - x coordinate of upper left corner of update region.
        
        * y (default: 0) - y coordinate of upper left corner of update region.
        
        * width (default: 0) - Width of update region.
        
        * height (default: 0) - Height of update region.
        """
        pass

    def gimp_drawables_close_popup(self, callback: str=None):
        """Close the drawable selection dialog.
        
        Closes an open drawable selection dialog.
        
        Parameters:
        
        * callback - The name of the callback registered for this pop-up.
        """
        pass

    def gimp_drawables_popup(self, callback: str=None, popup_title: str=None, drawable_type: str=None, initial_drawable: Gimp.Drawable=None, parent_window: GLib.Bytes=None):
        """Invokes the drawable selection dialog.
        
        Opens a dialog letting a user choose an drawable.
        
        Parameters:
        
        * callback - The callback PDB proc to call when user chooses an
          drawable.
        
        * popup_title - Title of the drawable selection dialog.
        
        * drawable_type - The name of the GIMP_TYPE_DRAWABLE subtype.
        
        * initial_drawable - The drawable to set as the initial choice.
        
        * parent_window - An optional parent window handle for the popup to be
          set transient to.
        """
        pass

    def gimp_drawables_set_popup(self, callback: str=None, drawable: Gimp.Drawable=None):
        """Sets the selected drawable in a drawable selection dialog.
        
        Sets the selected drawable in a drawable selection dialog.
        
        Parameters:
        
        * callback - The name of the callback registered for this pop-up.
        
        * drawable - The drawable to set as selected.
        """
        pass

    def gimp_dynamics_get_list(self, filter: str=None) -> List[str]:
        """Retrieve the list of loaded paint dynamics.
        
        This procedure returns a list of the paint dynamics that are currently
        available.
        
        Parameters:
        
        * filter - An optional regular expression used to filter the list.
        
        Returns:
        
        * dynamics_list - The list of paint dynamics names.
        """
        pass

    def gimp_dynamics_refresh(self):
        """Refresh current paint dynamics. This function always succeeds.
        
        This procedure retrieves all paint dynamics currently in the user's
        paint dynamics path and updates the paint dynamics dialogs
        accordingly.
        """
        pass

    def gimp_edit_copy(self, num_drawables: int=None, drawables: Gimp.ObjectArray=None) -> bool:
        """Copy from the specified drawables.
        
        If there is a selection in the image, then the area specified by the
        selection is copied from the specified drawables and placed in
        an internal GIMP edit buffer. It can subsequently be retrieved
        using the 'gimp-edit-paste' command. If there is no selection,
        then the specified drawables' contents will be stored in the
        internal GIMP edit buffer. This procedure will fail if the
        selected area lies completely outside the bounds of the current
        drawables and there is nothing to copy from. All the drawables
        must belong to the same image.
        
        Parameters:
        
        * num_drawables (default: 1) - The number of drawables to save.
        
        * drawables - Drawables to copy from.
        
        Returns:
        
        * non_empty (default: False) - TRUE if the cut was successful, FALSE
          if there was nothing to copy from.
        """
        pass

    def gimp_edit_copy_visible(self, image: Gimp.Image=None) -> bool:
        """Copy from the projection.
        
        If there is a selection in the image, then the area specified by the
        selection is copied from the projection and placed in an
        internal GIMP edit buffer. It can subsequently be retrieved
        using the 'gimp-edit-paste' command. If there is no selection,
        then the projection's contents will be stored in the internal
        GIMP edit buffer.
        
        Parameters:
        
        * image - The image to copy from.
        
        Returns:
        
        * non_empty (default: False) - TRUE if the copy was successful.
        """
        pass

    def gimp_edit_cut(self, num_drawables: int=None, drawables: Gimp.ObjectArray=None) -> bool:
        """Cut from the specified drawables.
        
        If there is a selection in the image, then the area specified by the
        selection is cut from the specified drawables and placed in an
        internal GIMP edit buffer. It can subsequently be retrieved
        using the 'gimp-edit-paste' command. If there is no selection
        and only one specified drawable, then the specified drawable
        will be removed and its contents stored in the internal GIMP
        edit buffer. This procedure will fail if the selected area lies
        completely outside the bounds of the current drawables and there
        is nothing to cut from.
        
        Parameters:
        
        * num_drawables (default: 1) - The number of drawables.
        
        * drawables - The drawables to cut from.
        
        Returns:
        
        * non_empty (default: False) - TRUE if the cut was successful, FALSE
          if there was nothing to copy from.
        """
        pass

    def gimp_edit_named_copy(self, num_drawables: int=None, drawables: Gimp.ObjectArray=None, buffer_name: str=None) -> str:
        """Copy into a named buffer.
        
        This procedure works like 'gimp-edit-copy', but additionally stores the
        copied buffer into a named buffer that will stay available for
        later pasting, regardless of any intermediate copy or cut
        operations.
        
        Parameters:
        
        * num_drawables (default: 1) - The number of drawables.
        
        * drawables - The drawables to copy from.
        
        * buffer_name - The name of the buffer to create.
        
        Returns:
        
        * real_name - The real name given to the buffer, or NULL if the copy
          failed.
        """
        pass

    def gimp_edit_named_copy_visible(self, image: Gimp.Image=None, buffer_name: str=None) -> str:
        """Copy from the projection into a named buffer.
        
        This procedure works like 'gimp-edit-copy-visible', but additionally
        stores the copied buffer into a named buffer that will stay
        available for later pasting, regardless of any intermediate copy
        or cut operations.
        
        Parameters:
        
        * image - The image to copy from.
        
        * buffer_name - The name of the buffer to create.
        
        Returns:
        
        * real_name - The real name given to the buffer, or NULL if the copy
          failed.
        """
        pass

    def gimp_edit_named_cut(self, num_drawables: int=None, drawables: Gimp.ObjectArray=None, buffer_name: str=None) -> str:
        """Cut into a named buffer.
        
        This procedure works like 'gimp-edit-cut', but additionally stores the
        cut buffer into a named buffer that will stay available for
        later pasting, regardless of any intermediate copy or cut
        operations.
        
        Parameters:
        
        * num_drawables (default: 1) - The number of drawables.
        
        * drawables - The drawables to cut from.
        
        * buffer_name - The name of the buffer to create.
        
        Returns:
        
        * real_name - The real name given to the buffer, or NULL if the cut
          failed.
        """
        pass

    def gimp_edit_named_paste(self, drawable: Gimp.Drawable=None, buffer_name: str=None, paste_into: bool=None) -> Gimp.Layer:
        """Paste named buffer to the specified drawable.
        
        This procedure works like 'gimp-edit-paste' but pastes a named buffer
        instead of the global buffer.
        
        Parameters:
        
        * drawable - The drawable to paste to.
        
        * buffer_name - The name of the buffer to paste.
        
        * paste_into (default: False) - Clear selection, or paste behind it?.
        
        Returns:
        
        * floating_sel - The new floating selection.
        """
        pass

    def gimp_edit_named_paste_as_new(self, buffer_name: str=None) -> Gimp.Image:
        """Paste named buffer to a new image.
        
        This procedure works like 'gimp-edit-paste-as-new-image' but pastes a
        named buffer instead of the global buffer.
        
        Parameters:
        
        * buffer_name - The name of the buffer to paste.
        
        Returns:
        
        * image - The new image.
        """
        pass

    def gimp_edit_named_paste_as_new_image(self, buffer_name: str=None) -> Gimp.Image:
        """Paste named buffer to a new image.
        
        This procedure works like 'gimp-edit-paste-as-new-image' but pastes a
        named buffer instead of the global buffer.
        
        Parameters:
        
        * buffer_name - The name of the buffer to paste.
        
        Returns:
        
        * image - The new image.
        """
        pass

    def gimp_edit_paste(self, drawable: Gimp.Drawable=None, paste_into: bool=None) -> Tuple[int, Gimp.ObjectArray]:
        """Paste buffer to the specified drawable.
        
        This procedure pastes a copy of the internal GIMP edit buffer to the
        specified drawable. The GIMP edit buffer will be empty unless a
        call was previously made to either 'gimp-edit-cut' or
        'gimp-edit-copy'. The "paste_into" option specifies whether to
        clear the current image selection, or to paste the buffer
        "behind" the selection. This allows the selection to act as a
        mask for the pasted buffer. Anywhere that the selection mask is
        non-zero, the pasted buffer will show through. The pasted data
        may be a floating selection when relevant, layers otherwise. If
        the image has a floating selection at the time of pasting, the
        old floating selection will be anchored to its drawable before
        the new floating selection is added. This procedure returns the
        new layers (floating or not). If the result is a floating
        selection, it will already be attached to the specified
        drawable, and a subsequent call to floating_sel_attach is not
        needed.
        
        Parameters:
        
        * drawable - The drawable to paste to.
        
        * paste_into (default: False) - Clear selection, or paste behind it?.
        
        Returns:
        
        * num_layers (default: 0) - The newly pasted layers.
        
        * layers - The list of pasted layers.
        """
        pass

    def gimp_edit_paste_as_new(self) -> Gimp.Image:
        """Paste buffer to a new image.
        
        This procedure pastes a copy of the internal GIMP edit buffer to a new
        image. The GIMP edit buffer will be empty unless a call was
        previously made to either 'gimp-edit-cut' or 'gimp-edit-copy'.
        This procedure returns the new image or -1 if the edit buffer
        was empty.
        
        Returns:
        
        * image - The new image.
        """
        pass

    def gimp_edit_paste_as_new_image(self) -> Gimp.Image:
        """Paste buffer to a new image.
        
        This procedure pastes a copy of the internal GIMP edit buffer to a new
        image. The GIMP edit buffer will be empty unless a call was
        previously made to either 'gimp-edit-cut' or 'gimp-edit-copy'.
        This procedure returns the new image or -1 if the edit buffer
        was empty.
        
        Returns:
        
        * image - The new image.
        """
        pass

    def gimp_eraser(self, drawable: Gimp.Drawable=None, num_strokes: int=None, strokes: Gimp.FloatArray=None, hardness: Gimp.BrushApplicationMode=None, method: Gimp.PaintApplicationMode=None):
        """Erase using the current brush.
        
        This tool erases using the current brush mask. If the specified drawable
        contains an alpha channel, then the erased pixels will become
        transparent. Otherwise, the eraser tool replaces the contents of
        the drawable with the background color. Like paintbrush, this
        tool linearly interpolates between the specified stroke
        coordinates.
        
        Parameters:
        
        * drawable - The affected drawable.
        
        * num_strokes (default: 2) - Number of stroke control points (count
          each coordinate as 2 points).
        
        * strokes - Array of stroke coordinates: { s1.x, s1.y, s2.x, s2.y,
          ..., sn.x, sn.y }.
        
        * hardness (default: <enum GIMP_BRUSH_HARD of type
          Gimp.BrushApplicationMode>) - How to apply the brush.
        
        * method (default: <enum GIMP_PAINT_CONSTANT of type
          Gimp.PaintApplicationMode>) - The paint method to use.
        """
        pass

    def gimp_eraser_default(self, drawable: Gimp.Drawable=None, num_strokes: int=None, strokes: Gimp.FloatArray=None):
        """Erase using the current brush.
        
        This tool erases using the current brush mask. This function performs
        exactly the same as the 'gimp-eraser' function except that the
        tools arguments are obtained from the eraser option dialog. It
        this dialog has not been activated then the dialogs default
        values will be used.
        
        Parameters:
        
        * drawable - The affected drawable.
        
        * num_strokes (default: 2) - Number of stroke control points (count
          each coordinate as 2 points).
        
        * strokes - Array of stroke coordinates: { s1.x, s1.y, s2.x, s2.y,
          ..., sn.x, sn.y }.
        """
        pass

    def gimp_file_load(self, file: Gio.File=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE) -> Gimp.Image:
        """Loads an image file by invoking the right load handler.
        
        This procedure invokes the correct file load handler using magic if
        possible, and falling back on the file's extension and/or prefix
        if not.
        
        Parameters:
        
        * file - The file to load.
        
        Returns:
        
        * image - The output image.
        """
        pass

    def gimp_file_load_layer(self, image: Gimp.Image=None, file: Gio.File=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE) -> Gimp.Layer:
        """Loads an image file as a layer for an existing image.
        
        This procedure behaves like the file-load procedure but opens the
        specified image as a layer for an existing image. The returned
        layer needs to be added to the existing image with
        'gimp-image-insert-layer'.
        
        Parameters:
        
        * image - Destination image.
        
        * file - The file to load.
        
        Returns:
        
        * layer - The layer created when loading the image file.
        """
        pass

    def gimp_file_load_layers(self, image: Gimp.Image=None, file: Gio.File=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE) -> Tuple[int, Gimp.ObjectArray]:
        """Loads an image file as layers for an existing image.
        
        This procedure behaves like the file-load procedure but opens the
        specified image as layers for an existing image. The returned
        layers needs to be added to the existing image with
        'gimp-image-insert-layer'.
        
        Parameters:
        
        * image - Destination image.
        
        * file - The file to load.
        
        Returns:
        
        * num_layers (default: 0) - The number of loaded layers.
        
        * layers - The list of loaded layers.
        """
        pass

    def gimp_file_load_thumbnail(self, file: Gio.File=None) -> Tuple[int, int, GLib.Bytes]:
        """Loads the thumbnail for a file.
        
        This procedure tries to load a thumbnail that belongs to the given file.
        The returned data is an array of colordepth 3 (RGB), regardless
        of the image type. Width and height of the thumbnail are also
        returned. Don't use this function if you need a thumbnail of an
        already opened image, use 'gimp-image-thumbnail' instead.
        
        Parameters:
        
        * file - The file that owns the thumbnail to load.
        
        Returns:
        
        * width (default: 0) - The width of the thumbnail.
        
        * height (default: 0) - The height of the thumbnail.
        
        * thumb_data - The thumbnail data.
        """
        pass

    def gimp_file_save(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, file: Gio.File=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Saves a file by extension.
        
        This procedure invokes the correct file save handler according to the
        file's extension and/or prefix.
        
        Parameters:
        
        * image - Input image.
        
        * num_drawables (default: 1) - The number of drawables to save.
        
        * drawables - Drawables to save.
        
        * file - The file to save the image in.
        """
        pass

    def gimp_file_save_thumbnail(self, image: Gimp.Image=None, file: Gio.File=None):
        """Saves a thumbnail for the given image.
        
        This procedure saves a thumbnail for the given image according to the
        Free Desktop Thumbnail Managing Standard. The thumbnail is saved
        so that it belongs to the given file. This means you have to
        save the image under this name first, otherwise this procedure
        will fail. This procedure may become useful if you want to
        explicitly save a thumbnail with a file.
        
        Parameters:
        
        * image - The image.
        
        * file - The file the thumbnail belongs to.
        """
        pass

    def gimp_floating_sel_anchor(self, floating_sel: Gimp.Layer=None):
        """Anchor the specified floating selection to its associated drawable.
        
        This procedure anchors the floating selection to its associated
        drawable. This is similar to merging with a merge type of
        ClipToBottomLayer. The floating selection layer is no longer
        valid after this operation.
        
        Parameters:
        
        * floating_sel - The floating selection.
        """
        pass

    def gimp_floating_sel_attach(self, layer: Gimp.Layer=None, drawable: Gimp.Drawable=None):
        """Attach the specified layer as floating to the specified drawable.
        
        This procedure attaches the layer as floating selection to the drawable.
        
        Parameters:
        
        * layer - The layer (is attached as floating selection).
        
        * drawable - The drawable (where to attach the floating selection).
        """
        pass

    def gimp_floating_sel_remove(self, floating_sel: Gimp.Layer=None):
        """Remove the specified floating selection from its associated drawable.
        
        This procedure removes the floating selection completely, without any
        side effects. The associated drawable is then set to active.
        
        Parameters:
        
        * floating_sel - The floating selection.
        """
        pass

    def gimp_floating_sel_to_layer(self, floating_sel: Gimp.Layer=None):
        """Transforms the specified floating selection into a layer.
        
        This procedure transforms the specified floating selection into a layer
        with the same offsets and extents. The composited image will
        look precisely the same, but the floating selection layer will
        no longer be clipped to the extents of the drawable it was
        attached to. The floating selection will become the active
        layer. This procedure will not work if the floating selection
        has a different base type from the underlying image. This might
        be the case if the floating selection is above an auxiliary
        channel or a layer mask.
        
        Parameters:
        
        * floating_sel - The floating selection.
        """
        pass

    def gimp_font_get_by_name(self, name: str=None) -> Gimp.Font:
        """Returns a font with the given name.
        
        If several fonts are named identically, the one which is returned by
        this function should be considered random. This can be used when
        you know you won't have multiple fonts of this name or that you
        don't want to choose (non-interactive scripts, etc.). If you
        need more control, you should use 'gimp-fonts-get-by-name'
        instead.
        
        Parameters:
        
        * name - The name of the font.
        
        Returns:
        
        * font - The font.
        """
        pass

    def gimp_font_get_lookup_name(self, font: Gimp.Font=None) -> str:
        """Retrieve the font lookup name.
        
        Retrieve the font lookup name.
        
        Parameters:
        
        * font - GimpFont object.
        
        Returns:
        
        * lookup_name - font lookup name.
        """
        pass

    def gimp_fonts_close_popup(self, font_callback: str=None):
        """Close the font selection dialog.
        
        Closes an open font selection dialog.
        
        Parameters:
        
        * font_callback - The name of the callback registered in the PDB for
          this dialog.
        """
        pass

    def gimp_fonts_get_by_name(self, name: str=None) -> Tuple[int, Gimp.ObjectArray]:
        """Returns the fonts with the given name.
        
        Returns the fonts with the given name. There may be more than one.
        
        Parameters:
        
        * name - The name of the font.
        
        Returns:
        
        * num_fonts (default: 0) - The number of fonts with the given name.
        
        * fonts - The fonts with the given name.
        """
        pass

    def gimp_fonts_get_custom_configs(self) -> Tuple[str, str, str, List[str]]:
        """Retrieve custom configs.
        
        This procedure returns custom FontConfig configs along with the fonts
        renaming config.
        
        Returns:
        
        * config - config path.
        
        * sysconfig - sysconfig path.
        
        * renaming_config - fonts renaming config.
        
        * dirs - custom fonts directories.
        """
        pass

    def gimp_fonts_get_list(self, filter: str=None) -> List[str]:
        """Retrieve the list of loaded fonts.
        
        This procedure returns a list of the fonts that are currently available.
        
        Parameters:
        
        * filter - An optional regular expression used to filter the list.
        
        Returns:
        
        * font_list - The list of font names.
        """
        pass

    def gimp_fonts_popup(self, font_callback: str=None, popup_title: str=None, initial_font: Gimp.Font=None, parent_window: GLib.Bytes=None):
        """Invokes the Gimp font selection dialog.
        
        Opens a dialog letting a user choose a font.
        
        Parameters:
        
        * font_callback - The callback PDB proc to call when user chooses a
          font.
        
        * popup_title - Title of the font selection dialog.
        
        * initial_font - The name of the initial font choice.
        
        * parent_window - An optional parent window handle for the popup to be
          set transient to.
        """
        pass

    def gimp_fonts_refresh(self):
        """Refresh current fonts. This function always succeeds.
        
        This procedure retrieves all fonts currently in the user's font path and
        updates the font dialogs accordingly. Depending on the amount of
        fonts on the system, this can take considerable time.
        """
        pass

    def gimp_fonts_set_popup(self, font_callback: str=None, font: Gimp.Font=None):
        """Sets the current font in a font selection dialog.
        
        Sets the current font in a font selection dialog.
        
        Parameters:
        
        * font_callback - The name of the callback registered in the PDB for
          the dialog.
        
        * font - The font to set as selected.
        """
        pass

    def gimp_get_color_configuration(self) -> str:
        """Get a serialized version of the color management configuration.
        
        Returns a string that can be deserialized into a GimpColorConfig object
        representing the current color management configuration.
        
        Returns:
        
        * config - Serialized color management configuration.
        """
        pass

    def gimp_get_default_comment(self) -> str:
        """Get the default image comment as specified in the Preferences.
        
        Returns a copy of the default image comment.
        
        Returns:
        
        * comment - Default image comment.
        """
        pass

    def gimp_get_default_unit(self) -> Gimp.Unit:
        """Get the default unit (taken from the user's locale).
        
        Returns the default unit's integer ID.
        
        Returns:
        
        * unit_id (default: 0) - Default unit.
        """
        pass

    def gimp_get_images(self) -> Tuple[int, Gimp.ObjectArray]:
        """Returns the list of images currently open.
        
        This procedure returns the list of images currently open in GIMP.
        
        Returns:
        
        * num_images (default: 0) - The number of images currently open.
        
        * images - The list of images currently open.
        """
        pass

    def gimp_get_module_load_inhibit(self) -> str:
        """Get the list of modules which should not be loaded.
        
        Returns a copy of the list of modules which should not be loaded.
        
        Returns:
        
        * load_inhibit - The list of modules.
        """
        pass

    def gimp_get_monitor_resolution(self) -> Tuple[float, float]:
        """Get the monitor resolution as specified in the Preferences.
        
        Returns the resolution of the monitor in pixels/inch. This value is
        taken from the Preferences (or the windowing system if this is
        set in the Preferences) and there's no guarantee for the value
        to be reasonable.
        
        Returns:
        
        * xres (default: 0.0) - X resolution.
        
        * yres (default: 0.0) - Y resolution.
        """
        pass

    def gimp_get_parasite(self, name: str=None) -> Gimp.Parasite:
        """Look up a global parasite.
        
        Finds and returns the global parasite that was previously attached.
        
        Parameters:
        
        * name - The name of the parasite to find.
        
        Returns:
        
        * parasite - The found parasite.
        """
        pass

    def gimp_get_parasite_list(self) -> List[str]:
        """List all parasites.
        
        Returns a list of all currently attached global parasites.
        
        Returns:
        
        * parasites - The names of currently attached parasites.
        """
        pass

    def gimp_getpid(self) -> int:
        """Returns the PID of the host GIMP process.
        
        This procedure returns the process ID of the currently running GIMP.
        
        Returns:
        
        * pid (default: 0) - The PID.
        """
        pass

    def gimp_gimprc_query(self, token: str=None) -> str:
        """Queries the gimprc file parser for information on a specified token.
        
        This procedure is used to locate additional information contained in the
        gimprc file considered extraneous to the operation of GIMP.
        Plug-ins that need configuration information can expect it will
        be stored in the user gimprc file and can use this procedure to
        retrieve it. This query procedure will return the value
        associated with the specified token. This corresponds _only_ to
        entries with the format: (<token> <value>). The value must be a
        string. Entries not corresponding to this format will cause
        warnings to be issued on gimprc parsing and will not be
        queryable.
        
        Parameters:
        
        * token - The token to query for.
        
        Returns:
        
        * value - The value associated with the queried token.
        """
        pass

    def gimp_gimprc_set(self, token: str=None, value: str=None):
        """Sets a gimprc token to a value and saves it in the gimprc.
        
        This procedure is used to add or change additional information in the
        gimprc file that is considered extraneous to the operation of
        GIMP. Plug-ins that need configuration information can use this
        function to store it, and 'gimp-gimprc-query' to retrieve it.
        This will accept _only_ string values in UTF-8 encoding.
        
        Parameters:
        
        * token - The token to add or modify.
        
        * value - The value to set the token to.
        """
        pass

    def gimp_gradient_get_by_name(self, name: str=None) -> Gimp.Gradient:
        """Returns the gradient with the given name.
        
        Returns the gradient with the given name.
        
        Parameters:
        
        * name - The name of the gradient.
        
        Returns:
        
        * gradient - The gradient.
        """
        pass

    def gimp_gradient_get_custom_samples(self, gradient: Gimp.Gradient=None, num_samples: int=None, positions: Gimp.FloatArray=None, reverse: bool=None) -> Tuple[int, Gimp.FloatArray]:
        """Sample the gradient in custom positions.
        
        Samples the color of the gradient at positions from a list. The left
        endpoint of the gradient corresponds to position 0.0, and the
        right endpoint corresponds to 1.0. Returns a list of
        floating-point values, four for each sample (RGBA.).
        
        Parameters:
        
        * gradient - The gradient.
        
        * num_samples (default: 1) - The number of samples to take.
        
        * positions - The list of positions to sample along the gradient.
        
        * reverse (default: False) - Use the reverse gradient.
        
        Returns:
        
        * num_color_samples (default: 0) - Length of the color_samples array
          (4 * num_samples).
        
        * color_samples - Color samples: { R1, G1, B1, A1, ..., Rn, Gn, Bn, An
          }.
        """
        pass

    def gimp_gradient_get_number_of_segments(self, gradient: Gimp.Gradient=None) -> int:
        """Gets the number of segments of the gradient.
        
        Gets the number of segments of the gradient.
        
        Parameters:
        
        * gradient - The gradient.
        
        Returns:
        
        * num_segments (default: 0) - Number of segments.
        """
        pass

    def gimp_gradient_get_uniform_samples(self, gradient: Gimp.Gradient=None, num_samples: int=None, reverse: bool=None) -> Tuple[int, Gimp.FloatArray]:
        """Sample the gradient in uniform parts.
        
        Samples colors uniformly across the gradient. It returns a list of
        floating-point values which correspond to the RGBA values for
        each sample. The minimum number of samples to take is 2, in
        which case the returned colors will correspond to the { 0.0, 1.0
        } positions in the gradient. For example, if the number of
        samples is 3, the procedure will return the colors at positions
        { 0.0, 0.5, 1.0 }.
        
        Parameters:
        
        * gradient - The gradient.
        
        * num_samples (default: 2) - The number of samples to take.
        
        * reverse (default: False) - Use the reverse gradient.
        
        Returns:
        
        * num_color_samples (default: 0) - Length of the color_samples array
          (4 * num_samples).
        
        * color_samples - Color samples: { R1, G1, B1, A1, ..., Rn, Gn, Bn, An
          }.
        """
        pass

    def gimp_gradient_new(self, name: str=None) -> Gimp.Gradient:
        """Creates a new gradient.
        
        Creates a new gradient having no segments.
        
        Parameters:
        
        * name - The requested name of the new gradient.
        
        Returns:
        
        * gradient - The gradient.
        """
        pass

    def gimp_gradient_segment_get_blending_function(self, gradient: Gimp.Gradient=None, segment: int=None) -> Gimp.GradientSegmentType:
        """Gets the gradient segment's blending function.
        
        Gets the blending function of the segment at the index. Returns an error
        when the segment index is out of range.
        
        Parameters:
        
        * gradient - The gradient.
        
        * segment (default: 0) - The index of a segment within the gradient.
        
        Returns:
        
        * blend_func (default: <enum GIMP_GRADIENT_SEGMENT_LINEAR of type
          Gimp.GradientSegmentType>) - The blending function of the
          segment.
        """
        pass

    def gimp_gradient_segment_get_coloring_type(self, gradient: Gimp.Gradient=None, segment: int=None) -> Gimp.GradientSegmentColor:
        """Gets the gradient segment's coloring type.
        
        Gets the coloring type of the segment at the index. Returns an error
        when the segment index is out of range.
        
        Parameters:
        
        * gradient - The gradient.
        
        * segment (default: 0) - The index of a segment within the gradient.
        
        Returns:
        
        * coloring_type (default: <enum GIMP_GRADIENT_SEGMENT_RGB of type
          Gimp.GradientSegmentColor>) - The coloring type of the
          segment.
        """
        pass

    def gimp_gradient_segment_get_left_color(self, gradient: Gimp.Gradient=None, segment: int=None) -> Gegl.Color:
        """Gets the left endpoint color of the segment.
        
        Gets the left endpoint color of the indexed segment of the gradient.
        Returns an error when the segment index is out of range.
        
        Parameters:
        
        * gradient - The gradient.
        
        * segment (default: 0) - The index of a segment within the gradient.
        
        Returns:
        
        * color - The return color.
        """
        pass

    def gimp_gradient_segment_get_left_pos(self, gradient: Gimp.Gradient=None, segment: int=None) -> float:
        """Gets the left endpoint position of a segment.
        
        Gets the position of the left endpoint of the segment of the gradient.
        Returns an error when the segment index is out of range.
        
        Parameters:
        
        * gradient - The gradient.
        
        * segment (default: 0) - The index of a segment within the gradient.
        
        Returns:
        
        * pos (default: 0.0) - The return position.
        """
        pass

    def gimp_gradient_segment_get_middle_pos(self, gradient: Gimp.Gradient=None, segment: int=None) -> float:
        """Gets the midpoint position of the segment.
        
        Gets the position of the midpoint of the segment of the gradient.
        Returns an error when the segment index is out of range.
        
        Parameters:
        
        * gradient - The gradient.
        
        * segment (default: 0) - The index of a segment within the gradient.
        
        Returns:
        
        * pos (default: 0.0) - The return position.
        """
        pass

    def gimp_gradient_segment_get_right_color(self, gradient: Gimp.Gradient=None, segment: int=None) -> Gegl.Color:
        """Gets the right endpoint color of the segment.
        
        Gets the color of the right endpoint color of the segment of the
        gradient. Returns an error when the segment index is out of
        range.
        
        Parameters:
        
        * gradient - The gradient.
        
        * segment (default: 0) - The index of a segment within the gradient.
        
        Returns:
        
        * color - The return color.
        """
        pass

    def gimp_gradient_segment_get_right_pos(self, gradient: Gimp.Gradient=None, segment: int=None) -> float:
        """Gets the right endpoint position of the segment.
        
        Gets the position of the right endpoint of the segment of the gradient.
        Returns an error when the segment index is out of range.
        
        Parameters:
        
        * gradient - The gradient.
        
        * segment (default: 0) - The index of a segment within the gradient.
        
        Returns:
        
        * pos (default: 0.0) - The return position.
        """
        pass

    def gimp_gradient_segment_range_blend_colors(self, gradient: Gimp.Gradient=None, start_segment: int=None, end_segment: int=None):
        """Blend the colors of the segment range.
        
        Blends the colors (but not the opacity) of the range of segments. The
        colors' transition will then be uniform across the range.
        Returns an error when a segment index is out of range, or
        gradient is not editable.
        
        Parameters:
        
        * gradient - The gradient.
        
        * start_segment (default: 0) - Index of the first segment to operate
          on.
        
        * end_segment (default: 0) - Index of the last segment to operate on.
          If negative, the range will extend to the end segment.
        """
        pass

    def gimp_gradient_segment_range_blend_opacity(self, gradient: Gimp.Gradient=None, start_segment: int=None, end_segment: int=None):
        """Blend the opacity of the segment range.
        
        Blends the opacity (but not the colors) of the range of segments. The
        opacity's transition will then be uniform across the range.
        Returns an error when a segment index is out of range, or
        gradient is not editable.
        
        Parameters:
        
        * gradient - The gradient.
        
        * start_segment (default: 0) - Index of the first segment to operate
          on.
        
        * end_segment (default: 0) - Index of the last segment to operate on.
          If negative, the range will extend to the end segment.
        """
        pass

    def gimp_gradient_segment_range_delete(self, gradient: Gimp.Gradient=None, start_segment: int=None, end_segment: int=None):
        """Delete the segment range.
        
        Deletes a range of segments. Returns an error when a segment index is
        out of range, or gradient is not editable. Deleting all the
        segments is undefined behavior.
        
        Parameters:
        
        * gradient - The gradient.
        
        * start_segment (default: 0) - Index of the first segment to operate
          on.
        
        * end_segment (default: 0) - Index of the last segment to operate on.
          If negative, the range will extend to the end segment.
        """
        pass

    def gimp_gradient_segment_range_flip(self, gradient: Gimp.Gradient=None, start_segment: int=None, end_segment: int=None):
        """Flip the segment range.
        
        Reverses the order of segments in a range, and swaps the left and right
        colors in each segment. As if the range as a 1D line were
        rotated in a plane. Returns an error when a segment index is out
        of range, or gradient is not editable.
        
        Parameters:
        
        * gradient - The gradient.
        
        * start_segment (default: 0) - Index of the first segment to operate
          on.
        
        * end_segment (default: 0) - Index of the last segment to operate on.
          If negative, the range will extend to the end segment.
        """
        pass

    def gimp_gradient_segment_range_move(self, gradient: Gimp.Gradient=None, start_segment: int=None, end_segment: int=None, delta: float=None, control_compress: bool=None) -> float:
        """Move the position of an entire segment range by a delta.
        
        Moves the position of an entire segment range by a delta. The actual
        delta (which is returned) will be limited by the control points
        of the neighboring segments. Returns the actual delta. Returns
        an error when a segment index is out of range, or gradient is
        not editable.
        
        Parameters:
        
        * gradient - The gradient.
        
        * start_segment (default: 0) - Index of the first segment to operate
          on.
        
        * end_segment (default: 0) - Index of the last segment to operate on.
          If negative, the range will extend to the end segment.
        
        * delta (default: -1.0) - The delta to move the segment range.
        
        * control_compress (default: False) - Whether or not to compress the
          neighboring segments.
        
        Returns:
        
        * final_delta (default: 0.0) - The final delta by which the range
          moved.
        """
        pass

    def gimp_gradient_segment_range_redistribute_handles(self, gradient: Gimp.Gradient=None, start_segment: int=None, end_segment: int=None):
        """Uniformly redistribute the segment range's handles.
        
        Redistributes the handles of the segment range of the gradient, so
        they'll be evenly spaced. A handle is where two segments meet.
        Segments will then have the same width. Returns an error when a
        segment index is out of range, or gradient is not editable.
        
        Parameters:
        
        * gradient - The gradient.
        
        * start_segment (default: 0) - Index of the first segment to operate
          on.
        
        * end_segment (default: 0) - Index of the last segment to operate on.
          If negative, the range will extend to the end segment.
        """
        pass

    def gimp_gradient_segment_range_replicate(self, gradient: Gimp.Gradient=None, start_segment: int=None, end_segment: int=None, replicate_times: int=None):
        """Replicate the segment range.
        
        Replicates a segment range a given number of times. Instead of the
        original segment range, several smaller scaled copies of it will
        appear in equal widths. Returns an error when a segment index is
        out of range, or gradient is not editable.
        
        Parameters:
        
        * gradient - The gradient.
        
        * start_segment (default: 0) - Index of the first segment to operate
          on.
        
        * end_segment (default: 0) - Index of the last segment to operate on.
          If negative, the range will extend to the end segment.
        
        * replicate_times (default: 2) - The number of replicas for each
          segment.
        """
        pass

    def gimp_gradient_segment_range_set_blending_function(self, gradient: Gimp.Gradient=None, start_segment: int=None, end_segment: int=None, blending_function: Gimp.GradientSegmentType=None):
        """Sets the blending function of a range of segments.
        
        Sets the blending function of a range of segments. Returns an error when
        a segment index is out of range, or gradient is not editable.
        
        Parameters:
        
        * gradient - The gradient.
        
        * start_segment (default: 0) - Index of the first segment to operate
          on.
        
        * end_segment (default: 0) - Index of the last segment to operate on.
          If negative, the range will extend to the end segment.
        
        * blending_function (default: <enum GIMP_GRADIENT_SEGMENT_LINEAR of
          type Gimp.GradientSegmentType>) - The blending function.
        """
        pass

    def gimp_gradient_segment_range_set_coloring_type(self, gradient: Gimp.Gradient=None, start_segment: int=None, end_segment: int=None, coloring_type: Gimp.GradientSegmentColor=None):
        """Sets the coloring type of a range of segments.
        
        Sets the coloring type of a range of segments. Returns an error when a
        segment index is out of range, or gradient is not editable.
        
        Parameters:
        
        * gradient - The gradient.
        
        * start_segment (default: 0) - Index of the first segment to operate
          on.
        
        * end_segment (default: 0) - Index of the last segment to operate on.
          If negative, the range will extend to the end segment.
        
        * coloring_type (default: <enum GIMP_GRADIENT_SEGMENT_RGB of type
          Gimp.GradientSegmentColor>) - The coloring type.
        """
        pass

    def gimp_gradient_segment_range_split_midpoint(self, gradient: Gimp.Gradient=None, start_segment: int=None, end_segment: int=None):
        """Splits each segment in the segment range at midpoint.
        
        Splits each segment in the segment range at its midpoint. Returns an
        error when a segment index is out of range, or gradient is not
        editable.
        
        Parameters:
        
        * gradient - The gradient.
        
        * start_segment (default: 0) - Index of the first segment to operate
          on.
        
        * end_segment (default: 0) - Index of the last segment to operate on.
          If negative, the range will extend to the end segment.
        """
        pass

    def gimp_gradient_segment_range_split_uniform(self, gradient: Gimp.Gradient=None, start_segment: int=None, end_segment: int=None, split_parts: int=None):
        """Splits each segment in the segment range uniformly.
        
        Splits each segment in the segment range uniformly into to the number of
        parts given. Returns an error when a segment index is out of
        range, or gradient is not editable.
        
        Parameters:
        
        * gradient - The gradient.
        
        * start_segment (default: 0) - Index of the first segment to operate
          on.
        
        * end_segment (default: 0) - Index of the last segment to operate on.
          If negative, the range will extend to the end segment.
        
        * split_parts (default: 2) - The number of uniform divisions to split
          each segment to.
        """
        pass

    def gimp_gradient_segment_set_left_color(self, gradient: Gimp.Gradient=None, segment: int=None, color: Gegl.Color=None):
        """Sets the left endpoint color of a segment.
        
        Sets the color of the left endpoint the indexed segment of the gradient.
        The alpha channel of the [class@Gegl.Color] is taken into
        account. Returns an error when gradient is not editable or index
        is out of range.
        
        Parameters:
        
        * gradient - The gradient.
        
        * segment (default: 0) - The index of a segment within the gradient.
        
        * color - The color to set.
        """
        pass

    def gimp_gradient_segment_set_left_pos(self, gradient: Gimp.Gradient=None, segment: int=None, pos: float=None) -> float:
        """Sets the left endpoint position of the segment.
        
        Sets the position of the left endpoint of the segment of the gradient.
        The final position will be the given fraction from the midpoint
        to the left to the midpoint of the current segment. Returns the
        final position. Returns an error when gradient is not editable
        or segment index is out of range.
        
        Parameters:
        
        * gradient - The gradient.
        
        * segment (default: 0) - The index of a segment within the gradient.
        
        * pos (default: 0.0) - The position to set the guidepoint to.
        
        Returns:
        
        * final_pos (default: 0.0) - The return position.
        """
        pass

    def gimp_gradient_segment_set_middle_pos(self, gradient: Gimp.Gradient=None, segment: int=None, pos: float=None) -> float:
        """Sets the midpoint position of the segment.
        
        Sets the midpoint position of the segment of the gradient. The final
        position will be the given fraction between the two endpoints of
        the segment. Returns the final position. Returns an error when
        gradient is not editable or segment index is out of range.
        
        Parameters:
        
        * gradient - The gradient.
        
        * segment (default: 0) - The index of a segment within the gradient.
        
        * pos (default: 0.0) - The position to set the guidepoint to.
        
        Returns:
        
        * final_pos (default: 0.0) - The return position.
        """
        pass

    def gimp_gradient_segment_set_right_color(self, gradient: Gimp.Gradient=None, segment: int=None, color: Gegl.Color=None):
        """Sets the right endpoint color of the segment.
        
        Sets the right endpoint color of the segment of the gradient. The alpha
        channel of the [class@Gegl.Color] is taken into account. Returns
        an error when gradient is not editable or segment index is out
        of range.
        
        Parameters:
        
        * gradient - The gradient.
        
        * segment (default: 0) - The index of a segment within the gradient.
        
        * color - The color to set.
        """
        pass

    def gimp_gradient_segment_set_right_pos(self, gradient: Gimp.Gradient=None, segment: int=None, pos: float=None) -> float:
        """Sets the right endpoint position of the segment.
        
        Sets the right endpoint position of the segment of the gradient. The
        final position will be the given fraction from the midpoint of
        the current segment to the midpoint of the segment to the right.
        Returns the final position. Returns an error when gradient is
        not editable or segment index is out of range.
        
        Parameters:
        
        * gradient - The gradient.
        
        * segment (default: 0) - The index of a segment within the gradient.
        
        * pos (default: 0.0) - The position to set the right endpoint to.
        
        Returns:
        
        * final_pos (default: 0.0) - The return position.
        """
        pass

    def gimp_gradients_close_popup(self, gradient_callback: str=None):
        """Close the gradient selection dialog.
        
        Closes an open gradient selection dialog.
        
        Parameters:
        
        * gradient_callback - The name of the callback registered for this
          pop-up.
        """
        pass

    def gimp_gradients_get_active(self) -> Gimp.Gradient:
        """Get the currently active gradient.
        
        Returns the currently active gradient.
        
        Returns:
        
        * gradient - The active gradient.
        """
        pass

    def gimp_gradients_get_gradient(self) -> Gimp.Gradient:
        """Get the currently active gradient.
        
        Returns the currently active gradient.
        
        Returns:
        
        * gradient - The active gradient.
        """
        pass

    def gimp_gradients_get_list(self, filter: str=None) -> List[str]:
        """Retrieve the list of loaded gradients.
        
        This procedure returns a list of the gradients that are currently
        loaded. You can later use the 'gimp-context-set-gradient'
        function to set the active gradient.
        
        Parameters:
        
        * filter - An optional regular expression used to filter the list.
        
        Returns:
        
        * gradient_list - The list of gradient names.
        """
        pass

    def gimp_gradients_popup(self, gradient_callback: str=None, popup_title: str=None, initial_gradient: Gimp.Gradient=None, parent_window: GLib.Bytes=None):
        """Invokes the Gimp gradients selection dialog.
        
        Opens a dialog letting a user choose a gradient.
        
        Parameters:
        
        * gradient_callback - The callback PDB proc to call when user chooses
          a gradient.
        
        * popup_title - Title of the gradient selection dialog.
        
        * initial_gradient - The initial gradient choice.
        
        * parent_window - An optional parent window handle for the popup to be
          set transient to.
        """
        pass

    def gimp_gradients_refresh(self):
        """Refresh current gradients. This function always succeeds.
        
        This procedure retrieves all gradients currently in the user's gradient
        path and updates the gradient dialogs accordingly.
        """
        pass

    def gimp_gradients_set_active(self, gradient: Gimp.Gradient=None):
        """Sets the active gradient.
        
        Sets the active gradient in the current context. The gradient will be
        used in subsequent gradient operations. Returns an error when
        the gradient data was uninstalled since the gradient object was
        created.
        
        Parameters:
        
        * gradient - The gradient.
        """
        pass

    def gimp_gradients_set_gradient(self, gradient: Gimp.Gradient=None):
        """Sets the active gradient.
        
        Sets the active gradient in the current context. The gradient will be
        used in subsequent gradient operations. Returns an error when
        the gradient data was uninstalled since the gradient object was
        created.
        
        Parameters:
        
        * gradient - The gradient.
        """
        pass

    def gimp_gradients_set_popup(self, gradient_callback: str=None, gradient: Gimp.Gradient=None):
        """Sets the current gradient in a gradient selection dialog.
        
        Sets the current gradient in a gradient selection dialog.
        
        Parameters:
        
        * gradient_callback - The name of the callback registered for this
          pop-up.
        
        * gradient - The gradient to set as selected.
        """
        pass

    def gimp_heal(self, drawable: Gimp.Drawable=None, src_drawable: Gimp.Drawable=None, src_x: float=None, src_y: float=None, num_strokes: int=None, strokes: Gimp.FloatArray=None):
        """Heal from the source to the dest drawable using the current brush.
        
        This tool heals the source drawable starting at the specified source
        coordinates to the dest drawable. For image healing, if the sum
        of the src coordinates and subsequent stroke offsets exceeds the
        extents of the src drawable, then no paint is transferred. The
        healing tool is capable of transforming between any image types
        except RGB->Indexed.
        
        Parameters:
        
        * drawable - The affected drawable.
        
        * src_drawable - The source drawable.
        
        * src_x (default: 0.0) - The x coordinate in the source image.
        
        * src_y (default: 0.0) - The y coordinate in the source image.
        
        * num_strokes (default: 2) - Number of stroke control points (count
          each coordinate as 2 points).
        
        * strokes - Array of stroke coordinates: { s1.x, s1.y, s2.x, s2.y,
          ..., sn.x, sn.y }.
        """
        pass

    def gimp_heal_default(self, drawable: Gimp.Drawable=None, num_strokes: int=None, strokes: Gimp.FloatArray=None):
        """Heal from the source to the dest drawable using the current brush.
        
        This tool heals from the source drawable starting at the specified
        source coordinates to the dest drawable. This function performs
        exactly the same as the 'gimp-heal' function except that the
        tools arguments are obtained from the healing option dialog. It
        this dialog has not been activated then the dialogs default
        values will be used.
        
        Parameters:
        
        * drawable - The affected drawable.
        
        * num_strokes (default: 2) - Number of stroke control points (count
          each coordinate as 2 points).
        
        * strokes - Array of stroke coordinates: { s1.x, s1.y, s2.x, s2.y,
          ..., sn.x, sn.y }.
        """
        pass

    def gimp_help(self, help_domain: str=None, help_id: str=None):
        """Load a help page.
        
        This procedure loads the specified help page into the helpbrowser or
        what ever is configured as help viewer. The help page is
        identified by its domain and ID: if help_domain is NULL, we use
        the help_domain which was registered using the
        'gimp-plugin-help-register' procedure. If help_domain is NULL
        and no help domain was registered, the help domain of the main
        GIMP installation is used.
        
        Parameters:
        
        * help_domain - The help domain in which help_id is registered.
        
        * help_id - The help page's ID.
        """
        pass

    def gimp_help_concepts_paths(self, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Bookmark to the user manual.
        
        Menu label: Using _Paths
        Menu path: <Image>/Help/User Manual
        """
        pass

    def gimp_help_concepts_usage(self, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Bookmark to the user manual.
        
        Menu label: _Basic Concepts
        Menu path: <Image>/Help/User Manual
        """
        pass

    def gimp_help_main(self, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Bookmark to the user manual.
        
        Menu label: _[Table of Contents]
        Menu path: <Image>/Help/User Manual
        """
        pass

    def gimp_help_using_docks(self, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Bookmark to the user manual.
        
        Menu label: How to Use _Dialogs
        Menu path: <Image>/Help/User Manual
        """
        pass

    def gimp_help_using_fileformats(self, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Bookmark to the user manual.
        
        Menu label: Create, Open and Save _Files
        Menu path: <Image>/Help/User Manual
        """
        pass

    def gimp_help_using_photography(self, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Bookmark to the user manual.
        
        Menu label: _Working with Digital Camera Photos
        Menu path: <Image>/Help/User Manual
        """
        pass

    def gimp_help_using_selections(self, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Bookmark to the user manual.
        
        Menu label: Create and Use _Selections
        """
        pass

    def gimp_help_using_simpleobjects(self, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Bookmark to the user manual.
        
        Menu label: Drawing _Simple Objects
        Menu paths: <Image>/Help/User Manual, <Image>/Help/User Manual
        """
        pass

    def gimp_help_using_web(self, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Bookmark to the user manual.
        
        Menu label: _Preparing your Images for the Web
        Menu path: <Image>/Help/User Manual
        """
        pass

    def gimp_image_add_hguide(self, image: Gimp.Image=None, yposition: int=None) -> int:
        """Add a horizontal guide to an image.
        
        This procedure adds a horizontal guide to an image. It takes the input
        image and the y-position of the new guide as parameters. It
        returns the guide ID of the new guide.
        
        Parameters:
        
        * image - The image.
        
        * yposition (default: 0) - The guide's y-offset from top of image.
        
        Returns:
        
        * guide (default: 1) - The new guide.
        """
        pass

    def gimp_image_add_sample_point(self, image: Gimp.Image=None, position_x: int=None, position_y: int=None) -> int:
        """Add a sample point to an image.
        
        This procedure adds a sample point to an image. It takes the input image
        and the position of the new sample points as parameters. It
        returns the sample point ID of the new sample point.
        
        Parameters:
        
        * image - The image.
        
        * position_x (default: 0) - The sample point's x-offset from left of
          image.
        
        * position_y (default: 0) - The sample point's y-offset from top of
          image.
        
        Returns:
        
        * sample_point (default: 1) - The new sample point.
        """
        pass

    def gimp_image_add_vguide(self, image: Gimp.Image=None, xposition: int=None) -> int:
        """Add a vertical guide to an image.
        
        This procedure adds a vertical guide to an image. It takes the input
        image and the x-position of the new guide as parameters. It
        returns the guide ID of the new guide.
        
        Parameters:
        
        * image - The image.
        
        * xposition (default: 0) - The guide's x-offset from left of image.
        
        Returns:
        
        * guide (default: 1) - The new guide.
        """
        pass

    def gimp_image_attach_parasite(self, image: Gimp.Image=None, parasite: Gimp.Parasite=None):
        """Add a parasite to an image.
        
        This procedure attaches a parasite to an image. It has no return values.
        
        Parameters:
        
        * image - The image.
        
        * parasite - The parasite to attach to an image.
        """
        pass

    def gimp_image_clean_all(self, image: Gimp.Image=None):
        """Set the image dirty count to 0.
        
        This procedure sets the specified image's dirty count to 0, allowing
        operations to occur without having a 'dirtied' image. This is
        especially useful for creating and loading images which should
        not initially be considered dirty, even though layers must be
        created, filled, and installed in the image. Note that save
        plug-ins must NOT call this function themselves after saving the
        image.
        
        Parameters:
        
        * image - The image.
        """
        pass

    def gimp_image_convert_color_profile(self, image: Gimp.Image=None, color_profile: GLib.Bytes=None, intent: Gimp.ColorRenderingIntent=None, bpc: bool=None):
        """Convert the image's layers to a color profile.
        
        This procedure converts from the image's color profile (or the default
        RGB or grayscale profile if none is set) to the given color
        profile. Only RGB and grayscale color profiles are accepted,
        according to the image's type.
        
        Parameters:
        
        * image - The image.
        
        * color_profile - The serialized color profile.
        
        * intent (default: <enum GIMP_COLOR_RENDERING_INTENT_PERCEPTUAL of
          type Gimp.ColorRenderingIntent>) - Rendering intent.
        
        * bpc (default: False) - Black point compensation.
        """
        pass

    def gimp_image_convert_color_profile_from_file(self, image: Gimp.Image=None, file: Gio.File=None, intent: Gimp.ColorRenderingIntent=None, bpc: bool=None):
        """Convert the image's layers to a color profile.
        
        This procedure converts from the image's color profile (or the default
        RGB or grayscale profile if none is set) to an ICC profile
        specified by 'file'. Only RGB and grayscale color profiles are
        accepted, according to the image's type.
        
        Parameters:
        
        * image - The image.
        
        * file - The file containing the new color profile.
        
        * intent (default: <enum GIMP_COLOR_RENDERING_INTENT_PERCEPTUAL of
          type Gimp.ColorRenderingIntent>) - Rendering intent.
        
        * bpc (default: False) - Black point compensation.
        """
        pass

    def gimp_image_convert_grayscale(self, image: Gimp.Image=None):
        """Convert specified image to grayscale.
        
        This procedure converts the specified image to grayscale. This process
        requires an image in RGB or Indexed color mode.
        
        Parameters:
        
        * image - The image.
        """
        pass

    def gimp_image_convert_indexed(self, image: Gimp.Image=None, dither_type: Gimp.ConvertDitherType=None, palette_type: Gimp.ConvertPaletteType=None, num_cols: int=None, alpha_dither: bool=None, remove_unused: bool=None, palette: str=None):
        """Convert specified image to and Indexed image.
        
        This procedure converts the specified image to 'indexed' color. This
        process requires an image in RGB or Grayscale mode. The
        'palette_type' specifies what kind of palette to use, A type of
        '0' means to use an optimal palette of 'num_cols' generated from
        the colors in the image. A type of '1' means to re-use the
        previous palette (not currently implemented). A type of '2'
        means to use the so-called WWW-optimized palette. Type '3' means
        to use only black and white colors. A type of '4' means to use a
        palette from the gimp palettes directories. The 'dither type'
        specifies what kind of dithering to use. '0' means no dithering,
        '1' means standard Floyd-Steinberg error diffusion, '2' means
        Floyd-Steinberg error diffusion with reduced bleeding, '3' means
        dithering based on pixel location ('Fixed' dithering).
        
        Parameters:
        
        * image - The image.
        
        * dither_type (default: <enum GIMP_CONVERT_DITHER_NONE of type
          Gimp.ConvertDitherType>) - The dither type to use.
        
        * palette_type (default: <enum GIMP_CONVERT_PALETTE_GENERATE of type
          Gimp.ConvertPaletteType>) - The type of palette to use.
        
        * num_cols (default: 0) - The number of colors to quantize to, ignored
          unless (palette_type == GIMP_CONVERT_PALETTE_GENERATE).
        
        * alpha_dither (default: False) - Dither transparency to fake partial
          opacity.
        
        * remove_unused (default: False) - Remove unused or duplicate color
          entries from final palette, ignored if (palette_type ==
          GIMP_CONVERT_PALETTE_GENERATE).
        
        * palette - The name of the custom palette to use, ignored unless
          (palette_type == GIMP_CONVERT_PALETTE_CUSTOM).
        """
        pass

    def gimp_image_convert_precision(self, image: Gimp.Image=None, precision: Gimp.Precision=None):
        """Convert the image to the specified precision.
        
        This procedure converts the image to the specified precision. Note that
        indexed images cannot be converted and are always in
        GIMP_PRECISION_U8.
        
        Parameters:
        
        * image - The image.
        
        * precision (default: <enum GIMP_PRECISION_U8_LINEAR of type
          Gimp.Precision>) - The new precision.
        """
        pass

    def gimp_image_convert_rgb(self, image: Gimp.Image=None):
        """Convert specified image to RGB color.
        
        This procedure converts the specified image to RGB color. This process
        requires an image in Grayscale or Indexed color mode. No image
        content is lost in this process aside from the colormap for an
        indexed image.
        
        Parameters:
        
        * image - The image.
        """
        pass

    def gimp_image_convert_set_dither_matrix(self, width: int=None, height: int=None, matrix: GLib.Bytes=None):
        """Set dither matrix for conversion to indexed.
        
        This procedure sets the dither matrix used when converting images to
        INDEXED mode with positional dithering.
        
        Parameters:
        
        * width (default: 0) - Width of the matrix (0 to reset to default
          matrix).
        
        * height (default: 0) - Height of the matrix (0 to reset to default
          matrix).
        
        * matrix - The matrix -- all values must be >= 1.
        """
        pass

    def gimp_image_crop(self, image: Gimp.Image=None, new_width: int=None, new_height: int=None, offx: int=None, offy: int=None):
        """Crop the image to the specified extents.
        
        This procedure crops the image so that it's new width and height are
        equal to the supplied parameters. Offsets are also provided
        which describe the position of the previous image's content. All
        channels and layers within the image are cropped to the new
        image extents; this includes the image selection mask. If any
        parameters are out of range, an error is returned.
        
        Parameters:
        
        * image - The image.
        
        * new_width (default: 1) - New image width: (0 < new_width <= width).
        
        * new_height (default: 1) - New image height: (0 < new_height <=
          height).
        
        * offx (default: 0) - X offset: (0 <= offx <= (width - new_width)).
        
        * offy (default: 0) - Y offset: (0 <= offy <= (height - new_height)).
        """
        pass

    def gimp_image_delete(self, image: Gimp.Image=None):
        """Delete the specified image.
        
        If there are no displays associated with this image it will be deleted.
        This means that you can not delete an image through the PDB that
        was created by the user. If the associated display was however
        created through the PDB and you know the display ID, you may
        delete the display. Removal of the last associated display will
        then delete the image.
        
        Parameters:
        
        * image - The image.
        """
        pass

    def gimp_image_delete_guide(self, image: Gimp.Image=None, guide: int=None):
        """Deletes a guide from an image.
        
        This procedure takes an image and a guide ID as input and removes the
        specified guide from the specified image.
        
        Parameters:
        
        * image - The image.
        
        * guide (default: 1) - The ID of the guide to be removed.
        """
        pass

    def gimp_image_delete_sample_point(self, image: Gimp.Image=None, sample_point: int=None):
        """Deletes a sample point from an image.
        
        This procedure takes an image and a sample point ID as input and removes
        the specified sample point from the specified image.
        
        Parameters:
        
        * image - The image.
        
        * sample_point (default: 1) - The ID of the sample point to be
          removed.
        """
        pass

    def gimp_image_detach_parasite(self, image: Gimp.Image=None, name: str=None):
        """Removes a parasite from an image.
        
        This procedure detaches a parasite from an image. It has no return
        values.
        
        Parameters:
        
        * image - The image.
        
        * name - The name of the parasite to detach from an image.
        """
        pass

    def gimp_image_duplicate(self, image: Gimp.Image=None) -> Gimp.Image:
        """Duplicate the specified image.
        
        This procedure duplicates the specified image, copying all layers,
        channels, and image information.
        
        Parameters:
        
        * image - The image.
        
        Returns:
        
        * new_image - The new, duplicated image.
        """
        pass

    def gimp_image_find_next_guide(self, image: Gimp.Image=None, guide: int=None) -> int:
        """Find next guide on an image.
        
        This procedure takes an image and a guide ID as input and finds the
        guide ID of the successor of the given guide ID in the image's
        guide list. If the supplied guide ID is 0, the procedure will
        return the first Guide. The procedure will return 0 if given the
        final guide ID as an argument or the image has no guides.
        
        Parameters:
        
        * image - The image.
        
        * guide (default: 1) - The ID of the current guide (0 if first
          invocation).
        
        Returns:
        
        * next_guide (default: 1) - The next guide's ID.
        """
        pass

    def gimp_image_find_next_sample_point(self, image: Gimp.Image=None, sample_point: int=None) -> int:
        """Find next sample point on an image.
        
        This procedure takes an image and a sample point ID as input and finds
        the sample point ID of the successor of the given sample point
        ID in the image's sample point list. If the supplied sample
        point ID is 0, the procedure will return the first sample point.
        The procedure will return 0 if given the final sample point ID
        as an argument or the image has no sample points.
        
        Parameters:
        
        * image - The image.
        
        * sample_point (default: 1) - The ID of the current sample point (0 if
          first invocation).
        
        Returns:
        
        * next_sample_point (default: 1) - The next sample point's ID.
        """
        pass

    def gimp_image_flatten(self, image: Gimp.Image=None) -> Gimp.Layer:
        """Flatten all visible layers into a single layer. Discard all invisible
        layers.
        
        This procedure combines the visible layers in a manner analogous to
        merging with the CLIP_TO_IMAGE merge type. Non-visible layers
        are discarded, and the resulting image is stripped of its alpha
        channel.
        
        Parameters:
        
        * image - The image.
        
        Returns:
        
        * layer - The resulting layer.
        """
        pass

    def gimp_image_flip(self, image: Gimp.Image=None, flip_type: Gimp.OrientationType=None):
        """Flips the image horizontally or vertically.
        
        This procedure flips (mirrors) the image.
        
        Parameters:
        
        * image - The image.
        
        * flip_type (default: <enum GIMP_ORIENTATION_HORIZONTAL of type
          Gimp.OrientationType>) - Type of flip.
        """
        pass

    def gimp_image_floating_sel_attached_to(self, image: Gimp.Image=None) -> Gimp.Drawable:
        """Return the drawable the floating selection is attached to.
        
        This procedure returns the drawable the image's floating selection is
        attached to, if it exists. If it doesn't exist, -1 is returned
        as the drawable ID.
        
        Parameters:
        
        * image - The image.
        
        Returns:
        
        * drawable - The drawable the floating selection is attached to.
        """
        pass

    def gimp_image_floating_selection(self, image: Gimp.Image=None) -> Gimp.Layer:
        """Return the floating selection of the image.
        
        This procedure returns the image's floating selection, if it exists. If
        it doesn't exist, -1 is returned as the layer ID.
        
        Parameters:
        
        * image - The image.
        
        Returns:
        
        * floating_sel - The image's floating selection.
        """
        pass

    def gimp_image_freeze_channels(self, image: Gimp.Image=None):
        """Freeze the image's channel list.
        
        This procedure freezes the channel list of the image, suppressing any
        updates to the Channels dialog in response to changes to the
        image's channels. This can significantly improve performance
        while applying changes affecting the channel list.
        
        Each call to 'gimp-image-freeze-channels' should be matched by a
        corresponding call to 'gimp-image-thaw-channels', undoing its
        effects.
        
        Parameters:
        
        * image - The image.
        """
        pass

    def gimp_image_freeze_layers(self, image: Gimp.Image=None):
        """Freeze the image's layer list.
        
        This procedure freezes the layer list of the image, suppressing any
        updates to the Layers dialog in response to changes to the
        image's layers. This can significantly improve performance while
        applying changes affecting the layer list.
        
        Each call to 'gimp-image-freeze-layers' should be matched by a
        corresponding call to 'gimp-image-thaw-layers', undoing its
        effects.
        
        Parameters:
        
        * image - The image.
        """
        pass

    def gimp_image_freeze_vectors(self, image: Gimp.Image=None):
        """Freeze the image's vectors list.
        
        This procedure freezes the vectors list of the image, suppressing any
        updates to the Paths dialog in response to changes to the
        image's vectors. This can significantly improve performance
        while applying changes affecting the vectors list.
        
        Each call to 'gimp-image-freeze-vectors' should be matched by a
        corresponding call to 'gimp-image-thaw-vectors', undoing its
        effects.
        
        Parameters:
        
        * image - The image.
        """
        pass

    def gimp_image_get_base_type(self, image: Gimp.Image=None) -> Gimp.ImageBaseType:
        """Get the base type of the image.
        
        This procedure returns the image's base type. Layers in the image must
        be of this subtype, but can have an optional alpha channel.
        
        Parameters:
        
        * image - The image.
        
        Returns:
        
        * base_type (default: <enum GIMP_RGB of type Gimp.ImageBaseType>) -
          The image's base type.
        """
        pass

    def gimp_image_get_channel_by_name(self, image: Gimp.Image=None, name: str=None) -> Gimp.Channel:
        """Find a channel with a given name in an image.
        
        This procedure returns the channel with the given name in the specified
        image.
        
        Parameters:
        
        * image - The image.
        
        * name - The name of the channel to find.
        
        Returns:
        
        * channel - The channel with the specified name.
        """
        pass

    def gimp_image_get_channel_by_tattoo(self, image: Gimp.Image=None, tattoo: int=None) -> Gimp.Channel:
        """Find a channel with a given tattoo in an image.
        
        This procedure returns the channel with the given tattoo in the
        specified image.
        
        Parameters:
        
        * image - The image.
        
        * tattoo (default: 1) - The tattoo of the channel to find.
        
        Returns:
        
        * channel - The channel with the specified tattoo.
        """
        pass

    def gimp_image_get_channel_position(self, image: Gimp.Image=None, item: Gimp.Item=None) -> int:
        """Returns the position of the item in its level of its item tree.
        
        This procedure determines the position of the specified item in its
        level in its item tree in the image. If the item doesn't exist
        in the image, or the item is not part of an item tree, an error
        is returned.
        
        Parameters:
        
        * image - The image.
        
        * item - The item.
        
        Returns:
        
        * position (default: 0) - The position of the item in its level in the
          item tree.
        """
        pass

    def gimp_image_get_channels(self, image: Gimp.Image=None) -> Tuple[int, Gimp.ObjectArray]:
        """Returns the list of channels contained in the specified image.
        
        This procedure returns the list of channels contained in the specified
        image. This does not include the selection mask, or layer masks.
        The order is from topmost to bottommost. Note that "channels"
        are custom channels and do not include the image's color
        components.
        
        Parameters:
        
        * image - The image.
        
        Returns:
        
        * num_channels (default: 0) - The number of channels contained in the
          image.
        
        * channels - The list of channels contained in the image.
        """
        pass

    def gimp_image_get_cmap(self, image: Gimp.Image=None) -> GLib.Bytes:
        """Returns the image's colormap.
        
        This procedure returns an actual pointer to the image's colormap, as
        well as the number of bytes contained in the colormap. The
        actual number of colors in the transmitted colormap will be
        'num-bytes' / 3. If the image is not in Indexed color mode, no
        colormap is returned.
        
        Parameters:
        
        * image - The image.
        
        Returns:
        
        * colormap - The image's colormap.
        """
        pass

    def gimp_image_get_color_profile(self, image: Gimp.Image=None) -> GLib.Bytes:
        """Returns the image's color profile.
        
        This procedure returns the image's color profile, or NULL if the image
        has no color profile assigned.
        
        Parameters:
        
        * image - The image.
        
        Returns:
        
        * profile_data - The image's serialized color profile.
        """
        pass

    def gimp_image_get_colormap(self, image: Gimp.Image=None) -> GLib.Bytes:
        """Returns the image's colormap.
        
        This procedure returns an actual pointer to the image's colormap, as
        well as the number of bytes contained in the colormap. The
        actual number of colors in the transmitted colormap will be
        'num-bytes' / 3. If the image is not in Indexed color mode, no
        colormap is returned.
        
        Parameters:
        
        * image - The image.
        
        Returns:
        
        * colormap - The image's colormap.
        """
        pass

    def gimp_image_get_component_active(self, image: Gimp.Image=None, component: Gimp.ChannelType=None) -> bool:
        """Returns if the specified image's image component is active.
        
        This procedure returns if the specified image's image component (i.e.
        Red, Green, Blue intensity channels in an RGB image) is active
        or inactive -- whether or not it can be modified. If the
        specified component is not valid for the image type, an error is
        returned.
        
        Parameters:
        
        * image - The image.
        
        * component (default: <enum GIMP_CHANNEL_RED of type
          Gimp.ChannelType>) - The image component.
        
        Returns:
        
        * active (default: False) - Component is active.
        """
        pass

    def gimp_image_get_component_visible(self, image: Gimp.Image=None, component: Gimp.ChannelType=None) -> bool:
        """Returns if the specified image's image component is visible.
        
        This procedure returns if the specified image's image component (i.e.
        Red, Green, Blue intensity channels in an RGB image) is visible
        or invisible -- whether or not it can be seen. If the specified
        component is not valid for the image type, an error is returned.
        
        Parameters:
        
        * image - The image.
        
        * component (default: <enum GIMP_CHANNEL_RED of type
          Gimp.ChannelType>) - The image component.
        
        Returns:
        
        * visible (default: False) - Component is visible.
        """
        pass

    def gimp_image_get_default_new_layer_mode(self, image: Gimp.Image=None) -> Gimp.LayerMode:
        """Get the default mode for newly created layers of this image.
        
        Returns the default mode for newly created layers of this image.
        
        Parameters:
        
        * image - The image.
        
        Returns:
        
        * mode (default: <enum GIMP_LAYER_MODE_NORMAL of type Gimp.LayerMode>)
          - The layer mode.
        """
        pass

    def gimp_image_get_effective_color_profile(self, image: Gimp.Image=None) -> GLib.Bytes:
        """Returns the color profile that is used for the image.
        
        This procedure returns the color profile that is actually used for this
        image, which is the profile returned by
        'gimp-image-get-color-profile' if the image has a profile
        assigned, or a generated default RGB or grayscale profile,
        according to the image's type.
        
        Parameters:
        
        * image - The image.
        
        Returns:
        
        * profile_data - The image's serialized color profile.
        """
        pass

    def gimp_image_get_exported_file(self, image: Gimp.Image=None) -> Gio.File:
        """Returns the exported file for the specified image.
        
        This procedure returns the file associated with the specified image if
        the image was exported a non-native GIMP format. If the image
        was not exported, this procedure returns %NULL.
        
        Parameters:
        
        * image - The image.
        
        Returns:
        
        * file - The exported file.
        """
        pass

    def gimp_image_get_file(self, image: Gimp.Image=None) -> Gio.File:
        """Returns the file for the specified image.
        
        This procedure returns the file associated with the specified image. The
        image has a file only if it was loaded or imported from a file
        or has since been saved or exported. Otherwise, this function
        returns %NULL. See also gimp-image-get-imported-file to get the
        current file if it was imported from a non-GIMP file format and
        not yet saved, or gimp-image-get-exported-file if the image has
        been exported to a non-GIMP file format.
        
        Parameters:
        
        * image - The image.
        
        Returns:
        
        * file - The file.
        """
        pass

    def gimp_image_get_floating_sel(self, image: Gimp.Image=None) -> Gimp.Layer:
        """Return the floating selection of the image.
        
        This procedure returns the image's floating selection, if it exists. If
        it doesn't exist, -1 is returned as the layer ID.
        
        Parameters:
        
        * image - The image.
        
        Returns:
        
        * floating_sel - The image's floating selection.
        """
        pass

    def gimp_image_get_guide_orientation(self, image: Gimp.Image=None, guide: int=None) -> Gimp.OrientationType:
        """Get orientation of a guide on an image.
        
        This procedure takes an image and a guide ID as input and returns the
        orientations of the guide.
        
        Parameters:
        
        * image - The image.
        
        * guide (default: 1) - The guide.
        
        Returns:
        
        * orientation (default: <enum GIMP_ORIENTATION_HORIZONTAL of type
          Gimp.OrientationType>) - The guide's orientation.
        """
        pass

    def gimp_image_get_guide_position(self, image: Gimp.Image=None, guide: int=None) -> int:
        """Get position of a guide on an image.
        
        This procedure takes an image and a guide ID as input and returns the
        position of the guide relative to the top or left of the image.
        
        Parameters:
        
        * image - The image.
        
        * guide (default: 1) - The guide.
        
        Returns:
        
        * position (default: 0) - The guide's position relative to top or left
          of image.
        """
        pass

    def gimp_image_get_height(self, image: Gimp.Image=None) -> int:
        """Return the height of the image.
        
        This procedure returns the image's height. This value is independent of
        any of the layers in this image. This is the "canvas" height.
        
        Parameters:
        
        * image - The image.
        
        Returns:
        
        * height (default: 0) - The image's height.
        """
        pass

    def gimp_image_get_imported_file(self, image: Gimp.Image=None) -> Gio.File:
        """Returns the imported file for the specified image.
        
        This procedure returns the file associated with the specified image if
        the image was imported from a non-native Gimp format. If the
        image was not imported, or has since been saved in the native
        Gimp format, this procedure returns %NULL.
        
        Parameters:
        
        * image - The image.
        
        Returns:
        
        * file - The imported file.
        """
        pass

    def gimp_image_get_item_position(self, image: Gimp.Image=None, item: Gimp.Item=None) -> int:
        """Returns the position of the item in its level of its item tree.
        
        This procedure determines the position of the specified item in its
        level in its item tree in the image. If the item doesn't exist
        in the image, or the item is not part of an item tree, an error
        is returned.
        
        Parameters:
        
        * image - The image.
        
        * item - The item.
        
        Returns:
        
        * position (default: 0) - The position of the item in its level in the
          item tree.
        """
        pass

    def gimp_image_get_layer_by_name(self, image: Gimp.Image=None, name: str=None) -> Gimp.Layer:
        """Find a layer with a given name in an image.
        
        This procedure returns the layer with the given name in the specified
        image.
        
        Parameters:
        
        * image - The image.
        
        * name - The name of the layer to find.
        
        Returns:
        
        * layer - The layer with the specified name.
        """
        pass

    def gimp_image_get_layer_by_tattoo(self, image: Gimp.Image=None, tattoo: int=None) -> Gimp.Layer:
        """Find a layer with a given tattoo in an image.
        
        This procedure returns the layer with the given tattoo in the specified
        image.
        
        Parameters:
        
        * image - The image.
        
        * tattoo (default: 1) - The tattoo of the layer to find.
        
        Returns:
        
        * layer - The layer with the specified tattoo.
        """
        pass

    def gimp_image_get_layer_position(self, image: Gimp.Image=None, item: Gimp.Item=None) -> int:
        """Returns the position of the item in its level of its item tree.
        
        This procedure determines the position of the specified item in its
        level in its item tree in the image. If the item doesn't exist
        in the image, or the item is not part of an item tree, an error
        is returned.
        
        Parameters:
        
        * image - The image.
        
        * item - The item.
        
        Returns:
        
        * position (default: 0) - The position of the item in its level in the
          item tree.
        """
        pass

    def gimp_image_get_layers(self, image: Gimp.Image=None) -> Tuple[int, Gimp.ObjectArray]:
        """Returns the list of root layers contained in the specified image.
        
        This procedure returns the list of root layers contained in the
        specified image. The order of layers is from topmost to
        bottommost. Note that this is not the full list of layers, but
        only the root layers, i.e. layers with no parents themselves. If
        you need all layers, it is up to you to verify that any of these
        layers is a group layer with 'gimp-item-is-group' and to obtain
        its children with 'gimp-item-get-children' (possibly recursively
        checking if these have children too).
        
        Parameters:
        
        * image - The image.
        
        Returns:
        
        * num_layers (default: 0) - The number of root layers contained in the
          image.
        
        * layers - The list of layers contained in the image.
        """
        pass

    def gimp_image_get_metadata(self, image: Gimp.Image=None) -> str:
        """Returns the image's metadata.
        
        Returns exif/iptc/xmp metadata from the image.
        
        Parameters:
        
        * image - The image.
        
        Returns:
        
        * metadata_string - The exif/ptc/xmp metadata as a string.
        """
        pass

    def gimp_image_get_name(self, image: Gimp.Image=None) -> str:
        """Returns the specified image's name.
        
        This procedure returns the image's name. If the image has a filename or
        an URI, then the returned name contains the filename's or URI's
        base name (the last component of the path). Otherwise it is the
        translated string "Untitled". The returned name is formatted
        like the image name in the image window title, it may contain
        '[]', '(imported)' etc. and should only be used to label user
        interface elements. Never use it to construct filenames.
        
        Parameters:
        
        * image - The image.
        
        Returns:
        
        * name - The name.
        """
        pass

    def gimp_image_get_palette(self, image: Gimp.Image=None) -> Gimp.Palette:
        """Returns the image's colormap.
        
        This procedure returns the image's colormap as a GimpPalette. If the
        image is not in Indexed color mode, %NULL is returned.
        
        Parameters:
        
        * image - The image.
        
        Returns:
        
        * colormap - The image's colormap.
        """
        pass

    def gimp_image_get_parasite(self, image: Gimp.Image=None, name: str=None) -> Gimp.Parasite:
        """Look up a parasite in an image.
        
        Finds and returns the parasite that was previously attached to an image.
        
        Parameters:
        
        * image - The image.
        
        * name - The name of the parasite to find.
        
        Returns:
        
        * parasite - The found parasite.
        """
        pass

    def gimp_image_get_parasite_list(self, image: Gimp.Image=None) -> List[str]:
        """List all parasites.
        
        Returns a list of the names of all currently attached parasites. These
        names can later be used to get the actual #GimpParasite with
        'gimp-image-get-parasite' when needed.
        
        Parameters:
        
        * image - The image.
        
        Returns:
        
        * parasites - The names of currently attached parasites.
        """
        pass

    def gimp_image_get_precision(self, image: Gimp.Image=None) -> Gimp.Precision:
        """Get the precision of the image.
        
        This procedure returns the image's precision.
        
        Parameters:
        
        * image - The image.
        
        Returns:
        
        * precision (default: <enum GIMP_PRECISION_U8_LINEAR of type
          Gimp.Precision>) - The image's precision.
        """
        pass

    def gimp_image_get_resolution(self, image: Gimp.Image=None) -> Tuple[float, float]:
        """Returns the specified image's resolution.
        
        This procedure returns the specified image's resolution in dots per
        inch. This value is independent of any of the layers in this
        image.
        
        Parameters:
        
        * image - The image.
        
        Returns:
        
        * xresolution (default: 0.0) - The resolution in the x-axis, in dots
          per inch.
        
        * yresolution (default: 0.0) - The resolution in the y-axis, in dots
          per inch.
        """
        pass

    def gimp_image_get_sample_point_position(self, image: Gimp.Image=None, sample_point: int=None) -> Tuple[int, int]:
        """Get position of a sample point on an image.
        
        This procedure takes an image and a sample point ID as input and returns
        the position of the sample point relative to the top and left of
        the image.
        
        Parameters:
        
        * image - The image.
        
        * sample_point (default: 1) - The guide.
        
        Returns:
        
        * position_x (default: 0) - The sample point's x-offset relative to
          left of image.
        
        * position_y (default: 0) - The sample point's y-offset relative to
          top of image.
        """
        pass

    def gimp_image_get_selected_channels(self, image: Gimp.Image=None) -> Tuple[int, Gimp.ObjectArray]:
        """Returns the specified image's selected channels.
        
        This procedure returns the list of selected channels in the specified
        image.
        
        Parameters:
        
        * image - The image.
        
        Returns:
        
        * num_channels (default: 0) - The number of selected channels in the
          image.
        
        * channels - The list of selected channels in the image.
        """
        pass

    def gimp_image_get_selected_drawables(self, image: Gimp.Image=None) -> Tuple[int, Gimp.ObjectArray]:
        """Get the image's selected drawables.
        
        This procedure returns the list of selected drawable in the specified
        image. This can be either layers, channels, or a layer mask. The
        active drawables are the active image channels. If there are
        none, these are the active image layers. If the active image
        layer has a layer mask and the layer mask is in edit mode, then
        the layer mask is the active drawable.
        
        Parameters:
        
        * image - The image.
        
        Returns:
        
        * num_drawables (default: 0) - The number of selected drawables in the
          image.
        
        * drawables - The list of selected drawables in the image.
        """
        pass

    def gimp_image_get_selected_layers(self, image: Gimp.Image=None) -> Tuple[int, Gimp.ObjectArray]:
        """Returns the specified image's selected layers.
        
        This procedure returns the list of selected layers in the specified
        image.
        
        Parameters:
        
        * image - The image.
        
        Returns:
        
        * num_layers (default: 0) - The number of selected layers in the
          image.
        
        * layers - The list of selected layers in the image.
        """
        pass

    def gimp_image_get_selected_vectors(self, image: Gimp.Image=None) -> Tuple[int, Gimp.ObjectArray]:
        """Returns the specified image's selected vectors.
        
        This procedure returns the list of selected vectors in the specified
        image.
        
        Parameters:
        
        * image - The image.
        
        Returns:
        
        * num_vectors (default: 0) - The number of selected vectors in the
          image.
        
        * vectors - The list of selected vectors in the image.
        """
        pass

    def gimp_image_get_selection(self, image: Gimp.Image=None) -> Gimp.Selection:
        """Returns the specified image's selection.
        
        This will always return a valid ID for a selection -- which is
        represented as a channel internally.
        
        Parameters:
        
        * image - The image.
        
        Returns:
        
        * selection - The selection channel.
        """
        pass

    def gimp_image_get_simulation_bpc(self, image: Gimp.Image=None) -> bool:
        """Returns whether the image has Black Point Compensation enabled for
        its simulation.
        
        This procedure returns whether the image has Black Point Compensation
        enabled for its simulation.
        
        Parameters:
        
        * image - The image.
        
        Returns:
        
        * bpc (default: False) - The Black Point Compensation status.
        """
        pass

    def gimp_image_get_simulation_intent(self, image: Gimp.Image=None) -> Gimp.ColorRenderingIntent:
        """Returns the image's simulation rendering intent.
        
        This procedure returns the image's simulation rendering intent.
        
        Parameters:
        
        * image - The image.
        
        Returns:
        
        * intent (default: <enum GIMP_COLOR_RENDERING_INTENT_PERCEPTUAL of
          type Gimp.ColorRenderingIntent>) - The image's simulation
          rendering intent.
        """
        pass

    def gimp_image_get_simulation_profile(self, image: Gimp.Image=None) -> GLib.Bytes:
        """Returns the image's simulation color profile.
        
        This procedure returns the image's simulation color profile, or NULL if
        the image has no simulation color profile assigned.
        
        Parameters:
        
        * image - The image.
        
        Returns:
        
        * profile_data - The image's serialized simulation color profile.
        """
        pass

    def gimp_image_get_tattoo_state(self, image: Gimp.Image=None) -> int:
        """Returns the tattoo state associated with the image.
        
        This procedure returns the tattoo state of the image. Use only by
        save/load plug-ins that wish to preserve an images tattoo state.
        Using this function at other times will produce unexpected
        results.
        
        Parameters:
        
        * image - The image.
        
        Returns:
        
        * tattoo_state (default: 1) - The tattoo state.
        """
        pass

    def gimp_image_get_unit(self, image: Gimp.Image=None) -> Gimp.Unit:
        """Returns the specified image's unit.
        
        This procedure returns the specified image's unit. This value is
        independent of any of the layers in this image. See the
        gimp_unit_*() procedure definitions for the valid range of unit
        IDs and a description of the unit system.
        
        Parameters:
        
        * image - The image.
        
        Returns:
        
        * unit (default: 0) - The unit.
        """
        pass

    def gimp_image_get_vectors(self, image: Gimp.Image=None) -> Tuple[int, Gimp.ObjectArray]:
        """Returns the list of vectors contained in the specified image.
        
        This procedure returns the list of vectors contained in the specified
        image.
        
        Parameters:
        
        * image - The image.
        
        Returns:
        
        * num_vectors (default: 0) - The number of vectors contained in the
          image.
        
        * vectors - The list of vectors contained in the image.
        """
        pass

    def gimp_image_get_vectors_by_name(self, image: Gimp.Image=None, name: str=None) -> Gimp.Vectors:
        """Find a vectors with a given name in an image.
        
        This procedure returns the vectors with the given name in the specified
        image.
        
        Parameters:
        
        * image - The image.
        
        * name - The name of the vectors to find.
        
        Returns:
        
        * vectors - The vectors with the specified name.
        """
        pass

    def gimp_image_get_vectors_by_tattoo(self, image: Gimp.Image=None, tattoo: int=None) -> Gimp.Vectors:
        """Find a vectors with a given tattoo in an image.
        
        This procedure returns the vectors with the given tattoo in the
        specified image.
        
        Parameters:
        
        * image - The image.
        
        * tattoo (default: 1) - The tattoo of the vectors to find.
        
        Returns:
        
        * vectors - The vectors with the specified tattoo.
        """
        pass

    def gimp_image_get_vectors_position(self, image: Gimp.Image=None, item: Gimp.Item=None) -> int:
        """Returns the position of the item in its level of its item tree.
        
        This procedure determines the position of the specified item in its
        level in its item tree in the image. If the item doesn't exist
        in the image, or the item is not part of an item tree, an error
        is returned.
        
        Parameters:
        
        * image - The image.
        
        * item - The item.
        
        Returns:
        
        * position (default: 0) - The position of the item in its level in the
          item tree.
        """
        pass

    def gimp_image_get_width(self, image: Gimp.Image=None) -> int:
        """Return the width of the image.
        
        This procedure returns the image's width. This value is independent of
        any of the layers in this image. This is the "canvas" width.
        
        Parameters:
        
        * image - The image.
        
        Returns:
        
        * width (default: 0) - The image's width.
        """
        pass

    def gimp_image_get_xcf_file(self, image: Gimp.Image=None) -> Gio.File:
        """Returns the XCF file for the specified image.
        
        This procedure returns the XCF file associated with the image. If there
        is no such file, this procedure returns %NULL.
        
        Parameters:
        
        * image - The image.
        
        Returns:
        
        * file - The imported XCF file.
        """
        pass

    def gimp_image_grid_get_background_color(self, image: Gimp.Image=None) -> Gegl.Color:
        """Sets the background color of an image's grid.
        
        This procedure gets the background color of an image's grid.
        
        Parameters:
        
        * image - The image.
        
        Returns:
        
        * bgcolor - The image's grid background color.
        """
        pass

    def gimp_image_grid_get_foreground_color(self, image: Gimp.Image=None) -> Gegl.Color:
        """Sets the foreground color of an image's grid.
        
        This procedure gets the foreground color of an image's grid.
        
        Parameters:
        
        * image - The image.
        
        Returns:
        
        * fgcolor - The image's grid foreground color.
        """
        pass

    def gimp_image_grid_get_offset(self, image: Gimp.Image=None) -> Tuple[float, float]:
        """Gets the offset of an image's grid.
        
        This procedure retrieves the horizontal and vertical offset of an
        image's grid. It takes the image as parameter.
        
        Parameters:
        
        * image - The image.
        
        Returns:
        
        * xoffset (default: 0.0) - The image's grid horizontal offset.
        
        * yoffset (default: 0.0) - The image's grid vertical offset.
        """
        pass

    def gimp_image_grid_get_spacing(self, image: Gimp.Image=None) -> Tuple[float, float]:
        """Gets the spacing of an image's grid.
        
        This procedure retrieves the horizontal and vertical spacing of an
        image's grid. It takes the image as parameter.
        
        Parameters:
        
        * image - The image.
        
        Returns:
        
        * xspacing (default: 0.0) - The image's grid horizontal spacing.
        
        * yspacing (default: 0.0) - The image's grid vertical spacing.
        """
        pass

    def gimp_image_grid_get_style(self, image: Gimp.Image=None) -> Gimp.GridStyle:
        """Gets the style of an image's grid.
        
        This procedure retrieves the style of an image's grid.
        
        Parameters:
        
        * image - The image.
        
        Returns:
        
        * style (default: <enum GIMP_GRID_DOTS of type Gimp.GridStyle>) - The
          image's grid style.
        """
        pass

    def gimp_image_grid_set_background_color(self, image: Gimp.Image=None, bgcolor: Gegl.Color=None):
        """Gets the background color of an image's grid.
        
        This procedure sets the background color of an image's grid.
        
        Parameters:
        
        * image - The image.
        
        * bgcolor - The new background color.
        """
        pass

    def gimp_image_grid_set_foreground_color(self, image: Gimp.Image=None, fgcolor: Gegl.Color=None):
        """Gets the foreground color of an image's grid.
        
        This procedure sets the foreground color of an image's grid.
        
        Parameters:
        
        * image - The image.
        
        * fgcolor - The new foreground color.
        """
        pass

    def gimp_image_grid_set_offset(self, image: Gimp.Image=None, xoffset: float=None, yoffset: float=None):
        """Sets the offset of an image's grid.
        
        This procedure sets the horizontal and vertical offset of an image's
        grid.
        
        Parameters:
        
        * image - The image.
        
        * xoffset (default: 0.0) - The image's grid horizontal offset.
        
        * yoffset (default: 0.0) - The image's grid vertical offset.
        """
        pass

    def gimp_image_grid_set_spacing(self, image: Gimp.Image=None, xspacing: float=None, yspacing: float=None):
        """Sets the spacing of an image's grid.
        
        This procedure sets the horizontal and vertical spacing of an image's
        grid.
        
        Parameters:
        
        * image - The image.
        
        * xspacing (default: 0.0) - The image's grid horizontal spacing.
        
        * yspacing (default: 0.0) - The image's grid vertical spacing.
        """
        pass

    def gimp_image_grid_set_style(self, image: Gimp.Image=None, style: Gimp.GridStyle=None):
        """Sets the style unit of an image's grid.
        
        This procedure sets the style of an image's grid. It takes the image and
        the new style as parameters.
        
        Parameters:
        
        * image - The image.
        
        * style (default: <enum GIMP_GRID_DOTS of type Gimp.GridStyle>) - The
          image's grid style.
        """
        pass

    def gimp_image_id_is_valid(self, image_id: int=None) -> bool:
        """Returns TRUE if the image ID is valid.
        
        This procedure checks if the given image ID is valid and refers to an
        existing image.
        
        Parameters:
        
        * image_id (default: 0) - The image ID to check.
        
        Returns:
        
        * valid (default: False) - Whether the image ID is valid.
        """
        pass

    def gimp_image_insert_channel(self, image: Gimp.Image=None, channel: Gimp.Channel=None, parent: Gimp.Channel=None, position: int=None):
        """Add the specified channel to the image.
        
        This procedure adds the specified channel to the image at the given
        position. Since channel groups are not currently supported, the
        parent argument must always be 0. The position argument
        specifies the location of the channel inside the stack, starting
        from the top (0) and increasing. If the position is specified as
        -1, then the channel is inserted above the active channel.
        
        Parameters:
        
        * image - The image.
        
        * channel - The channel.
        
        * parent - The parent channel.
        
        * position (default: 0) - The channel position.
        """
        pass

    def gimp_image_insert_layer(self, image: Gimp.Image=None, layer: Gimp.Layer=None, parent: Gimp.Layer=None, position: int=None):
        """Add the specified layer to the image.
        
        This procedure adds the specified layer to the image at the given
        position. If the specified parent is a valid layer group (See
        'gimp-item-is-group' and 'gimp-layer-group-new') then the layer
        is added inside the group. If the parent is 0, the layer is
        added inside the main stack, outside of any group. The position
        argument specifies the location of the layer inside the stack
        (or the group, if a valid parent was supplied), starting from
        the top (0) and increasing. If the position is specified as -1
        and the parent is specified as 0, then the layer is inserted
        above the active layer, or inside the group if the active layer
        is a layer group. The layer type must be compatible with the
        image base type.
        
        Parameters:
        
        * image - The image.
        
        * layer - The layer.
        
        * parent - The parent layer.
        
        * position (default: 0) - The layer position.
        """
        pass

    def gimp_image_insert_vectors(self, image: Gimp.Image=None, vectors: Gimp.Vectors=None, parent: Gimp.Vectors=None, position: int=None):
        """Add the specified vectors to the image.
        
        This procedure adds the specified vectors to the image at the given
        position. Since vectors groups are not currently supported, the
        parent argument must always be 0. The position argument
        specifies the location of the vectors inside the stack, starting
        from the top (0) and increasing. If the position is specified as
        -1, then the vectors is inserted above the active vectors.
        
        Parameters:
        
        * image - The image.
        
        * vectors - The vectors.
        
        * parent - The parent vectors.
        
        * position (default: 0) - The vectors position.
        """
        pass

    def gimp_image_is_dirty(self, image: Gimp.Image=None) -> bool:
        """Checks if the image has unsaved changes.
        
        This procedure checks the specified image's dirty count to see if it
        needs to be saved. Note that saving the image does not
        automatically set the dirty count to 0, you need to call
        'gimp-image-clean-all' after calling a save procedure to make
        the image clean.
        
        Parameters:
        
        * image - The image.
        
        Returns:
        
        * dirty (default: False) - TRUE if the image has unsaved changes.
        """
        pass

    def gimp_image_lower_channel(self, image: Gimp.Image=None, item: Gimp.Item=None):
        """Lower the specified item in its level in its item tree.
        
        This procedure lowers the specified item one step in the item tree. The
        procedure call will fail if there is no item below it.
        
        Parameters:
        
        * image - The image.
        
        * item - The item to lower.
        """
        pass

    def gimp_image_lower_item(self, image: Gimp.Image=None, item: Gimp.Item=None):
        """Lower the specified item in its level in its item tree.
        
        This procedure lowers the specified item one step in the item tree. The
        procedure call will fail if there is no item below it.
        
        Parameters:
        
        * image - The image.
        
        * item - The item to lower.
        """
        pass

    def gimp_image_lower_item_to_bottom(self, image: Gimp.Image=None, item: Gimp.Item=None):
        """Lower the specified item to the bottom of its level in its item tree.
        
        This procedure lowers the specified item to bottom of its level in the
        item tree. It will not move the layer if there is no layer below
        it.
        
        Parameters:
        
        * image - The image.
        
        * item - The item to lower to bottom.
        """
        pass

    def gimp_image_lower_layer(self, image: Gimp.Image=None, item: Gimp.Item=None):
        """Lower the specified item in its level in its item tree.
        
        This procedure lowers the specified item one step in the item tree. The
        procedure call will fail if there is no item below it.
        
        Parameters:
        
        * image - The image.
        
        * item - The item to lower.
        """
        pass

    def gimp_image_lower_layer_to_bottom(self, image: Gimp.Image=None, item: Gimp.Item=None):
        """Lower the specified item to the bottom of its level in its item tree.
        
        This procedure lowers the specified item to bottom of its level in the
        item tree. It will not move the layer if there is no layer below
        it.
        
        Parameters:
        
        * image - The image.
        
        * item - The item to lower to bottom.
        """
        pass

    def gimp_image_lower_vectors(self, image: Gimp.Image=None, item: Gimp.Item=None):
        """Lower the specified item in its level in its item tree.
        
        This procedure lowers the specified item one step in the item tree. The
        procedure call will fail if there is no item below it.
        
        Parameters:
        
        * image - The image.
        
        * item - The item to lower.
        """
        pass

    def gimp_image_lower_vectors_to_bottom(self, image: Gimp.Image=None, item: Gimp.Item=None):
        """Lower the specified item to the bottom of its level in its item tree.
        
        This procedure lowers the specified item to bottom of its level in the
        item tree. It will not move the layer if there is no layer below
        it.
        
        Parameters:
        
        * image - The image.
        
        * item - The item to lower to bottom.
        """
        pass

    def gimp_image_merge_down(self, image: Gimp.Image=None, merge_layer: Gimp.Layer=None, merge_type: Gimp.MergeType=None) -> Gimp.Layer:
        """Merge the layer passed and the first visible layer below.
        
        This procedure combines the passed layer and the first visible layer
        below it using the specified merge type. A merge type of
        EXPAND_AS_NECESSARY expands the final layer to encompass the
        areas of the visible layers. A merge type of CLIP_TO_IMAGE clips
        the final layer to the extents of the image. A merge type of
        CLIP_TO_BOTTOM_LAYER clips the final layer to the size of the
        bottommost layer.
        
        Parameters:
        
        * image - The image.
        
        * merge_layer - The layer to merge down from.
        
        * merge_type (default: <enum GIMP_EXPAND_AS_NECESSARY of type
          Gimp.MergeType>) - The type of merge.
        
        Returns:
        
        * layer - The resulting layer.
        """
        pass

    def gimp_image_merge_layer_group(self, image: Gimp.Image=None, layer_group: Gimp.Layer=None) -> Gimp.Layer:
        """Merge the passed layer group's layers into one normal layer.
        
        This procedure combines the layers of the passed layer group into a
        single normal layer, replacing the group.
        
        Parameters:
        
        * image - The image.
        
        * layer_group - The layer group to merge.
        
        Returns:
        
        * layer - The resulting layer.
        """
        pass

    def gimp_image_merge_visible_layers(self, image: Gimp.Image=None, merge_type: Gimp.MergeType=None) -> Gimp.Layer:
        """Merge the visible image layers into one.
        
        This procedure combines the visible layers into a single layer using the
        specified merge type. A merge type of EXPAND_AS_NECESSARY
        expands the final layer to encompass the areas of the visible
        layers. A merge type of CLIP_TO_IMAGE clips the final layer to
        the extents of the image. A merge type of CLIP_TO_BOTTOM_LAYER
        clips the final layer to the size of the bottommost layer.
        
        Parameters:
        
        * image - The image.
        
        * merge_type (default: <enum GIMP_EXPAND_AS_NECESSARY of type
          Gimp.MergeType>) - The type of merge.
        
        Returns:
        
        * layer - The resulting layer.
        """
        pass

    def gimp_image_new(self, width: int=None, height: int=None, type: Gimp.ImageBaseType=None) -> Gimp.Image:
        """Creates a new image with the specified width, height, and type.
        
        Creates a new image, undisplayed, with the specified extents and type. A
        layer should be created and added before this image is
        displayed, or subsequent calls to 'gimp-display-new' with this
        image as an argument will fail. Layers can be created using the
        'gimp-layer-new' commands. They can be added to an image using
        the 'gimp-image-insert-layer' command.
        
        If your image's type if INDEXED, a colormap must also be added with
        'gimp-image-set-colormap'. An indexed image without a colormap
        will output unexpected colors.
        
        Parameters:
        
        * width (default: 1) - The width of the image.
        
        * height (default: 1) - The height of the image.
        
        * type (default: <enum GIMP_RGB of type Gimp.ImageBaseType>) - The
          type of image.
        
        Returns:
        
        * image - The newly created image.
        """
        pass

    def gimp_image_new_with_precision(self, width: int=None, height: int=None, type: Gimp.ImageBaseType=None, precision: Gimp.Precision=None) -> Gimp.Image:
        """Creates a new image with the specified width, height, type and
        precision.
        
        Creates a new image, undisplayed with the specified extents, type and
        precision. Indexed images can only be created at
        GIMP_PRECISION_U8_NON_LINEAR precision. See 'gimp-image-new' for
        further details.
        
        Parameters:
        
        * width (default: 1) - The width of the image.
        
        * height (default: 1) - The height of the image.
        
        * type (default: <enum GIMP_RGB of type Gimp.ImageBaseType>) - The
          type of image.
        
        * precision (default: <enum GIMP_PRECISION_U8_LINEAR of type
          Gimp.Precision>) - The precision.
        
        Returns:
        
        * image - The newly created image.
        """
        pass

    def gimp_image_parasite_attach(self, image: Gimp.Image=None, parasite: Gimp.Parasite=None):
        """Add a parasite to an image.
        
        This procedure attaches a parasite to an image. It has no return values.
        
        Parameters:
        
        * image - The image.
        
        * parasite - The parasite to attach to an image.
        """
        pass

    def gimp_image_parasite_detach(self, image: Gimp.Image=None, name: str=None):
        """Removes a parasite from an image.
        
        This procedure detaches a parasite from an image. It has no return
        values.
        
        Parameters:
        
        * image - The image.
        
        * name - The name of the parasite to detach from an image.
        """
        pass

    def gimp_image_parasite_find(self, image: Gimp.Image=None, name: str=None) -> Gimp.Parasite:
        """Look up a parasite in an image.
        
        Finds and returns the parasite that was previously attached to an image.
        
        Parameters:
        
        * image - The image.
        
        * name - The name of the parasite to find.
        
        Returns:
        
        * parasite - The found parasite.
        """
        pass

    def gimp_image_parasite_list(self, image: Gimp.Image=None) -> List[str]:
        """List all parasites.
        
        Returns a list of the names of all currently attached parasites. These
        names can later be used to get the actual #GimpParasite with
        'gimp-image-get-parasite' when needed.
        
        Parameters:
        
        * image - The image.
        
        Returns:
        
        * parasites - The names of currently attached parasites.
        """
        pass

    def gimp_image_pick_color(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, x: float=None, y: float=None, sample_merged: bool=None, sample_average: bool=None, average_radius: float=None) -> Gegl.Color:
        """Determine the color at the given coordinates.
        
        This tool determines the color at the specified coordinates. The
        returned color is an RGB triplet even for grayscale and indexed
        drawables. If the coordinates lie outside of the extents of the
        specified drawables, then an error is returned. All drawables
        must belong to the image and be of the same type. If only one
        drawable is given and it has an alpha channel, the algorithm
        examines the alpha value of the drawable at the coordinates. If
        the alpha value is completely transparent (0), then an error is
        returned. With several drawables specified, the composite image
        with only these drawables is used. If the sample_merged
        parameter is TRUE, the data of the composite image will be used
        instead of that for the specified drawables. This is equivalent
        to sampling for colors after merging all visible layers. In the
        case of a merged sampling, the supplied drawables are ignored.
        
        Parameters:
        
        * image - The image.
        
        * num_drawables (default: 1) - The number of drawables.
        
        * drawables - The drawables to pick from.
        
        * x (default: 0.0) - x coordinate of upper-left corner of rectangle.
        
        * y (default: 0.0) - y coordinate of upper-left corner of rectangle.
        
        * sample_merged (default: False) - Use the composite image, not the
          drawables.
        
        * sample_average (default: False) - Average the color of all the
          pixels in a specified radius.
        
        * average_radius (default: 0.0) - The radius of pixels to average.
        
        Returns:
        
        * color - The return color.
        """
        pass

    def gimp_image_pick_correlate_layer(self, image: Gimp.Image=None, x: int=None, y: int=None) -> Gimp.Layer:
        """Find the layer visible at the specified coordinates.
        
        This procedure finds the layer which is visible at the specified
        coordinates. Layers which do not qualify are those whose extents
        do not pass within the specified coordinates, or which are
        transparent at the specified coordinates. This procedure will
        return -1 if no layer is found.
        
        Parameters:
        
        * image - The image.
        
        * x (default: 0) - The x coordinate for the pick.
        
        * y (default: 0) - The y coordinate for the pick.
        
        Returns:
        
        * layer - The layer found at the specified coordinates.
        """
        pass

    def gimp_image_policy_color_profile(self, image: Gimp.Image=None, interactive: bool=None):
        """Execute the color profile conversion policy.
        
        Process the image according to the color profile policy as set in
        Preferences. If GIMP is running as a GUI and interactive is
        TRUE, a dialog may be presented to the user depending on the
        policy. Otherwise, if the policy does not mandate the conversion
        to perform, the conversion to the preferred RGB or grayscale
        profile will happen, defaulting to built-in profiles if no
        preferred profiles were set in `Preferences`. This function
        should be used only if you want to follow user settings. If you
        intend to convert to a specific profile, call preferably
        'gimp-image-convert-color-profile'. And if you wish to leave
        whatever profile an image has, do not call any of these
        functions. Finally it is unnecessary to call this function in a
        format load procedure because this is called automatically by
        the core code when loading any image. You should only call this
        function explicitly when loading an image through a PDB call.
        
        Parameters:
        
        * image - The image.
        
        * interactive (default: False) - Querying the user through a dialog is
          a possibility.
        """
        pass

    def gimp_image_policy_rotate(self, image: Gimp.Image=None, interactive: bool=None):
        """Execute the "Orientation" metadata policy.
        
        Process the image according to the rotation policy as set in
        Preferences. If GIMP is running as a GUI and interactive is
        TRUE, a dialog may be presented to the user depending on the set
        policy. Otherwise, if the policy does not mandate the action to
        perform, the image will be rotated following the Orientation
        metadata. If you wish absolutely to rotate a loaded image
        following the Orientation metadata, do not use this function and
        process the metadata yourself. Indeed even with `interactive` to
        FALSE, user settings may leave the image unrotated. Finally it
        is unnecessary to call this function in a format load procedure
        because this is called automatically by the core code when
        loading any image. You should only call this function explicitly
        when loading an image through a PDB call.
        
        Parameters:
        
        * image - The image.
        
        * interactive (default: False) - Querying the user through a dialog is
          a possibility.
        """
        pass

    def gimp_image_raise_channel(self, image: Gimp.Image=None, item: Gimp.Item=None):
        """Raise the specified item in its level in its item tree.
        
        This procedure raises the specified item one step in the item tree. The
        procedure call will fail if there is no item above it.
        
        Parameters:
        
        * image - The image.
        
        * item - The item to raise.
        """
        pass

    def gimp_image_raise_item(self, image: Gimp.Image=None, item: Gimp.Item=None):
        """Raise the specified item in its level in its item tree.
        
        This procedure raises the specified item one step in the item tree. The
        procedure call will fail if there is no item above it.
        
        Parameters:
        
        * image - The image.
        
        * item - The item to raise.
        """
        pass

    def gimp_image_raise_item_to_top(self, image: Gimp.Image=None, item: Gimp.Item=None):
        """Raise the specified item to the top of its level in its item tree.
        
        This procedure raises the specified item to top of its level in the item
        tree. It will not move the item if there is no item above it.
        
        Parameters:
        
        * image - The image.
        
        * item - The item to raise to top.
        """
        pass

    def gimp_image_raise_layer(self, image: Gimp.Image=None, item: Gimp.Item=None):
        """Raise the specified item in its level in its item tree.
        
        This procedure raises the specified item one step in the item tree. The
        procedure call will fail if there is no item above it.
        
        Parameters:
        
        * image - The image.
        
        * item - The item to raise.
        """
        pass

    def gimp_image_raise_layer_to_top(self, image: Gimp.Image=None, item: Gimp.Item=None):
        """Raise the specified item to the top of its level in its item tree.
        
        This procedure raises the specified item to top of its level in the item
        tree. It will not move the item if there is no item above it.
        
        Parameters:
        
        * image - The image.
        
        * item - The item to raise to top.
        """
        pass

    def gimp_image_raise_vectors(self, image: Gimp.Image=None, item: Gimp.Item=None):
        """Raise the specified item in its level in its item tree.
        
        This procedure raises the specified item one step in the item tree. The
        procedure call will fail if there is no item above it.
        
        Parameters:
        
        * image - The image.
        
        * item - The item to raise.
        """
        pass

    def gimp_image_raise_vectors_to_top(self, image: Gimp.Image=None, item: Gimp.Item=None):
        """Raise the specified item to the top of its level in its item tree.
        
        This procedure raises the specified item to top of its level in the item
        tree. It will not move the item if there is no item above it.
        
        Parameters:
        
        * image - The image.
        
        * item - The item to raise to top.
        """
        pass

    def gimp_image_remove_channel(self, image: Gimp.Image=None, channel: Gimp.Channel=None):
        """Remove the specified channel from the image.
        
        This procedure removes the specified channel from the image. If the
        channel doesn't exist, an error is returned.
        
        Parameters:
        
        * image - The image.
        
        * channel - The channel.
        """
        pass

    def gimp_image_remove_layer(self, image: Gimp.Image=None, layer: Gimp.Layer=None):
        """Remove the specified layer from the image.
        
        This procedure removes the specified layer from the image. If the layer
        doesn't exist, an error is returned. If there are no layers left
        in the image, this call will fail. If this layer is the last
        layer remaining, the image will become empty and have no active
        layer.
        
        Parameters:
        
        * image - The image.
        
        * layer - The layer.
        """
        pass

    def gimp_image_remove_vectors(self, image: Gimp.Image=None, vectors: Gimp.Vectors=None):
        """Remove the specified path from the image.
        
        This procedure removes the specified path from the image. If the path
        doesn't exist, an error is returned.
        
        Parameters:
        
        * image - The image.
        
        * vectors - The vectors object.
        """
        pass

    def gimp_image_reorder_item(self, image: Gimp.Image=None, item: Gimp.Item=None, parent: Gimp.Item=None, position: int=None):
        """Reorder the specified item within its item tree.
        
        This procedure reorders the specified item within its item tree.
        
        Parameters:
        
        * image - The image.
        
        * item - The item to reorder.
        
        * parent - The new parent item.
        
        * position (default: 0) - The new position of the item.
        """
        pass

    def gimp_image_resize(self, image: Gimp.Image=None, new_width: int=None, new_height: int=None, offx: int=None, offy: int=None):
        """Resize the image to the specified extents.
        
        This procedure resizes the image so that it's new width and height are
        equal to the supplied parameters. Offsets are also provided
        which describe the position of the previous image's content. All
        channels within the image are resized according to the specified
        parameters; this includes the image selection mask. All layers
        within the image are repositioned according to the specified
        offsets.
        
        Parameters:
        
        * image - The image.
        
        * new_width (default: 1) - New image width.
        
        * new_height (default: 1) - New image height.
        
        * offx (default: 0) - x offset between upper left corner of old and
          new images: (new - old).
        
        * offy (default: 0) - y offset between upper left corner of old and
          new images: (new - old).
        """
        pass

    def gimp_image_resize_to_layers(self, image: Gimp.Image=None):
        """Resize the image to fit all layers.
        
        This procedure resizes the image to the bounding box of all layers of
        the image. All channels within the image are resized to the new
        size; this includes the image selection mask. All layers within
        the image are repositioned to the new image area.
        
        Parameters:
        
        * image - The image.
        """
        pass

    def gimp_image_rotate(self, image: Gimp.Image=None, rotate_type: Gimp.RotationType=None):
        """Rotates the image by the specified degrees.
        
        This procedure rotates the image.
        
        Parameters:
        
        * image - The image.
        
        * rotate_type (default: <enum GIMP_ROTATE_DEGREES90 of type
          Gimp.RotationType>) - Angle of rotation.
        """
        pass

    def gimp_image_scale(self, image: Gimp.Image=None, new_width: int=None, new_height: int=None):
        """Scale the image using the default interpolation method.
        
        This procedure scales the image so that its new width and height are
        equal to the supplied parameters. All layers and channels within
        the image are scaled according to the specified parameters; this
        includes the image selection mask. The interpolation method used
        can be set with 'gimp-context-set-interpolation'.
        
        Parameters:
        
        * image - The image.
        
        * new_width (default: 1) - New image width.
        
        * new_height (default: 1) - New image height.
        """
        pass

    def gimp_image_select_color(self, image: Gimp.Image=None, operation: Gimp.ChannelOps=None, drawable: Gimp.Drawable=None, color: Gegl.Color=None):
        """Create a selection by selecting all pixels (in the specified
        drawable) with the same (or similar) color to that specified.
        
        This tool creates a selection over the specified image. A by-color
        selection is determined by the supplied color under the
        constraints of the current context settings. Essentially, all
        pixels (in the drawable) that have color sufficiently close to
        the specified color (as determined by the threshold and
        criterion context values) are included in the selection. To
        select transparent regions, the color specified must also have
        minimum alpha.
        
        This procedure is affected by the following context setters:
        'gimp-context-set-antialias', 'gimp-context-set-feather',
        'gimp-context-set-feather-radius',
        'gimp-context-set-sample-merged',
        'gimp-context-set-sample-criterion',
        'gimp-context-set-sample-threshold',
        'gimp-context-set-sample-transparent'.
        
        In the case of a merged sampling, the supplied drawable is ignored.
        
        Parameters:
        
        * image - The affected image.
        
        * operation (default: <enum GIMP_CHANNEL_OP_ADD of type
          Gimp.ChannelOps>) - The selection operation.
        
        * drawable - The affected drawable.
        
        * color - The color to select.
        """
        pass

    def gimp_image_select_contiguous_color(self, image: Gimp.Image=None, operation: Gimp.ChannelOps=None, drawable: Gimp.Drawable=None, x: float=None, y: float=None):
        """Create a selection by selecting all pixels around specified
        coordinates with the same (or similar) color to that at the
        coordinates.
        
        This tool creates a contiguous selection over the specified image. A
        contiguous color selection is determined by a seed fill under
        the constraints of the current context settings. Essentially,
        the color at the specified coordinates (in the drawable) is
        measured and the selection expands outwards from that point to
        any adjacent pixels which are not significantly different (as
        determined by the threshold and criterion context settings).
        This process continues until no more expansion is possible. If
        antialiasing is turned on, the final selection mask will contain
        intermediate values based on close misses to the threshold bar
        at pixels along the seed fill boundary.
        
        This procedure is affected by the following context setters:
        'gimp-context-set-antialias', 'gimp-context-set-feather',
        'gimp-context-set-feather-radius',
        'gimp-context-set-sample-merged',
        'gimp-context-set-sample-criterion',
        'gimp-context-set-sample-threshold',
        'gimp-context-set-sample-transparent',
        'gimp-context-set-diagonal-neighbors'.
        
        In the case of a merged sampling, the supplied drawable is ignored. If
        the sample is merged, the specified coordinates are relative to
        the image origin; otherwise, they are relative to the drawable's
        origin.
        
        Parameters:
        
        * image - The affected image.
        
        * operation (default: <enum GIMP_CHANNEL_OP_ADD of type
          Gimp.ChannelOps>) - The selection operation.
        
        * drawable - The affected drawable.
        
        * x (default: 0.0) - x coordinate of initial seed fill point: (image
          coordinates).
        
        * y (default: 0.0) - y coordinate of initial seed fill point: (image
          coordinates).
        """
        pass

    def gimp_image_select_ellipse(self, image: Gimp.Image=None, operation: Gimp.ChannelOps=None, x: float=None, y: float=None, width: float=None, height: float=None):
        """Create an elliptical selection over the specified image.
        
        This tool creates an elliptical selection over the specified image. The
        elliptical region can be either added to, subtracted from, or
        replace the contents of the previous selection mask.
        
        This procedure is affected by the following context setters:
        'gimp-context-set-antialias', 'gimp-context-set-feather',
        'gimp-context-set-feather-radius'.
        
        Parameters:
        
        * image - The image.
        
        * operation (default: <enum GIMP_CHANNEL_OP_ADD of type
          Gimp.ChannelOps>) - The selection operation.
        
        * x (default: 0.0) - x coordinate of upper-left corner of ellipse
          bounding box.
        
        * y (default: 0.0) - y coordinate of upper-left corner of ellipse
          bounding box.
        
        * width (default: 0.0) - The width of the ellipse.
        
        * height (default: 0.0) - The height of the ellipse.
        """
        pass

    def gimp_image_select_item(self, image: Gimp.Image=None, operation: Gimp.ChannelOps=None, item: Gimp.Item=None):
        """Transforms the specified item into a selection.
        
        This procedure renders the item's outline into the current selection of
        the image the item belongs to. What exactly the item's outline
        is depends on the item type: for layers, it's the layer's alpha
        channel, for vectors the vector's shape.
        
        This procedure is affected by the following context setters:
        'gimp-context-set-antialias', 'gimp-context-set-feather',
        'gimp-context-set-feather-radius'.
        
        Parameters:
        
        * image - The image.
        
        * operation (default: <enum GIMP_CHANNEL_OP_ADD of type
          Gimp.ChannelOps>) - The desired operation with current
          selection.
        
        * item - The item to render to the selection.
        """
        pass

    def gimp_image_select_polygon(self, image: Gimp.Image=None, operation: Gimp.ChannelOps=None, num_segs: int=None, segs: Gimp.FloatArray=None):
        """Create a polygonal selection over the specified image.
        
        This tool creates a polygonal selection over the specified image. The
        polygonal region can be either added to, subtracted from, or
        replace the contents of the previous selection mask. The polygon
        is specified through an array of floating point numbers and its
        length. The length of array must be 2n, where n is the number of
        points. Each point is defined by 2 floating point values which
        correspond to the x and y coordinates. If the final point does
        not connect to the starting point, a connecting segment is
        automatically added.
        
        This procedure is affected by the following context setters:
        'gimp-context-set-antialias', 'gimp-context-set-feather',
        'gimp-context-set-feather-radius'.
        
        Parameters:
        
        * image - The image.
        
        * operation (default: <enum GIMP_CHANNEL_OP_ADD of type
          Gimp.ChannelOps>) - The selection operation.
        
        * num_segs (default: 2) - Number of points (count 1 coordinate as two
          points).
        
        * segs - Array of points: { p1.x, p1.y, p2.x, p2.y, ..., pn.x, pn.y}.
        """
        pass

    def gimp_image_select_rectangle(self, image: Gimp.Image=None, operation: Gimp.ChannelOps=None, x: float=None, y: float=None, width: float=None, height: float=None):
        """Create a rectangular selection over the specified image;.
        
        This tool creates a rectangular selection over the specified image. The
        rectangular region can be either added to, subtracted from, or
        replace the contents of the previous selection mask.
        
        This procedure is affected by the following context setters:
        'gimp-context-set-feather', 'gimp-context-set-feather-radius'.
        
        Parameters:
        
        * image - The image.
        
        * operation (default: <enum GIMP_CHANNEL_OP_ADD of type
          Gimp.ChannelOps>) - The selection operation.
        
        * x (default: 0.0) - x coordinate of upper-left corner of rectangle.
        
        * y (default: 0.0) - y coordinate of upper-left corner of rectangle.
        
        * width (default: 0.0) - The width of the rectangle.
        
        * height (default: 0.0) - The height of the rectangle.
        """
        pass

    def gimp_image_select_round_rectangle(self, image: Gimp.Image=None, operation: Gimp.ChannelOps=None, x: float=None, y: float=None, width: float=None, height: float=None, corner_radius_x: float=None, corner_radius_y: float=None):
        """Create a rectangular selection with round corners over the specified
        image;.
        
        This tool creates a rectangular selection with round corners over the
        specified image. The rectangular region can be either added to,
        subtracted from, or replace the contents of the previous
        selection mask. This procedure is affected by the following
        context setters: 'gimp-context-set-antialias',
        'gimp-context-set-feather', 'gimp-context-set-feather-radius'.
        
        Parameters:
        
        * image - The image.
        
        * operation (default: <enum GIMP_CHANNEL_OP_ADD of type
          Gimp.ChannelOps>) - The selection operation.
        
        * x (default: 0.0) - x coordinate of upper-left corner of rectangle.
        
        * y (default: 0.0) - y coordinate of upper-left corner of rectangle.
        
        * width (default: 0.0) - The width of the rectangle.
        
        * height (default: 0.0) - The height of the rectangle.
        
        * corner_radius_x (default: 0.0) - The corner radius in X direction.
        
        * corner_radius_y (default: 0.0) - The corner radius in Y direction.
        """
        pass

    def gimp_image_set_cmap(self, image: Gimp.Image=None, colormap: GLib.Bytes=None):
        """Sets the entries in the image's colormap.
        
        This procedure sets the entries in the specified image's colormap. The
        number of entries is specified by the 'num-bytes' parameter and
        corresponds to the number of INT8 triples that must be contained
        in the 'colormap' array. The actual number of colors in the
        transmitted colormap is 'num-bytes' / 3.
        
        Parameters:
        
        * image - The image.
        
        * colormap - The new colormap values.
        """
        pass

    def gimp_image_set_color_profile(self, image: Gimp.Image=None, color_profile: GLib.Bytes=None):
        """Sets the image's color profile.
        
        This procedure sets the image's color profile, or unsets it if NULL is
        passed as 'color_profile'. This procedure does no color
        conversion. However, it will change the pixel format of all
        layers to contain the babl space matching the profile. You must
        call this procedure before adding layers to the image.
        
        Parameters:
        
        * image - The image.
        
        * color_profile - The new serialized color profile.
        """
        pass

    def gimp_image_set_color_profile_from_file(self, image: Gimp.Image=None, file: Gio.File=None):
        """Sets the image's color profile from an ICC file.
        
        This procedure sets the image's color profile from a file containing an
        ICC profile, or unsets it if NULL is passed as 'file'. This
        procedure does no color conversion. However, it will change the
        pixel format of all layers to contain the babl space matching
        the profile. You must call this procedure before adding layers
        to the image.
        
        Parameters:
        
        * image - The image.
        
        * file - The file containing the new color profile.
        """
        pass

    def gimp_image_set_colormap(self, image: Gimp.Image=None, colormap: GLib.Bytes=None):
        """Sets the entries in the image's colormap.
        
        This procedure sets the entries in the specified image's colormap. The
        number of entries is specified by the 'num-bytes' parameter and
        corresponds to the number of INT8 triples that must be contained
        in the 'colormap' array. The actual number of colors in the
        transmitted colormap is 'num-bytes' / 3.
        
        Parameters:
        
        * image - The image.
        
        * colormap - The new colormap values.
        """
        pass

    def gimp_image_set_component_active(self, image: Gimp.Image=None, component: Gimp.ChannelType=None, active: bool=None):
        """Sets if the specified image's image component is active.
        
        This procedure sets if the specified image's image component (i.e. Red,
        Green, Blue intensity channels in an RGB image) is active or
        inactive -- whether or not it can be modified. If the specified
        component is not valid for the image type, an error is returned.
        
        Parameters:
        
        * image - The image.
        
        * component (default: <enum GIMP_CHANNEL_RED of type
          Gimp.ChannelType>) - The image component.
        
        * active (default: False) - Component is active.
        """
        pass

    def gimp_image_set_component_visible(self, image: Gimp.Image=None, component: Gimp.ChannelType=None, visible: bool=None):
        """Sets if the specified image's image component is visible.
        
        This procedure sets if the specified image's image component (i.e. Red,
        Green, Blue intensity channels in an RGB image) is visible or
        invisible -- whether or not it can be seen. If the specified
        component is not valid for the image type, an error is returned.
        
        Parameters:
        
        * image - The image.
        
        * component (default: <enum GIMP_CHANNEL_RED of type
          Gimp.ChannelType>) - The image component.
        
        * visible (default: False) - Component is visible.
        """
        pass

    def gimp_image_set_file(self, image: Gimp.Image=None, file: Gio.File=None):
        """Sets the specified XCF image's file.
        
        This procedure sets the specified image's file. This is to set the XCF
        file associated with your image. In particular, do not use this
        function to set the imported file in file import plug-ins. This
        is done by the core process.
        
        Parameters:
        
        * image - The image.
        
        * file - The new image file.
        """
        pass

    def gimp_image_set_metadata(self, image: Gimp.Image=None, metadata_string: str=None):
        """Set the image's metadata.
        
        Sets exif/iptc/xmp metadata on the image.
        
        Parameters:
        
        * image - The image.
        
        * metadata_string - The exif/ptc/xmp metadata as a string.
        """
        pass

    def gimp_image_set_resolution(self, image: Gimp.Image=None, xresolution: float=None, yresolution: float=None):
        """Sets the specified image's resolution.
        
        This procedure sets the specified image's resolution in dots per inch.
        This value is independent of any of the layers in this image. No
        scaling or resizing is performed.
        
        Parameters:
        
        * image - The image.
        
        * xresolution (default: 0.0) - The new image resolution in the x-axis,
          in dots per inch.
        
        * yresolution (default: 0.0) - The new image resolution in the y-axis,
          in dots per inch.
        """
        pass

    def gimp_image_set_selected_channels(self, image: Gimp.Image=None, num_channels: int=None, channels: Gimp.ObjectArray=None):
        """Sets the specified image's selected channels.
        
        The channels are set as the selected channels in the image. Any previous
        selected layers or channels are unselected. An exception is a
        previously existing floating selection, in which case this
        procedure will return an execution error.
        
        Parameters:
        
        * image - The image.
        
        * num_channels (default: 0) - The number of channels to select.
        
        * channels - The list of channels to select.
        """
        pass

    def gimp_image_set_selected_layers(self, image: Gimp.Image=None, num_layers: int=None, layers: Gimp.ObjectArray=None):
        """Sets the specified image's selected layers.
        
        The layers are set as the selected layers in the image. Any previous
        selected layers or channels are unselected. An exception is a
        previously existing floating selection, in which case this
        procedure will return an execution error.
        
        Parameters:
        
        * image - The image.
        
        * num_layers (default: 0) - The number of layers to select.
        
        * layers - The list of layers to select.
        """
        pass

    def gimp_image_set_selected_vectors(self, image: Gimp.Image=None, num_vectors: int=None, vectors: Gimp.ObjectArray=None):
        """Sets the specified image's selected vectors.
        
        The vectors are set as the selected vectors in the image.
        
        Parameters:
        
        * image - The image.
        
        * num_vectors (default: 0) - The number of vectors to select.
        
        * vectors - The list of vectors to select.
        """
        pass

    def gimp_image_set_simulation_bpc(self, image: Gimp.Image=None, bpc: bool=None):
        """Sets whether the image has Black Point Compensation enabled for its
        simulation.
        
        This procedure whether the image has Black Point Compensation enabled
        for its simulation.
        
        Parameters:
        
        * image - The image.
        
        * bpc (default: False) - The Black Point Compensation status.
        """
        pass

    def gimp_image_set_simulation_intent(self, image: Gimp.Image=None, intent: Gimp.ColorRenderingIntent=None):
        """Sets the image's simulation rendering intent.
        
        This procedure sets the image's simulation rendering intent.
        
        Parameters:
        
        * image - The image.
        
        * intent (default: <enum GIMP_COLOR_RENDERING_INTENT_PERCEPTUAL of
          type Gimp.ColorRenderingIntent>) - A
          GimpColorRenderingIntent.
        """
        pass

    def gimp_image_set_simulation_profile(self, image: Gimp.Image=None, color_profile: GLib.Bytes=None):
        """Sets the image's simulation color profile.
        
        This procedure sets the image's simulation color profile, or unsets it
        if NULL is passed as 'color_profile'. This procedure does no
        color conversion.
        
        Parameters:
        
        * image - The image.
        
        * color_profile - The new serialized simulation color profile.
        """
        pass

    def gimp_image_set_simulation_profile_from_file(self, image: Gimp.Image=None, file: Gio.File=None):
        """Sets the image's simulation color profile from an ICC file.
        
        This procedure sets the image's simulation color profile from a file
        containing an ICC profile, or unsets it if NULL is passed as
        'file'. This procedure does no color conversion.
        
        Parameters:
        
        * image - The image.
        
        * file - The file containing the new simulation color profile.
        """
        pass

    def gimp_image_set_tattoo_state(self, image: Gimp.Image=None, tattoo_state: int=None):
        """Set the tattoo state associated with the image.
        
        This procedure sets the tattoo state of the image. Use only by save/load
        plug-ins that wish to preserve an images tattoo state. Using
        this function at other times will produce unexpected results. A
        full check of uniqueness of states in layers, channels and paths
        will be performed by this procedure and a execution failure will
        be returned if this fails. A failure will also be returned if
        the new tattoo state value is less than the maximum tattoo value
        from all of the tattoos from the paths, layers and channels.
        After the image data has been loaded and all the tattoos have
        been set then this is the last procedure that should be called.
        If effectively does a status check on the tattoo values that
        have been set to make sure that all is OK.
        
        Parameters:
        
        * image - The image.
        
        * tattoo_state (default: 1) - The new image tattoo state.
        """
        pass

    def gimp_image_set_unit(self, image: Gimp.Image=None, unit: Gimp.Unit=None):
        """Sets the specified image's unit.
        
        This procedure sets the specified image's unit. No scaling or resizing
        is performed. This value is independent of any of the layers in
        this image. See the gimp_unit_*() procedure definitions for the
        valid range of unit IDs and a description of the unit system.
        
        Parameters:
        
        * image - The image.
        
        * unit (default: 1) - The new image unit.
        """
        pass

    def gimp_image_thaw_channels(self, image: Gimp.Image=None):
        """Thaw the image's channel list.
        
        This procedure thaws the channel list of the image, re-enabling updates
        to the Channels dialog.
        
        This procedure should match a corresponding call to
        'gimp-image-freeze-channels'.
        
        Parameters:
        
        * image - The image.
        """
        pass

    def gimp_image_thaw_layers(self, image: Gimp.Image=None):
        """Thaw the image's layer list.
        
        This procedure thaws the layer list of the image, re-enabling updates to
        the Layers dialog.
        
        This procedure should match a corresponding call to
        'gimp-image-freeze-layers'.
        
        Parameters:
        
        * image - The image.
        """
        pass

    def gimp_image_thaw_vectors(self, image: Gimp.Image=None):
        """Thaw the image's vectors list.
        
        This procedure thaws the vectors list of the image, re-enabling updates
        to the Paths dialog.
        
        This procedure should match a corresponding call to
        'gimp-image-freeze-vectors'.
        
        Parameters:
        
        * image - The image.
        """
        pass

    def gimp_image_thumbnail(self, image: Gimp.Image=None, width: int=None, height: int=None) -> Tuple[int, int, int, GLib.Bytes]:
        """Get a thumbnail of an image.
        
        This function gets data from which a thumbnail of an image preview can
        be created. Maximum x or y dimension is 1024 pixels. The pixels
        are returned in RGB[A] or GRAY[A] format. The bpp return value
        gives the number of bits per pixel in the image.
        
        Parameters:
        
        * image - The image.
        
        * width (default: 1) - The requested thumbnail width.
        
        * height (default: 1) - The requested thumbnail height.
        
        Returns:
        
        * actual_width (default: 0) - The previews width.
        
        * actual_height (default: 0) - The previews height.
        
        * bpp (default: 0) - The previews bpp.
        
        * thumbnail_data - The thumbnail data.
        """
        pass

    def gimp_image_undo_disable(self, image: Gimp.Image=None) -> bool:
        """Disable the image's undo stack.
        
        This procedure disables the image's undo stack, allowing subsequent
        operations to ignore their undo steps. This is generally called
        in conjunction with 'gimp-image-undo-enable' to temporarily
        disable an image undo stack. This is advantageous because saving
        undo steps can be time and memory intensive.
        
        Parameters:
        
        * image - The image.
        
        Returns:
        
        * disabled (default: False) - TRUE if the image undo has been
          disabled.
        """
        pass

    def gimp_image_undo_enable(self, image: Gimp.Image=None) -> bool:
        """Enable the image's undo stack.
        
        This procedure enables the image's undo stack, allowing subsequent
        operations to store their undo steps. This is generally called
        in conjunction with 'gimp-image-undo-disable' to temporarily
        disable an image undo stack.
        
        Parameters:
        
        * image - The image.
        
        Returns:
        
        * enabled (default: False) - TRUE if the image undo has been enabled.
        """
        pass

    def gimp_image_undo_freeze(self, image: Gimp.Image=None) -> bool:
        """Freeze the image's undo stack.
        
        This procedure freezes the image's undo stack, allowing subsequent
        operations to ignore their undo steps. This is generally called
        in conjunction with 'gimp-image-undo-thaw' to temporarily
        disable an image undo stack. This is advantageous because saving
        undo steps can be time and memory intensive.
        'gimp-image-undo-freeze' / 'gimp-image-undo-thaw' and
        'gimp-image-undo-disable' / 'gimp-image-undo-enable' differ in
        that the former does not free up all undo steps when undo is
        thawed, so is more suited to interactive in-situ previews. It is
        important in this case that the image is back to the same state
        it was frozen in before thawing, else 'undo' behavior is
        undefined.
        
        Parameters:
        
        * image - The image.
        
        Returns:
        
        * frozen (default: False) - TRUE if the image undo has been frozen.
        """
        pass

    def gimp_image_undo_group_end(self, image: Gimp.Image=None):
        """Finish a group undo.
        
        This function must be called once for each 'gimp-image-undo-group-start'
        call that is made.
        
        Parameters:
        
        * image - The ID of the image in which to close an undo group.
        """
        pass

    def gimp_image_undo_group_start(self, image: Gimp.Image=None):
        """Starts a group undo.
        
        This function is used to start a group undo--necessary for logically
        combining two or more undo operations into a single operation.
        This call must be used in conjunction with a
        'gimp-image-undo-group-end' call.
        
        Parameters:
        
        * image - The ID of the image in which to open an undo group.
        """
        pass

    def gimp_image_undo_is_enabled(self, image: Gimp.Image=None) -> bool:
        """Check if the image's undo stack is enabled.
        
        This procedure checks if the image's undo stack is currently enabled or
        disabled. This is useful when several plug-ins or scripts call
        each other and want to check if their caller has already used
        'gimp-image-undo-disable' or 'gimp-image-undo-freeze'.
        
        Parameters:
        
        * image - The image.
        
        Returns:
        
        * enabled (default: False) - TRUE if undo is enabled for this image.
        """
        pass

    def gimp_image_undo_thaw(self, image: Gimp.Image=None) -> bool:
        """Thaw the image's undo stack.
        
        This procedure thaws the image's undo stack, allowing subsequent
        operations to store their undo steps. This is generally called
        in conjunction with 'gimp-image-undo-freeze' to temporarily
        freeze an image undo stack. 'gimp-image-undo-thaw' does NOT free
        the undo stack as 'gimp-image-undo-enable' does, so is suited
        for situations where one wishes to leave the undo stack in the
        same state in which one found it despite non-destructively
        playing with the image in the meantime. An example would be
        in-situ plug-in previews. Balancing freezes and thaws and
        ensuring image consistency is the responsibility of the caller.
        
        Parameters:
        
        * image - The image.
        
        Returns:
        
        * thawed (default: False) - TRUE if the image undo has been thawed.
        """
        pass

    def gimp_image_unset_active_channel(self, image: Gimp.Image=None):
        """Unsets the active channel in the specified image.
        
        If an active channel exists, it is unset. There then exists no active
        channel, and if desired, one can be set through a call to 'Set
        Active Channel'. No error is returned in the case of no existing
        active channel.
        
        Parameters:
        
        * image - The image.
        """
        pass

    def gimp_item_attach_parasite(self, item: Gimp.Item=None, parasite: Gimp.Parasite=None):
        """Add a parasite to an item.
        
        This procedure attaches a parasite to an item. It has no return values.
        
        Parameters:
        
        * item - The item.
        
        * parasite - The parasite to attach to the item.
        """
        pass

    def gimp_item_delete(self, item: Gimp.Item=None):
        """Delete a item.
        
        This procedure deletes the specified item. This must not be done if the
        image containing this item was already deleted or if the item
        was already removed from the image. The only case in which this
        procedure is useful is if you want to get rid of a item which
        has not yet been added to an image.
        
        Parameters:
        
        * item - The item to delete.
        """
        pass

    def gimp_item_detach_parasite(self, item: Gimp.Item=None, name: str=None):
        """Removes a parasite from an item.
        
        This procedure detaches a parasite from an item. It has no return
        values.
        
        Parameters:
        
        * item - The item.
        
        * name - The name of the parasite to detach from the item.
        """
        pass

    def gimp_item_get_children(self, item: Gimp.Item=None) -> Tuple[int, Gimp.ObjectArray]:
        """Returns the item's list of children.
        
        This procedure returns the list of items which are children of the
        specified item. The order is topmost to bottommost.
        
        Parameters:
        
        * item - The item.
        
        Returns:
        
        * num_children (default: 0) - The item's number of children.
        
        * children - The item's list of children.
        """
        pass

    def gimp_item_get_color_tag(self, item: Gimp.Item=None) -> Gimp.ColorTag:
        """Get the color tag of the specified item.
        
        This procedure returns the specified item's color tag.
        
        Parameters:
        
        * item - The item.
        
        Returns:
        
        * color_tag (default: <enum GIMP_COLOR_TAG_NONE of type
          Gimp.ColorTag>) - The item's color tag.
        """
        pass

    def gimp_item_get_expanded(self, item: Gimp.Item=None) -> bool:
        """Returns whether the item is expanded.
        
        This procedure returns TRUE if the specified item is expanded.
        
        Parameters:
        
        * item - The item.
        
        Returns:
        
        * expanded (default: False) - TRUE if the item is expanded, FALSE
          otherwise.
        """
        pass

    def gimp_item_get_image(self, item: Gimp.Item=None) -> Gimp.Image:
        """Returns the item's image.
        
        This procedure returns the item's image.
        
        Parameters:
        
        * item - The item.
        
        Returns:
        
        * image - The item's image.
        """
        pass

    def gimp_item_get_lock_content(self, item: Gimp.Item=None) -> bool:
        """Get the 'lock content' state of the specified item.
        
        This procedure returns the specified item's lock content state.
        
        Parameters:
        
        * item - The item.
        
        Returns:
        
        * lock_content (default: False) - Whether the item's contents are
          locked.
        """
        pass

    def gimp_item_get_lock_position(self, item: Gimp.Item=None) -> bool:
        """Get the 'lock position' state of the specified item.
        
        This procedure returns the specified item's lock position state.
        
        Parameters:
        
        * item - The item.
        
        Returns:
        
        * lock_position (default: False) - Whether the item's position is
          locked.
        """
        pass

    def gimp_item_get_lock_visibility(self, item: Gimp.Item=None) -> bool:
        """Get the 'lock visibility' state of the specified item.
        
        This procedure returns the specified item's lock visibility state.
        
        Parameters:
        
        * item - The item.
        
        Returns:
        
        * lock_visibility (default: False) - Whether the item's visibility is
          locked.
        """
        pass

    def gimp_item_get_name(self, item: Gimp.Item=None) -> str:
        """Get the name of the specified item.
        
        This procedure returns the specified item's name.
        
        Parameters:
        
        * item - The item.
        
        Returns:
        
        * name - The item name.
        """
        pass

    def gimp_item_get_parasite(self, item: Gimp.Item=None, name: str=None) -> Gimp.Parasite:
        """Look up a parasite in an item.
        
        Finds and returns the parasite that is attached to an item.
        
        Parameters:
        
        * item - The item.
        
        * name - The name of the parasite to find.
        
        Returns:
        
        * parasite - The found parasite.
        """
        pass

    def gimp_item_get_parasite_list(self, item: Gimp.Item=None) -> List[str]:
        """List all parasites.
        
        Returns a list of all parasites currently attached the an item.
        
        Parameters:
        
        * item - The item.
        
        Returns:
        
        * parasites - The names of currently attached parasites.
        """
        pass

    def gimp_item_get_parent(self, item: Gimp.Item=None) -> Gimp.Item:
        """Returns the item's parent item.
        
        This procedure returns the item's parent item, if any.
        
        Parameters:
        
        * item - The item.
        
        Returns:
        
        * parent - The item's parent item.
        """
        pass

    def gimp_item_get_tattoo(self, item: Gimp.Item=None) -> int:
        """Get the tattoo of the specified item.
        
        This procedure returns the specified item's tattoo. A tattoo is a unique
        and permanent identifier attached to a item that can be used to
        uniquely identify a item within an image even between sessions.
        
        Parameters:
        
        * item - The item.
        
        Returns:
        
        * tattoo (default: 1) - The item tattoo.
        """
        pass

    def gimp_item_get_visible(self, item: Gimp.Item=None) -> bool:
        """Get the visibility of the specified item.
        
        This procedure returns the specified item's visibility.
        
        Parameters:
        
        * item - The item.
        
        Returns:
        
        * visible (default: False) - The item visibility.
        """
        pass

    def gimp_item_id_is_channel(self, item_id: int=None) -> bool:
        """Returns whether the item ID is a channel.
        
        This procedure returns TRUE if the specified item ID is a channel.
        
        Parameters:
        
        * item_id (default: 0) - The item ID.
        
        Returns:
        
        * channel (default: False) - TRUE if the item ID is a channel, FALSE
          otherwise.
        """
        pass

    def gimp_item_id_is_drawable(self, item_id: int=None) -> bool:
        """Returns whether the item ID is a drawable.
        
        This procedure returns TRUE if the specified item ID is a drawable.
        
        Parameters:
        
        * item_id (default: 0) - The item ID.
        
        Returns:
        
        * drawable (default: False) - TRUE if the item ID is a drawable, FALSE
          otherwise.
        """
        pass

    def gimp_item_id_is_layer(self, item_id: int=None) -> bool:
        """Returns whether the item ID is a layer.
        
        This procedure returns TRUE if the specified item ID is a layer.
        
        Parameters:
        
        * item_id (default: 0) - The item ID.
        
        Returns:
        
        * layer (default: False) - TRUE if the item is a layer, FALSE
          otherwise.
        """
        pass

    def gimp_item_id_is_layer_mask(self, item_id: int=None) -> bool:
        """Returns whether the item ID is a layer mask.
        
        This procedure returns TRUE if the specified item ID is a layer mask.
        
        Parameters:
        
        * item_id (default: 0) - The item.
        
        Returns:
        
        * layer_mask (default: False) - TRUE if the item ID is a layer mask,
          FALSE otherwise.
        """
        pass

    def gimp_item_id_is_selection(self, item_id: int=None) -> bool:
        """Returns whether the item ID is a selection.
        
        This procedure returns TRUE if the specified item ID is a selection.
        
        Parameters:
        
        * item_id (default: 0) - The item ID.
        
        Returns:
        
        * selection (default: False) - TRUE if the item ID is a selection,
          FALSE otherwise.
        """
        pass

    def gimp_item_id_is_text_layer(self, item_id: int=None) -> bool:
        """Returns whether the item ID is a text layer.
        
        This procedure returns TRUE if the specified item ID is a text layer.
        
        Parameters:
        
        * item_id (default: 0) - The item ID.
        
        Returns:
        
        * text_layer (default: False) - TRUE if the item is a text layer,
          FALSE otherwise.
        """
        pass

    def gimp_item_id_is_valid(self, item_id: int=None) -> bool:
        """Returns TRUE if the item ID is valid.
        
        This procedure checks if the given item ID is valid and refers to an
        existing item.
        
        Parameters:
        
        * item_id (default: 0) - The item ID to check.
        
        Returns:
        
        * valid (default: False) - Whether the item ID is valid.
        """
        pass

    def gimp_item_id_is_vectors(self, item_id: int=None) -> bool:
        """Returns whether the item ID is a vectors.
        
        This procedure returns TRUE if the specified item ID is a vectors.
        
        Parameters:
        
        * item_id (default: 0) - The item ID.
        
        Returns:
        
        * vectors (default: False) - TRUE if the item ID is a vectors, FALSE
          otherwise.
        """
        pass

    def gimp_item_is_group(self, item: Gimp.Item=None) -> bool:
        """Returns whether the item is a group item.
        
        This procedure returns TRUE if the specified item is a group item which
        can have children.
        
        Parameters:
        
        * item - The item.
        
        Returns:
        
        * group (default: False) - TRUE if the item is a group, FALSE
          otherwise.
        """
        pass

    def gimp_item_set_color_tag(self, item: Gimp.Item=None, color_tag: Gimp.ColorTag=None):
        """Set the color tag of the specified item.
        
        This procedure sets the specified item's color tag.
        
        Parameters:
        
        * item - The item.
        
        * color_tag (default: <enum GIMP_COLOR_TAG_NONE of type
          Gimp.ColorTag>) - The new item color tag.
        """
        pass

    def gimp_item_set_expanded(self, item: Gimp.Item=None, expanded: bool=None):
        """Sets the expanded state of the item.
        
        This procedure expands or collapses the item.
        
        Parameters:
        
        * item - The item.
        
        * expanded (default: False) - TRUE to expand the item, FALSE to
          collapse the item.
        """
        pass

    def gimp_item_set_lock_content(self, item: Gimp.Item=None, lock_content: bool=None):
        """Set the 'lock content' state of the specified item.
        
        This procedure sets the specified item's lock content state.
        
        Parameters:
        
        * item - The item.
        
        * lock_content (default: False) - The new item 'lock content' state.
        """
        pass

    def gimp_item_set_lock_position(self, item: Gimp.Item=None, lock_position: bool=None):
        """Set the 'lock position' state of the specified item.
        
        This procedure sets the specified item's lock position state.
        
        Parameters:
        
        * item - The item.
        
        * lock_position (default: False) - The new item 'lock position' state.
        """
        pass

    def gimp_item_set_lock_visibility(self, item: Gimp.Item=None, lock_visibility: bool=None):
        """Set the 'lock visibility' state of the specified item.
        
        This procedure sets the specified item's lock visibility state.
        
        Parameters:
        
        * item - The item.
        
        * lock_visibility (default: False) - The new item 'lock visibility'
          state.
        """
        pass

    def gimp_item_set_name(self, item: Gimp.Item=None, name: str=None):
        """Set the name of the specified item.
        
        This procedure sets the specified item's name.
        
        Parameters:
        
        * item - The item.
        
        * name - The new item name.
        """
        pass

    def gimp_item_set_tattoo(self, item: Gimp.Item=None, tattoo: int=None):
        """Set the tattoo of the specified item.
        
        This procedure sets the specified item's tattoo. A tattoo is a unique
        and permanent identifier attached to a item that can be used to
        uniquely identify a item within an image even between sessions.
        
        Parameters:
        
        * item - The item.
        
        * tattoo (default: 1) - The new item tattoo.
        """
        pass

    def gimp_item_set_visible(self, item: Gimp.Item=None, visible: bool=None):
        """Set the visibility of the specified item.
        
        This procedure sets the specified item's visibility.
        
        Parameters:
        
        * item - The item.
        
        * visible (default: False) - The new item visibility.
        """
        pass

    def gimp_item_transform_2d(self, item: Gimp.Item=None, source_x: float=None, source_y: float=None, scale_x: float=None, scale_y: float=None, angle: float=None, dest_x: float=None, dest_y: float=None) -> Gimp.Item:
        """Transform the specified item in 2d.
        
        This procedure transforms the specified item.
        
        The transformation is done by scaling by the x and y scale factors about
        the point (source_x, source_y), then rotating around the same
        point, then translating that point to the new position (dest_x,
        dest_y).
        
        If a selection exists and the item is a drawable, the portion of the
        drawable which lies under the selection is cut from the drawable
        and made into a floating selection which is then transformed as
        specified. The return value is the ID of the transformed
        floating selection.
        
        If there is no selection or the item is not a drawable, the entire item
        will be transformed according to the specified parameters. The
        return value will be equal to the item ID supplied as input.
        
        This procedure is affected by the following context setters:
        'gimp-context-set-interpolation',
        'gimp-context-set-transform-direction',
        'gimp-context-set-transform-resize'.
        
        Parameters:
        
        * item - The affected item.
        
        * source_x (default: 0.0) - X coordinate of the transformation center.
        
        * source_y (default: 0.0) - Y coordinate of the transformation center.
        
        * scale_x (default: 0.0) - Amount to scale in x direction.
        
        * scale_y (default: 0.0) - Amount to scale in y direction.
        
        * angle (default: 0.0) - The angle of rotation (radians).
        
        * dest_x (default: 0.0) - X coordinate of where the center goes.
        
        * dest_y (default: 0.0) - Y coordinate of where the center goes.
        
        Returns:
        
        * item - The transformed item.
        """
        pass

    def gimp_item_transform_flip(self, item: Gimp.Item=None, x0: float=None, y0: float=None, x1: float=None, y1: float=None) -> Gimp.Item:
        """Flip the specified item around a given line.
        
        This procedure flips the specified item.
        
        If a selection exists and the item is a drawable, the portion of the
        drawable which lies under the selection is cut from the drawable
        and made into a floating selection which is then flipped. The
        axis to flip around is specified by specifying two points from
        that line. The return value is the ID of the flipped floating
        selection.
        
        If there is no selection or the item is not a drawable, the entire item
        will be flipped around the specified axis. The return value will
        be equal to the item ID supplied as input.
        
        This procedure is affected by the following context setters:
        'gimp-context-set-interpolation',
        'gimp-context-set-transform-direction',
        'gimp-context-set-transform-resize'.
        
        Parameters:
        
        * item - The affected item.
        
        * x0 (default: 0.0) - horz. coord. of one end of axis.
        
        * y0 (default: 0.0) - vert. coord. of one end of axis.
        
        * x1 (default: 0.0) - horz. coord. of other end of axis.
        
        * y1 (default: 0.0) - vert. coord. of other end of axis.
        
        Returns:
        
        * item - The flipped item.
        """
        pass

    def gimp_item_transform_flip_simple(self, item: Gimp.Item=None, flip_type: Gimp.OrientationType=None, auto_center: bool=None, axis: float=None) -> Gimp.Item:
        """Flip the specified item either vertically or horizontally.
        
        This procedure flips the specified item.
        
        If a selection exists and the item is a drawable, the portion of the
        drawable which lies under the selection is cut from the drawable
        and made into a floating selection which is then flipped. If
        auto_center is set to TRUE, the flip is around the selection's
        center. Otherwise, the coordinate of the axis needs to be
        specified. The return value is the ID of the flipped floating
        selection.
        
        If there is no selection or the item is not a drawable, the entire item
        will be flipped around its center if auto_center is set to TRUE,
        otherwise the coordinate of the axis needs to be specified. The
        return value will be equal to the item ID supplied as input.
        
        This procedure is affected by the following context setters:
        'gimp-context-set-transform-resize'.
        
        Parameters:
        
        * item - The affected item.
        
        * flip_type (default: <enum GIMP_ORIENTATION_HORIZONTAL of type
          Gimp.OrientationType>) - Type of flip.
        
        * auto_center (default: False) - Whether to automatically position the
          axis in the selection center.
        
        * axis (default: 0.0) - coord. of flip axis.
        
        Returns:
        
        * item - The flipped item.
        """
        pass

    def gimp_item_transform_matrix(self, item: Gimp.Item=None, coeff_0_0: float=None, coeff_0_1: float=None, coeff_0_2: float=None, coeff_1_0: float=None, coeff_1_1: float=None, coeff_1_2: float=None, coeff_2_0: float=None, coeff_2_1: float=None, coeff_2_2: float=None) -> Gimp.Item:
        """Transform the specified item in 2d.
        
        This procedure transforms the specified item.
        
        The transformation is done by assembling a 3x3 matrix from the
        coefficients passed.
        
        If a selection exists and the item is a drawable, the portion of the
        drawable which lies under the selection is cut from the drawable
        and made into a floating selection which is then transformed as
        specified. The return value is the ID of the transformed
        floating selection.
        
        If there is no selection or the item is not a drawable, the entire item
        will be transformed according to the specified matrix. The
        return value will be equal to the item ID supplied as input.
        
        This procedure is affected by the following context setters:
        'gimp-context-set-interpolation',
        'gimp-context-set-transform-direction',
        'gimp-context-set-transform-resize'.
        
        Parameters:
        
        * item - The affected item.
        
        * coeff_0_0 (default: 0.0) - coefficient (0,0) of the transformation
          matrix.
        
        * coeff_0_1 (default: 0.0) - coefficient (0,1) of the transformation
          matrix.
        
        * coeff_0_2 (default: 0.0) - coefficient (0,2) of the transformation
          matrix.
        
        * coeff_1_0 (default: 0.0) - coefficient (1,0) of the transformation
          matrix.
        
        * coeff_1_1 (default: 0.0) - coefficient (1,1) of the transformation
          matrix.
        
        * coeff_1_2 (default: 0.0) - coefficient (1,2) of the transformation
          matrix.
        
        * coeff_2_0 (default: 0.0) - coefficient (2,0) of the transformation
          matrix.
        
        * coeff_2_1 (default: 0.0) - coefficient (2,1) of the transformation
          matrix.
        
        * coeff_2_2 (default: 0.0) - coefficient (2,2) of the transformation
          matrix.
        
        Returns:
        
        * item - The transformed item.
        """
        pass

    def gimp_item_transform_perspective(self, item: Gimp.Item=None, x0: float=None, y0: float=None, x1: float=None, y1: float=None, x2: float=None, y2: float=None, x3: float=None, y3: float=None) -> Gimp.Item:
        """Perform a possibly non-affine transformation on the specified item.
        
        This procedure performs a possibly non-affine transformation on the
        specified item by allowing the corners of the original bounding
        box to be arbitrarily remapped to any values.
        
        The 4 coordinates specify the new locations of each corner of the
        original bounding box. By specifying these values, any affine
        transformation (rotation, scaling, translation) can be affected.
        Additionally, these values can be specified such that the
        resulting transformed item will appear to have been projected
        via a perspective transform.
        
        If a selection exists and the item is a drawable, the portion of the
        drawable which lies under the selection is cut from the drawable
        and made into a floating selection which is then transformed as
        specified. The return value is the ID of the transformed
        floating selection.
        
        If there is no selection or the item is not a drawable, the entire item
        will be transformed according to the specified mapping. The
        return value will be equal to the item ID supplied as input.
        
        This procedure is affected by the following context setters:
        'gimp-context-set-interpolation',
        'gimp-context-set-transform-direction',
        'gimp-context-set-transform-resize'.
        
        Parameters:
        
        * item - The affected item.
        
        * x0 (default: 0.0) - The new x coordinate of upper-left corner of
          original bounding box.
        
        * y0 (default: 0.0) - The new y coordinate of upper-left corner of
          original bounding box.
        
        * x1 (default: 0.0) - The new x coordinate of upper-right corner of
          original bounding box.
        
        * y1 (default: 0.0) - The new y coordinate of upper-right corner of
          original bounding box.
        
        * x2 (default: 0.0) - The new x coordinate of lower-left corner of
          original bounding box.
        
        * y2 (default: 0.0) - The new y coordinate of lower-left corner of
          original bounding box.
        
        * x3 (default: 0.0) - The new x coordinate of lower-right corner of
          original bounding box.
        
        * y3 (default: 0.0) - The new y coordinate of lower-right corner of
          original bounding box.
        
        Returns:
        
        * item - The transformed item.
        """
        pass

    def gimp_item_transform_rotate(self, item: Gimp.Item=None, angle: float=None, auto_center: bool=None, center_x: float=None, center_y: float=None) -> Gimp.Item:
        """Rotate the specified item about given coordinates through the
        specified angle.
        
        This function rotates the specified item.
        
        If a selection exists and the item is a drawable, the portion of the
        drawable which lies under the selection is cut from the drawable
        and made into a floating selection which is then rotated by the
        specified amount. If auto_center is set to TRUE, the rotation is
        around the selection's center. Otherwise, the coordinate of the
        center point needs to be specified. The return value is the ID
        of the rotated floating selection.
        
        If there is no selection or the item is not a drawable, the entire item
        will be rotated around its center if auto_center is set to TRUE,
        otherwise the coordinate of the center point needs to be
        specified. The return value will be equal to the item ID
        supplied as input.
        
        This procedure is affected by the following context setters:
        'gimp-context-set-interpolation',
        'gimp-context-set-transform-direction',
        'gimp-context-set-transform-resize'.
        
        Parameters:
        
        * item - The affected item.
        
        * angle (default: 0.0) - The angle of rotation (radians).
        
        * auto_center (default: False) - Whether to automatically rotate
          around the selection center.
        
        * center_x (default: 0.0) - The hor. coordinate of the center of
          rotation.
        
        * center_y (default: 0.0) - The vert. coordinate of the center of
          rotation.
        
        Returns:
        
        * item - The rotated item.
        """
        pass

    def gimp_item_transform_rotate_simple(self, item: Gimp.Item=None, rotate_type: Gimp.RotationType=None, auto_center: bool=None, center_x: float=None, center_y: float=None) -> Gimp.Item:
        """Rotate the specified item about given coordinates through the
        specified angle.
        
        This function rotates the specified item.
        
        If a selection exists and the item is a drawable, the portion of the
        drawable which lies under the selection is cut from the drawable
        and made into a floating selection which is then rotated by the
        specified amount. If auto_center is set to TRUE, the rotation is
        around the selection's center. Otherwise, the coordinate of the
        center point needs to be specified. The return value is the ID
        of the rotated floating selection.
        
        If there is no selection or the item is not a drawable, the entire item
        will be rotated around its center if auto_center is set to TRUE,
        otherwise the coordinate of the center point needs to be
        specified. The return value will be equal to the item ID
        supplied as input.
        
        This procedure is affected by the following context setters:
        'gimp-context-set-transform-resize'.
        
        Parameters:
        
        * item - The affected item.
        
        * rotate_type (default: <enum GIMP_ROTATE_DEGREES90 of type
          Gimp.RotationType>) - Type of rotation.
        
        * auto_center (default: False) - Whether to automatically rotate
          around the selection center.
        
        * center_x (default: 0.0) - The hor. coordinate of the center of
          rotation.
        
        * center_y (default: 0.0) - The vert. coordinate of the center of
          rotation.
        
        Returns:
        
        * item - The rotated item.
        """
        pass

    def gimp_item_transform_scale(self, item: Gimp.Item=None, x0: float=None, y0: float=None, x1: float=None, y1: float=None) -> Gimp.Item:
        """Scale the specified item.
        
        This procedure scales the specified item.
        
        The 2 coordinates specify the new locations of the top-left and
        bottom-roght corners of the original bounding box.
        
        If a selection exists and the item is a drawable, the portion of the
        drawable which lies under the selection is cut from the drawable
        and made into a floating selection which is then scaled as
        specified. The return value is the ID of the scaled floating
        selection. If there is no selection or the item is not a
        drawable, the entire item will be scaled according to the
        specified coordinates. The return value will be equal to the
        item ID supplied as input.
        
        This procedure is affected by the following context setters:
        'gimp-context-set-interpolation',
        'gimp-context-set-transform-direction',
        'gimp-context-set-transform-resize'.
        
        Parameters:
        
        * item - The affected item.
        
        * x0 (default: 0.0) - The new x coordinate of the upper-left corner of
          the scaled region.
        
        * y0 (default: 0.0) - The new y coordinate of the upper-left corner of
          the scaled region.
        
        * x1 (default: 0.0) - The new x coordinate of the lower-right corner
          of the scaled region.
        
        * y1 (default: 0.0) - The new y coordinate of the lower-right corner
          of the scaled region.
        
        Returns:
        
        * item - The scaled item.
        """
        pass

    def gimp_item_transform_shear(self, item: Gimp.Item=None, shear_type: Gimp.OrientationType=None, magnitude: float=None) -> Gimp.Item:
        """Shear the specified item about its center by the specified magnitude.
        
        This procedure shears the specified item.
        
        The shear type parameter indicates whether the shear will be applied
        horizontally or vertically. The magnitude can be either positive
        or negative and indicates the extent (in pixels) to shear by.
        
        If a selection exists and the item is a drawable, the portion of the
        drawable which lies under the selection is cut from the drawable
        and made into a floating selection which is then sheared as
        specified. The return value is the ID of the sheared floating
        selection.
        
        If there is no selection or the item is not a drawable, the entire item
        will be sheared according to the specified parameters. The
        return value will be equal to the item ID supplied as input.
        
        This procedure is affected by the following context setters:
        'gimp-context-set-interpolation',
        'gimp-context-set-transform-direction',
        'gimp-context-set-transform-resize'.
        
        Parameters:
        
        * item - The affected item.
        
        * shear_type (default: <enum GIMP_ORIENTATION_HORIZONTAL of type
          Gimp.OrientationType>) - Type of shear.
        
        * magnitude (default: 0.0) - The magnitude of the shear.
        
        Returns:
        
        * item - The sheared item.
        """
        pass

    def gimp_item_transform_translate(self, item: Gimp.Item=None, off_x: float=None, off_y: float=None) -> Gimp.Item:
        """Translate the item by the specified offsets.
        
        This procedure translates the item by the amounts specified in the off_x
        and off_y arguments. These can be negative, and are considered
        offsets from the current position. The offsets will be rounded
        to the nearest pixel unless the item is a path.
        
        Parameters:
        
        * item - The item.
        
        * off_x (default: 0.0) - Offset in x direction.
        
        * off_y (default: 0.0) - Offset in y direction.
        
        Returns:
        
        * item - The translated item.
        """
        pass

    def gimp_layer_add_alpha(self, layer: Gimp.Layer=None):
        """Add an alpha channel to the layer if it doesn't already have one.
        
        This procedure adds an additional component to the specified layer if it
        does not already possess an alpha channel. An alpha channel
        makes it possible to clear and erase to transparency, instead of
        the background color. This transforms layers of type RGB to
        RGBA, GRAY to GRAYA, and INDEXED to INDEXEDA.
        
        Parameters:
        
        * layer - The layer.
        """
        pass

    def gimp_layer_add_mask(self, layer: Gimp.Layer=None, mask: Gimp.LayerMask=None):
        """Add a layer mask to the specified layer.
        
        This procedure adds a layer mask to the specified layer. Layer masks
        serve as an additional alpha channel for a layer. This procedure
        will fail if a number of prerequisites aren't met. The layer
        cannot already have a layer mask. The specified mask must exist
        and have the same dimensions as the layer. The layer must have
        been created for use with the specified image and the mask must
        have been created with the procedure 'gimp-layer-create-mask'.
        
        Parameters:
        
        * layer - The layer to receive the mask.
        
        * mask - The mask to add to the layer.
        """
        pass

    def gimp_layer_copy(self, layer: Gimp.Layer=None, add_alpha: bool=None) -> Gimp.Layer:
        """Copy a layer.
        
        This procedure copies the specified layer and returns the copy. The
        newly copied layer is for use within the original layer's image.
        It should not be subsequently added to any other image. The
        copied layer can optionally have an added alpha channel. This is
        useful if the background layer in an image is being copied and
        added to the same image.
        
        Parameters:
        
        * layer - The layer to copy.
        
        * add_alpha (default: False) - Add an alpha channel to the copied
          layer.
        
        Returns:
        
        * layer_copy - The newly copied layer.
        """
        pass

    def gimp_layer_create_mask(self, layer: Gimp.Layer=None, mask_type: Gimp.AddMaskType=None) -> Gimp.LayerMask:
        """Create a layer mask for the specified layer.
        
        This procedure creates a layer mask for the specified layer. Layer masks
        serve as an additional alpha channel for a layer. Different
        types of masks are allowed for initialisation: - white mask
        (leaves the layer fully visible); - black mask (gives the layer
        complete transparency); - the layer's alpha channel (either a
        copy, or a transfer, which leaves the layer fully visible, but
        which may be more useful than a white mask); - the current
        selection; - a grayscale copy of the layer; - or a copy of the
        active channel.
        
        The layer mask still needs to be added to the layer. This can be done
        with a call to 'gimp-layer-add-mask'. 'gimp-layer-create-mask'
        will fail if there are no active channels on the image, when
        called with 'ADD-CHANNEL-MASK'. It will return a black mask when
        called with 'ADD-ALPHA-MASK' or 'ADD-ALPHA-TRANSFER-MASK' on a
        layer with no alpha channels, or with 'ADD-SELECTION-MASK' when
        there is no selection on the image.
        
        Parameters:
        
        * layer - The layer to which to add the mask.
        
        * mask_type (default: <enum GIMP_ADD_MASK_WHITE of type
          Gimp.AddMaskType>) - The type of mask.
        
        Returns:
        
        * mask - The newly created mask.
        """
        pass

    def gimp_layer_delete(self, item: Gimp.Item=None):
        """Delete a item.
        
        This procedure deletes the specified item. This must not be done if the
        image containing this item was already deleted or if the item
        was already removed from the image. The only case in which this
        procedure is useful is if you want to get rid of a item which
        has not yet been added to an image.
        
        Parameters:
        
        * item - The item to delete.
        """
        pass

    def gimp_layer_flatten(self, layer: Gimp.Layer=None):
        """Remove the alpha channel from the layer if it has one.
        
        This procedure removes the alpha channel from a layer, blending all
        (partially) transparent pixels in the layer against the
        background color. This transforms layers of type RGBA to RGB,
        GRAYA to GRAY, and INDEXEDA to INDEXED.
        
        Parameters:
        
        * layer - The layer.
        """
        pass

    def gimp_layer_from_mask(self, mask: Gimp.LayerMask=None) -> Gimp.Layer:
        """Get the specified mask's layer.
        
        This procedure returns the specified mask's layer , or -1 if none
        exists.
        
        Parameters:
        
        * mask - Mask for which to return the layer.
        
        Returns:
        
        * layer - The mask's layer.
        """
        pass

    def gimp_layer_get_apply_mask(self, layer: Gimp.Layer=None) -> bool:
        """Get the apply mask setting of the specified layer.
        
        This procedure returns the specified layer's apply mask setting. If the
        value is TRUE, then the layer mask for this layer is currently
        being composited with the layer's alpha channel.
        
        Parameters:
        
        * layer - The layer.
        
        Returns:
        
        * apply_mask (default: False) - The layer's apply mask setting.
        """
        pass

    def gimp_layer_get_blend_space(self, layer: Gimp.Layer=None) -> Gimp.LayerColorSpace:
        """Get the blend space of the specified layer.
        
        This procedure returns the specified layer's blend space.
        
        Parameters:
        
        * layer - The layer.
        
        Returns:
        
        * blend_space (default: <enum GIMP_LAYER_COLOR_SPACE_AUTO of type
          Gimp.LayerColorSpace>) - The layer blend space.
        """
        pass

    def gimp_layer_get_composite_mode(self, layer: Gimp.Layer=None) -> Gimp.LayerCompositeMode:
        """Get the composite mode of the specified layer.
        
        This procedure returns the specified layer's composite mode.
        
        Parameters:
        
        * layer - The layer.
        
        Returns:
        
        * composite_mode (default: <enum GIMP_LAYER_COMPOSITE_AUTO of type
          Gimp.LayerCompositeMode>) - The layer composite mode.
        """
        pass

    def gimp_layer_get_composite_space(self, layer: Gimp.Layer=None) -> Gimp.LayerColorSpace:
        """Get the composite space of the specified layer.
        
        This procedure returns the specified layer's composite space.
        
        Parameters:
        
        * layer - The layer.
        
        Returns:
        
        * composite_space (default: <enum GIMP_LAYER_COLOR_SPACE_AUTO of type
          Gimp.LayerColorSpace>) - The layer composite space.
        """
        pass

    def gimp_layer_get_edit_mask(self, layer: Gimp.Layer=None) -> bool:
        """Get the edit mask setting of the specified layer.
        
        This procedure returns the specified layer's edit mask setting. If the
        value is TRUE, then the layer mask for this layer is currently
        active, and not the layer.
        
        Parameters:
        
        * layer - The layer.
        
        Returns:
        
        * edit_mask (default: False) - The layer's edit mask setting.
        """
        pass

    def gimp_layer_get_lock_alpha(self, layer: Gimp.Layer=None) -> bool:
        """Get the lock alpha channel setting of the specified layer.
        
        This procedure returns the specified layer's lock alpha channel setting.
        
        Parameters:
        
        * layer - The layer.
        
        Returns:
        
        * lock_alpha (default: False) - The layer's lock alpha channel
          setting.
        """
        pass

    def gimp_layer_get_mask(self, layer: Gimp.Layer=None) -> Gimp.LayerMask:
        """Get the specified layer's mask if it exists.
        
        This procedure returns the specified layer's mask, or -1 if none exists.
        
        Parameters:
        
        * layer - The layer.
        
        Returns:
        
        * mask - The layer mask.
        """
        pass

    def gimp_layer_get_mode(self, layer: Gimp.Layer=None) -> Gimp.LayerMode:
        """Get the combination mode of the specified layer.
        
        This procedure returns the specified layer's combination mode.
        
        Parameters:
        
        * layer - The layer.
        
        Returns:
        
        * mode (default: <enum GIMP_LAYER_MODE_NORMAL of type Gimp.LayerMode>)
          - The layer combination mode.
        """
        pass

    def gimp_layer_get_name(self, item: Gimp.Item=None) -> str:
        """Get the name of the specified item.
        
        This procedure returns the specified item's name.
        
        Parameters:
        
        * item - The item.
        
        Returns:
        
        * name - The item name.
        """
        pass

    def gimp_layer_get_opacity(self, layer: Gimp.Layer=None) -> float:
        """Get the opacity of the specified layer.
        
        This procedure returns the specified layer's opacity.
        
        Parameters:
        
        * layer - The layer.
        
        Returns:
        
        * opacity (default: 0.0) - The layer opacity.
        """
        pass

    def gimp_layer_get_preserve_trans(self, layer: Gimp.Layer=None) -> bool:
        """Get the lock alpha channel setting of the specified layer.
        
        This procedure returns the specified layer's lock alpha channel setting.
        
        Parameters:
        
        * layer - The layer.
        
        Returns:
        
        * lock_alpha (default: False) - The layer's lock alpha channel
          setting.
        """
        pass

    def gimp_layer_get_show_mask(self, layer: Gimp.Layer=None) -> bool:
        """Get the show mask setting of the specified layer.
        
        This procedure returns the specified layer's show mask setting. This
        controls whether the layer or its mask is visible. TRUE
        indicates that the mask should be visible. If the layer has no
        mask, then this function returns an error.
        
        Parameters:
        
        * layer - The layer.
        
        Returns:
        
        * show_mask (default: False) - The layer's show mask setting.
        """
        pass

    def gimp_layer_get_tattoo(self, item: Gimp.Item=None) -> int:
        """Get the tattoo of the specified item.
        
        This procedure returns the specified item's tattoo. A tattoo is a unique
        and permanent identifier attached to a item that can be used to
        uniquely identify a item within an image even between sessions.
        
        Parameters:
        
        * item - The item.
        
        Returns:
        
        * tattoo (default: 1) - The item tattoo.
        """
        pass

    def gimp_layer_get_visible(self, item: Gimp.Item=None) -> bool:
        """Get the visibility of the specified item.
        
        This procedure returns the specified item's visibility.
        
        Parameters:
        
        * item - The item.
        
        Returns:
        
        * visible (default: False) - The item visibility.
        """
        pass

    def gimp_layer_group_new(self, image: Gimp.Image=None) -> Gimp.Layer:
        """Create a new layer group.
        
        This procedure creates a new layer group. Attributes such as layer mode
        and opacity should be set with explicit procedure calls. Add the
        new layer group (which is a kind of layer) with the
        'gimp-image-insert-layer' command. Other procedures useful with
        layer groups: 'gimp-image-reorder-item', 'gimp-item-get-parent',
        'gimp-item-get-children', 'gimp-item-is-group'.
        
        Parameters:
        
        * image - The image to which to add the layer group.
        
        Returns:
        
        * layer_group - The newly created layer group.
        """
        pass

    def gimp_layer_is_floating_sel(self, layer: Gimp.Layer=None) -> bool:
        """Is the specified layer a floating selection?.
        
        This procedure returns whether the layer is a floating selection.
        Floating selections are special cases of layers which are
        attached to a specific drawable.
        
        Parameters:
        
        * layer - The layer.
        
        Returns:
        
        * is_floating_sel (default: False) - TRUE if the layer is a floating
          selection.
        """
        pass

    def gimp_layer_mask(self, layer: Gimp.Layer=None) -> Gimp.LayerMask:
        """Get the specified layer's mask if it exists.
        
        This procedure returns the specified layer's mask, or -1 if none exists.
        
        Parameters:
        
        * layer - The layer.
        
        Returns:
        
        * mask - The layer mask.
        """
        pass

    def gimp_layer_new(self, image: Gimp.Image=None, width: int=None, height: int=None, type: Gimp.ImageType=None, name: str=None, opacity: float=None, mode: Gimp.LayerMode=None) -> Gimp.Layer:
        """Create a new layer.
        
        This procedure creates a new layer with the specified width, height, and
        type. Name, opacity, and mode are also supplied parameters. The
        new layer still needs to be added to the image, as this is not
        automatic. Add the new layer with the 'gimp-image-insert-layer'
        command. Other attributes such as layer mask modes, and offsets
        should be set with explicit procedure calls.
        
        Parameters:
        
        * image - The image to which to add the layer.
        
        * width (default: 1) - The layer width.
        
        * height (default: 1) - The layer height.
        
        * type (default: <enum GIMP_RGB_IMAGE of type Gimp.ImageType>) - The
          layer type.
        
        * name - The layer name.
        
        * opacity (default: 0.0) - The layer opacity.
        
        * mode (default: <enum GIMP_LAYER_MODE_NORMAL of type Gimp.LayerMode>)
          - The layer combination mode.
        
        Returns:
        
        * layer - The newly created layer.
        """
        pass

    def gimp_layer_new_from_drawable(self, drawable: Gimp.Drawable=None, dest_image: Gimp.Image=None) -> Gimp.Layer:
        """Create a new layer by copying an existing drawable.
        
        This procedure creates a new layer as a copy of the specified drawable.
        The new layer still needs to be added to the image, as this is
        not automatic. Add the new layer with the
        'gimp-image-insert-layer' command. Other attributes such as
        layer mask modes, and offsets should be set with explicit
        procedure calls.
        
        Parameters:
        
        * drawable - The source drawable from where the new layer is copied.
        
        * dest_image - The destination image to which to add the layer.
        
        Returns:
        
        * layer_copy - The newly copied layer.
        """
        pass

    def gimp_layer_new_from_visible(self, image: Gimp.Image=None, dest_image: Gimp.Image=None, name: str=None) -> Gimp.Layer:
        """Create a new layer from what is visible in an image.
        
        This procedure creates a new layer from what is visible in the given
        image. The new layer still needs to be added to the destination
        image, as this is not automatic. Add the new layer with the
        'gimp-image-insert-layer' command. Other attributes such as
        layer mask modes, and offsets should be set with explicit
        procedure calls.
        
        Parameters:
        
        * image - The source image from where the content is copied.
        
        * dest_image - The destination image to which to add the layer.
        
        * name - The layer name.
        
        Returns:
        
        * layer - The newly created layer.
        """
        pass

    def gimp_layer_remove_mask(self, layer: Gimp.Layer=None, mode: Gimp.MaskApplyMode=None):
        """Remove the specified layer mask from the layer.
        
        This procedure removes the specified layer mask from the layer. If the
        mask doesn't exist, an error is returned.
        
        Parameters:
        
        * layer - The layer from which to remove mask.
        
        * mode (default: <enum GIMP_MASK_APPLY of type Gimp.MaskApplyMode>) -
          Removal mode.
        """
        pass

    def gimp_layer_resize(self, layer: Gimp.Layer=None, new_width: int=None, new_height: int=None, offx: int=None, offy: int=None):
        """Resize the layer to the specified extents.
        
        This procedure resizes the layer so that its new width and height are
        equal to the supplied parameters. Offsets are also provided
        which describe the position of the previous layer's content.
        This operation only works if the layer has been added to an
        image.
        
        Parameters:
        
        * layer - The layer.
        
        * new_width (default: 1) - New layer width.
        
        * new_height (default: 1) - New layer height.
        
        * offx (default: 0) - x offset between upper left corner of old and
          new layers: (old - new).
        
        * offy (default: 0) - y offset between upper left corner of old and
          new layers: (old - new).
        """
        pass

    def gimp_layer_resize_to_image_size(self, layer: Gimp.Layer=None):
        """Resize a layer to the image size.
        
        This procedure resizes the layer so that it's new width and height are
        equal to the width and height of its image container.
        
        Parameters:
        
        * layer - The layer to resize.
        """
        pass

    def gimp_layer_scale(self, layer: Gimp.Layer=None, new_width: int=None, new_height: int=None, local_origin: bool=None):
        """Scale the layer using the default interpolation method.
        
        This procedure scales the layer so that its new width and height are
        equal to the supplied parameters. The 'local-origin' parameter
        specifies whether to scale from the center of the layer, or from
        the image origin. This operation only works if the layer has
        been added to an image. The interpolation method used can be set
        with 'gimp-context-set-interpolation'.
        
        Parameters:
        
        * layer - The layer.
        
        * new_width (default: 1) - New layer width.
        
        * new_height (default: 1) - New layer height.
        
        * local_origin (default: False) - Use a local origin (as opposed to
          the image origin).
        """
        pass

    def gimp_layer_set_apply_mask(self, layer: Gimp.Layer=None, apply_mask: bool=None):
        """Set the apply mask setting of the specified layer.
        
        This procedure sets the specified layer's apply mask setting. This
        controls whether the layer's mask is currently affecting the
        alpha channel. If there is no layer mask, this function will
        return an error.
        
        Parameters:
        
        * layer - The layer.
        
        * apply_mask (default: False) - The new layer's apply mask setting.
        """
        pass

    def gimp_layer_set_blend_space(self, layer: Gimp.Layer=None, blend_space: Gimp.LayerColorSpace=None):
        """Set the blend space of the specified layer.
        
        This procedure sets the specified layer's blend space.
        
        Parameters:
        
        * layer - The layer.
        
        * blend_space (default: <enum GIMP_LAYER_COLOR_SPACE_AUTO of type
          Gimp.LayerColorSpace>) - The new layer blend space.
        """
        pass

    def gimp_layer_set_composite_mode(self, layer: Gimp.Layer=None, composite_mode: Gimp.LayerCompositeMode=None):
        """Set the composite mode of the specified layer.
        
        This procedure sets the specified layer's composite mode.
        
        Parameters:
        
        * layer - The layer.
        
        * composite_mode (default: <enum GIMP_LAYER_COMPOSITE_AUTO of type
          Gimp.LayerCompositeMode>) - The new layer composite mode.
        """
        pass

    def gimp_layer_set_composite_space(self, layer: Gimp.Layer=None, composite_space: Gimp.LayerColorSpace=None):
        """Set the composite space of the specified layer.
        
        This procedure sets the specified layer's composite space.
        
        Parameters:
        
        * layer - The layer.
        
        * composite_space (default: <enum GIMP_LAYER_COLOR_SPACE_AUTO of type
          Gimp.LayerColorSpace>) - The new layer composite space.
        """
        pass

    def gimp_layer_set_edit_mask(self, layer: Gimp.Layer=None, edit_mask: bool=None):
        """Set the edit mask setting of the specified layer.
        
        This procedure sets the specified layer's edit mask setting. This
        controls whether the layer or it's mask is currently active for
        editing. If the specified layer has no layer mask, then this
        procedure will return an error.
        
        Parameters:
        
        * layer - The layer.
        
        * edit_mask (default: False) - The new layer's edit mask setting.
        """
        pass

    def gimp_layer_set_lock_alpha(self, layer: Gimp.Layer=None, lock_alpha: bool=None):
        """Set the lock alpha channel setting of the specified layer.
        
        This procedure sets the specified layer's lock alpha channel setting.
        
        Parameters:
        
        * layer - The layer.
        
        * lock_alpha (default: False) - The new layer's lock alpha channel
          setting.
        """
        pass

    def gimp_layer_set_mode(self, layer: Gimp.Layer=None, mode: Gimp.LayerMode=None):
        """Set the combination mode of the specified layer.
        
        This procedure sets the specified layer's combination mode.
        
        Parameters:
        
        * layer - The layer.
        
        * mode (default: <enum GIMP_LAYER_MODE_NORMAL of type Gimp.LayerMode>)
          - The new layer combination mode.
        """
        pass

    def gimp_layer_set_name(self, item: Gimp.Item=None, name: str=None):
        """Set the name of the specified item.
        
        This procedure sets the specified item's name.
        
        Parameters:
        
        * item - The item.
        
        * name - The new item name.
        """
        pass

    def gimp_layer_set_offsets(self, layer: Gimp.Layer=None, offx: int=None, offy: int=None):
        """Set the layer offsets.
        
        This procedure sets the offsets for the specified layer. The offsets are
        relative to the image origin and can be any values. This
        operation is valid only on layers which have been added to an
        image.
        
        Parameters:
        
        * layer - The layer.
        
        * offx (default: 0) - Offset in x direction.
        
        * offy (default: 0) - Offset in y direction.
        """
        pass

    def gimp_layer_set_opacity(self, layer: Gimp.Layer=None, opacity: float=None):
        """Set the opacity of the specified layer.
        
        This procedure sets the specified layer's opacity.
        
        Parameters:
        
        * layer - The layer.
        
        * opacity (default: 0.0) - The new layer opacity.
        """
        pass

    def gimp_layer_set_preserve_trans(self, layer: Gimp.Layer=None, lock_alpha: bool=None):
        """Set the lock alpha channel setting of the specified layer.
        
        This procedure sets the specified layer's lock alpha channel setting.
        
        Parameters:
        
        * layer - The layer.
        
        * lock_alpha (default: False) - The new layer's lock alpha channel
          setting.
        """
        pass

    def gimp_layer_set_show_mask(self, layer: Gimp.Layer=None, show_mask: bool=None):
        """Set the show mask setting of the specified layer.
        
        This procedure sets the specified layer's show mask setting. This
        controls whether the layer or its mask is visible. TRUE
        indicates that the mask should be visible. If there is no layer
        mask, this function will return an error.
        
        Parameters:
        
        * layer - The layer.
        
        * show_mask (default: False) - The new layer's show mask setting.
        """
        pass

    def gimp_layer_set_tattoo(self, item: Gimp.Item=None, tattoo: int=None):
        """Set the tattoo of the specified item.
        
        This procedure sets the specified item's tattoo. A tattoo is a unique
        and permanent identifier attached to a item that can be used to
        uniquely identify a item within an image even between sessions.
        
        Parameters:
        
        * item - The item.
        
        * tattoo (default: 1) - The new item tattoo.
        """
        pass

    def gimp_layer_set_visible(self, item: Gimp.Item=None, visible: bool=None):
        """Set the visibility of the specified item.
        
        This procedure sets the specified item's visibility.
        
        Parameters:
        
        * item - The item.
        
        * visible (default: False) - The new item visibility.
        """
        pass

    def gimp_message(self, message: str=None):
        """Displays a dialog box with a message.
        
        Displays a dialog box with a message. Useful for status or error
        reporting. The message must be in UTF-8 encoding.
        
        Parameters:
        
        * message - Message to display in the dialog.
        """
        pass

    def gimp_message_get_handler(self) -> Gimp.MessageHandlerType:
        """Returns the current state of where warning messages are displayed.
        
        This procedure returns the way g_message warnings are displayed. They
        can be shown in a dialog box or printed on the console where
        gimp was started.
        
        Returns:
        
        * handler (default: <enum GIMP_MESSAGE_BOX of type
          Gimp.MessageHandlerType>) - The current handler type.
        """
        pass

    def gimp_message_set_handler(self, handler: Gimp.MessageHandlerType=None):
        """Controls where warning messages are displayed.
        
        This procedure controls how g_message warnings are displayed. They can
        be shown in a dialog box or printed on the console where gimp
        was started.
        
        Parameters:
        
        * handler (default: <enum GIMP_MESSAGE_BOX of type
          Gimp.MessageHandlerType>) - The new handler type.
        """
        pass

    def gimp_online_bugs_features(self, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Bookmark to the bug tracker of GIMP.
        
        Menu label: _Bug Reports and Feature Requests
        Menu path: <Image>/Help/GIMP Online
        """
        pass

    def gimp_online_developer_web_site(self, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Bookmark to the GIMP web site.
        
        Menu label: _Developer Web Site
        Menu path: <Image>/Help/GIMP Online
        """
        pass

    def gimp_online_docs_web_site(self, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Bookmark to the GIMP web site.
        
        Menu label: _User Manual Web Site
        Menu path: <Image>/Help/GIMP Online
        """
        pass

    def gimp_online_main_web_site(self, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Bookmark to the GIMP web site.
        
        Menu label: _Main Web Site
        Menu path: <Image>/Help/GIMP Online
        """
        pass

    def gimp_online_roadmap(self, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Bookmark to the roadmaps of GIMP.
        
        Menu label: _Roadmaps
        Menu path: <Image>/Help/GIMP Online
        """
        pass

    def gimp_paintbrush(self, drawable: Gimp.Drawable=None, fade_out: float=None, num_strokes: int=None, strokes: Gimp.FloatArray=None, method: Gimp.PaintApplicationMode=None, gradient_length: float=None):
        """Paint in the current brush with optional fade out parameter and pull
        colors from a gradient.
        
        This tool is the standard paintbrush. It draws linearly interpolated
        lines through the specified stroke coordinates. It operates on
        the specified drawable in the foreground color with the active
        brush. The 'fade-out' parameter is measured in pixels and allows
        the brush stroke to linearly fall off. The pressure is set to
        the maximum at the beginning of the stroke. As the distance of
        the stroke nears the fade-out value, the pressure will approach
        zero. The gradient-length is the distance to spread the gradient
        over. It is measured in pixels. If the gradient-length is 0, no
        gradient is used.
        
        Parameters:
        
        * drawable - The affected drawable.
        
        * fade_out (default: 0.0) - Fade out parameter.
        
        * num_strokes (default: 2) - Number of stroke control points (count
          each coordinate as 2 points).
        
        * strokes - Array of stroke coordinates: { s1.x, s1.y, s2.x, s2.y,
          ..., sn.x, sn.y }.
        
        * method (default: <enum GIMP_PAINT_CONSTANT of type
          Gimp.PaintApplicationMode>) - The paint method to use.
        
        * gradient_length (default: 0.0) - Length of gradient to draw.
        """
        pass

    def gimp_paintbrush_default(self, drawable: Gimp.Drawable=None, num_strokes: int=None, strokes: Gimp.FloatArray=None):
        """Paint in the current brush. The fade out parameter and pull colors
        from a gradient parameter are set from the paintbrush options
        dialog. If this dialog has not been activated then the dialog
        defaults will be used.
        
        This tool is similar to the standard paintbrush. It draws linearly
        interpolated lines through the specified stroke coordinates. It
        operates on the specified drawable in the foreground color with
        the active brush. The 'fade-out' parameter is measured in pixels
        and allows the brush stroke to linearly fall off (value obtained
        from the option dialog). The pressure is set to the maximum at
        the beginning of the stroke. As the distance of the stroke nears
        the fade-out value, the pressure will approach zero. The
        gradient-length (value obtained from the option dialog) is the
        distance to spread the gradient over. It is measured in pixels.
        If the gradient-length is 0, no gradient is used.
        
        Parameters:
        
        * drawable - The affected drawable.
        
        * num_strokes (default: 2) - Number of stroke control points (count
          each coordinate as 2 points).
        
        * strokes - Array of stroke coordinates: { s1.x, s1.y, s2.x, s2.y,
          ..., sn.x, sn.y }.
        """
        pass

    def gimp_palette_add_entry(self, palette: Gimp.Palette=None, entry_name: str=None, color: Gegl.Color=None) -> int:
        """Appends an entry to the palette.
        
        Appends an entry to the palette. Neither color nor name must be unique
        within the palette. When name is the empty string, this sets the
        entry name to "Untitled". Returns the index of the entry.
        Returns an error when palette is not editable.
        
        Parameters:
        
        * palette - The palette.
        
        * entry_name - A name for the entry.
        
        * color - The color for the added entry.
        
        Returns:
        
        * entry_num (default: 0) - The index of the added entry.
        """
        pass

    def gimp_palette_delete_entry(self, palette: Gimp.Palette=None, entry_num: int=None):
        """Deletes an entry from the palette.
        
        This function will fail and return %FALSE if the index is out or range
        or if the palette is not editable. Additionally if the palette
        belongs to an indexed image, it will only be possible to delete
        palette colors not in use in the image.
        
        Parameters:
        
        * palette - The palette.
        
        * entry_num (default: 0) - The index of the entry to delete.
        """
        pass

    def gimp_palette_entry_get_color(self, palette: Gimp.Palette=None, entry_num: int=None) -> Gegl.Color:
        """Gets the color of an entry in the palette.
        
        Returns the color of the entry at the given zero-based index into the
        palette. Returns %NULL when the index is out of range.
        
        Parameters:
        
        * palette - The palette.
        
        * entry_num (default: 0) - The index of the entry to get the color of.
        
        Returns:
        
        * color - The color at the index.
        """
        pass

    def gimp_palette_entry_get_name(self, palette: Gimp.Palette=None, entry_num: int=None) -> str:
        """Gets the name of an entry in the palette.
        
        Gets the name of the entry at the zero-based index into the palette.
        Returns an error when the index is out of range.
        
        Parameters:
        
        * palette - The palette.
        
        * entry_num (default: 0) - The entry to get.
        
        Returns:
        
        * entry_name - The name of the entry.
        """
        pass

    def gimp_palette_entry_set_color(self, palette: Gimp.Palette=None, entry_num: int=None, color: Gegl.Color=None):
        """Sets the color of an entry in the palette.
        
        Sets the color of the entry at the zero-based index into the palette.
        Returns an error when the index is out of range. Returns an
        error when the palette is not editable.
        
        Parameters:
        
        * palette - The palette.
        
        * entry_num (default: 0) - The entry to get.
        
        * color - The new color.
        """
        pass

    def gimp_palette_entry_set_name(self, palette: Gimp.Palette=None, entry_num: int=None, entry_name: str=None):
        """Sets the name of an entry in the palette.
        
        Sets the name of the entry at the zero-based index into the palette.
        Returns an error if the index is out or range. Returns an error
        if the palette is not editable.
        
        Parameters:
        
        * palette - The palette.
        
        * entry_num (default: 0) - The entry to get.
        
        * entry_name - The new name.
        """
        pass

    def gimp_palette_export_css(self, dirname: Gio.File=None, string: str=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Export the active palette as a CSS stylesheet with the color entry
        name as their class name, and the color itself as the color
        attribute.
        
        Menu label: _CSS stylesheet...
        Menu path: <Palettes>/Export as
        
        Parameters:
        
        * dirname - Folder for the output file.
        
        * string (default: palette.css) - The name of the file to create (if a
          file with this name already exist, it will be replaced).
        """
        pass

    def gimp_palette_export_java(self, dirname: Gio.File=None, string: str=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Export the active palette as a
        java.util.Hashtable&lt;String,Color&gt;.
        
        Menu label: J_ava map...
        Menu path: <Palettes>/Export as
        
        Parameters:
        
        * dirname - Folder for the output file.
        
        * string (default: palette.java) - The name of the file to create (if
          a file with this name already exist, it will be replaced).
        """
        pass

    def gimp_palette_export_php(self, dirname: Gio.File=None, string: str=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Export the active palette as a PHP dictionary (name => color).
        
        Menu label: P_HP dictionary...
        Menu path: <Palettes>/Export as
        
        Parameters:
        
        * dirname - Folder for the output file.
        
        * string (default: palette.php) - The name of the file to create (if a
          file with this name already exist, it will be replaced).
        """
        pass

    def gimp_palette_export_python(self, dirname: Gio.File=None, string: str=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Export the active palette as a Python dictionary (name: color).
        
        Menu label: _Python dictionary...
        Menu path: <Palettes>/Export as
        
        Parameters:
        
        * dirname - Folder for the output file.
        
        * string (default: palette.py) - The name of the file to create (if a
          file with this name already exist, it will be replaced).
        """
        pass

    def gimp_palette_export_text(self, dirname: Gio.File=None, string: str=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Write all the colors in a palette to a text file, one hexadecimal
        value per line (no names).
        
        Menu label: _Text file...
        Menu path: <Palettes>/Export as
        
        Parameters:
        
        * dirname - Folder for the output file.
        
        * string (default: palette.txt) - The name of the file to create (if a
          file with this name already exist, it will be replaced).
        """
        pass

    def gimp_palette_get_background(self) -> Gegl.Color:
        """Get the current GIMP background color.
        
        Returns the current GIMP background color. The background color is used
        in a variety of tools such as blending, erasing (with non-alpha
        images), and image filling.
        
        Returns:
        
        * background - The background color.
        """
        pass

    def gimp_palette_get_by_name(self, name: str=None) -> Gimp.Palette:
        """Returns the palette with the given name.
        
        Returns the palette with the given name.
        
        Parameters:
        
        * name - The name of the palette.
        
        Returns:
        
        * palette - The palette.
        """
        pass

    def gimp_palette_get_color_count(self, palette: Gimp.Palette=None) -> int:
        """Get the count of colors in the palette.
        
        Returns the number of colors in the palette.
        
        Parameters:
        
        * palette - The palette.
        
        Returns:
        
        * num_colors (default: 0) - The number of colors in the palette.
        """
        pass

    def gimp_palette_get_colors(self, palette: Gimp.Palette=None):
        """Gets colors in the palette.
        
        Returns an array of colors in the palette. Free the returned array with
        'gimp-color-array-free'.
        
        Parameters:
        
        * palette - The palette.
        """
        pass

    def gimp_palette_get_columns(self, palette: Gimp.Palette=None) -> int:
        """Gets the number of columns used to display the palette.
        
        Gets the preferred number of columns to display the palette.
        
        Parameters:
        
        * palette - The palette.
        
        Returns:
        
        * num_columns (default: 0) - The number of columns used to display
          this palette.
        """
        pass

    def gimp_palette_get_foreground(self) -> Gegl.Color:
        """Get the current GIMP foreground color.
        
        Returns the current GIMP foreground color. The foreground color is used
        in a variety of tools such as paint tools, blending, and bucket
        fill.
        
        Returns:
        
        * foreground - The foreground color.
        """
        pass

    def gimp_palette_new(self, name: str=None) -> Gimp.Palette:
        """Creates a new palette.
        
        Creates a new palette. The new palette has no color entries. You must
        add color entries for a user to choose. The actual name might be
        different than the requested name, when the requested name is
        already in use.
        
        Parameters:
        
        * name - The requested name of the new palette.
        
        Returns:
        
        * palette - The palette.
        """
        pass

    def gimp_palette_refresh(self):
        """Refreshes current palettes. This function always succeeds.
        
        This procedure retrieves all palettes currently in the user's palette
        path and updates the palette dialogs accordingly.
        """
        pass

    def gimp_palette_set_background(self, background: Gegl.Color=None):
        """Set the current GIMP background color.
        
        Sets the current GIMP background color. After this is set, operations
        which use background such as blending, filling images, clearing,
        and erasing (in non-alpha images) will use the new value.
        
        Parameters:
        
        * background - The background color.
        """
        pass

    def gimp_palette_set_columns(self, palette: Gimp.Palette=None, columns: int=None):
        """Sets the number of columns used to display the palette.
        
        Set the number of colors shown per row when the palette is displayed.
        Returns an error when the palette is not editable. The maximum
        allowed value is 64.
        
        Parameters:
        
        * palette - The palette.
        
        * columns (default: 0) - The new number of columns.
        """
        pass

    def gimp_palette_set_default_colors(self):
        """Set the current GIMP foreground and background colors to black and
        white.
        
        Sets the current GIMP foreground and background colors to their initial
        default values, black and white.
        """
        pass

    def gimp_palette_set_foreground(self, foreground: Gegl.Color=None):
        """Set the current GIMP foreground color.
        
        Sets the current GIMP foreground color. After this is set, operations
        which use foreground such as paint tools, blending, and bucket
        fill will use the new value.
        
        Parameters:
        
        * foreground - The foreground color.
        """
        pass

    def gimp_palette_swap_colors(self):
        """Swap the current GIMP foreground and background colors.
        
        Swaps the current GIMP foreground and background colors, so that the new
        foreground color becomes the old background color and vice
        versa.
        """
        pass

    def gimp_palettes_close_popup(self, palette_callback: str=None):
        """Close the palette selection dialog.
        
        Closes an open palette selection dialog.
        
        Parameters:
        
        * palette_callback - The name of the callback registered for this
          pop-up.
        """
        pass

    def gimp_palettes_get_list(self, filter: str=None) -> List[str]:
        """Retrieves a list of all of the available palettes.
        
        This procedure returns a complete listing of available palettes. Each
        name returned can be used as input to the command
        'gimp-context-set-palette'.
        
        Parameters:
        
        * filter - An optional regular expression used to filter the list.
        
        Returns:
        
        * palette_list - The list of palette names.
        """
        pass

    def gimp_palettes_popup(self, palette_callback: str=None, popup_title: str=None, initial_palette: Gimp.Palette=None, parent_window: GLib.Bytes=None):
        """Invokes the Gimp palette selection dialog.
        
        Opens a dialog letting a user choose a palette.
        
        Parameters:
        
        * palette_callback - The callback PDB proc to call when user chooses a
          palette.
        
        * popup_title - Title of the palette selection dialog.
        
        * initial_palette - The palette to set as the initial choice.
        
        * parent_window - An optional parent window handle for the popup to be
          set transient to.
        """
        pass

    def gimp_palettes_refresh(self):
        """Refreshes current palettes. This function always succeeds.
        
        This procedure retrieves all palettes currently in the user's palette
        path and updates the palette dialogs accordingly.
        """
        pass

    def gimp_palettes_set_palette(self, palette: Gimp.Palette=None):
        """Set the active palette.
        
        Sets the active palette in the current context. The palette will be used
        in subsequent paint operations. Returns an error when the
        palette data was uninstalled since the palette object was
        created.
        
        Parameters:
        
        * palette - The palette.
        """
        pass

    def gimp_palettes_set_popup(self, palette_callback: str=None, palette: Gimp.Palette=None):
        """Sets the current palette in a palette selection dialog.
        
        Sets the current palette in a palette selection dialog.
        
        Parameters:
        
        * palette_callback - The name of the callback registered for this
          pop-up.
        
        * palette - The palette to set as selected.
        """
        pass

    def gimp_parasite_attach(self, parasite: Gimp.Parasite=None):
        """Add a global parasite.
        
        This procedure attaches a global parasite. It has no return values.
        
        Parameters:
        
        * parasite - The parasite to attach.
        """
        pass

    def gimp_parasite_detach(self, name: str=None):
        """Removes a global parasite.
        
        This procedure detaches a global parasite from. It has no return values.
        
        Parameters:
        
        * name - The name of the parasite to detach.
        """
        pass

    def gimp_parasite_find(self, name: str=None) -> Gimp.Parasite:
        """Look up a global parasite.
        
        Finds and returns the global parasite that was previously attached.
        
        Parameters:
        
        * name - The name of the parasite to find.
        
        Returns:
        
        * parasite - The found parasite.
        """
        pass

    def gimp_parasite_list(self) -> List[str]:
        """List all parasites.
        
        Returns a list of all currently attached global parasites.
        
        Returns:
        
        * parasites - The names of currently attached parasites.
        """
        pass

    def gimp_pattern_get_by_name(self, name: str=None) -> Gimp.Pattern:
        """Returns the pattern with the given name.
        
        Returns the pattern with the given name.
        
        Parameters:
        
        * name - The name of the pattern.
        
        Returns:
        
        * pattern - The pattern.
        """
        pass

    def gimp_pattern_get_info(self, pattern: Gimp.Pattern=None) -> Tuple[int, int, int]:
        """Gets information about the pattern.
        
        Gets information about the pattern: the pattern extents (width and
        height) and bytes per pixel.
        
        Parameters:
        
        * pattern - The pattern.
        
        Returns:
        
        * width (default: 0) - The pattern width.
        
        * height (default: 0) - The pattern height.
        
        * bpp (default: 0) - The pattern bpp.
        """
        pass

    def gimp_pattern_get_pixels(self, pattern: Gimp.Pattern=None) -> Tuple[int, int, int, GLib.Bytes]:
        """Gets information about the pattern (including pixels).
        
        Gets information about the pattern: the pattern extents (width and
        height), its bpp, and its pixel data.
        
        Parameters:
        
        * pattern - The pattern.
        
        Returns:
        
        * width (default: 0) - The pattern width.
        
        * height (default: 0) - The pattern height.
        
        * bpp (default: 0) - The pattern bpp.
        
        * color_bytes - The pattern data.
        """
        pass

    def gimp_patterns_close_popup(self, pattern_callback: str=None):
        """Close the pattern selection dialog.
        
        Closes an open pattern selection dialog.
        
        Parameters:
        
        * pattern_callback - The name of the callback registered for this
          pop-up.
        """
        pass

    def gimp_patterns_get_list(self, filter: str=None) -> List[str]:
        """Retrieve a complete listing of the available patterns.
        
        This procedure returns a complete listing of available GIMP patterns.
        Each name returned can be used as input to the
        'gimp-context-set-pattern'.
        
        Parameters:
        
        * filter - An optional regular expression used to filter the list.
        
        Returns:
        
        * pattern_list - The list of pattern names.
        """
        pass

    def gimp_patterns_list(self, filter: str=None) -> List[str]:
        """Retrieve a complete listing of the available patterns.
        
        This procedure returns a complete listing of available GIMP patterns.
        Each name returned can be used as input to the
        'gimp-context-set-pattern'.
        
        Parameters:
        
        * filter - An optional regular expression used to filter the list.
        
        Returns:
        
        * pattern_list - The list of pattern names.
        """
        pass

    def gimp_patterns_popup(self, pattern_callback: str=None, popup_title: str=None, initial_pattern: Gimp.Pattern=None, parent_window: GLib.Bytes=None):
        """Invokes the Gimp pattern selection.
        
        Opens the pattern selection dialog.
        
        Parameters:
        
        * pattern_callback - The callback PDB proc to call when the user
          chooses a pattern.
        
        * popup_title - Title of the pattern selection dialog.
        
        * initial_pattern - The pattern to set as the initial choice.
        
        * parent_window - An optional parent window handle for the popup to be
          set transient to.
        """
        pass

    def gimp_patterns_refresh(self):
        """Refresh current patterns. This function always succeeds.
        
        This procedure retrieves all patterns currently in the user's pattern
        path and updates all pattern dialogs accordingly.
        """
        pass

    def gimp_patterns_set_pattern(self, pattern: Gimp.Pattern=None):
        """Set the active pattern.
        
        Sets the active pattern in the current context. The pattern will be used
        in subsequent fill operations using a pattern. Returns an error
        when the pattern data was uninstalled since the pattern object
        was created.
        
        Parameters:
        
        * pattern - The pattern.
        """
        pass

    def gimp_patterns_set_popup(self, pattern_callback: str=None, pattern: Gimp.Pattern=None):
        """Sets the current pattern in a pattern selection dialog.
        
        Sets the current pattern in a pattern selection dialog.
        
        Parameters:
        
        * pattern_callback - The name of the callback registered for this
          pop-up.
        
        * pattern - The pattern to set as selected.
        """
        pass

    def gimp_pdb_add_proc_menu_path(self, procedure_name: str=None, menu_path: str=None):
        """Register an additional menu path for a plug-in procedure.
        
        This procedure installs an additional menu entry for the given
        procedure.
        
        Parameters:
        
        * procedure_name - The procedure for which to install the menu path.
        
        * menu_path - The procedure's additional menu path.
        """
        pass

    def gimp_pdb_dump(self, file: Gio.File=None):
        """Dumps the current contents of the procedural database.
        
        This procedure dumps the contents of the procedural database to the
        specified file. The file will contain all of the information
        provided for each registered procedure.
        
        Parameters:
        
        * file - The dump filename.
        """
        pass

    def gimp_pdb_get_data(self, identifier: str=None) -> GLib.Bytes:
        """Returns data associated with the specified identifier.
        
        This procedure returns any data which may have been associated with the
        specified identifier. The data is a variable length array of
        bytes. If no data has been associated with the identifier, an
        error is returned.
        
        Parameters:
        
        * identifier - The identifier associated with data.
        
        Returns:
        
        * data - A byte array containing data.
        """
        pass

    def gimp_pdb_get_proc_argument(self, procedure_name: str=None, arg_num: int=None) -> GObject.ParamSpec:
        """Queries the procedural database for information on the specified
        procedure's argument.
        
        This procedure returns the #GParamSpec of procedure_name's argument.
        
        Parameters:
        
        * procedure_name - The procedure name.
        
        * arg_num (default: 0) - The argument number.
        
        Returns:
        
        * param_spec - The GParamSpec of the argument.
        """
        pass

    def gimp_pdb_get_proc_attribution(self, procedure_name: str=None) -> Tuple[str, str, str]:
        """Queries the procedural database for attribution information on the
        specified procedure.
        
        This procedure returns attribution information on the specified
        procedure. The authors, copyright information and date are
        returned.
        
        Parameters:
        
        * procedure_name - The procedure name.
        
        Returns:
        
        * authors - Authors of the procedure.
        
        * copyright - The copyright.
        
        * date - Copyright date.
        """
        pass

    def gimp_pdb_get_proc_documentation(self, procedure_name: str=None) -> Tuple[str, str, str]:
        """Queries the procedural database for documentation on the specified
        procedure.
        
        This procedure returns documentation on the specified procedure. A short
        blurb, detailed help and help_id.
        
        Parameters:
        
        * procedure_name - The procedure name.
        
        Returns:
        
        * blurb - A short blurb.
        
        * help - Detailed procedure help.
        
        * help_id - The procedure help_id.
        """
        pass

    def gimp_pdb_get_proc_image_types(self, procedure_name: str=None) -> str:
        """Queries the procedural database for the image types supported by the
        specified procedure.
        
        This procedure returns the image types supported by the specified
        procedure.
        
        Parameters:
        
        * procedure_name - The procedure name.
        
        Returns:
        
        * image_types - The image types.
        """
        pass

    def gimp_pdb_get_proc_info(self, procedure_name: str=None) -> Tuple[Gimp.PDBProcType, int, int]:
        """Queries the procedural database for information on the specified
        procedure.
        
        This procedure returns information on the specified procedure. The
        procedure type, number of input, and number of return values are
        returned. For specific information on each input argument and
        return value, use the 'gimp-pdb-db-proc-argument' and
        'gimp-pdb-db-proc-return-value' procedures.
        
        Parameters:
        
        * procedure_name - The procedure name.
        
        Returns:
        
        * proc_type (default: <enum GIMP_PDB_PROC_TYPE_INTERNAL of type
          Gimp.PDBProcType>) - The procedure type.
        
        * num_args (default: 0) - The number of input arguments.
        
        * num_values (default: 0) - The number of return values.
        """
        pass

    def gimp_pdb_get_proc_menu_label(self, procedure_name: str=None) -> str:
        """Queries the procedural database for the procedure's menu label.
        
        This procedure returns the menu label of the specified procedure.
        
        Parameters:
        
        * procedure_name - The procedure name.
        
        Returns:
        
        * menu_label - The menu_label.
        """
        pass

    def gimp_pdb_get_proc_menu_paths(self, procedure_name: str=None) -> List[str]:
        """Queries the procedural database for the procedure's menu paths.
        
        This procedure returns the menu paths of the specified procedure.
        
        Parameters:
        
        * procedure_name - The procedure name.
        
        Returns:
        
        * menu_paths - The menu paths of the plug-in.
        """
        pass

    def gimp_pdb_get_proc_return_value(self, procedure_name: str=None, val_num: int=None) -> GObject.ParamSpec:
        """Queries the procedural database for information on the specified
        procedure's return value.
        
        This procedure returns the #GParamSpec of procedure_name's return value.
        
        Parameters:
        
        * procedure_name - The procedure name.
        
        * val_num (default: 0) - The return value number.
        
        Returns:
        
        * param_spec - The GParamSpec of the return value.
        """
        pass

    def gimp_pdb_proc_exists(self, procedure_name: str=None) -> bool:
        """Checks if the specified procedure exists in the procedural database.
        
        This procedure checks if the specified procedure is registered in the
        procedural database.
        
        Parameters:
        
        * procedure_name - The procedure name.
        
        Returns:
        
        * exists (default: False) - Whether a procedure of that name is
          registered.
        """
        pass

    def gimp_pdb_query(self, name: str=None, blurb: str=None, help: str=None, authors: str=None, copyright: str=None, date: str=None, proc_type: str=None) -> List[str]:
        """Queries the procedural database for its contents using regular
        expression matching.
        
        This procedure queries the contents of the procedural database. It is
        supplied with seven arguments matching procedures on { name,
        blurb, help, authors, copyright, date, procedure type}. This is
        accomplished using regular expression matching. For instance, to
        find all procedures with "jpeg" listed in the blurb, all seven
        arguments can be supplied as ".*", except for the second, which
        can be supplied as ".*jpeg.*". There are two return arguments
        for this procedure. The first is the number of procedures
        matching the query. The second is a concatenated list of
        procedure names corresponding to those matching the query. If no
        matching entries are found, then the returned string is NULL and
        the number of entries is 0.
        
        Parameters:
        
        * name - The regex for procedure name.
        
        * blurb - The regex for procedure blurb.
        
        * help - The regex for procedure help.
        
        * authors - The regex for procedure authors.
        
        * copyright - The regex for procedure copyright.
        
        * date - The regex for procedure date.
        
        * proc_type - The regex for procedure type: { 'Internal GIMP
          procedure', 'GIMP Plug-in', 'GIMP Extension', 'Temporary
          Procedure' }.
        
        Returns:
        
        * procedure_names - The list of procedure names.
        """
        pass

    def gimp_pdb_set_batch_interpreter(self, procedure_name: str=None, interpreter_name: str=None):
        """Registers a batch interpreter procedure.
        
        Registers a procedural database procedure to be called with the command
        line interface options --batch-interpreter and --batch.
        
        Parameters:
        
        * procedure_name - The name of the procedure to be used for running
          batch commands.
        
        * interpreter_name - A public-facing name for the interpreter, such as
          "Python 3".
        """
        pass

    def gimp_pdb_set_data(self, identifier: str=None, data: GLib.Bytes=None):
        """Associates the specified identifier with the supplied data.
        
        This procedure associates the supplied data with the provided
        identifier. The data may be subsequently retrieved by a call to
        'procedural-db-get-data'.
        
        Parameters:
        
        * identifier - The identifier associated with data.
        
        * data - A byte array containing data.
        """
        pass

    def gimp_pdb_set_file_proc_handles_raw(self, procedure_name: str=None):
        """Registers a file handler procedure as capable of handling raw camera
        files.
        
        Registers a file handler procedure as capable of handling raw digital
        camera files. Use this procedure only to register raw load
        handlers, calling it on a save handler will generate an error.
        
        Parameters:
        
        * procedure_name - The name of the procedure to enable raw handling
          for.
        """
        pass

    def gimp_pdb_set_file_proc_handles_remote(self, procedure_name: str=None):
        """Registers a file handler procedure as capable of handling remote
        URIs.
        
        Registers a file handler procedure as capable of handling remote URIs.
        This allows GIMP to call the procedure directly for all kinds of
        URIs, not only on local file:// URIs.
        
        Parameters:
        
        * procedure_name - The name of the procedure to enable remote URIs
          for.
        """
        pass

    def gimp_pdb_set_file_proc_load_handler(self, procedure_name: str=None, extensions: str=None, prefixes: str=None, magics: str=None):
        """Registers a file load handler procedure.
        
        Registers a procedural database procedure to be called to load files of
        a particular file format using magic file information.
        
        Parameters:
        
        * procedure_name - The name of the procedure to be used for loading.
        
        * extensions - comma separated list of extensions this handler can
          load (i.e. "jpg,jpeg").
        
        * prefixes - comma separated list of prefixes this handler can load
          (i.e. "http:,ftp:").
        
        * magics - comma separated list of magic file information this handler
          can load (i.e. "0,string,GIF").
        """
        pass

    def gimp_pdb_set_file_proc_mime_types(self, procedure_name: str=None, mime_types: str=None):
        """Associates MIME types with a file handler procedure.
        
        Registers MIME types for a file handler procedure. This allows GIMP to
        determine the MIME type of the file opened or saved using this
        procedure. It is recommended that only one MIME type is
        registered per file procedure; when registering more than one
        MIME type, GIMP will associate the first one with files opened
        or saved with this procedure.
        
        Parameters:
        
        * procedure_name - The name of the procedure to associate a MIME type
          with.
        
        * mime_types - A comma-separated list of MIME types, such as
          "image/jpeg".
        """
        pass

    def gimp_pdb_set_file_proc_priority(self, procedure_name: str=None, priority: int=None):
        """Sets the priority of a file handler procedure.
        
        Sets the priority of a file handler procedure. When more than one
        procedure matches a given file, the procedure with the lowest
        priority is used; if more than one procedure has the lowest
        priority, it is unspecified which one of them is used. The
        default priority for file handler procedures is 0.
        
        Parameters:
        
        * procedure_name - The name of the procedure to set the priority of.
        
        * priority (default: 0) - The procedure priority.
        """
        pass

    def gimp_pdb_set_file_proc_save_handler(self, procedure_name: str=None, extensions: str=None, prefixes: str=None):
        """Registers a file save handler procedure.
        
        Registers a procedural database procedure to be called to save files in
        a particular file format.
        
        Parameters:
        
        * procedure_name - The name of the procedure to be used for saving.
        
        * extensions - comma separated list of extensions this handler can
          save (i.e. "jpg,jpeg").
        
        * prefixes - comma separated list of prefixes this handler can save
          (i.e. "http:,ftp:").
        """
        pass

    def gimp_pdb_set_file_proc_thumbnail_loader(self, load_proc: str=None, thumb_proc: str=None):
        """Associates a thumbnail loader with a file load procedure.
        
        Some file formats allow for embedded thumbnails, other file formats
        contain a scalable image or provide the image data in different
        resolutions. A file plug-in for such a format may register a
        special procedure that allows GIMP to load a thumbnail preview
        of the image. This procedure is then associated with the
        standard load procedure using this function.
        
        Parameters:
        
        * load_proc - The name of the file load procedure.
        
        * thumb_proc - The name of the thumbnail load procedure.
        """
        pass

    def gimp_pdb_set_proc_attribution(self, procedure_name: str=None, authors: str=None, copyright: str=None, date: str=None):
        """Set the attribution for a plug-in procedure.
        
        This procedure sets the attribution for the given procedure.
        
        Parameters:
        
        * procedure_name - The procedure for which to install the menu path.
        
        * authors - Authors of the procedure.
        
        * copyright - The copyright.
        
        * date - Copyright date.
        """
        pass

    def gimp_pdb_set_proc_documentation(self, procedure_name: str=None, blurb: str=None, help: str=None, help_id: str=None):
        """Set the documentation for a plug-in procedure.
        
        This procedure sets the documentation for the given procedure.
        
        Parameters:
        
        * procedure_name - The procedure for which to install the menu path.
        
        * blurb - A short blurb.
        
        * help - Detailed procedure help.
        
        * help_id - The procedure help_id.
        """
        pass

    def gimp_pdb_set_proc_icon(self, procedure_name: str=None, icon_type: Gimp.IconType=None, icon_data: GLib.Bytes=None):
        """Register an icon for a plug-in procedure.
        
        This procedure installs an icon for the given procedure.
        
        Parameters:
        
        * procedure_name - The procedure for which to install the icon.
        
        * icon_type (default: <enum GIMP_ICON_TYPE_ICON_NAME of type
          Gimp.IconType>) - The type of the icon.
        
        * icon_data - The procedure's icon. The format depends on the
          'icon_type' parameter.
        """
        pass

    def gimp_pdb_set_proc_image_types(self, procedure_name: str=None, image_types: str=None):
        """Set the supported image types for a plug-in procedure.
        
        This procedure sets the supported images types for the given procedure.
        
        Parameters:
        
        * procedure_name - The procedure for which to install the menu path.
        
        * image_types - The procedure's supported image types.
        """
        pass

    def gimp_pdb_set_proc_menu_label(self, procedure_name: str=None, menu_label: str=None):
        """Set the menu label for a plug-in procedure.
        
        This procedure sets the menu label for the given procedure.
        
        Parameters:
        
        * procedure_name - The procedure for which to install the menu path.
        
        * menu_label - The procedure's menu label.
        """
        pass

    def gimp_pdb_set_proc_sensitivity_mask(self, procedure_name: str=None, mask: int=None):
        """Set the sensitivity mask for a plug-in procedure.
        
        This procedure sets the sensitivity mask for the given procedure.
        
        Parameters:
        
        * procedure_name - The procedure.
        
        * mask (default: 0) - The procedure's sensitivity mask.
        """
        pass

    def gimp_pdb_temp_name(self) -> str:
        """Generates a unique temporary PDB name.
        
        This procedure generates a temporary PDB entry name that is guaranteed
        to be unique.
        
        Returns:
        
        * temp_name - A unique temporary name for a temporary PDB entry.
        """
        pass

    def gimp_pencil(self, drawable: Gimp.Drawable=None, num_strokes: int=None, strokes: Gimp.FloatArray=None):
        """Paint in the current brush without sub-pixel sampling.
        
        This tool is the standard pencil. It draws linearly interpolated lines
        through the specified stroke coordinates. It operates on the
        specified drawable in the foreground color with the active
        brush. The brush mask is treated as though it contains only
        black and white values. Any value below half is treated as
        black; any above half, as white.
        
        Parameters:
        
        * drawable - The affected drawable.
        
        * num_strokes (default: 2) - Number of stroke control points (count
          each coordinate as 2 points).
        
        * strokes - Array of stroke coordinates: { s1.x, s1.y, s2.x, s2.y,
          ..., sn.x, sn.y }.
        """
        pass

    def gimp_plug_in_get_pdb_error_handler(self) -> Gimp.PDBErrorHandler:
        """Retrieves the active error handler for procedure calls.
        
        This procedure retrieves the currently active error handler for
        procedure calls made by the calling plug-in. See
        'gimp-plugin-set-pdb-error-handler' for details.
        
        Returns:
        
        * handler (default: <enum GIMP_PDB_ERROR_HANDLER_INTERNAL of type
          Gimp.PDBErrorHandler>) - Who is responsible for handling
          procedure call errors.
        """
        pass

    def gimp_plug_in_help_register(self, domain_name: str=None, domain_file: Gio.File=None):
        """Register a help path for a plug-in.
        
        This procedure registers user documentation for the calling plug-in with
        the GIMP help system. The domain_uri parameter points to the
        root directory where the plug-in help is installed. For each
        supported language there should be a file called 'gimp-help.xml'
        that maps the help IDs to the actual help files.
        
        Parameters:
        
        * domain_name - The XML namespace of the plug-in's help pages.
        
        * domain_file - The root URI of the plug-in's help pages.
        """
        pass

    def gimp_plug_in_menu_branch_register(self, menu_path: str=None, menu_name: str=None):
        """Register a sub-menu.
        
        This procedure installs a sub-menu which does not belong to any
        procedure. The menu-name should be the untranslated menu label.
        GIMP will look up the translation in the textdomain registered
        for the plug-in.
        
        Parameters:
        
        * menu_path - The sub-menu's menu path.
        
        * menu_name - The name of the sub-menu.
        """
        pass

    def gimp_plug_in_set_pdb_error_handler(self, handler: Gimp.PDBErrorHandler=None):
        """Sets an error handler for procedure calls.
        
        This procedure changes the way that errors in procedure calls are
        handled. By default GIMP will raise an error dialog if a
        procedure call made by a plug-in fails. Using this procedure the
        plug-in can change this behavior. If the error handler is set to
        %GIMP_PDB_ERROR_HANDLER_PLUGIN, then the plug-in is responsible
        for calling 'gimp-get-pdb-error' and handling the error whenever
        one if its procedure calls fails. It can do this by displaying
        the error message or by forwarding it in its own return values.
        
        Parameters:
        
        * handler (default: <enum GIMP_PDB_ERROR_HANDLER_INTERNAL of type
          Gimp.PDBErrorHandler>) - Who is responsible for handling
          procedure call errors.
        """
        pass

    def gimp_plug_ins_query(self, search_string: str=None) -> Tuple[List[str], List[str], List[str], int, Gimp.Int32Array]:
        """Queries the plug-in database for its contents.
        
        This procedure queries the contents of the plug-in database.
        
        Parameters:
        
        * search_string - If not an empty string then use this as a search
          pattern.
        
        Returns:
        
        * procedures - The plug-in procedure name.
        
        * accelerators - String representing keyboard accelerator (could be
          empty string).
        
        * locations - Location of the plug-in program.
        
        * num_install_times (default: 0) - The number of matching procedures.
        
        * install_times - Time that the plug-in was installed.
        """
        pass

    def gimp_progress_cancel(self, progress_callback: str=None):
        """Cancels a running progress.
        
        This function cancels the currently running progress.
        
        Parameters:
        
        * progress_callback - The name of the callback registered for this
          progress.
        """
        pass

    def gimp_progress_end(self):
        """Ends the progress bar for the current plug-in.
        
        Ends the progress display for the current plug-in. Most plug-ins don't
        need to call this, they just exit when the work is done. It is
        only valid to call this procedure from a plug-in.
        """
        pass

    def gimp_progress_get_window_handle(self) -> GLib.Bytes:
        """Returns the native handle of the toplevel window this plug-in's
        progress is displayed in.
        
        This function returns the native handle allowing to identify the
        toplevel window this plug-in's progress is displayed in. This
        handle can be of various types (integer, string, etc.) depending
        on the platform you are running on which is why it returns a
        GBytes. There are usually no reasons to call this directly.
        
        Returns:
        
        * handle - The progress bar's toplevel window's handle.
        """
        pass

    def gimp_progress_init(self, message: str=None, gdisplay: Gimp.Display=None):
        """Initializes the progress bar for the current plug-in.
        
        Initializes the progress bar for the current plug-in. It is only valid
        to call this procedure from a plug-in.
        
        Parameters:
        
        * message - Message to use in the progress dialog.
        
        * gdisplay - GimpDisplay to update progressbar in, or %NULL for a
          separate window.
        """
        pass

    def gimp_progress_install(self, progress_callback: str=None):
        """Installs a progress callback for the current plug-in.
        
        This function installs a temporary PDB procedure which will handle all
        progress calls made by this plug-in and any procedure it calls.
        Calling this function multiple times simply replaces the old
        progress callbacks.
        
        Parameters:
        
        * progress_callback - The callback PDB proc to call.
        """
        pass

    def gimp_progress_pulse(self):
        """Pulses the progress bar for the current plug-in.
        
        Updates the progress bar for the current plug-in. It is only valid to
        call this procedure from a plug-in. Use this function instead of
        'gimp-progress-update' if you cannot tell how much progress has
        been made. This usually causes the the progress bar to enter
        "activity mode", where a block bounces back and forth.
        """
        pass

    def gimp_progress_set_text(self, message: str=None):
        """Changes the text in the progress bar for the current plug-in.
        
        This function changes the text in the progress bar for the current
        plug-in. Unlike 'gimp-progress-init' it does not change the
        displayed value.
        
        Parameters:
        
        * message - Message to use in the progress dialog.
        """
        pass

    def gimp_progress_uninstall(self, progress_callback: str=None):
        """Uninstalls the progress callback for the current plug-in.
        
        This function uninstalls any progress callback installed with
        'gimp-progress-install' before.
        
        Parameters:
        
        * progress_callback - The name of the callback registered for this
          progress.
        """
        pass

    def gimp_progress_update(self, percentage: float=None):
        """Updates the progress bar for the current plug-in.
        
        Updates the progress bar for the current plug-in. It is only valid to
        call this procedure from a plug-in.
        
        Parameters:
        
        * percentage (default: 0.0) - Percentage of progress completed which
          must be between 0.0 and 1.0.
        """
        pass

    def gimp_quit(self, force: bool=None):
        """Causes GIMP to exit gracefully.
        
        If there are unsaved images in an interactive GIMP session, the user
        will be asked for confirmation. If force is TRUE, the
        application is quit without querying the user to save any dirty
        images.
        
        Parameters:
        
        * force (default: False) - Force GIMP to quit without asking.
        """
        pass

    def gimp_resource_delete(self, resource: Gimp.Resource=None):
        """Deletes a resource.
        
        Deletes a resource. Returns an error if the resource is not deletable.
        Deletes the resource's data. You should not use the resource
        afterwards.
        
        Parameters:
        
        * resource - The resource.
        """
        pass

    def gimp_resource_duplicate(self, resource: Gimp.Resource=None) -> Gimp.Resource:
        """Duplicates a resource.
        
        Returns a copy having a different, unique ID.
        
        Parameters:
        
        * resource - The resource.
        
        Returns:
        
        * resource_copy - A copy of the resource.
        """
        pass

    def gimp_resource_get_by_identifiers(self, type_name: str=None, resource_name: str=None, collection: str=None, is_internal: bool=None) -> Gimp.Resource:
        """Returns the resource contained in a given file with a given name.
        
        Returns a resource specifically stored in a given file path, under a
        given name (a single path may be a collection containing several
        resources).
        
        Parameters:
        
        * type_name - The name of the resource type.
        
        * resource_name - The name of the resource.
        
        * collection - The collection identifier.
        
        * is_internal (default: False) - Whether this is the identifier for
          internal data.
        
        Returns:
        
        * resource - The resource.
        """
        pass

    def gimp_resource_get_by_name(self, type_name: str=None, resource_name: str=None) -> Gimp.Resource:
        """Returns a resource with the given name.
        
        Returns a resource with the given name.
        
        Parameters:
        
        * type_name - The name of the resource type.
        
        * resource_name - The name of the resource.
        
        Returns:
        
        * resource - The resource.
        """
        pass

    def gimp_resource_get_identifiers(self, resource: Gimp.Resource=None) -> Tuple[bool, str, str]:
        """Returns a triplet identifying the resource.
        
        This procedure returns 2 strings and a boolean. The first string is the
        resource name, similar to what you would obtain calling
        'gimp-resource-get-name'. The second is an opaque identifier for
        the collection this resource belongs to. Note: as far as GIMP is
        concerned, a collection of resource usually corresponds to a
        single file on disk (which may or may not contain several
        resources). Therefore the identifier may be derived from the
        local file path. Nevertheless you should not use this string as
        such as this is not guaranteed to be always the case. You should
        consider it as an opaque identifier only to be used again
        through _'gimp-resource-get-by-identifier'.
        
        Parameters:
        
        * resource - The resource.
        
        Returns:
        
        * is_internal (default: False) - Whether this is the identifier for
          internal data.
        
        * name - The resource's name.
        
        * collection_id - The resource's collection identifier.
        """
        pass

    def gimp_resource_get_name(self, resource: Gimp.Resource=None) -> str:
        """Returns the resource's name.
        
        This procedure returns the resource's name.
        
        Parameters:
        
        * resource - The resource.
        
        Returns:
        
        * name - The resource's name.
        """
        pass

    def gimp_resource_id_is_brush(self, resource_id: int=None) -> bool:
        """Returns whether the resource ID is a brush.
        
        This procedure returns TRUE if the specified resource ID is a brush.
        
        Parameters:
        
        * resource_id (default: 0) - The resource ID.
        
        Returns:
        
        * brush (default: False) - TRUE if the resource ID is a brush, FALSE
          otherwise.
        """
        pass

    def gimp_resource_id_is_font(self, resource_id: int=None) -> bool:
        """Returns whether the resource ID is a font.
        
        This procedure returns TRUE if the specified resource ID is a font.
        
        Parameters:
        
        * resource_id (default: 0) - The resource ID.
        
        Returns:
        
        * font (default: False) - TRUE if the resource ID is a font, FALSE
          otherwise.
        """
        pass

    def gimp_resource_id_is_gradient(self, resource_id: int=None) -> bool:
        """Returns whether the resource ID is a gradient.
        
        This procedure returns TRUE if the specified resource ID is a gradient.
        
        Parameters:
        
        * resource_id (default: 0) - The resource ID.
        
        Returns:
        
        * gradient (default: False) - TRUE if the resource ID is a gradient,
          FALSE otherwise.
        """
        pass

    def gimp_resource_id_is_palette(self, resource_id: int=None) -> bool:
        """Returns whether the resource ID is a palette.
        
        This procedure returns TRUE if the specified resource ID is a palette.
        
        Parameters:
        
        * resource_id (default: 0) - The resource ID.
        
        Returns:
        
        * palette (default: False) - TRUE if the resource ID is a palette,
          FALSE otherwise.
        """
        pass

    def gimp_resource_id_is_pattern(self, resource_id: int=None) -> bool:
        """Returns whether the resource ID is a pattern.
        
        This procedure returns TRUE if the specified resource ID is a pattern.
        
        Parameters:
        
        * resource_id (default: 0) - The resource ID.
        
        Returns:
        
        * pattern (default: False) - TRUE if the resource ID is a pattern,
          FALSE otherwise.
        """
        pass

    def gimp_resource_id_is_valid(self, resource_id: int=None) -> bool:
        """Returns TRUE if the resource ID is valid.
        
        This procedure checks if the given resource ID is valid and refers to an
        existing resource.
        
        Parameters:
        
        * resource_id (default: 0) - The resource ID to check.
        
        Returns:
        
        * valid (default: False) - Whether the resource ID is valid.
        """
        pass

    def gimp_resource_is_editable(self, resource: Gimp.Resource=None) -> bool:
        """Whether the resource can be edited.
        
        Returns TRUE if you have permission to change the resource.
        
        Parameters:
        
        * resource - The resource.
        
        Returns:
        
        * editable (default: False) - TRUE if the resource can be edited.
        """
        pass

    def gimp_resource_rename(self, resource: Gimp.Resource=None, new_name: str=None):
        """Renames a resource. When the name is in use, renames to a unique
        name.
        
        Renames a resource. When the proposed name is already used, GIMP
        generates a unique name.
        
        Parameters:
        
        * resource - The resource.
        
        * new_name - The proposed new name of the resource.
        """
        pass

    def gimp_selection_all(self, image: Gimp.Image=None):
        """Select all of the image.
        
        This procedure sets the selection mask to completely encompass the
        image. Every pixel in the selection channel is set to 255.
        
        Parameters:
        
        * image - The image.
        """
        pass

    def gimp_selection_border(self, image: Gimp.Image=None, radius: int=None):
        """Border the image's selection.
        
        This procedure borders the selection. Bordering creates a new selection
        which is defined along the boundary of the previous selection at
        every point within the specified radius.
        
        Parameters:
        
        * image - The image.
        
        * radius (default: 0) - Radius of border (in pixels).
        """
        pass

    def gimp_selection_bounds(self, image: Gimp.Image=None) -> Tuple[bool, int, int, int, int]:
        """Find the bounding box of the current selection.
        
        This procedure returns whether there is a selection for the specified
        image. If there is one, the upper left and lower right corners
        of the bounding box are returned. These coordinates are relative
        to the image. Please note that the pixel specified by the lower
        right coordinate of the bounding box is not part of the
        selection. The selection ends at the upper left corner of this
        pixel. This means the width of the selection can be calculated
        as (x2 - x1), its height as (y2 - y1).
        
        Parameters:
        
        * image - The image.
        
        Returns:
        
        * non_empty (default: False) - TRUE if there is a selection.
        
        * x1 (default: 0) - x coordinate of upper left corner of selection
          bounds.
        
        * y1 (default: 0) - y coordinate of upper left corner of selection
          bounds.
        
        * x2 (default: 0) - x coordinate of lower right corner of selection
          bounds.
        
        * y2 (default: 0) - y coordinate of lower right corner of selection
          bounds.
        """
        pass

    def gimp_selection_clear(self, image: Gimp.Image=None):
        """Deselect the entire image.
        
        This procedure deselects the entire image. Every pixel in the selection
        channel is set to 0.
        
        Parameters:
        
        * image - The image.
        """
        pass

    def gimp_selection_feather(self, image: Gimp.Image=None, radius: float=None):
        """Feather the image's selection.
        
        This procedure feathers the selection. Feathering is implemented using a
        gaussian blur.
        
        Parameters:
        
        * image - The image.
        
        * radius (default: 0.0) - Radius of feather (in pixels).
        """
        pass

    def gimp_selection_float(self, num_drawables: int=None, drawables: Gimp.ObjectArray=None, offx: int=None, offy: int=None) -> Gimp.Layer:
        """Float the selection from the specified drawable with initial offsets
        as specified.
        
        This procedure determines the region of the specified drawable that lies
        beneath the current selection. The region is then cut from the
        drawable and the resulting data is made into a new layer which
        is instantiated as a floating selection. The offsets allow
        initial positioning of the new floating selection.
        
        Parameters:
        
        * num_drawables (default: 1) - The number of drawables.
        
        * drawables - The drawables from which to float selection.
        
        * offx (default: 0) - x offset for translation.
        
        * offy (default: 0) - y offset for translation.
        
        Returns:
        
        * layer - The floated layer.
        """
        pass

    def gimp_selection_flood(self, image: Gimp.Image=None):
        """Remove holes from the image's selection.
        
        This procedure removes holes from the selection, that can come from
        selecting a patchy area with the Fuzzy Select Tool. In technical
        terms this procedure floods the selection. See the Algorithms
        page in the developer wiki for details.
        
        Parameters:
        
        * image - The image.
        """
        pass

    def gimp_selection_grow(self, image: Gimp.Image=None, steps: int=None):
        """Grow the image's selection.
        
        This procedure grows the selection. Growing involves expanding the
        boundary in all directions by the specified pixel amount.
        
        Parameters:
        
        * image - The image.
        
        * steps (default: 0) - Steps of grow (in pixels).
        """
        pass

    def gimp_selection_invert(self, image: Gimp.Image=None):
        """Invert the selection mask.
        
        This procedure inverts the selection mask. For every pixel in the
        selection channel, its new value is calculated as (255 -
        old-value).
        
        Parameters:
        
        * image - The image.
        """
        pass

    def gimp_selection_is_empty(self, image: Gimp.Image=None) -> bool:
        """Determine whether the selection is empty.
        
        This procedure returns TRUE if the selection for the specified image is
        empty.
        
        Parameters:
        
        * image - The image.
        
        Returns:
        
        * is_empty (default: False) - Is the selection empty?.
        """
        pass

    def gimp_selection_none(self, image: Gimp.Image=None):
        """Deselect the entire image.
        
        This procedure deselects the entire image. Every pixel in the selection
        channel is set to 0.
        
        Parameters:
        
        * image - The image.
        """
        pass

    def gimp_selection_save(self, image: Gimp.Image=None) -> Gimp.Channel:
        """Copy the selection mask to a new channel.
        
        This procedure copies the selection mask and stores the content in a new
        channel. The new channel is automatically inserted into the
        image's list of channels.
        
        Parameters:
        
        * image - The image.
        
        Returns:
        
        * channel - The new channel.
        """
        pass

    def gimp_selection_sharpen(self, image: Gimp.Image=None):
        """Sharpen the selection mask.
        
        This procedure sharpens the selection mask. For every pixel in the
        selection channel, if the value is > 127, the new pixel is
        assigned a value of 255. This removes any "anti-aliasing" that
        might exist in the selection mask's boundary.
        
        Parameters:
        
        * image - The image.
        """
        pass

    def gimp_selection_shrink(self, image: Gimp.Image=None, steps: int=None):
        """Shrink the image's selection.
        
        This procedure shrinks the selection. Shrinking involves trimming the
        existing selection boundary on all sides by the specified number
        of pixels.
        
        Parameters:
        
        * image - The image.
        
        * steps (default: 0) - Steps of shrink (in pixels).
        """
        pass

    def gimp_selection_translate(self, image: Gimp.Image=None, offx: int=None, offy: int=None):
        """Translate the selection by the specified offsets.
        
        This procedure actually translates the selection for the specified image
        by the specified offsets. Regions that are translated from
        beyond the bounds of the image are set to empty. Valid regions
        of the selection which are translated beyond the bounds of the
        image because of this call are lost.
        
        Parameters:
        
        * image - The image.
        
        * offx (default: 0) - x offset for translation.
        
        * offy (default: 0) - y offset for translation.
        """
        pass

    def gimp_selection_value(self, image: Gimp.Image=None, x: int=None, y: int=None) -> int:
        """Find the value of the selection at the specified coordinates.
        
        This procedure returns the value of the selection at the specified
        coordinates. If the coordinates lie out of bounds, 0 is
        returned.
        
        Parameters:
        
        * image - The image.
        
        * x (default: 0) - x coordinate of value.
        
        * y (default: 0) - y coordinate of value.
        
        Returns:
        
        * value (default: 0) - Value of the selection.
        """
        pass

    def gimp_smudge(self, drawable: Gimp.Drawable=None, pressure: float=None, num_strokes: int=None, strokes: Gimp.FloatArray=None):
        """Smudge image with varying pressure.
        
        This tool simulates a smudge using the current brush. High pressure
        results in a greater smudge of paint while low pressure results
        in a lesser smudge.
        
        Parameters:
        
        * drawable - The affected drawable.
        
        * pressure (default: 0.0) - The pressure of the smudge strokes.
        
        * num_strokes (default: 2) - Number of stroke control points (count
          each coordinate as 2 points).
        
        * strokes - Array of stroke coordinates: { s1.x, s1.y, s2.x, s2.y,
          ..., sn.x, sn.y }.
        """
        pass

    def gimp_smudge_default(self, drawable: Gimp.Drawable=None, num_strokes: int=None, strokes: Gimp.FloatArray=None):
        """Smudge image with varying pressure.
        
        This tool simulates a smudge using the current brush. It behaves exactly
        the same as 'gimp-smudge' except that the pressure value is
        taken from the smudge tool options or the options default if the
        tools option dialog has not been activated.
        
        Parameters:
        
        * drawable - The affected drawable.
        
        * num_strokes (default: 2) - Number of stroke control points (count
          each coordinate as 2 points).
        
        * strokes - Array of stroke coordinates: { s1.x, s1.y, s2.x, s2.y,
          ..., sn.x, sn.y }.
        """
        pass

    def gimp_temp_file(self, extension: str=None) -> Gio.File:
        """Generates a unique temporary file.
        
        Generates a unique file using the temp path supplied in the user's
        gimprc.
        
        Parameters:
        
        * extension - The extension the file will have.
        
        Returns:
        
        * file - The new temp file.
        """
        pass

    def gimp_text_font(self, image: Gimp.Image=None, drawable: Gimp.Drawable=None, x: float=None, y: float=None, text: str=None, border: int=None, antialias: bool=None, size: float=None, font: Gimp.Font=None) -> Gimp.Layer:
        """Add text at the specified location as a floating selection or a new
        layer.
        
        The x and y parameters together control the placement of the new text by
        specifying the upper left corner of the text bounding box. If
        the specified drawable parameter is valid, the text will be
        created as a floating selection attached to the drawable. If the
        drawable parameter is not valid (%NULL), the text will appear as
        a new layer. Finally, a border can be specified around the final
        rendered text. The border is measured in pixels. The size is
        always in pixels. If you need to display a font in points,
        divide the size in points by 72.0 and multiply it by the image's
        vertical resolution.
        
        Parameters:
        
        * image - The image.
        
        * drawable - The affected drawable: (%NULL for a new text layer).
        
        * x (default: 0.0) - The x coordinate for the left of the text
          bounding box.
        
        * y (default: 0.0) - The y coordinate for the top of the text bounding
          box.
        
        * text - The text to generate (in UTF-8 encoding).
        
        * border (default: -1) - The size of the border.
        
        * antialias (default: False) - Antialiasing.
        
        * size (default: 0.0) - The size of text in pixels.
        
        * font - The font.
        
        Returns:
        
        * text_layer - The new text layer or %NULL if no layer was created.
        """
        pass

    def gimp_text_get_extents_font(self, text: str=None, size: float=None, font: Gimp.Font=None) -> Tuple[int, int, int, int]:
        """Get extents of the bounding box for the specified text.
        
        This tool returns the width and height of a bounding box for the
        specified text rendered with the specified font information.
        Ascent and descent of the glyph extents are returned as well.
        The ascent is the distance from the baseline to the highest
        point of the character. This is positive if the glyph ascends
        above the baseline. The descent is the distance from the
        baseline to the lowest point of the character. This is positive
        if the glyph descends below the baseline. The size is always in
        pixels. If you need to set a font in points, divide the size in
        points by 72.0 and multiply it by the vertical resolution of the
        image you are taking into account.
        
        Parameters:
        
        * text - The text to generate (in UTF-8 encoding).
        
        * size (default: 0.0) - The size of text in either pixels or points.
        
        * font - The name of the font.
        
        Returns:
        
        * width (default: 0) - The width of the glyph extents.
        
        * height (default: 0) - The height of the glyph extents.
        
        * ascent (default: 0) - The ascent of the glyph extents.
        
        * descent (default: 0) - The descent of the glyph extents.
        """
        pass

    def gimp_text_layer_get_antialias(self, layer: Gimp.TextLayer=None) -> bool:
        """Check if antialiasing is used in the text layer.
        
        This procedure checks if antialiasing is enabled in the specified text
        layer.
        
        Parameters:
        
        * layer - The text layer.
        
        Returns:
        
        * antialias (default: False) - A flag which is true if antialiasing is
          used for rendering the font in the text layer.
        """
        pass

    def gimp_text_layer_get_base_direction(self, layer: Gimp.TextLayer=None) -> Gimp.TextDirection:
        """Get the base direction used for rendering the text layer.
        
        This procedure returns the base direction used for rendering the text in
        the text layer.
        
        Parameters:
        
        * layer - The text layer.
        
        Returns:
        
        * direction (default: <enum GIMP_TEXT_DIRECTION_LTR of type
          Gimp.TextDirection>) - The based direction used for the text
          layer.
        """
        pass

    def gimp_text_layer_get_color(self, layer: Gimp.TextLayer=None) -> Gegl.Color:
        """Get the color of the text in a text layer.
        
        This procedure returns the color of the text in a text layer.
        
        Parameters:
        
        * layer - The text layer.
        
        Returns:
        
        * color - The color of the text.
        """
        pass

    def gimp_text_layer_get_font(self, layer: Gimp.TextLayer=None) -> Gimp.Font:
        """Get the font from a text layer as string.
        
        This procedure returns the font from a text layer.
        
        Parameters:
        
        * layer - The text layer.
        
        Returns:
        
        * font - The font which is used in the specified text layer.
        """
        pass

    def gimp_text_layer_get_font_size(self, layer: Gimp.TextLayer=None) -> Tuple[float, Gimp.Unit]:
        """Get the font size from a text layer.
        
        This procedure returns the size of the font which is used in a text
        layer. You will receive the size as a float 'font-size' in
        'unit' units.
        
        Parameters:
        
        * layer - The text layer.
        
        Returns:
        
        * font_size (default: 0.0) - The font size.
        
        * unit (default: 0) - The unit used for the font size.
        """
        pass

    def gimp_text_layer_get_hint_style(self, layer: Gimp.TextLayer=None) -> Gimp.TextHintStyle:
        """Get information about hinting in the specified text layer.
        
        This procedure provides information about the hinting that is being used
        in a text layer. Hinting can be optimized for fidelity or
        contrast or it can be turned entirely off.
        
        Parameters:
        
        * layer - The text layer.
        
        Returns:
        
        * style (default: <enum GIMP_TEXT_HINT_STYLE_NONE of type
          Gimp.TextHintStyle>) - The hint style used for font
          outlines.
        """
        pass

    def gimp_text_layer_get_indent(self, layer: Gimp.TextLayer=None) -> float:
        """Get the line indentation of text layer.
        
        This procedure returns the indentation of the first line in a text
        layer.
        
        Parameters:
        
        * layer - The text layer.
        
        Returns:
        
        * indent (default: 0.0) - The indentation value of the first line.
        """
        pass

    def gimp_text_layer_get_justification(self, layer: Gimp.TextLayer=None) -> Gimp.TextJustification:
        """Get the text justification information of the text layer.
        
        This procedure returns the alignment of the lines in the text layer
        relative to each other.
        
        Parameters:
        
        * layer - The text layer.
        
        Returns:
        
        * justify (default: <enum GIMP_TEXT_JUSTIFY_LEFT of type
          Gimp.TextJustification>) - The justification used in the
          text layer.
        """
        pass

    def gimp_text_layer_get_kerning(self, layer: Gimp.TextLayer=None) -> bool:
        """Check if kerning is used in the text layer.
        
        This procedure checks if kerning is enabled in the specified text layer.
        
        Parameters:
        
        * layer - The text layer.
        
        Returns:
        
        * kerning (default: False) - A flag which is true if kerning is used
          in the text layer.
        """
        pass

    def gimp_text_layer_get_language(self, layer: Gimp.TextLayer=None) -> str:
        """Get the language used in the text layer.
        
        This procedure returns the language string which is set for the text in
        the text layer.
        
        Parameters:
        
        * layer - The text layer.
        
        Returns:
        
        * language - The language used in the text layer.
        """
        pass

    def gimp_text_layer_get_letter_spacing(self, layer: Gimp.TextLayer=None) -> float:
        """Get the letter spacing used in a text layer.
        
        This procedure returns the additional spacing between the single glyphs
        in a text layer.
        
        Parameters:
        
        * layer - The text layer.
        
        Returns:
        
        * letter_spacing (default: 0.0) - The letter-spacing value.
        """
        pass

    def gimp_text_layer_get_line_spacing(self, layer: Gimp.TextLayer=None) -> float:
        """Get the spacing between lines of text.
        
        This procedure returns the line-spacing between lines of text in a text
        layer.
        
        Parameters:
        
        * layer - The text layer.
        
        Returns:
        
        * line_spacing (default: 0.0) - The line-spacing value.
        """
        pass

    def gimp_text_layer_get_markup(self, layer: Gimp.TextLayer=None) -> str:
        """Get the markup from a text layer as string.
        
        This procedure returns the markup of the styles from a text layer. The
        markup will be in the form of Pango's markup - See
        https://www.pango.org/ for more information about Pango and its
        markup.
        
        Parameters:
        
        * layer - The text layer.
        
        Returns:
        
        * markup - The markup which represents the style of the specified text
          layer.
        """
        pass

    def gimp_text_layer_get_text(self, layer: Gimp.TextLayer=None) -> str:
        """Get the text from a text layer as string.
        
        This procedure returns the text from a text layer as a string.
        
        Parameters:
        
        * layer - The text layer.
        
        Returns:
        
        * text - The text from the specified text layer.
        """
        pass

    def gimp_text_layer_new(self, image: Gimp.Image=None, text: str=None, font: Gimp.Font=None, size: float=None, unit: Gimp.Unit=None) -> Gimp.TextLayer:
        """Creates a new text layer.
        
        This procedure creates a new text layer. The arguments are kept as
        simple as necessary for the normal case. All text attributes,
        however, can be modified with the appropriate
        gimp_text_layer_set_*() procedures. The new layer still needs to
        be added to the image, as this is not automatic. Add the new
        layer using 'gimp-image-insert-layer'.
        
        Parameters:
        
        * image - The image.
        
        * text - The text to generate (in UTF-8 encoding).
        
        * font - The font to write the text with.
        
        * size (default: 0.0) - The size of text in either pixels or points.
        
        * unit (default: 0) - The units of specified size.
        
        Returns:
        
        * layer - The new text layer.
        """
        pass

    def gimp_text_layer_resize(self, layer: Gimp.TextLayer=None, width: float=None, height: float=None):
        """Resize the box of a text layer.
        
        This procedure changes the width and height of a text layer while
        keeping it as a text layer and not converting it to a bitmap
        like 'gimp-layer-resize' would do.
        
        Parameters:
        
        * layer - The text layer.
        
        * width (default: 0.0) - The new box width in pixels.
        
        * height (default: 0.0) - The new box height in pixels.
        """
        pass

    def gimp_text_layer_set_antialias(self, layer: Gimp.TextLayer=None, antialias: bool=None):
        """Enable/disable anti-aliasing in a text layer.
        
        This procedure enables or disables anti-aliasing of the text in a text
        layer.
        
        Parameters:
        
        * layer - The text layer.
        
        * antialias (default: False) - Enable/disable antialiasing of the
          text.
        """
        pass

    def gimp_text_layer_set_base_direction(self, layer: Gimp.TextLayer=None, direction: Gimp.TextDirection=None):
        """Set the base direction in the text layer.
        
        This procedure sets the base direction used in applying the Unicode
        bidirectional algorithm when rendering the text.
        
        Parameters:
        
        * layer - The text layer.
        
        * direction (default: <enum GIMP_TEXT_DIRECTION_LTR of type
          Gimp.TextDirection>) - The base direction of the text.
        """
        pass

    def gimp_text_layer_set_color(self, layer: Gimp.TextLayer=None, color: Gimp.RGB=None):
        """Set the color of the text in the text layer.
        
        This procedure sets the text color in the text layer 'layer'.
        
        Parameters:
        
        * layer - The text layer.
        
        * color - The color to use for the text.
        """
        pass

    def gimp_text_layer_set_font(self, layer: Gimp.TextLayer=None, font: Gimp.Font=None):
        """Set the font of a text layer.
        
        This procedure modifies the font used in the specified text layer.
        
        Parameters:
        
        * layer - The text layer.
        
        * font - The new font to use.
        """
        pass

    def gimp_text_layer_set_font_size(self, layer: Gimp.TextLayer=None, font_size: float=None, unit: Gimp.Unit=None):
        """Set the font size.
        
        This procedure changes the font size of a text layer. The size of your
        font will be a double 'font-size' of 'unit' units.
        
        Parameters:
        
        * layer - The text layer.
        
        * font_size (default: 0.0) - The font size.
        
        * unit (default: 0) - The unit to use for the font size.
        """
        pass

    def gimp_text_layer_set_hint_style(self, layer: Gimp.TextLayer=None, style: Gimp.TextHintStyle=None):
        """Control how font outlines are hinted in a text layer.
        
        This procedure sets the hint style for font outlines in a text layer.
        This controls whether to fit font outlines to the pixel grid,
        and if so, whether to optimize for fidelity or contrast.
        
        Parameters:
        
        * layer - The text layer.
        
        * style (default: <enum GIMP_TEXT_HINT_STYLE_NONE of type
          Gimp.TextHintStyle>) - The new hint style.
        """
        pass

    def gimp_text_layer_set_indent(self, layer: Gimp.TextLayer=None, indent: float=None):
        """Set the indentation of the first line in a text layer.
        
        This procedure sets the indentation of the first line in the text layer.
        
        Parameters:
        
        * layer - The text layer.
        
        * indent (default: -8192.0) - The indentation for the first line.
        """
        pass

    def gimp_text_layer_set_justification(self, layer: Gimp.TextLayer=None, justify: Gimp.TextJustification=None):
        """Set the justification of the text in a text layer.
        
        This procedure sets the alignment of the lines in the text layer
        relative to each other.
        
        Parameters:
        
        * layer - The text layer.
        
        * justify (default: <enum GIMP_TEXT_JUSTIFY_LEFT of type
          Gimp.TextJustification>) - The justification for your text.
        """
        pass

    def gimp_text_layer_set_kerning(self, layer: Gimp.TextLayer=None, kerning: bool=None):
        """Enable/disable kerning in a text layer.
        
        This procedure enables or disables kerning in a text layer.
        
        Parameters:
        
        * layer - The text layer.
        
        * kerning (default: False) - Enable/disable kerning in the text.
        """
        pass

    def gimp_text_layer_set_language(self, layer: Gimp.TextLayer=None, language: str=None):
        """Set the language of the text layer.
        
        This procedure sets the language of the text in text layer. For some
        scripts the language has an influence of how the text is
        rendered.
        
        Parameters:
        
        * layer - The text layer.
        
        * language - The new language to use for the text layer.
        """
        pass

    def gimp_text_layer_set_letter_spacing(self, layer: Gimp.TextLayer=None, letter_spacing: float=None):
        """Adjust the letter spacing in a text layer.
        
        This procedure sets the additional spacing between the single glyphs in
        a text layer.
        
        Parameters:
        
        * layer - The text layer.
        
        * letter_spacing (default: -8192.0) - The additional letter spacing to
          use.
        """
        pass

    def gimp_text_layer_set_line_spacing(self, layer: Gimp.TextLayer=None, line_spacing: float=None):
        """Adjust the line spacing in a text layer.
        
        This procedure sets the additional spacing used between lines a text
        layer.
        
        Parameters:
        
        * layer - The text layer.
        
        * line_spacing (default: -8192.0) - The additional line spacing to
          use.
        """
        pass

    def gimp_text_layer_set_markup(self, layer: Gimp.TextLayer=None, markup: str=None):
        """Set the markup for a text layer from a string.
        
        This procedure sets the markup of the styles for a text layer. The
        markup should be in the form of Pango's markup - See
        https://docs.gtk.org/Pango/pango_markup.html for a reference.
        Note that GIMP's text tool does not support all of Pango markup.
        Any unsupported markup will still be applied to your text layer,
        yet would be dropped as soon as you edit text with the tool.
        
        Parameters:
        
        * layer - The text layer.
        
        * markup - The new markup to set.
        """
        pass

    def gimp_text_layer_set_text(self, layer: Gimp.TextLayer=None, text: str=None):
        """Set the text of a text layer.
        
        This procedure changes the text of a text layer.
        
        Parameters:
        
        * layer - The text layer.
        
        * text - The new text to set.
        """
        pass

    def gimp_undo_push_group_end(self, image: Gimp.Image=None):
        """Finish a group undo.
        
        This function must be called once for each 'gimp-image-undo-group-start'
        call that is made.
        
        Parameters:
        
        * image - The ID of the image in which to close an undo group.
        """
        pass

    def gimp_undo_push_group_start(self, image: Gimp.Image=None):
        """Starts a group undo.
        
        This function is used to start a group undo--necessary for logically
        combining two or more undo operations into a single operation.
        This call must be used in conjunction with a
        'gimp-image-undo-group-end' call.
        
        Parameters:
        
        * image - The ID of the image in which to open an undo group.
        """
        pass

    def gimp_unit_get_abbreviation(self, unit_id: Gimp.Unit=None) -> str:
        """Returns the abbreviation of the unit.
        
        This procedure returns the abbreviation of the unit ("in" for inches).
        
        Parameters:
        
        * unit_id (default: 0) - The unit's integer ID.
        
        Returns:
        
        * abbreviation - The unit's abbreviation.
        """
        pass

    def gimp_unit_get_deletion_flag(self, unit_id: Gimp.Unit=None) -> bool:
        """Returns the deletion flag of the unit.
        
        This procedure returns the deletion flag of the unit. If this value is
        TRUE the unit's definition will not be saved in the user's
        unitrc file on gimp exit.
        
        Parameters:
        
        * unit_id (default: 0) - The unit's integer ID.
        
        Returns:
        
        * deletion_flag (default: False) - The unit's deletion flag.
        """
        pass

    def gimp_unit_get_digits(self, unit_id: Gimp.Unit=None) -> int:
        """Returns the number of digits of the unit.
        
        This procedure returns the number of digits you should provide in input
        or output functions to get approximately the same accuracy as
        with two digits and inches. Note that asking for the digits of
        "pixels" will produce an error.
        
        Parameters:
        
        * unit_id (default: 0) - The unit's integer ID.
        
        Returns:
        
        * digits (default: 0) - The unit's number of digits.
        """
        pass

    def gimp_unit_get_factor(self, unit_id: Gimp.Unit=None) -> float:
        """Returns the factor of the unit.
        
        This procedure returns the unit's factor which indicates how many units
        make up an inch. Note that asking for the factor of "pixels"
        will produce an error.
        
        Parameters:
        
        * unit_id (default: 0) - The unit's integer ID.
        
        Returns:
        
        * factor (default: 0.0) - The unit's factor.
        """
        pass

    def gimp_unit_get_identifier(self, unit_id: Gimp.Unit=None) -> str:
        """Returns the textual identifier of the unit.
        
        This procedure returns the textual identifier of the unit. For built-in
        units it will be the english singular form of the unit's name.
        For user-defined units this should equal to the singular form.
        
        Parameters:
        
        * unit_id (default: 0) - The unit's integer ID.
        
        Returns:
        
        * identifier - The unit's textual identifier.
        """
        pass

    def gimp_unit_get_number_of_built_in_units(self) -> int:
        """Returns the number of built-in units.
        
        This procedure returns the number of defined units built-in to GIMP.
        
        Returns:
        
        * num_units (default: 0) - The number of built-in units.
        """
        pass

    def gimp_unit_get_number_of_units(self) -> int:
        """Returns the number of units.
        
        This procedure returns the number of defined units.
        
        Returns:
        
        * num_units (default: 0) - The number of units.
        """
        pass

    def gimp_unit_get_plural(self, unit_id: Gimp.Unit=None) -> str:
        """Returns the plural form of the unit.
        
        This procedure returns the plural form of the unit.
        
        Parameters:
        
        * unit_id (default: 0) - The unit's integer ID.
        
        Returns:
        
        * plural - The unit's plural form.
        """
        pass

    def gimp_unit_get_singular(self, unit_id: Gimp.Unit=None) -> str:
        """Returns the singular form of the unit.
        
        This procedure returns the singular form of the unit.
        
        Parameters:
        
        * unit_id (default: 0) - The unit's integer ID.
        
        Returns:
        
        * singular - The unit's singular form.
        """
        pass

    def gimp_unit_get_symbol(self, unit_id: Gimp.Unit=None) -> str:
        """Returns the symbol of the unit.
        
        This procedure returns the symbol of the unit ("''" for inches).
        
        Parameters:
        
        * unit_id (default: 0) - The unit's integer ID.
        
        Returns:
        
        * symbol - The unit's symbol.
        """
        pass

    def gimp_unit_new(self, identifier: str=None, factor: float=None, digits: int=None, symbol: str=None, abbreviation: str=None, singular: str=None, plural: str=None) -> Gimp.Unit:
        """Creates a new unit and returns it's integer ID.
        
        This procedure creates a new unit and returns it's integer ID. Note that
        the new unit will have it's deletion flag set to TRUE, so you
        will have to set it to FALSE with 'gimp-unit-set-deletion-flag'
        to make it persistent.
        
        Parameters:
        
        * identifier - The new unit's identifier.
        
        * factor (default: 0.0) - The new unit's factor.
        
        * digits (default: 0) - The new unit's digits.
        
        * symbol - The new unit's symbol.
        
        * abbreviation - The new unit's abbreviation.
        
        * singular - The new unit's singular form.
        
        * plural - The new unit's plural form.
        
        Returns:
        
        * unit_id (default: 0) - The new unit's ID.
        """
        pass

    def gimp_unit_set_deletion_flag(self, unit_id: Gimp.Unit=None, deletion_flag: bool=None):
        """Sets the deletion flag of a unit.
        
        This procedure sets the unit's deletion flag. If the deletion flag of a
        unit is TRUE on gimp exit, this unit's definition will not be
        saved in the user's unitrc.
        
        Parameters:
        
        * unit_id (default: 0) - The unit's integer ID.
        
        * deletion_flag (default: False) - The new deletion flag of the unit.
        """
        pass

    def gimp_vectors_bezier_stroke_conicto(self, vectors: Gimp.Vectors=None, stroke_id: int=None, x0: float=None, y0: float=None, x1: float=None, y1: float=None):
        """Extends a bezier stroke with a conic bezier spline.
        
        Extends a bezier stroke with a conic bezier spline. Actually a cubic
        bezier spline gets added that realizes the shape of a conic
        bezier spline.
        
        Parameters:
        
        * vectors - The vectors object.
        
        * stroke_id (default: 0) - The stroke ID.
        
        * x0 (default: 0.0) - The x-coordinate of the control point.
        
        * y0 (default: 0.0) - The y-coordinate of the control point.
        
        * x1 (default: 0.0) - The x-coordinate of the end point.
        
        * y1 (default: 0.0) - The y-coordinate of the end point.
        """
        pass

    def gimp_vectors_bezier_stroke_cubicto(self, vectors: Gimp.Vectors=None, stroke_id: int=None, x0: float=None, y0: float=None, x1: float=None, y1: float=None, x2: float=None, y2: float=None):
        """Extends a bezier stroke with a cubic bezier spline.
        
        Extends a bezier stroke with a cubic bezier spline.
        
        Parameters:
        
        * vectors - The vectors object.
        
        * stroke_id (default: 0) - The stroke ID.
        
        * x0 (default: 0.0) - The x-coordinate of the first control point.
        
        * y0 (default: 0.0) - The y-coordinate of the first control point.
        
        * x1 (default: 0.0) - The x-coordinate of the second control point.
        
        * y1 (default: 0.0) - The y-coordinate of the second control point.
        
        * x2 (default: 0.0) - The x-coordinate of the end point.
        
        * y2 (default: 0.0) - The y-coordinate of the end point.
        """
        pass

    def gimp_vectors_bezier_stroke_lineto(self, vectors: Gimp.Vectors=None, stroke_id: int=None, x0: float=None, y0: float=None):
        """Extends a bezier stroke with a lineto.
        
        Extends a bezier stroke with a lineto.
        
        Parameters:
        
        * vectors - The vectors object.
        
        * stroke_id (default: 0) - The stroke ID.
        
        * x0 (default: 0.0) - The x-coordinate of the lineto.
        
        * y0 (default: 0.0) - The y-coordinate of the lineto.
        """
        pass

    def gimp_vectors_bezier_stroke_new_ellipse(self, vectors: Gimp.Vectors=None, x0: float=None, y0: float=None, radius_x: float=None, radius_y: float=None, angle: float=None) -> int:
        """Adds a bezier stroke describing an ellipse the vectors object.
        
        Adds a bezier stroke describing an ellipse the vectors object.
        
        Parameters:
        
        * vectors - The vectors object.
        
        * x0 (default: 0.0) - The x-coordinate of the center.
        
        * y0 (default: 0.0) - The y-coordinate of the center.
        
        * radius_x (default: 0.0) - The radius in x direction.
        
        * radius_y (default: 0.0) - The radius in y direction.
        
        * angle (default: 0.0) - The angle the x-axis of the ellipse (radians,
          counterclockwise).
        
        Returns:
        
        * stroke_id (default: 0) - The resulting stroke.
        """
        pass

    def gimp_vectors_bezier_stroke_new_moveto(self, vectors: Gimp.Vectors=None, x0: float=None, y0: float=None) -> int:
        """Adds a bezier stroke with a single moveto to the vectors object.
        
        Adds a bezier stroke with a single moveto to the vectors object.
        
        Parameters:
        
        * vectors - The vectors object.
        
        * x0 (default: 0.0) - The x-coordinate of the moveto.
        
        * y0 (default: 0.0) - The y-coordinate of the moveto.
        
        Returns:
        
        * stroke_id (default: 0) - The resulting stroke.
        """
        pass

    def gimp_vectors_copy(self, vectors: Gimp.Vectors=None) -> Gimp.Vectors:
        """Copy a vectors object.
        
        This procedure copies the specified vectors object and returns the copy.
        
        Parameters:
        
        * vectors - The vectors object to copy.
        
        Returns:
        
        * vectors_copy - The newly copied vectors object.
        """
        pass

    def gimp_vectors_export_to_file(self, image: Gimp.Image=None, file: Gio.File=None, vectors: Gimp.Vectors=None):
        """Save a path as an SVG file.
        
        This procedure creates an SVG file to save a Vectors object, that is, a
        path. The resulting file can be edited using a vector graphics
        application, or later reloaded into GIMP. Pass %NULL as the
        'vectors' argument to export all paths in the image.
        
        Parameters:
        
        * image - The image.
        
        * file - The SVG file to create.
        
        * vectors - The vectors object to export, or %NULL for all in the
          image.
        """
        pass

    def gimp_vectors_export_to_string(self, image: Gimp.Image=None, vectors: Gimp.Vectors=None) -> str:
        """Save a path as an SVG string.
        
        This procedure works like 'gimp-vectors-export-to-file' but creates a
        string rather than a file. The string is NULL-terminated and
        holds a complete XML document. Pass %NULL as the 'vectors'
        argument to export all paths in the image.
        
        Parameters:
        
        * image - The image.
        
        * vectors - The vectors object to export, or %NULL for all in the
          image.
        
        Returns:
        
        * string - A string whose contents are a complete SVG document.
        """
        pass

    def gimp_vectors_get_image(self, item: Gimp.Item=None) -> Gimp.Image:
        """Returns the item's image.
        
        This procedure returns the item's image.
        
        Parameters:
        
        * item - The item.
        
        Returns:
        
        * image - The item's image.
        """
        pass

    def gimp_vectors_get_name(self, item: Gimp.Item=None) -> str:
        """Get the name of the specified item.
        
        This procedure returns the specified item's name.
        
        Parameters:
        
        * item - The item.
        
        Returns:
        
        * name - The item name.
        """
        pass

    def gimp_vectors_get_strokes(self, vectors: Gimp.Vectors=None) -> Tuple[int, Gimp.Int32Array]:
        """List the strokes associated with the passed path.
        
        Returns an Array with the stroke-IDs associated with the passed path.
        
        Parameters:
        
        * vectors - The vectors object.
        
        Returns:
        
        * num_strokes (default: 0) - The number of strokes returned.
        
        * stroke_ids - List of the strokes belonging to the path.
        """
        pass

    def gimp_vectors_get_tattoo(self, item: Gimp.Item=None) -> int:
        """Get the tattoo of the specified item.
        
        This procedure returns the specified item's tattoo. A tattoo is a unique
        and permanent identifier attached to a item that can be used to
        uniquely identify a item within an image even between sessions.
        
        Parameters:
        
        * item - The item.
        
        Returns:
        
        * tattoo (default: 1) - The item tattoo.
        """
        pass

    def gimp_vectors_get_visible(self, item: Gimp.Item=None) -> bool:
        """Get the visibility of the specified item.
        
        This procedure returns the specified item's visibility.
        
        Parameters:
        
        * item - The item.
        
        Returns:
        
        * visible (default: False) - The item visibility.
        """
        pass

    def gimp_vectors_import_from_file(self, image: Gimp.Image=None, file: Gio.File=None, merge: bool=None, scale: bool=None) -> Tuple[int, Gimp.ObjectArray]:
        """Import paths from an SVG file.
        
        This procedure imports paths from an SVG file. SVG elements other than
        paths and basic shapes are ignored.
        
        Parameters:
        
        * image - The image.
        
        * file - The SVG file to import.
        
        * merge (default: False) - Merge paths into a single vectors object.
        
        * scale (default: False) - Scale the SVG to image dimensions.
        
        Returns:
        
        * num_vectors (default: 0) - The number of newly created vectors.
        
        * vectors - The list of newly created vectors.
        """
        pass

    def gimp_vectors_import_from_string(self, image: Gimp.Image=None, string: str=None, length: int=None, merge: bool=None, scale: bool=None) -> Tuple[int, Gimp.ObjectArray]:
        """Import paths from an SVG string.
        
        This procedure works like 'gimp-vectors-import-from-file' but takes a
        string rather than reading the SVG from a file. This allows you
        to write scripts that generate SVG and feed it to GIMP.
        
        Parameters:
        
        * image - The image.
        
        * string - A string that must be a complete and valid SVG document.
        
        * length (default: 0) - Number of bytes in string or -1 if the string
          is NULL terminated.
        
        * merge (default: False) - Merge paths into a single vectors object.
        
        * scale (default: False) - Scale the SVG to image dimensions.
        
        Returns:
        
        * num_vectors (default: 0) - The number of newly created vectors.
        
        * vectors - The list of newly created vectors.
        """
        pass

    def gimp_vectors_new(self, image: Gimp.Image=None, name: str=None) -> Gimp.Vectors:
        """Creates a new empty vectors object.
        
        Creates a new empty vectors object. The vectors object needs to be added
        to the image using 'gimp-image-insert-vectors'.
        
        Parameters:
        
        * image - The image.
        
        * name - the name of the new vector object.
        
        Returns:
        
        * vectors - the current vector object, 0 if no vector exists in the
          image.
        """
        pass

    def gimp_vectors_new_from_text_layer(self, image: Gimp.Image=None, layer: Gimp.Layer=None) -> Gimp.Vectors:
        """Creates a new vectors object from a text layer.
        
        Creates a new vectors object from a text layer. The vectors object needs
        to be added to the image using 'gimp-image-insert-vectors'.
        
        Parameters:
        
        * image - The image.
        
        * layer - The text layer.
        
        Returns:
        
        * vectors - The vectors of the text layer.
        """
        pass

    def gimp_vectors_parasite_attach(self, item: Gimp.Item=None, parasite: Gimp.Parasite=None):
        """Add a parasite to an item.
        
        This procedure attaches a parasite to an item. It has no return values.
        
        Parameters:
        
        * item - The item.
        
        * parasite - The parasite to attach to the item.
        """
        pass

    def gimp_vectors_parasite_detach(self, item: Gimp.Item=None, name: str=None):
        """Removes a parasite from an item.
        
        This procedure detaches a parasite from an item. It has no return
        values.
        
        Parameters:
        
        * item - The item.
        
        * name - The name of the parasite to detach from the item.
        """
        pass

    def gimp_vectors_parasite_find(self, item: Gimp.Item=None, name: str=None) -> Gimp.Parasite:
        """Look up a parasite in an item.
        
        Finds and returns the parasite that is attached to an item.
        
        Parameters:
        
        * item - The item.
        
        * name - The name of the parasite to find.
        
        Returns:
        
        * parasite - The found parasite.
        """
        pass

    def gimp_vectors_parasite_list(self, item: Gimp.Item=None) -> List[str]:
        """List all parasites.
        
        Returns a list of all parasites currently attached the an item.
        
        Parameters:
        
        * item - The item.
        
        Returns:
        
        * parasites - The names of currently attached parasites.
        """
        pass

    def gimp_vectors_remove_stroke(self, vectors: Gimp.Vectors=None, stroke_id: int=None):
        """Remove the stroke from a vectors object.
        
        Remove the stroke from a vectors object.
        
        Parameters:
        
        * vectors - The vectors object.
        
        * stroke_id (default: 0) - The stroke ID.
        """
        pass

    def gimp_vectors_set_name(self, item: Gimp.Item=None, name: str=None):
        """Set the name of the specified item.
        
        This procedure sets the specified item's name.
        
        Parameters:
        
        * item - The item.
        
        * name - The new item name.
        """
        pass

    def gimp_vectors_set_tattoo(self, item: Gimp.Item=None, tattoo: int=None):
        """Set the tattoo of the specified item.
        
        This procedure sets the specified item's tattoo. A tattoo is a unique
        and permanent identifier attached to a item that can be used to
        uniquely identify a item within an image even between sessions.
        
        Parameters:
        
        * item - The item.
        
        * tattoo (default: 1) - The new item tattoo.
        """
        pass

    def gimp_vectors_set_visible(self, item: Gimp.Item=None, visible: bool=None):
        """Set the visibility of the specified item.
        
        This procedure sets the specified item's visibility.
        
        Parameters:
        
        * item - The item.
        
        * visible (default: False) - The new item visibility.
        """
        pass

    def gimp_vectors_stroke_close(self, vectors: Gimp.Vectors=None, stroke_id: int=None):
        """Closes the specified stroke.
        
        Closes the specified stroke.
        
        Parameters:
        
        * vectors - The vectors object.
        
        * stroke_id (default: 0) - The stroke ID.
        """
        pass

    def gimp_vectors_stroke_flip(self, vectors: Gimp.Vectors=None, stroke_id: int=None, flip_type: Gimp.OrientationType=None, axis: float=None):
        """Flips the given stroke.
        
        Rotates the given stroke around given center by angle (in degrees).
        
        Parameters:
        
        * vectors - The vectors object.
        
        * stroke_id (default: 0) - The stroke ID.
        
        * flip_type (default: <enum GIMP_ORIENTATION_HORIZONTAL of type
          Gimp.OrientationType>) - Flip orientation, either vertical
          or horizontal.
        
        * axis (default: 0.0) - axis coordinate about which to flip, in
          pixels.
        """
        pass

    def gimp_vectors_stroke_flip_free(self, vectors: Gimp.Vectors=None, stroke_id: int=None, x1: float=None, y1: float=None, x2: float=None, y2: float=None):
        """Flips the given stroke about an arbitrary axis.
        
        Flips the given stroke about an arbitrary axis. Axis is defined by two
        coordinates in the image (in pixels), through which the flipping
        axis passes.
        
        Parameters:
        
        * vectors - The vectors object.
        
        * stroke_id (default: 0) - The stroke ID.
        
        * x1 (default: 0.0) - X coordinate of the first point of the flipping
          axis.
        
        * y1 (default: 0.0) - Y coordinate of the first point of the flipping
          axis.
        
        * x2 (default: 0.0) - X coordinate of the second point of the flipping
          axis.
        
        * y2 (default: 0.0) - Y coordinate of the second point of the flipping
          axis.
        """
        pass

    def gimp_vectors_stroke_get_length(self, vectors: Gimp.Vectors=None, stroke_id: int=None, precision: float=None) -> float:
        """Measure the length of the given stroke.
        
        Measure the length of the given stroke.
        
        Parameters:
        
        * vectors - The vectors object.
        
        * stroke_id (default: 0) - The stroke ID.
        
        * precision (default: 0.1) - The precision used for approximating
          straight portions of the stroke.
        
        Returns:
        
        * length (default: 0.0) - The length (in pixels) of the given stroke.
        """
        pass

    def gimp_vectors_stroke_get_point_at_dist(self, vectors: Gimp.Vectors=None, stroke_id: int=None, dist: float=None, precision: float=None) -> Tuple[float, float, float, bool]:
        """Get point at a specified distance along the stroke.
        
        This will return the x,y position of a point at a given distance along
        the stroke. The distance will be obtained by first digitizing
        the curve internally and then walking along the curve. For a
        closed stroke the start of the path is the first point on the
        path that was created. This might not be obvious. If the stroke
        is not long enough, a "valid" flag will be FALSE.
        
        Parameters:
        
        * vectors - The vectors object.
        
        * stroke_id (default: 0) - The stroke ID.
        
        * dist (default: 0.0) - The given distance.
        
        * precision (default: 0.0) - The precision used for the approximation.
        
        Returns:
        
        * x_point (default: 0.0) - The x position of the point.
        
        * y_point (default: 0.0) - The y position of the point.
        
        * slope (default: 0.0) - The slope (dy / dx) at the specified point.
        
        * valid (default: False) - Indicator for the validity of the returned
          data.
        """
        pass

    def gimp_vectors_stroke_get_points(self, vectors: Gimp.Vectors=None, stroke_id: int=None) -> Tuple[Gimp.VectorsStrokeType, int, Gimp.FloatArray, bool]:
        """Returns the control points of a stroke.
        
        Returns the control points of a stroke. The interpretation of the
        coordinates returned depends on the type of the stroke. For Gimp
        2.4 this is always a bezier stroke, where the coordinates are
        the control points.
        
        Parameters:
        
        * vectors - The vectors object.
        
        * stroke_id (default: 0) - The stroke ID.
        
        Returns:
        
        * type (default: <enum GIMP_VECTORS_STROKE_TYPE_BEZIER of type
          Gimp.VectorsStrokeType>) - type of the stroke (always
          GIMP_VECTORS_STROKE_TYPE_BEZIER for now).
        
        * num_points (default: 0) - The number of floats returned.
        
        * controlpoints - List of the control points for the stroke (x0, y0,
          x1, y1, ...).
        
        * closed (default: False) - Whether the stroke is closed or not.
        """
        pass

    def gimp_vectors_stroke_interpolate(self, vectors: Gimp.Vectors=None, stroke_id: int=None, precision: float=None) -> Tuple[int, Gimp.FloatArray, bool]:
        """Returns polygonal approximation of the stroke.
        
        Returns polygonal approximation of the stroke.
        
        Parameters:
        
        * vectors - The vectors object.
        
        * stroke_id (default: 0) - The stroke ID.
        
        * precision (default: 0.0) - The precision used for the approximation.
        
        Returns:
        
        * num_coords (default: 0) - The number of floats returned.
        
        * coords - List of the coords along the path (x0, y0, x1, y1, ...).
        
        * closed (default: False) - Whether the stroke is closed or not.
        """
        pass

    def gimp_vectors_stroke_new_from_points(self, vectors: Gimp.Vectors=None, type: Gimp.VectorsStrokeType=None, num_points: int=None, controlpoints: Gimp.FloatArray=None, closed: bool=None) -> int:
        """Adds a stroke of a given type to the vectors object.
        
        Adds a stroke of a given type to the vectors object. The coordinates of
        the control points can be specified. For now only strokes of the
        type GIMP_VECTORS_STROKE_TYPE_BEZIER are supported. The control
        points are specified as a pair of float values for the x- and
        y-coordinate. The Bezier stroke type needs a multiple of three
        control points. Each Bezier segment endpoint (anchor, A) has two
        additional control points (C) associated. They are specified in
        the order CACCACCAC...
        
        Parameters:
        
        * vectors - The vectors object.
        
        * type (default: <enum GIMP_VECTORS_STROKE_TYPE_BEZIER of type
          Gimp.VectorsStrokeType>) - type of the stroke (always
          GIMP_VECTORS_STROKE_TYPE_BEZIER for now).
        
        * num_points (default: 0) - The number of elements in the array, i.e.
          the number of controlpoints in the stroke * 2 (x- and
          y-coordinate).
        
        * controlpoints - List of the x- and y-coordinates of the control
          points.
        
        * closed (default: False) - Whether the stroke is to be closed or not.
        
        Returns:
        
        * stroke_id (default: 0) - The stroke ID of the newly created stroke.
        """
        pass

    def gimp_vectors_stroke_reverse(self, vectors: Gimp.Vectors=None, stroke_id: int=None):
        """Reverses the specified stroke.
        
        Reverses the specified stroke.
        
        Parameters:
        
        * vectors - The vectors object.
        
        * stroke_id (default: 0) - The stroke ID.
        """
        pass

    def gimp_vectors_stroke_rotate(self, vectors: Gimp.Vectors=None, stroke_id: int=None, center_x: float=None, center_y: float=None, angle: float=None):
        """Rotates the given stroke.
        
        Rotates the given stroke around given center by angle (in degrees).
        
        Parameters:
        
        * vectors - The vectors object.
        
        * stroke_id (default: 0) - The stroke ID.
        
        * center_x (default: 0.0) - X coordinate of the rotation center.
        
        * center_y (default: 0.0) - Y coordinate of the rotation center.
        
        * angle (default: 0.0) - angle to rotate about.
        """
        pass

    def gimp_vectors_stroke_scale(self, vectors: Gimp.Vectors=None, stroke_id: int=None, scale_x: float=None, scale_y: float=None):
        """Scales the given stroke.
        
        Scale the given stroke.
        
        Parameters:
        
        * vectors - The vectors object.
        
        * stroke_id (default: 0) - The stroke ID.
        
        * scale_x (default: 0.0) - Scale factor in x direction.
        
        * scale_y (default: 0.0) - Scale factor in y direction.
        """
        pass

    def gimp_vectors_stroke_translate(self, vectors: Gimp.Vectors=None, stroke_id: int=None, off_x: float=None, off_y: float=None):
        """Translate the given stroke.
        
        Translate the given stroke.
        
        Parameters:
        
        * vectors - The vectors object.
        
        * stroke_id (default: 0) - The stroke ID.
        
        * off_x (default: 0.0) - Offset in x direction.
        
        * off_y (default: 0.0) - Offset in y direction.
        """
        pass

    def gimp_version(self) -> str:
        """Returns the host GIMP version.
        
        This procedure returns the version number of the currently running GIMP.
        
        Returns:
        
        * version - GIMP version number.
        """
        pass

    def gimp_xcf_load(self, file: Gio.File=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE) -> Gimp.Image:
        """Loads file saved in the .xcf file format.
        
        The XCF file format has been designed specifically for loading and
        saving tiled and layered images in GIMP. This procedure will
        load the specified file.
        
        Parameters:
        
        * file - The file to load.
        
        Returns:
        
        * image - Output image.
        """
        pass

    def gimp_xcf_save(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, file: Gio.File=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Saves file in the .xcf file format.
        
        The XCF file format has been designed specifically for loading and
        saving tiled and layered images in GIMP. This procedure will
        save the specified image in the xcf file format.
        
        Parameters:
        
        * image - Input image.
        
        * num_drawables (default: 0) - Number of drawables.
        
        * drawables - Selected drawables.
        
        * file - The file to save the image in.
        """
        pass

    def gradient_save_as_css(self, gradient: Gimp.Gradient=None, file: Gio.File=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Creates a new palette from a given gradient.
        
        Menu label: Save Gradient as CSS...
        Menu path: <Gradients>
        
        Creates a new palette from a given gradient.
        
        Parameters:
        
        * gradient -
        
        * file -
        """
        pass

    def histogram_export(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, file: Gio.File=None, bucket_size: float=None, sample_average: bool=None, output_format: str=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Exports the image histogram to a text file (CSV).
        
        Image types: *
        Menu label: _Export histogram...
        Menu path: <Image>/Colors/Info
        
        Exports the image histogram to a text file, so that it can be used by
        other programs and loaded into spreadsheets.
        
        The resulting file is a CSV file (Comma Separated Values), which can be
        imported directly in most spreadsheet programs.
        
        The first two columns are the bucket boundaries, followed by the
        selected columns. The histogram refers to the selected image
        area, and can use either Sample Average data or data from the
        current drawable only.;
        
        The output is in "weighted pixels" - meaning all fully transparent
        pixels are not counted.
        
        Check the gimp-histogram call.
        
        Parameters:
        
        * image - The input image.
        
        * num_drawables (default: 1) - Number of input drawables.
        
        * drawables - The input drawables.
        
        * file - Histogram export file.
        
        * bucket_size (default: 0.01) - Bucket Size.
        
        * sample_average (default: False) - Sample Average.
        
        * output_format (default: pixel count) - Output format: 'pixel count',
          'normalized', 'percent'.
        """
        pass

    def plug_in_alienmap2(self, image: Gimp.Image=None, drawable: Gimp.Drawable=None, redfrequency: float=None, redangle: float=None, greenfrequency: float=None, greenangle: float=None, bluefrequency: float=None, blueangle: float=None, colormodel: int=None, redmode: int=None, greenmode: int=None, bluemode: int=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Alter colors in various psychedelic ways.
        
        No help yet. Just try it and you'll see!.
        
        Parameters:
        
        * image - Input image (unused).
        
        * drawable - Input drawable.
        
        * redfrequency (default: 0.0) - Red/hue component frequency factor.
        
        * redangle (default: 0.0) - Red/hue component angle factor (0-360).
        
        * greenfrequency (default: 0.0) - Green/saturation component frequency
          factor.
        
        * greenangle (default: 0.0) - Green/saturation component angle factor
          (0-360).
        
        * bluefrequency (default: 0.0) - Blue/luminance component frequency
          factor.
        
        * blueangle (default: 0.0) - Blue/luminance component angle factor
          (0-360).
        
        * colormodel (default: \x00) - Color model { RGB-MODEL (0), HSL-MODEL (1)
          }.
        
        * redmode (default: \x00) - Red/hue application mode { TRUE, FALSE }.
        
        * greenmode (default: \x00) - Green/saturation application mode { TRUE,
          FALSE }.
        
        * bluemode (default: \x00) - Blue/luminance application mode { TRUE,
          FALSE }.
        """
        pass

    def plug_in_align_layers(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, horizontal_style: int=None, horizontal_base: int=None, vertical_style: int=None, vertical_base: int=None, grid_size: int=None, ignore_bottom_layer: bool=None, use_bottom_layer: bool=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Align all visible layers of the image.
        
        Image types: *
        Menu label: Align Visi_ble Layers...
        Menu path: <Image>/Image/[Arrange]
        
        Align visible layers.
        
        Parameters:
        
        * image - The input image.
        
        * num_drawables (default: 1) - Number of input drawables.
        
        * drawables - The input drawables.
        
        * horizontal_style (default: 0) - (None = 0, Collect = 1, Fill left to
          right = 2, Fill right to left = 3, Snap to grid = 4).
        
        * horizontal_base (default: 0) - (Left edge = 0, Center = 1, Right
          edge = 2).
        
        * vertical_style (default: 0) - (None = 0, Collect = 1, Fill left to
          right = 2, Fill right to left = 3, Snap to grid = 4).
        
        * vertical_base (default: 0) - (Left edge = 0, Center = 1, Right edge
          = 2).
        
        * grid_size (default: 10) - Grid.
        
        * ignore_bottom_layer (default: True) - Ignore the bottom layer even
          if visible.
        
        * use_bottom_layer (default: False) - Use the (invisible) bottom layer
          as the base.
        """
        pass

    def plug_in_animationoptimize(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE) -> Gimp.Image:
        """Modify image to reduce size when saved as GIF animation.
        
        Image types: *
        Menu label: Optimize (for _GIF)
        Menu path: <Image>/Filters/Animation
        
        This procedure applies various optimizations to a GIMP layer-based
        animation in an attempt to reduce the final file size.
        
        If a frame of theanimation can use the 'combine' mode, this procedure
        attempts to maximize the number of ajdacent pixels having the
        same color, whichimproves the compression for some image formats
        such as GIF or MNG.
        
        Parameters:
        
        * image - The input image.
        
        * num_drawables (default: 1) - Number of input drawables.
        
        * drawables - The input drawables.
        
        Returns:
        
        * result - Resultimg image.
        """
        pass

    def plug_in_animationoptimize_diff(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE) -> Gimp.Image:
        """Reduce file size where combining layers is possible.
        
        Image types: *
        Menu label: _Optimize (Difference)
        Menu path: <Image>/Filters/Animation
        
        This procedure applies various optimizations to a GIMP layer-based
        animation in an attempt to reduce the final file size.
        
        If a frame of the animation can use the 'combine' mode, this procedure
        uses a simple difference between the frames.
        
        Parameters:
        
        * image - The input image.
        
        * num_drawables (default: 1) - Number of input drawables.
        
        * drawables - The input drawables.
        
        Returns:
        
        * result - Resultimg image.
        """
        pass

    def plug_in_animationplay(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Preview a GIMP layer-based animation.
        
        Image types: *
        Menu label: _Playback...
        Menu path: <Image>/Filters/Animation
        
        Parameters:
        
        * image - The input image.
        
        * num_drawables (default: 1) - Number of input drawables.
        
        * drawables - The input drawables.
        """
        pass

    def plug_in_animationunoptimize(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE) -> Gimp.Image:
        """Remove optimization to make editing easier.
        
        Image types: *
        Menu label: _Unoptimize
        Menu path: <Image>/Filters/Animation
        
        This procedure 'simplifies' a GIMP layer-based animation that has been
        optimized for animation. This makes editing the animation much
        easier.
        
        Parameters:
        
        * image - The input image.
        
        * num_drawables (default: 1) - Number of input drawables.
        
        * drawables - The input drawables.
        
        Returns:
        
        * result - Resultimg image.
        """
        pass

    def plug_in_antialias(self, image: Gimp.Image=None, drawable: Gimp.Drawable=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Antialias using the Scale3X edge-extrapolation algorithm.
        
        No more help.
        
        Parameters:
        
        * image - Input image (unused).
        
        * drawable - Input drawable.
        """
        pass

    def plug_in_apply_canvas(self, image: Gimp.Image=None, drawable: Gimp.Drawable=None, direction: int=None, depth: int=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Add a canvas texture to the image.
        
        This function applies a canvas texture map to the drawable.
        
        Parameters:
        
        * image - Input image (unused).
        
        * drawable - Input drawable.
        
        * direction (default: 0) - Light direction (0 - 3).
        
        * depth (default: 1) - Texture depth (1 - 50).
        """
        pass

    def plug_in_applylens(self, image: Gimp.Image=None, drawable: Gimp.Drawable=None, refraction: float=None, keep_surroundings: bool=None, set_background: bool=None, set_transparent: bool=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Simulate an elliptical lens over the image.
        
        This plug-in uses Snell's law to draw an ellipsoid lens over the image.
        
        Parameters:
        
        * image - Input image (unused).
        
        * drawable - Input drawable.
        
        * refraction (default: 1.0) - Lens refraction index.
        
        * keep_surroundings (default: False) - Keep lens surroundings.
        
        * set_background (default: False) - Set lens surroundings to BG value.
        
        * set_transparent (default: False) - Set lens surroundings
          transparent.
        """
        pass

    def plug_in_autocrop(self, image: Gimp.Image=None, drawable: Gimp.Drawable=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Remove empty borders from the image.
        
        Remove empty borders from the image.
        
        Parameters:
        
        * image - Input image).
        
        * drawable - Input drawable.
        """
        pass

    def plug_in_autocrop_layer(self, image: Gimp.Image=None, drawable: Gimp.Drawable=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Crop the selected layers based on empty borders of the input
        drawable.
        
        Crop the selected layers of the input "image" based on empty borders of
        the input "drawable".
        
        The input drawable serves as a base for detecting cropping extents
        (transparency or background color), and is not necessarily among
        the cropped layers (the current selected layers).
        
        Parameters:
        
        * image - Input image).
        
        * drawable - Input drawable.
        """
        pass

    def plug_in_autostretch_hsv(self, image: Gimp.Image=None, drawable: Gimp.Drawable=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Stretch contrast to cover the maximum possible range.
        
        This simple plug-in does an automatic contrast stretch. For each channel
        in the image, it finds the minimum and maximum values... it uses
        those values to stretch the individual histograms to the full
        contrast range. For some images it may do just what you want;
        for others it may be total crap :). This version differs from
        Contrast Autostretch in that it works in HSV space, and
        preserves hue.
        
        Parameters:
        
        * image - Input image (unused).
        
        * drawable - Input drawable.
        """
        pass

    def plug_in_blinds(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, angle_displacement: int=None, num_segments: int=None, orientation: int=None, bg_transparent: bool=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Simulate an image painted on window blinds.
        
        Image types: RGB*, GRAY*
        Menu label: _Blinds...
        Menu path: <Image>/Filters/Distorts
        
        More here later.
        
        Parameters:
        
        * image - The input image.
        
        * num_drawables (default: 1) - Number of input drawables.
        
        * drawables - The input drawables.
        
        * angle_displacement (default: 30) - Angle of Displacement.
        
        * num_segments (default: 3) - Number of segments in blinds.
        
        * orientation (default: 0) - The orientation.
        
        * bg_transparent (default: False) - Background transparent.
        """
        pass

    def plug_in_borderaverage(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, thickness: int=None, bucket_exponent: int=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE) -> Gimp.RGB:
        """Set foreground to the average color of the image border.
        
        Image types: RGB*
        Menu label: _Border Average...
        Menu path: <Image>/Colors/Info
        
        Parameters:
        
        * image - The input image.
        
        * num_drawables (default: 1) - Number of input drawables.
        
        * drawables - The input drawables.
        
        * thickness (default: 3) - Border size to take in count.
        
        * bucket_exponent (default: 4) - Bits for bucket size (default=4: 16
          Levels).
        
        Returns:
        
        * borderaverage - The average color of the specified border.
        """
        pass

    def plug_in_bump_map(self, image: Gimp.Image=None, drawable: Gimp.Drawable=None, bumpmap: Gimp.Drawable=None, azimuth: float=None, elevation: float=None, depth: int=None, xofs: int=None, yofs: int=None, waterlevel: float=None, ambient: float=None, compensate: bool=None, invert: bool=None, type: int=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Create an embossing effect using a bump map.
        
        This plug-in uses the algorithm described by John Schlag, "Fast
        Embossing Effects on Raster Image Data" in Graphics GEMS IV
        (ISBN 0-12-336155-9). It takes a drawable to be applied as a
        bump map to another image and produces a nice embossing effect.
        
        Parameters:
        
        * image - Input image (unused).
        
        * drawable - Input drawable.
        
        * bumpmap - Bump map drawable.
        
        * azimuth (default: 0.0) - Azimuth.
        
        * elevation (default: 0.5) - Elevation.
        
        * depth (default: 1) - Depth.
        
        * xofs (default: 0) - X offset.
        
        * yofs (default: 0) - Y offset.
        
        * waterlevel (default: 0.0) - Level that full transparency should
          represent.
        
        * ambient (default: 0.0) - Ambient lighting factor.
        
        * compensate (default: False) - Compensate for darkening.
        
        * invert (default: False) - Invert bumpmap.
        
        * type (default: 0) - Type of map { LINEAR (0), SPHERICAL (1),
          SINUSOIDAL (2) }.
        """
        pass

    def plug_in_bump_map_tiled(self, image: Gimp.Image=None, drawable: Gimp.Drawable=None, bumpmap: Gimp.Drawable=None, azimuth: float=None, elevation: float=None, depth: int=None, xofs: int=None, yofs: int=None, waterlevel: float=None, ambient: float=None, compensate: bool=None, invert: bool=None, type: int=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Create an embossing effect using a tiled image as a bump map.
        
        This plug-in uses the algorithm described by John Schlag, "Fast
        Embossing Effects on Raster Image Data" in Graphics GEMS IV
        (ISBN 0-12-336155-9). It takes a drawable to be tiled and
        applied as a bump map to another image and produces a nice
        embossing effect.
        
        Parameters:
        
        * image - Input image (unused).
        
        * drawable - Input drawable.
        
        * bumpmap - Bump map drawable.
        
        * azimuth (default: 0.0) - Azimuth.
        
        * elevation (default: 0.5) - Elevation.
        
        * depth (default: 1) - Depth.
        
        * xofs (default: 0) - X offset.
        
        * yofs (default: 0) - Y offset.
        
        * waterlevel (default: 0.0) - Level that full transparency should
          represent.
        
        * ambient (default: 0.0) - Ambient lighting factor.
        
        * compensate (default: False) - Compensate for darkening.
        
        * invert (default: False) - Invert bumpmap.
        
        * type (default: 0) - Type of map { LINEAR (0), SPHERICAL (1),
          SINUSOIDAL (2) }.
        """
        pass

    def plug_in_busy_dialog(self, read_fd: int=None, write_fd: int=None, message: str=None, cancelable: bool=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Show a dialog while waiting for an operation to finish.
        
        Used by GIMP to display a dialog, containing a spinner and a custom
        message, while waiting for an ongoing operation to finish.
        Optionally, the dialog may provide a "Cancel" button, which can
        be used to cancel the operation.
        
        Parameters:
        
        * read_fd (default: 0) - The read file descriptor.
        
        * write_fd (default: 0) - The write file descriptor.
        
        * message - The message.
        
        * cancelable (default: False) - Whether the dialog is cancelable.
        """
        pass

    def plug_in_c_astretch(self, image: Gimp.Image=None, drawable: Gimp.Drawable=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Stretch contrast to cover the maximum possible range.
        
        This simple plug-in does an automatic contrast stretch. For each channel
        in the image, it finds the minimum and maximum values... it uses
        those values to stretch the individual histograms to the full
        contrast range. For some images it may do just what you want;
        for others it may not work that well.
        
        Parameters:
        
        * image - Input image (unused).
        
        * drawable - Input drawable.
        """
        pass

    def plug_in_cartoon(self, image: Gimp.Image=None, drawable: Gimp.Drawable=None, mask_radius: float=None, pct_black: float=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Simulate a cartoon by enhancing edges.
        
        Propagates dark values in an image based on each pixel's relative
        darkness to a neighboring average. The idea behind this filter
        is to give the look of a black felt pen drawing subsequently
        shaded with color. This is achieved by darkening areas of the
        image which are measured to be darker than a neighborhood
        average. In this way, sufficiently large shifts in intensity are
        darkened to black. The rate at which they are darkened to black
        is determined by the second pct_black parameter. The mask_radius
        parameter controls the size of the pixel neighborhood over which
        the average intensity is computed and then compared to each
        pixel in the neighborhood to decide whether or not to darken it
        to black. Large values for mask_radius result in very thick
        black areas bordering the shaded regions of color and much less
        detail for black areas everywhere including inside regions of
        color. Small values result in more subtle pen strokes and detail
        everywhere. Small values for the pct_black make the blend from
        the color regions to the black border lines smoother and the
        lines themselves thinner and less noticeable; larger values
        achieve the opposite effect.
        
        Parameters:
        
        * image - Input image (unused).
        
        * drawable - Input drawable.
        
        * mask_radius (default: 1.0) - Cartoon mask radius (radius of pixel
          neighborhood).
        
        * pct_black (default: 0.0) - Percentage of darkened pixels to set to
          black.
        """
        pass

    def plug_in_checkerboard(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, psychobily: bool=None, check_size: int=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Create a checkerboard pattern.
        
        Image types: RGB*, GRAY*
        Menu label: _Checkerboard (legacy)...
        Menu path: <Image>/Filters/Render/Pattern
        
        More here later.
        
        Parameters:
        
        * image - The input image.
        
        * num_drawables (default: 1) - Number of input drawables.
        
        * drawables - The input drawables.
        
        * psychobily (default: False) - Render a psychobilly checkerboard.
        
        * check_size (default: 10) - Size of the checks.
        """
        pass

    def plug_in_cml_explorer(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, parameter_file: Gio.File=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Create abstract Coupled-Map Lattice patterns.
        
        Image types: RGB*, GRAY*
        Menu label: CML _Explorer...
        Menu path: <Image>/Filters/Render/Pattern
        
        Make an image of Coupled-Map Lattice (CML). CML is a kind of Cellular
        Automata on continuous (value) domain. In
        GIMP_RUN_NONINTERACTIVE, the name of a parameter file is passed
        as the 4th arg. You can control CML_explorer via parameter file.
        
        Parameters:
        
        * image - The input image.
        
        * num_drawables (default: 1) - Number of input drawables.
        
        * drawables - The input drawables.
        
        * parameter_file - The parameter file from which CML_explorer makes an
          image. This argument is only used in non-interactive runs.
        """
        pass

    def plug_in_colormap_remap(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, map: GLib.Bytes=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Rearrange the colormap.
        
        Image types: INDEXED*
        Menu label: R_earrange Colormap...
        Menu paths: <Image>/Colors/Map/[Colormap], <Colormap>
        
        This procedure takes an indexed image and lets you alter the positions
        of colors in the colormap without visually changing the image.
        
        Parameters:
        
        * image - The input image.
        
        * num_drawables (default: 1) - Number of input drawables.
        
        * drawables - The input drawables.
        
        * map - Remap array for the colormap.
        """
        pass

    def plug_in_colormap_swap(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, index1: int=None, index2: int=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Swap two colors in the colormap.
        
        Image types: INDEXED*
        Menu label: _Swap Colors
        
        This procedure takes an indexed image and lets you swap the positions of
        two colors in the colormap without visually changing the image.
        
        Parameters:
        
        * image - The input image.
        
        * num_drawables (default: 1) - Number of input drawables.
        
        * drawables - The input drawables.
        
        * index1 (default: 0) - First index in the colormap.
        
        * index2 (default: 0) - Second (other) index in the colormap.
        """
        pass

    def plug_in_colors_channel_mixer(self, image: Gimp.Image=None, drawable: Gimp.Drawable=None, monochrome: int=None, rr_gain: float=None, rg_gain: float=None, rb_gain: float=None, gr_gain: float=None, gg_gain: float=None, gb_gain: float=None, br_gain: float=None, bg_gain: float=None, bb_gain: float=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Alter colors by mixing RGB Channels.
        
        This plug-in mixes the RGB channels.
        
        Parameters:
        
        * image - Input image (unused).
        
        * drawable - Input drawable.
        
        * monochrome (default: 0) - Monochrome { TRUE, FALSE }.
        
        * rr_gain (default: -2.0) - Set the red gain for the red channel.
        
        * rg_gain (default: -2.0) - Set the green gain for the red channel.
        
        * rb_gain (default: -2.0) - Set the blue gain for the red channel.
        
        * gr_gain (default: -2.0) - Set the red gain for the green channel.
        
        * gg_gain (default: -2.0) - Set the green gain for the green channel.
        
        * gb_gain (default: -2.0) - Set the blue gain for the green channel.
        
        * br_gain (default: -2.0) - Set the red gain for the blue channel.
        
        * bg_gain (default: -2.0) - Set the green gain for the blue channel.
        
        * bb_gain (default: -2.0) - Set the blue gain for the blue channel.
        """
        pass

    def plug_in_colortoalpha(self, image: Gimp.Image=None, drawable: Gimp.Drawable=None, color: Gimp.RGB=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Convert a specified color to transparency.
        
        This replaces as much of a given color as possible in each pixel with a
        corresponding amount of alpha, then readjusts the color
        accordingly.
        
        Parameters:
        
        * image - Input image (unused).
        
        * drawable - Input drawable.
        
        * color - Color to remove.
        """
        pass

    def plug_in_compose(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, image_2: Gimp.Image=None, image_3: Gimp.Image=None, image_4: Gimp.Image=None, compose_type: str=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE) -> Gimp.Image:
        """Create an image using multiple gray images as color channels.
        
        Image types: GRAY*
        Menu label: C_ompose...
        Menu path: <Image>/Colors/Components
        
        This function creates a new image from multiple gray images.
        
        Parameters:
        
        * image - The input image.
        
        * num_drawables (default: 1) - Number of input drawables.
        
        * drawables - The input drawables.
        
        * image_2 - Second input image.
        
        * image_3 - Third input image.
        
        * image_4 - Fourth input image.
        
        * compose_type - What to compose: "RGB", "RGBA", "HSV", "HSL", "CMYK",
          "LAB", "LCH", "YCbCr_ITU_R470", "YCbCr_ITU_R709",
          "YCbCr_ITU_R470_256", "YCbCr_ITU_R709_256".
        
        Returns:
        
        * new_image - Output image.
        """
        pass

    def plug_in_convmatrix(self, image: Gimp.Image=None, drawable: Gimp.Drawable=None, argc_matrix: int=None, matrix: Gimp.FloatArray=None, alpha_alg: bool=None, divisor: float=None, offset: float=None, argc_channels: int=None, channels: Gimp.Int32Array=None, bmode: int=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Apply a generic 5x5 convolution matrix.
        
        Apply a generic 5x5 convolution matrix.
        
        Parameters:
        
        * image - Input image (unused).
        
        * drawable - Input drawable.
        
        * argc_matrix (default: 0) - The number of elements in the following
          array, must always be 25.
        
        * matrix - The 5x5 convolution matrix.
        
        * alpha_alg (default: False) - Enable weighting by alpha channel.
        
        * divisor (default: 0.0) - Divisor.
        
        * offset (default: 0.0) - Offset.
        
        * argc_channels (default: 0) - The number of elements in following
          array, must always be 5.
        
        * channels - Mask of the channels to be filtered.
        
        * bmode (default: 0) - Mode for treating image borders { EXTEND (0),
          WRAP (1), CLEAR (2) }.
        """
        pass

    def plug_in_cubism(self, image: Gimp.Image=None, drawable: Gimp.Drawable=None, tile_size: float=None, tile_saturation: float=None, bg_color: int=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Convert the image into randomly rotated square blobs.
        
        Convert the image into randomly rotated square blobs.
        
        Parameters:
        
        * image - Input image (unused).
        
        * drawable - Input drawable.
        
        * tile_size (default: 0.0) - Average diameter of each tile (in
          pixels).
        
        * tile_saturation (default: 0.0) - Expand tiles by this amount.
        
        * bg_color (default: 0) - Background color { BLACK (0), BG (1) }.
        """
        pass

    def plug_in_curve_bend(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, rotation: float=None, smoothing: bool=None, antialias: bool=None, work_on_copy: bool=None, curve_type: int=None, curve_border: int=None, argc_upper_point_x: int=None, upper_point_x: Gimp.FloatArray=None, argc_upper_point_y: int=None, upper_point_y: Gimp.FloatArray=None, argc_lower_point_x: int=None, lower_point_x: Gimp.FloatArray=None, argc_lower_point_y: int=None, lower_point_y: Gimp.FloatArray=None, upper_val_y: GLib.Bytes=None, lower_val_y: GLib.Bytes=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE) -> Gimp.Layer:
        """Bend the image using two control curves.
        
        Image types: RGB*, GRAY*
        Menu label: _Curve Bend...
        Menu path: <Image>/Filters/Distorts
        
        This plug-in bends the active layer. If there is a current selection it
        is copied to floating selection and the curve_bend distortion is
        done on the floating selection. If work_on_copy parameter is
        TRUE, the curve_bend distortion is done on a copy of the active
        layer (or floating selection). The upper and lower edges are
        bent in shape of 2 spline curves. Both (upper and lower) curves
        are determined by up to 17 points or by 256 Y-Values if
        curve_type == 1 (freehand mode). If rotation is not 0, the layer
        is rotated before and rotated back after the bend operation.
        This enables bending in other directions than vertical. Bending
        usually changes the size of the handled layer. This plug-in sets
        the offsets of the handled layer to keep its center at the same
        position.
        
        Parameters:
        
        * image - The input image.
        
        * num_drawables (default: 1) - Number of input drawables.
        
        * drawables - The input drawables.
        
        * rotation (default: 0.0) - Direction {angle 0 to 360 degree } of the
          bend effect.
        
        * smoothing (default: True) - Smoothing.
        
        * antialias (default: True) - Antialias.
        
        * work_on_copy (default: False) - Copy the drawable and bend the copy.
        
        * curve_type (default: 0) - { 0 == smooth (use 17 points), 1 ==
          freehand (use 256 val_y) }.
        
        * curve_border (default: 0) - Choose the active border line to edit.
        
        * argc_upper_point_x (default: 2) - Argc upper point X.
        
        * upper_point_x - Array of 17 x point coords { 0.0 <= x <= 1.0 or -1
          for unused point }.
        
        * argc_upper_point_y (default: 2) - Argc upper point Y.
        
        * upper_point_y - Array of 17 y point coords { 0.0 <= y <= 1.0 or -1
          for unused point }.
        
        * argc_lower_point_x (default: 2) - Argc lower point X.
        
        * lower_point_x - Array of 17 x point coords { 0.0 <= x <= 1.0 or -1
          for unused point }.
        
        * argc_lower_point_y (default: 2) - Argc lower point Y.
        
        * lower_point_y - Array of 17 y point coords { 0.0 <= y <= 1.0 or -1
          for unused point }.
        
        * upper_val_y - Array of 256 y freehand coords { 0 <= y <= 255 }.
        
        * lower_val_y - Array of 256 y freehand coords { 0 <= y <= 255 }.
        
        Returns:
        
        * bent_layer - The transformed layer.
        """
        pass

    def plug_in_dbbrowser(self, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """List available procedures in the PDB.
        
        Menu label: Procedure _Browser
        Menu path: <Image>/Help/[Programming]
        """
        pass

    def plug_in_decompose(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, decompose_type: str=None, layers_mode: bool=None, use_registration: bool=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE) -> Tuple[Gimp.Image, Gimp.Image, Gimp.Image, Gimp.Image]:
        """Decompose an image into separate colorspace components.
        
        Image types: RGB*
        Menu label: _Decompose...
        Menu path: <Image>/Colors/Components
        
        This function creates new gray images with different channel information
        in each of them.
        
        Parameters:
        
        * image - The input image.
        
        * num_drawables (default: 1) - Number of input drawables.
        
        * drawables - The input drawables.
        
        * decompose_type (default: RGB) - What to decompose: "RGB", "RGBA",
          "Red", "Green", "Blue", "Alpha", "HSV", "Hue", "Saturation",
          "Value", "HSL", "Hue (HSL)", "Saturation (HSL)",
          "Lightness", "CMYK", "Cyan", "Magenta", "Yellow", "Black",
          "LAB", "LCH", "YCbCr_ITU_R470", "YCbCr_ITU_R470_256",
          "YCbCr_ITU_R709", "YCbCr_ITU_R709_256".
        
        * layers_mode (default: True) - Create channels as layers in a single
          image.
        
        * use_registration (default: False) - When enabled, pixels in the
          foreground color will appear black in all output images.
          This can be used for things like crop marks that have to
          show up on all channels.
        
        Returns:
        
        * new_image_1 - Output gray image 1.
        
        * new_image_2 - Output gray image 2 (N/A for single channel extract).
        
        * new_image_3 - Output gray image 3 (N/A for single channel extract).
        
        * new_image_4 - Output gray image 4 (N/A for single channel extract).
        """
        pass

    def plug_in_deinterlace(self, image: Gimp.Image=None, drawable: Gimp.Drawable=None, evenodd: int=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Fix images where every other row is missing.
        
        Deinterlace is useful for processing images from video capture cards.
        When only the odd or even fields get captured, deinterlace can
        be used to interpolate between the existing fields to correct
        this.
        
        Parameters:
        
        * image - Input image (unused).
        
        * drawable - Input drawable.
        
        * evenodd (default: 0) - Which lines to keep { KEEP-ODD (0), KEEP-EVEN
          (1).
        """
        pass

    def plug_in_depth_merge(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, source_1: Gimp.Drawable=None, depth_map_1: Gimp.Drawable=None, source_2: Gimp.Drawable=None, depth_map_2: Gimp.Drawable=None, overlap: float=None, offset: float=None, scale_1: float=None, scale_2: float=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Combine two images using depth maps (z-buffers).
        
        Image types: RGB*, GRAY*
        Menu label: _Depth Merge...
        Menu path: <Image>/Filters/Combine
        
        Taking as input two full-color, full-alpha images and two corresponding
        grayscale depth maps, this plug-in combines the images based on
        which is closer (has a lower depth map value) at each point.
        
        Parameters:
        
        * image - The input image.
        
        * num_drawables (default: 1) - Number of input drawables.
        
        * drawables - The input drawables.
        
        * source_1 - Source 1.
        
        * depth_map_1 - Depth map 1.
        
        * source_2 - Source 2.
        
        * depth_map_2 - Depth map 2.
        
        * overlap (default: 0.0) - Overlap.
        
        * offset (default: 0.0) - Depth relative offset.
        
        * scale_1 (default: 1.0) - Depth relative scale 1.
        
        * scale_2 (default: 1.0) - Depth relative scale 2.
        """
        pass

    def plug_in_despeckle(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, radius: int=None, type: int=None, black: int=None, white: int=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Remove speckle noise from the image.
        
        Image types: RGB*, GRAY*
        Menu label: Des_peckle...
        Menu path: <Image>/Filters/Enhance
        
        This plug-in selectively performs a median or adaptive box filter on an
        image.
        
        Parameters:
        
        * image - The input image.
        
        * num_drawables (default: 1) - Number of input drawables.
        
        * drawables - The input drawables.
        
        * radius (default: 3) - Filter box radius.
        
        * type (default: 1) - Filter type { MEDIAN (0), ADAPTIVE (1),
          RECURSIVE-MEDIAN (2), RECURSIVE-ADAPTIVE (3) }.
        
        * black (default: 7) - Black level.
        
        * white (default: 248) - White level.
        """
        pass

    def plug_in_destripe(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, avg_width: int=None, create_histogram: bool=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Remove vertical stripe artifacts from the image.
        
        Image types: RGB*, GRAY*
        Menu label: Des_tripe...
        Menu path: <Image>/Colors/Tone Mapping
        
        This plug-in tries to remove vertical stripes from an image.
        
        Parameters:
        
        * image - The input image.
        
        * num_drawables (default: 1) - Number of input drawables.
        
        * drawables - The input drawables.
        
        * avg_width (default: 36) - Averaging filter width.
        
        * create_histogram (default: False) - Output a histogram.
        """
        pass

    def plug_in_diffraction(self, image: Gimp.Image=None, drawable: Gimp.Drawable=None, lam_r: float=None, lam_g: float=None, lam_b: float=None, contour_r: float=None, contour_g: float=None, contour_b: float=None, edges_r: float=None, edges_g: float=None, edges_b: float=None, brightness: float=None, scattering: float=None, polarization: float=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Generate diffraction patterns.
        
        Help? What help?.
        
        Parameters:
        
        * image - Input image (unused).
        
        * drawable - Input drawable.
        
        * lam_r (default: 0.0) - Light frequency (red).
        
        * lam_g (default: 0.0) - Light frequency (green).
        
        * lam_b (default: 0.0) - Light frequency (blue).
        
        * contour_r (default: 0.0) - Number of contours (red).
        
        * contour_g (default: 0.0) - Number of contours (green).
        
        * contour_b (default: 0.0) - Number of contours (blue).
        
        * edges_r (default: 0.0) - Number of sharp edges (red).
        
        * edges_g (default: 0.0) - Number of sharp edges (green).
        
        * edges_b (default: 0.0) - Number of sharp edges (blue).
        
        * brightness (default: 0.0) - Brightness and shifting/fattening of
          contours.
        
        * scattering (default: 0.0) - Scattering (Speed vs. quality).
        
        * polarization (default: -1.0) - Polarization.
        """
        pass

    def plug_in_dilate(self, image: Gimp.Image=None, drawable: Gimp.Drawable=None, propagate_mode: int=None, propagating_channel: int=None, propagating_rate: float=None, direction_mask: int=None, lower_limit: int=None, upper_limit: int=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Grow lighter areas of the image.
        
        Dilate image.
        
        Parameters:
        
        * image - Input image (unused).
        
        * drawable - Input drawable.
        
        * propagate_mode (default: 0) - Propagate mode { 0:white, 1:black,
          2:middle value 3:foreground to peak, 4:foreground,
          5:background, 6:opaque, 7:transparent }.
        
        * propagating_channel (default: 0) - Channels which values are
          propagated.
        
        * propagating_rate (default: 0.0) - Propagating rate.
        
        * direction_mask (default: 0) - Direction mask.
        
        * lower_limit (default: 0) - Lower limit.
        
        * upper_limit (default: 0) - Upper limit.
        """
        pass

    def plug_in_displace(self, image: Gimp.Image=None, drawable: Gimp.Drawable=None, amount_x: float=None, amount_y: float=None, do_x: bool=None, do_y: bool=None, displace_map_x: Gimp.Drawable=None, displace_map_y: Gimp.Drawable=None, displace_type: int=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Displace pixels as indicated by displacement maps.
        
        Displaces the contents of the specified drawable by the amounts
        specified by 'amount-x' and 'amount-y' multiplied by the
        luminance of corresponding pixels in the 'displace-map'
        drawables.
        
        Parameters:
        
        * image - Input image (unused).
        
        * drawable - Input drawable.
        
        * amount_x (default: -500.0) - Displace multiplier for x direction.
        
        * amount_y (default: -500.0) - Displace multiplier for y direction.
        
        * do_x (default: False) - Displace in x direction ?.
        
        * do_y (default: False) - Displace in y direction ?.
        
        * displace_map_x - Displacement map for x direction.
        
        * displace_map_y - Displacement map for y direction.
        
        * displace_type (default: 1) - Edge behavior { WRAP (1), SMEAR (2),
          BLACK (3) }.
        """
        pass

    def plug_in_displace_polar(self, image: Gimp.Image=None, drawable: Gimp.Drawable=None, amount_x: float=None, amount_y: float=None, do_x: bool=None, do_y: bool=None, displace_map_x: Gimp.Drawable=None, displace_map_y: Gimp.Drawable=None, displace_type: int=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Displace pixels as indicated by displacement maps.
        
        Just like plug-in-displace but working in polar coordinates. The
        drawable is whirled and pinched according to the map.
        
        Parameters:
        
        * image - Input image (unused).
        
        * drawable - Input drawable.
        
        * amount_x (default: -500.0) - Displace multiplier for radial
          direction.
        
        * amount_y (default: -500.0) - Displace multiplier for tangent
          direction.
        
        * do_x (default: False) - Displace in radial direction ?.
        
        * do_y (default: False) - Displace in tangent direction ?.
        
        * displace_map_x - Displacement map for radial direction.
        
        * displace_map_y - Displacement map for tangent direction.
        
        * displace_type (default: 1) - Edge behavior { WRAP (1), SMEAR (2),
          BLACK (3) }.
        """
        pass

    def plug_in_dog(self, image: Gimp.Image=None, drawable: Gimp.Drawable=None, inner: float=None, outer: float=None, normalize: bool=None, invert: bool=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Edge detection with control of edge thickness.
        
        Applies two Gaussian blurs to the drawable, and subtracts the results.
        This is robust and widely used method for detecting edges.
        
        Parameters:
        
        * image - Input image (unused).
        
        * drawable - Input drawable.
        
        * inner (default: 0.0) - Radius of inner gaussian blur in pixels.
        
        * outer (default: 0.0) - Radius of outer gaussian blur in pixels.
        
        * normalize (default: False) - Normalize.
        
        * invert (default: False) - Invert.
        """
        pass

    def plug_in_drawable_compose(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, drawable_2: Gimp.Drawable=None, drawable_3: Gimp.Drawable=None, drawable_4: Gimp.Drawable=None, compose_type: str=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE) -> Gimp.Image:
        """Compose an image from multiple drawables of gray images.
        
        Image types: GRAY*
        
        This function creates a new image from multiple drawables of gray
        images.
        
        Parameters:
        
        * image - The input image.
        
        * num_drawables (default: 1) - Number of input drawables.
        
        * drawables - The input drawables.
        
        * drawable_2 - Second input drawable.
        
        * drawable_3 - Third input drawable.
        
        * drawable_4 - Fourth input drawable.
        
        * compose_type - What to compose: "RGB", "RGBA", "HSV", "HSL", "CMYK",
          "LAB", "LCH", "YCbCr_ITU_R470", "YCbCr_ITU_R709",
          "YCbCr_ITU_R470_256", "YCbCr_ITU_R709_256".
        
        Returns:
        
        * new_image - Output image.
        """
        pass

    def plug_in_edge(self, image: Gimp.Image=None, drawable: Gimp.Drawable=None, amount: float=None, warpmode: int=None, edgemode: int=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Several simple methods for detecting edges.
        
        Perform edge detection on the contents of the specified drawable. AMOUNT
        is an arbitrary constant, WRAPMODE is like displace plug-in
        (useful for tileable image). EDGEMODE sets the kind of matrix
        transform applied to the pixels, SOBEL was the method used in
        older versions.
        
        Parameters:
        
        * image - Input image (unused).
        
        * drawable - Input drawable.
        
        * amount (default: 1.0) - Edge detection amount.
        
        * warpmode (default: 0) - Edge detection behavior { NONE (0), WRAP
          (1), SMEAR (2), BLACK (3) }.
        
        * edgemode (default: 0) - Edge detection algorithm { SOBEL (0),
          PREWITT (1), GRADIENT (2), ROBERTS (3), DIFFERENTIAL (4),
          LAPLACE (5) }.
        """
        pass

    def plug_in_emboss(self, image: Gimp.Image=None, drawable: Gimp.Drawable=None, azimuth: float=None, elevation: float=None, depth: int=None, emboss: bool=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Simulate an image created by embossing.
        
        Emboss or Bumpmap the given drawable, specifying the angle and elevation
        for the light source.
        
        Parameters:
        
        * image - Input image (unused).
        
        * drawable - Input drawable.
        
        * azimuth (default: 0.0) - The Light Angle (degrees).
        
        * elevation (default: 0.0) - The Elevation Angle (degrees).
        
        * depth (default: 1) - The Filter Width.
        
        * emboss (default: False) - Emboss (TRUE), Bumpmap (FALSE).
        """
        pass

    def plug_in_engrave(self, image: Gimp.Image=None, drawable: Gimp.Drawable=None, height: int=None, limit: bool=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Simulate an antique engraving.
        
        Creates a black-and-white 'engraved' version of an image as seen in old
        illustrations.
        
        Parameters:
        
        * image - Input image (unused).
        
        * drawable - Input drawable.
        
        * height (default: 2) - Resolution in pixels.
        
        * limit (default: False) - Limit line width.
        """
        pass

    def plug_in_erode(self, image: Gimp.Image=None, drawable: Gimp.Drawable=None, propagate_mode: int=None, propagating_channel: int=None, propagating_rate: float=None, direction_mask: int=None, lower_limit: int=None, upper_limit: int=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Shrink lighter areas of the image.
        
        Erode image.
        
        Parameters:
        
        * image - Input image (unused).
        
        * drawable - Input drawable.
        
        * propagate_mode (default: 0) - Propagate mode { 0:white, 1:black,
          2:middle value 3:foreground to peak, 4:foreground,
          5:background, 6:opaque, 7:transparent }.
        
        * propagating_channel (default: 0) - Channels which values are
          propagated.
        
        * propagating_rate (default: 0.0) - Propagating rate.
        
        * direction_mask (default: 0) - Direction mask.
        
        * lower_limit (default: 0) - Lower limit.
        
        * upper_limit (default: 0) - Upper limit.
        """
        pass

    def plug_in_exchange(self, image: Gimp.Image=None, drawable: Gimp.Drawable=None, from_red: int=None, from_green: int=None, from_blue: int=None, to_red: int=None, to_green: int=None, to_blue: int=None, red_threshold: int=None, green_threshold: int=None, blue_threshold: int=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Swap one color with another.
        
        Exchange one color with another, optionally setting a threshold to
        convert from one shade to another.
        
        Parameters:
        
        * image - Input image (unused).
        
        * drawable - Input drawable.
        
        * from_red (default: \x00) - Red value (from).
        
        * from_green (default: \x00) - Green value (from).
        
        * from_blue (default: \x00) - Blue value (from).
        
        * to_red (default: \x00) - Red value (to).
        
        * to_green (default: \x00) - Green value (to).
        
        * to_blue (default: \x00) - Blue value (to).
        
        * red_threshold (default: \x00) - Red threshold.
        
        * green_threshold (default: \x00) - Green threshold.
        
        * blue_threshold (default: \x00) - Blue threshold.
        """
        pass

    def plug_in_film(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, film_height: int=None, film_color: Gegl.Color=None, number_start: int=None, number_font: Gimp.Font=None, number_color: Gegl.Color=None, at_top: bool=None, at_bottom: bool=None, images: Gimp.ObjectArray=None, picture_height: float=None, picture_spacing: float=None, hole_offset: float=None, hole_width: float=None, hole_height: float=None, hole_spacing: float=None, number_height: float=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE) -> Gimp.Image:
        """Combine several images on a film strip.
        
        Image types: *
        Menu label: _Filmstrip...
        Menu path: <Image>/Filters/Combine
        
        Compose several images to a roll film.
        
        Parameters:
        
        * image - The input image.
        
        * num_drawables (default: 1) - Number of input drawables.
        
        * drawables - The input drawables.
        
        * film_height (default: 0) - Height of film (0: fit to images).
        
        * film_color - Color of the film.
        
        * number_start (default: 1) - Start index for numbering.
        
        * number_font - Font for drawing numbers.
        
        * number_color - Color for numbers.
        
        * at_top (default: True) - Draw numbers at top.
        
        * at_bottom (default: True) - Draw numbers at bottom.
        
        * images - Images to be used for film.
        
        * picture_height (default: 0.695) - As fraction of the strip height.
        
        * picture_spacing (default: 0.04) - The spacing between 2 images, as
          fraction of the strip height.
        
        * hole_offset (default: 0.058) - The offset from the edge of film, as
          fraction of the strip height.
        
        * hole_width (default: 0.052) - The width of the holes, as fraction of
          the strip height.
        
        * hole_height (default: 0.081) - The height of the holes, as fraction
          of the strip height.
        
        * hole_spacing (default: 0.081) - The distance between holes, as
          fraction of the strip height.
        
        * number_height (default: 0.052) - The height of drawn numbers, as
          fraction of the strip height.
        
        Returns:
        
        * new_image - Output image.
        """
        pass

    def plug_in_flame(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, brightness: float=None, contrast: float=None, gamma: float=None, sample_density: float=None, spatial_oversample: int=None, spatial_filter_radius: float=None, zoom: float=None, x: float=None, y: float=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Create cosmic recursive fractal flames.
        
        Image types: RGB*
        Menu label: _Flame...
        Menu path: <Image>/Filters/Render/Fractals
        
        Create cosmic recursive fractal flames.
        
        Parameters:
        
        * image - The input image.
        
        * num_drawables (default: 1) - Number of input drawables.
        
        * drawables - The input drawables.
        
        * brightness (default: 1.0) -
        
        * contrast (default: 1.0) -
        
        * gamma (default: 1.0) -
        
        * sample_density (default: 5.0) -
        
        * spatial_oversample (default: 2) -
        
        * spatial_filter_radius (default: 0.75) -
        
        * zoom (default: 0.0) -
        
        * x (default: 0.0) -
        
        * y (default: 0.0) -
        """
        pass

    def plug_in_flarefx(self, image: Gimp.Image=None, drawable: Gimp.Drawable=None, pos_x: int=None, pos_y: int=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Add a lens flare effect.
        
        Adds a lens flare effects. Makes your image look like it was snapped
        with a cheap camera with a lot of lens :).
        
        Parameters:
        
        * image - Input image (unused).
        
        * drawable - Input drawable.
        
        * pos_x (default: 0) - X-Position.
        
        * pos_y (default: 0) - Y-Position.
        """
        pass

    def plug_in_fractal_trace(self, image: Gimp.Image=None, drawable: Gimp.Drawable=None, xmin: float=None, xmax: float=None, ymin: float=None, ymax: float=None, depth: int=None, outside_type: int=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Transform image with the Mandelbrot Fractal.
        
        Transform image with the Mandelbrot Fractal.
        
        Parameters:
        
        * image - Input image (unused).
        
        * drawable - Input drawable.
        
        * xmin (default: -50.0) - xmin fractal image delimiter.
        
        * xmax (default: -50.0) - xmax fractal image delimiter.
        
        * ymin (default: -50.0) - ymin fractal image delimiter.
        
        * ymax (default: -50.0) - ymax fractal image delimiter.
        
        * depth (default: 1) - Trace depth.
        
        * outside_type (default: 0) - Outside type { WRAP (0), TRANS (1),
          BLACK (2), WHITE (3) }.
        """
        pass

    def plug_in_fractalexplorer(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, fractal_type: str=None, xmin: float=None, xmax: float=None, ymin: float=None, ymax: float=None, iter: float=None, cx: float=None, cy: float=None, color_mode: int=None, red_stretch: float=None, green_stretch: float=None, blue_stretch: float=None, red_mode: str=None, green_mode: str=None, blue_mode: str=None, red_invert: bool=None, green_invert: bool=None, blue_invert: bool=None, n_colors: int=None, use_loglog_smoothing: bool=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Render fractal art.
        
        Image types: RGB*, GRAY*
        Menu label: _Fractal Explorer...
        Menu path: <Image>/Filters/Render/Fractals
        
        No help yet.
        
        Parameters:
        
        * image - The input image.
        
        * num_drawables (default: 1) - Number of input drawables.
        
        * drawables - The input drawables.
        
        * fractal_type - Type of Fractal Pattern.
        
        * xmin (default: -2.0) - X min fractal image delimiter.
        
        * xmax (default: 2.0) - X max fractal image delimiter.
        
        * ymin (default: -1.5) - Y min fractal image delimiter.
        
        * ymax (default: 1.5) - Y max fractal image delimiter.
        
        * iter (default: 50.0) - Iteration value.
        
        * cx (default: -0.75) - cx value.
        
        * cy (default: -0.2) - cy value.
        
        * color_mode (default: 0) - 0: Apply colormap as specified by the
          parameters below; 1: Apply active gradient to final image.
        
        * red_stretch (default: 1.0) - Red stretching factor.
        
        * green_stretch (default: 1.0) - Green stretching factor.
        
        * blue_stretch (default: 1.0) - Blue stretching factor.
        
        * red_mode - Red application mode.
        
        * green_mode - Green application mode.
        
        * blue_mode - Blue application mode.
        
        * red_invert (default: False) - Red inversion mode.
        
        * green_invert (default: False) - Green inversion mode.
        
        * blue_invert (default: False) - Blue inversion mode.
        
        * n_colors (default: 512) - Number of Colors for mapping.
        
        * use_loglog_smoothing (default: False) - Use log log smoothing to
          eliminate "banding" in the result.
        """
        pass

    def plug_in_gauss(self, image: Gimp.Image=None, drawable: Gimp.Drawable=None, horizontal: float=None, vertical: float=None, method: int=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Simplest, most commonly used way of blurring.
        
        Applies a gaussian blur to the drawable, with specified radius of
        affect. The standard deviation of the normal distribution used
        to modify pixel values is calculated based on the supplied
        radius. Horizontal and vertical blurring can be independently
        invoked by specifying only one to run. The 'method' parameter is
        ignored.
        
        Parameters:
        
        * image - Input image (unused).
        
        * drawable - Input drawable.
        
        * horizontal (default: 0.0) - Horizontal radius of gaussian blur (in
          pixels.
        
        * vertical (default: 0.0) - Vertical radius of gaussian blur (in
          pixels.
        
        * method (default: 0) - Blur method { IIR (0), RLE (1) }.
        """
        pass

    def plug_in_gauss_iir(self, image: Gimp.Image=None, drawable: Gimp.Drawable=None, radius: float=None, horizontal: bool=None, vertical: bool=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Apply a gaussian blur.
        
        Applies a gaussian blur to the drawable, with specified radius of
        affect. The standard deviation of the normal distribution used
        to modify pixel values is calculated based on the supplied
        radius. Horizontal and vertical blurring can be independently
        invoked by specifying only one to run.
        
        Parameters:
        
        * image - Input image (unused).
        
        * drawable - Input drawable.
        
        * radius (default: 0.0) - Radius of gaussian blur (in pixels.
        
        * horizontal (default: False) - Blur in horizontal direction.
        
        * vertical (default: False) - Blur in vertical direction.
        """
        pass

    def plug_in_gauss_iir2(self, image: Gimp.Image=None, drawable: Gimp.Drawable=None, horizontal: float=None, vertical: float=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Apply a gaussian blur.
        
        Applies a gaussian blur to the drawable, with specified radius of
        affect. The standard deviation of the normal distribution used
        to modify pixel values is calculated based on the supplied
        radius. Horizontal and vertical blurring can be independently
        invoked by specifying only one to run.
        
        Parameters:
        
        * image - Input image (unused).
        
        * drawable - Input drawable.
        
        * horizontal (default: 0.0) - Horizontal radius of gaussian blur (in
          pixels.
        
        * vertical (default: 0.0) - Vertical radius of gaussian blur (in
          pixels.
        """
        pass

    def plug_in_gauss_rle(self, image: Gimp.Image=None, drawable: Gimp.Drawable=None, radius: float=None, horizontal: bool=None, vertical: bool=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Apply a gaussian blur.
        
        Applies a gaussian blur to the drawable, with specified radius of
        affect. The standard deviation of the normal distribution used
        to modify pixel values is calculated based on the supplied
        radius. Horizontal and vertical blurring can be independently
        invoked by specifying only one to run.
        
        Parameters:
        
        * image - Input image (unused).
        
        * drawable - Input drawable.
        
        * radius (default: 0.0) - Radius of gaussian blur (in pixels.
        
        * horizontal (default: False) - Blur in horizontal direction.
        
        * vertical (default: False) - Blur in vertical direction.
        """
        pass

    def plug_in_gauss_rle2(self, image: Gimp.Image=None, drawable: Gimp.Drawable=None, horizontal: float=None, vertical: float=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Apply a gaussian blur.
        
        Applies a gaussian blur to the drawable, with specified radius of
        affect. The standard deviation of the normal distribution used
        to modify pixel values is calculated based on the supplied
        radius. Horizontal and vertical blurring can be independently
        invoked by specifying only one to run.
        
        Parameters:
        
        * image - Input image (unused).
        
        * drawable - Input drawable.
        
        * horizontal (default: 0.0) - Horizontal radius of gaussian blur (in
          pixels.
        
        * vertical (default: 0.0) - Vertical radius of gaussian blur (in
          pixels.
        """
        pass

    def plug_in_gfig(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Create geometric shapes.
        
        Image types: RGB*, GRAY*
        Menu label: _Gfig...
        Menu path: <Image>/Filters/Render
        
        Draw Vector Graphics and paint them onto your images. Gfig allows you to
        draw many types of objects including Lines, Circles, Ellipses,
        Curves, Polygons, pointed stars, Bezier curves, and Spirals.
        Objects can be painted using Brushes or other tools or filled
        using colors or patterns. Gfig objects can also be used to
        create selections.
        
        Parameters:
        
        * image - The input image.
        
        * num_drawables (default: 1) - Number of input drawables.
        
        * drawables - The input drawables.
        """
        pass

    def plug_in_gflare(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, gflare_name: str=None, center_x: int=None, center_y: int=None, radius: float=None, rotation: float=None, hue: float=None, vector_angle: float=None, vector_length: float=None, use_asupsample: bool=None, asupsample_max_depth: int=None, asupsample_threshold: float=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Produce a lense flare effect using gradients.
        
        Image types: RGB*, GRAY*
        Menu label: _Gradient Flare...
        Menu path: <Image>/Filters/Light and Shadow/[Light]
        
        This plug-in produces a lense flare effect using custom gradients. In
        interactive call, the user can edit their own favorite lense
        flare (GFlare) and render it. Edited gflare is saved
        automatically to the folder in gflare-path, if it is defined in
        gimprc. In non-interactive call, the user can only render one of
        GFlare which has been stored in gflare-path already.
        
        Parameters:
        
        * image - The input image.
        
        * num_drawables (default: 1) - Number of input drawables.
        
        * drawables - The input drawables.
        
        * gflare_name (default: Default) - Name of the GFlare to render.
        
        * center_x (default: 128) - X coordinate of center of GFlare.
        
        * center_y (default: 128) - Y coordinate of center of GFlare.
        
        * radius (default: 100.0) - Radius of GFlare (pixel).
        
        * rotation (default: 0.0) - Rotation of GFlare (degree).
        
        * hue (default: 0.0) - Hue rotation of GFlare (degree).
        
        * vector_angle (default: 60.0) - Vector angle for second flares
          (degree).
        
        * vector_length (default: 400.0) - Vector length for second flares
          (percentage of Radius).
        
        * use_asupsample (default: False) - Use adaptive supersampling while
          rendering.
        
        * asupsample_max_depth (default: 3) - Max depth for adaptive
          supersampling.
        
        * asupsample_threshold (default: 0.2) - Threshold for adaptive
          supersampling.
        """
        pass

    def plug_in_gimpressionist(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, preset: str=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Performs various artistic operations.
        
        Image types: RGB*, GRAY*
        Menu label: _GIMPressionist...
        Menu path: <Image>/Filters/Artistic
        
        Performs various artistic operations on an image.
        
        Parameters:
        
        * image - The input image.
        
        * num_drawables (default: 1) - Number of input drawables.
        
        * drawables - The input drawables.
        
        * preset - Preset Name.
        """
        pass

    def plug_in_glasstile(self, image: Gimp.Image=None, drawable: Gimp.Drawable=None, tilex: int=None, tiley: int=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Simulate distortion caused by square glass tiles.
        
        Divide the image into square glassblocks in which the image is
        refracted.
        
        Parameters:
        
        * image - Input image (unused).
        
        * drawable - Input drawable.
        
        * tilex (default: 10) - Tile width.
        
        * tiley (default: 10) - Tile height.
        """
        pass

    def plug_in_goat_exercise_c(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Exercise a goat in the C language.
        
        Image types: *
        Menu label: Exercise in _C minor
        Menu path: <Image>/Filters/Development/Goat exercises
        
        Takes a goat for a walk.
        
        Parameters:
        
        * image - The input image.
        
        * num_drawables (default: 1) - Number of input drawables.
        
        * drawables - The input drawables.
        """
        pass

    def plug_in_goat_exercise_lua(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Exercise a goat in the Lua language.
        
        Image types: *
        Menu label: Exercise a Lua goat
        Menu path: <Image>/Filters/Development/Goat exercises
        
        Takes a goat for a walk in Lua.
        
        Parameters:
        
        * image - The input image.
        
        * num_drawables (default: 1) - Number of input drawables.
        
        * drawables - The input drawables.
        """
        pass

    def plug_in_goat_exercise_python(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Exercise a goat in the Python 3 language.
        
        Image types: *
        Menu label: Exercise a goat and a python
        Menu path: <Image>/Filters/Development/Goat exercises
        
        Takes a goat for a walk in Python 3.
        
        Parameters:
        
        * image - The input image.
        
        * num_drawables (default: 1) - Number of input drawables.
        
        * drawables - The input drawables.
        """
        pass

    def plug_in_goat_exercise_vala(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Exercise a goat in the Vala language.
        
        Image types: RGB*, INDEXED*, GRAY*
        Menu label: Exercise a Vala goat
        Menu path: <Image>/Filters/Development/Goat exercises
        
        Takes a goat for a walk in Vala.
        
        Parameters:
        
        * image - The input image.
        
        * num_drawables (default: 1) - Number of input drawables.
        
        * drawables - The input drawables.
        """
        pass

    def plug_in_gradmap(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Recolor the image using colors from the active gradient.
        
        Image types: RGB*, GRAY*
        Menu label: _Gradient Map
        Menu path: <Image>/Colors/Map
        
        This plug-in maps the contents of the specified drawable with active
        gradient. It calculates luminosity of each pixel and replaces
        the pixel by the sample of active gradient at the position
        proportional to that luminosity. Complete black pixel becomes
        the leftmost color of the gradient, and complete white becomes
        the rightmost. Works on both Grayscale and RGB image
        with/without alpha channel.
        
        Parameters:
        
        * image - The input image.
        
        * num_drawables (default: 1) - Number of input drawables.
        
        * drawables - The input drawables.
        """
        pass

    def plug_in_grid(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, hwidth: int=None, hspace: int=None, hoffset: int=None, hcolor: Gegl.Color=None, vwidth: int=None, vspace: int=None, voffset: int=None, vcolor: Gegl.Color=None, iwidth: int=None, ispace: int=None, ioffset: int=None, icolor: Gegl.Color=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Draw a grid on the image.
        
        Image types: *
        Menu label: _Grid (legacy)...
        Menu path: <Image>/Filters/Render/Pattern
        
        Draws a grid using the specified colors. The grid origin is the upper
        left corner.
        
        Parameters:
        
        * image - The input image.
        
        * num_drawables (default: 1) - Number of input drawables.
        
        * drawables - The input drawables.
        
        * hwidth (default: 1) - Horizontal width.
        
        * hspace (default: 16) - Horizontal spacing.
        
        * hoffset (default: 8) - Horizontal offset.
        
        * hcolor - Horizontal color.
        
        * vwidth (default: 1) - Vertical width.
        
        * vspace (default: 16) - Vertical spacing.
        
        * voffset (default: 8) - Vertical offset.
        
        * vcolor - Vertical color.
        
        * iwidth (default: 0) - Intersection width.
        
        * ispace (default: 2) - Intersection spacing.
        
        * ioffset (default: 6) - Intersection offset.
        
        * icolor - Intersection color.
        """
        pass

    def plug_in_guillotine(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE) -> Tuple[int, Gimp.ObjectArray]:
        """Slice the image into subimages using guides.
        
        Image types: *
        Menu label: Slice Using G_uides
        Menu path: <Image>/Image/[Crop]
        
        This function takes an image and slices it along its guides, creating
        new images. The original image is not modified.
        
        Parameters:
        
        * image - The input image.
        
        * num_drawables (default: 1) - Number of input drawables.
        
        * drawables - The input drawables.
        
        Returns:
        
        * image_count (default: 0) - Number of images created.
        
        * images - Output images.
        """
        pass

    def plug_in_hot(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, mode: int=None, action: int=None, new_layer: bool=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Find and fix pixels that may be unsafely bright.
        
        Image types: RGB
        Menu label: _Hot...
        Menu path: <Image>/Colors/[Modify]
        
        Hot scans an image for pixels that will give unsave values of
        chrominance or composite signale amplitude when encoded into an
        NTSC or PAL signal. Three actions can be performed on these
        'hot' pixels. (0) reduce luminance, (1) reduce saturation, or
        (2) Blacken.
        
        Parameters:
        
        * image - The input image.
        
        * num_drawables (default: 1) - Number of input drawables.
        
        * drawables - The input drawables.
        
        * mode (default: 0) - Mode { NTSC (0), PAL (1) }.
        
        * action (default: 0) - Action { (0) reduce luminance, (1) reduce
          saturation, or (2) Blacken }.
        
        * new_layer (default: True) - Create a new layer.
        """
        pass

    def plug_in_hsv_noise(self, image: Gimp.Image=None, drawable: Gimp.Drawable=None, holdness: int=None, hue_distance: int=None, saturation_distance: int=None, value_distance: int=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Randomize hue, saturation and value independently.
        
        Scattering pixel values in HSV space.
        
        Parameters:
        
        * image - Input image (unused).
        
        * drawable - Input drawable.
        
        * holdness (default: 1) - Convolution strength.
        
        * hue_distance (default: 0) - Scattering of hue angle.
        
        * saturation_distance (default: 0) - Distribution distance on
          saturation axis.
        
        * value_distance (default: 0) - Distribution distance on value axis.
        """
        pass

    def plug_in_ifscompose(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Create an Iterated Function System (IFS) fractal.
        
        Image types: *
        Menu label: _IFS Fractal...
        Menu path: <Image>/Filters/Render/Fractals
        
        Interactively create an Iterated Function System fractal. Use the window
        on the upper left to adjustthe component transformations of the
        fractal. The operation that is performed is selected by the
        buttons underneath the window, or from a menu popped up by the
        right mouse button. The fractal will be rendered with a
        transparent background if the current image has an alpha
        channel.
        
        Parameters:
        
        * image - The input image.
        
        * num_drawables (default: 1) - Number of input drawables.
        
        * drawables - The input drawables.
        """
        pass

    def plug_in_illusion(self, image: Gimp.Image=None, drawable: Gimp.Drawable=None, division: int=None, type: int=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Superimpose many altered copies of the image.
        
        Produce illusion.
        
        Parameters:
        
        * image - Input image (unused).
        
        * drawable - Input drawable.
        
        * division (default: 0) - The number of divisions.
        
        * type (default: 0) - Illusion type { TYPE1 (0), TYPE2 (1) }.
        """
        pass

    def plug_in_imagemap(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Create a clickable imagemap.
        
        Image types: *
        Menu label: _Image Map...
        Menu path: <Image>/Filters/Web
        
        Parameters:
        
        * image - The input image.
        
        * num_drawables (default: 1) - Number of input drawables.
        
        * drawables - The input drawables.
        """
        pass

    def plug_in_jigsaw(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, x: int=None, y: int=None, style: int=None, blend_lines: int=None, blend_amount: float=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Add a jigsaw-puzzle pattern to the image.
        
        Image types: RGB*
        Menu label: _Jigsaw...
        Menu path: <Image>/Filters/Render/Pattern
        
        Jigsaw puzzle look.
        
        Parameters:
        
        * image - The input image.
        
        * num_drawables (default: 1) - Number of input drawables.
        
        * drawables - The input drawables.
        
        * x (default: 5) - Number of pieces going across.
        
        * y (default: 5) - Number of pieces going down.
        
        * style (default: 0) - The style/shape of the jigsaw puzzle { Square
          (0), Curved (1) }.
        
        * blend_lines (default: 3) - Degree of slope of each piece's edge.
        
        * blend_amount (default: 0.5) - The amount of highlighting on the
          edges of each piece.
        """
        pass

    def plug_in_laplace(self, image: Gimp.Image=None, drawable: Gimp.Drawable=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """High-resolution edge detection.
        
        This plug-in creates one-pixel wide edges from the image, with the value
        proportional to the gradient. It uses the Laplace operator (a
        3x3 kernel with -8 in the middle). The image has to be
        laplacered to get useful results, a gauss_iir with 1.5 - 5.0
        depending on the noise in the image is best.
        
        Parameters:
        
        * image - Input image (unused).
        
        * drawable - Input drawable.
        """
        pass

    def plug_in_lens_distortion(self, image: Gimp.Image=None, drawable: Gimp.Drawable=None, offset_x: float=None, offset_y: float=None, main_adjust: float=None, edge_adjust: float=None, rescale: float=None, brighten: float=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Corrects lens distortion.
        
        Corrects barrel or pincushion lens distortion.
        
        Parameters:
        
        * image - Input image (unused).
        
        * drawable - Input drawable.
        
        * offset_x (default: -100.0) - Effect centre offset in X.
        
        * offset_y (default: -100.0) - Effect centre offset in Y.
        
        * main_adjust (default: -100.0) - Amount of second-order distortion.
        
        * edge_adjust (default: -100.0) - Amount of fourth-order distortion.
        
        * rescale (default: -100.0) - Rescale overall image size.
        
        * brighten (default: -100.0) - Adjust brightness in corners.
        """
        pass

    def plug_in_lic(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, effect_channel: str=None, effect_operator: str=None, effect_convolve: str=None, effect_image: Gimp.Drawable=None, filter_length: float=None, noise_magnitude: float=None, integration_steps: float=None, min_value: float=None, max_value: float=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Special effects that nobody understands.
        
        Image types: RGB*
        Menu label: _Van Gogh (LIC)...
        Menu path: <Image>/Filters/Artistic
        
        No help yet.
        
        Parameters:
        
        * image - The input image.
        
        * num_drawables (default: 1) - Number of input drawables.
        
        * drawables - The input drawables.
        
        * effect_channel - Effect Channel.
        
        * effect_operator - Effect Operator.
        
        * effect_convolve - Convolve.
        
        * effect_image - Effect image.
        
        * filter_length (default: 5.0) - Filter length.
        
        * noise_magnitude (default: 2.0) - Noise Magnitude.
        
        * integration_steps (default: 25.0) - Integration steps.
        
        * min_value (default: -25.0) - Minimum value.
        
        * max_value (default: 25.0) - Maximum value.
        """
        pass

    def plug_in_lighting(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, bump_drawable: Gimp.Drawable=None, env_drawable: Gimp.Drawable=None, do_bumpmap: bool=None, do_envmap: bool=None, bumpmap_type: str=None, bumpmap_max_height: float=None, light_type_1: str=None, light_color_1: Gegl.Color=None, light_intensity_1: float=None, light_position_x_1: float=None, light_position_y_1: float=None, light_position_z_1: float=None, light_direction_x_1: float=None, light_direction_y_1: float=None, light_direction_z_1: float=None, ambient_intensity: float=None, diffuse_intensity: float=None, diffuse_reflectivity: float=None, specular_reflectivity: float=None, highlight: float=None, metallic: bool=None, antialiasing: bool=None, new_image: bool=None, transparent_background: bool=None, distance: float=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Apply various lighting effects to an image.
        
        Image types: RGB*
        Menu label: _Lighting Effects...
        Menu path: <Image>/Filters/Light and Shadow/[Light]
        
        No help yet.
        
        Parameters:
        
        * image - The input image.
        
        * num_drawables (default: 1) - Number of input drawables.
        
        * drawables - The input drawables.
        
        * bump_drawable - Bumpmap drawable (set to NULL if disabled).
        
        * env_drawable - Environmentmap drawable (set to NULL if disabled).
        
        * do_bumpmap (default: True) - Enable bumpmapping.
        
        * do_envmap (default: True) - Enable envmapping.
        
        * bumpmap_type - Type of mapping.
        
        * bumpmap_max_height (default: 0.1) - The maximum height of the
          bumpmap.
        
        * light_type_1 - Type of light source.
        
        * light_color_1 - Light source color.
        
        * light_intensity_1 (default: 1.0) - Light source intensity.
        
        * light_position_x_1 (default: -1.0) - Light source position (x,y,z).
        
        * light_position_y_1 (default: -1.0) - Light source position (x,y,z).
        
        * light_position_z_1 (default: 1.0) - Light source position (x,y,z).
        
        * light_direction_x_1 (default: -1.0) - Light source direction
          (x,y,z).
        
        * light_direction_y_1 (default: -1.0) - Light source direction
          (x,y,z).
        
        * light_direction_z_1 (default: 1.0) - Light source direction (x,y,z).
        
        * ambient_intensity (default: 0.2) - Material ambient intensity
          (Glowing).
        
        * diffuse_intensity (default: 0.5) - Material diffuse intensity
          (Bright).
        
        * diffuse_reflectivity (default: 0.4) - Material diffuse reflectivity.
        
        * specular_reflectivity (default: 0.5) - Material specular
          reflectivity.
        
        * highlight (default: 27.0) - Material highlight (note, it's
          exponential) (Polished).
        
        * metallic (default: False) - Make surfaces look metallic.
        
        * antialiasing (default: False) - Apply antialiasing.
        
        * new_image (default: False) - Create a new image.
        
        * transparent_background (default: False) - Make background
          transparent.
        
        * distance (default: 0.25) - Distance of observer from surface.
        """
        pass

    def plug_in_make_seamless(self, image: Gimp.Image=None, drawable: Gimp.Drawable=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Alters edges to make the image seamlessly tileable.
        
        This plug-in creates a seamless tileable from the input drawable.
        
        Parameters:
        
        * image - Input image (unused).
        
        * drawable - Input drawable.
        """
        pass

    def plug_in_map_object(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, map_type: str=None, viewpoint_x: float=None, viewpoint_y: float=None, viewpoint_z: float=None, position_x: float=None, position_y: float=None, position_z: float=None, first_axis_x: float=None, first_axis_y: float=None, first_axis_z: float=None, second_axis_x: float=None, second_axis_y: float=None, second_axis_z: float=None, rotation_angle_x: float=None, rotation_angle_y: float=None, rotation_angle_z: float=None, light_type: str=None, light_color: Gegl.Color=None, light_position_x: float=None, light_position_y: float=None, light_position_z: float=None, light_direction_x: float=None, light_direction_y: float=None, light_direction_z: float=None, ambient_intensity: float=None, diffuse_intensity: float=None, diffuse_reflectivity: float=None, specular_reflectivity: float=None, highlight: float=None, antialiasing: bool=None, depth: float=None, threshold: float=None, tiled: bool=None, new_image: bool=None, new_layer: bool=None, transparent_background: bool=None, sphere_radius: float=None, box_front_drawable: Gimp.Drawable=None, box_back_drawable: Gimp.Drawable=None, box_top_drawable: Gimp.Drawable=None, box_bottom_drawable: Gimp.Drawable=None, box_left_drawable: Gimp.Drawable=None, box_right_drawable: Gimp.Drawable=None, x_scale: float=None, y_scale: float=None, z_scale: float=None, cyl_top_drawable: Gimp.Drawable=None, cyl_bottom_drawable: Gimp.Drawable=None, cylinder_radius: float=None, cylinder_length: float=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Map the image to an object (plane, sphere, box or cylinder).
        
        Image types: RGB*
        Menu label: Map _Object...
        Menu path: <Image>/Filters/Map
        
        No help yet.
        
        Parameters:
        
        * image - The input image.
        
        * num_drawables (default: 1) - Number of input drawables.
        
        * drawables - The input drawables.
        
        * map_type - Type of mapping.
        
        * viewpoint_x (default: 0.5) - Position of viewpoint (x,y,z).
        
        * viewpoint_y (default: 0.5) - Position of viewpoint (x,y,z).
        
        * viewpoint_z (default: 2.0) - Position of viewpoint (x,y,z).
        
        * position_x (default: 0.5) - Object position (x,y,z).
        
        * position_y (default: 0.5) - Object position (x,y,z).
        
        * position_z (default: 0.0) - Object position (x,y,z).
        
        * first_axis_x (default: 1.0) - First axis of object (x,y,z).
        
        * first_axis_y (default: 0.0) - First axis of object (x,y,z).
        
        * first_axis_z (default: 0.0) - First axis of object (x,y,z).
        
        * second_axis_x (default: 0.0) - Second axis of object (x,y,z).
        
        * second_axis_y (default: 1.0) - Second axis of object (x,y,z).
        
        * second_axis_z (default: 0.0) - Second axis of object (x,y,z).
        
        * rotation_angle_x (default: 0.0) - Rotation about X axis in degrees.
        
        * rotation_angle_y (default: 0.0) - Rotation about Y axis in degrees.
        
        * rotation_angle_z (default: 0.0) - Rotation about Z axis in degrees.
        
        * light_type - Type of lightsource.
        
        * light_color - Light source color.
        
        * light_position_x (default: -0.5) - Light source position (x,y,z).
        
        * light_position_y (default: -0.5) - Light source position (x,y,z).
        
        * light_position_z (default: 2.0) - Light source position (x,y,z).
        
        * light_direction_x (default: -1.0) - Light source direction (x,y,z).
        
        * light_direction_y (default: -1.0) - Light source direction (x,y,z).
        
        * light_direction_z (default: 1.0) - Light source direction (x,y,z).
        
        * ambient_intensity (default: 0.3) - Material ambient intensity.
        
        * diffuse_intensity (default: 1.0) - Material diffuse intensity.
        
        * diffuse_reflectivity (default: 0.5) - Material diffuse reflectivity.
        
        * specular_reflectivity (default: 0.5) - Material specular
          reflectivity.
        
        * highlight (default: 27.0) - Material highlight (note, it's
          exponential).
        
        * antialiasing (default: True) - Apply antialiasing.
        
        * depth (default: 3.0) - Antialiasing quality. Higher is better, but
          slower.
        
        * threshold (default: 0.25) - Stop when pixel differences are smaller
          than this value.
        
        * tiled (default: False) - Tile source image.
        
        * new_image (default: False) - Create a new image.
        
        * new_layer (default: False) - Create a new layer when applying
          filter.
        
        * transparent_background (default: False) - Make background
          transparent.
        
        * sphere_radius (default: 0.25) - Sphere radius.
        
        * box_front_drawable - Box front face (set this to NULL if not used).
        
        * box_back_drawable - Box back face.
        
        * box_top_drawable - Box top face.
        
        * box_bottom_drawable - Box bottom face.
        
        * box_left_drawable - Box left face.
        
        * box_right_drawable - Box right face.
        
        * x_scale (default: 0.5) - Box X size.
        
        * y_scale (default: 0.5) - Box Y size.
        
        * z_scale (default: 0.5) - Box Z size.
        
        * cyl_top_drawable - Cylinder top face (set this to NULL if not used).
        
        * cyl_bottom_drawable - Cylinder bottom face (set this to NULL if not
          used).
        
        * cylinder_radius (default: 0.25) - Cylinder radius.
        
        * cylinder_length (default: 0.25) - Cylinder length.
        """
        pass

    def plug_in_maze(self, image: Gimp.Image=None, drawable: Gimp.Drawable=None, width: int=None, height: int=None, tileable: int=None, algorithm: int=None, seed: int=None, multiple: int=None, offset: int=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Draw a labyrinth.
        
        Generates a maze using either the depth-first search method or Prim's
        algorithm. Can make tileable mazes too.
        
        Parameters:
        
        * image - Input image (unused).
        
        * drawable - Input drawable.
        
        * width (default: 1) - Width of the passages.
        
        * height (default: 1) - Height of the passages.
        
        * tileable (default: \x00) - Tileable maze? (TRUE or FALSE).
        
        * algorithm (default: \x00) - Generation algorithm (0 = DEPTH FIRST, 1 =
          PRIM'S ALGORITHM).
        
        * seed (default: 0) - Random Seed.
        
        * multiple (default: 0) - Multiple (use 57).
        
        * offset (default: 0) - Offset (use 1).
        """
        pass

    def plug_in_mblur(self, image: Gimp.Image=None, drawable: Gimp.Drawable=None, type: int=None, length: float=None, angle: float=None, center_x: float=None, center_y: float=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Simulate movement using directional blur.
        
        This plug-in simulates the effect seen when photographing a moving
        object at a slow shutter speed. Done by adding multiple
        displaced copies.
        
        Parameters:
        
        * image - Input image (unused).
        
        * drawable - Input drawable.
        
        * type (default: 0) - Type of motion blur { LINEAR (0), RADIAL (1),
          ZOOM (2) }.
        
        * length (default: 0.0) - Length.
        
        * angle (default: 0.0) - Angle.
        
        * center_x (default: 0.0) - Center X.
        
        * center_y (default: 0.0) - Center Y.
        """
        pass

    def plug_in_mblur_inward(self, image: Gimp.Image=None, drawable: Gimp.Drawable=None, type: int=None, length: float=None, angle: float=None, center_x: float=None, center_y: float=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Simulate movement using directional blur.
        
        This procedure is equivalent to plug-in-mblur but performs the zoom blur
        inward instead of outward.
        
        Parameters:
        
        * image - Input image (unused).
        
        * drawable - Input drawable.
        
        * type (default: 0) - Type of motion blur { LINEAR (0), RADIAL (1),
          ZOOM (2) }.
        
        * length (default: 0.0) - Length.
        
        * angle (default: 0.0) - Angle.
        
        * center_x (default: 0.0) - Center X.
        
        * center_y (default: 0.0) - Center Y.
        """
        pass

    def plug_in_median_blur(self, image: Gimp.Image=None, drawable: Gimp.Drawable=None, radius: int=None, percentile: float=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Blur using the median color near each pixel.
        
        Blur resulting from computing the median color in the neighborhood of
        each pixel.
        
        Parameters:
        
        * image - Input image (unused).
        
        * drawable - Input drawable.
        
        * radius (default: -400) - Neighborhood radius, a negative value will
          calculate with inverted percentiles.
        
        * percentile (default: 0.0) - Neighborhood color percentile.
        """
        pass

    def plug_in_metadata_editor(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Edit metadata (IPTC, EXIF, XMP).
        
        Image types: *
        Menu label: _Edit Metadata
        Menu path: <Image>/Image/Metadata
        
        Edit metadata information attached to the current image. Some or all of
        this metadata will be saved in the file, depending on the output
        file format.
        
        Parameters:
        
        * image - The input image.
        
        * num_drawables (default: 1) - Number of input drawables.
        
        * drawables - The input drawables.
        """
        pass

    def plug_in_metadata_viewer(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """View metadata (Exif, IPTC, XMP).
        
        Image types: *
        Menu label: _View Metadata
        Menu path: <Image>/Image/Metadata
        
        View metadata information attached to the current image. This can
        include Exif, IPTC and/or XMP information.
        
        Parameters:
        
        * image - The input image.
        
        * num_drawables (default: 1) - Number of input drawables.
        
        * drawables - The input drawables.
        """
        pass

    def plug_in_mosaic(self, image: Gimp.Image=None, drawable: Gimp.Drawable=None, tile_size: float=None, tile_height: float=None, tile_spacing: float=None, tile_neatness: float=None, tile_allow_split: int=None, light_dir: float=None, color_variation: float=None, antialiasing: int=None, color_averaging: int=None, tile_type: int=None, tile_surface: int=None, grout_color: int=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Convert the image into irregular tiles.
        
        Mosaic is a filter which transforms an image into what appears to be a
        mosaic, composed of small primitives, each of constant color and
        of an approximate size.
        
        Parameters:
        
        * image - Input image (unused).
        
        * drawable - Input drawable.
        
        * tile_size (default: 1.0) - Average diameter of each tile (in
          pixels).
        
        * tile_height (default: 1.0) - Apparent height of each tile (in
          pixels).
        
        * tile_spacing (default: 0.1) - Inter_tile spacing (in pixels).
        
        * tile_neatness (default: 0.0) - Deviation from perfectly formed
          tiles.
        
        * tile_allow_split (default: 0) - Allows splitting tiles at hard
          edges.
        
        * light_dir (default: 0.0) - Direction of light_source (in degrees).
        
        * color_variation (default: 0.0) - Magnitude of random color
          variations.
        
        * antialiasing (default: 0) - Enables smoother tile output at the cost
          of speed.
        
        * color_averaging (default: 0) - Tile color based on average of
          subsumed pixels.
        
        * tile_type (default: 0) - Tile geometry { SQUARES (0), HEXAGONS (1),
          OCTAGONS (2), TRIANGLES (3) }.
        
        * tile_surface (default: 0) - Surface characteristics { SMOOTH (0),
          ROUGH (1) }.
        
        * grout_color (default: 0) - Grout color (black/white or
          fore/background) { BW (0), FG-BG (1) }.
        """
        pass

    def plug_in_neon(self, image: Gimp.Image=None, drawable: Gimp.Drawable=None, radius: float=None, amount: float=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Simulate the glowing boundary of a neon light.
        
        This filter works in a manner similar to the edge plug-in, but uses the
        first derivative of the gaussian operator to achieve resolution
        independence. The IIR method of calculating the effect is
        utilized to keep the processing time constant between large and
        small standard deviations.
        
        Parameters:
        
        * image - Input image (unused).
        
        * drawable - Input drawable.
        
        * radius (default: 0.0) - Radius of neon effect (in pixels).
        
        * amount (default: 0.0) - Effect enhancement variable.
        """
        pass

    def plug_in_newsprint(self, image: Gimp.Image=None, drawable: Gimp.Drawable=None, cell_width: int=None, colorspace: int=None, k_pullout: int=None, gry_ang: float=None, gry_spotfn: int=None, red_ang: float=None, red_spotfn: int=None, grn_ang: float=None, grn_spotfn: int=None, blu_ang: float=None, blu_spotfn: int=None, oversample: int=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Halftone the image to give newspaper-like effect.
        
        Halftone the image to give newspaper-like effect.
        
        Parameters:
        
        * image - Input image (unused).
        
        * drawable - Input drawable.
        
        * cell_width (default: 0) - Screen cell width in pixels.
        
        * colorspace (default: 0) - Separate to { GRAYSCALE (0), RGB (1), CMYK
          (2), LUMINANCE (3) }.
        
        * k_pullout (default: 0) - Percentage of black to pullout (CMYK only).
        
        * gry_ang (default: 0.0) - Grey/black screen angle (degrees).
        
        * gry_spotfn (default: 0) - Grey/black spot function { DOTS (0), LINES
          (1), DIAMONDS (2), EUCLIDIAN-DOT (3), PS-DIAMONDS (4) }.
        
        * red_ang (default: 0.0) - Red/cyan screen angle (degrees).
        
        * red_spotfn (default: 0) - Red/cyan spot function { DOTS (0), LINES
          (1), DIAMONDS (2), EUCLIDIAN-DOT (3), PS-DIAMONDS (4) }.
        
        * grn_ang (default: 0.0) - Green/magenta screen angle (degrees).
        
        * grn_spotfn (default: 0) - Green/magenta spot function { DOTS (0),
          LINES (1), DIAMONDS (2), EUCLIDIAN-DOT (3), PS-DIAMONDS (4)
          }.
        
        * blu_ang (default: 0.0) - Blue/yellow screen angle (degrees).
        
        * blu_spotfn (default: 0) - Blue/yellow spot function { DOTS (0),
          LINES (1), DIAMONDS (2), EUCLIDIAN-DOT (3), PS-DIAMONDS (4)
          }.
        
        * oversample (default: 0) - how many times to oversample spot fn.
        """
        pass

    def plug_in_nl_filter(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, alpha: float=None, radius: float=None, filter: int=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Nonlinear swiss army knife filter.
        
        Image types: RGB, GRAY
        Menu label: _NL Filter...
        Menu path: <Image>/Filters/Enhance
        
        This is the pnmnlfilt, in GIMP's clothing. See the pnmnlfilt manpage for
        details.
        
        Parameters:
        
        * image - The input image.
        
        * num_drawables (default: 1) - Number of input drawables.
        
        * drawables - The input drawables.
        
        * alpha (default: 0.3) - The amount of the filter to apply.
        
        * radius (default: 0.3333333333333333) - The filter radius.
        
        * filter (default: 0) - The Filter to Run, 0 - alpha trimmed mean; 1 -
          optimal estimation (alpha controls noise variance); 2 - edge
          enhancement.
        """
        pass

    def plug_in_noisify(self, image: Gimp.Image=None, drawable: Gimp.Drawable=None, independent: bool=None, noise_1: float=None, noise_2: float=None, noise_3: float=None, noise_4: float=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Adds random noise to image channels.
        
        Add normally distributed random values to image channels. For color
        images each color channel may be treated together or
        independently.
        
        Parameters:
        
        * image - Input image (unused).
        
        * drawable - Input drawable.
        
        * independent (default: False) - Noise in channels independent.
        
        * noise_1 (default: 0.0) - Noise in the first channel (red, gray).
        
        * noise_2 (default: 0.0) - Noise in the second channel (green,
          gray_alpha).
        
        * noise_3 (default: 0.0) - Noise in the third channel (blue).
        
        * noise_4 (default: 0.0) - Noise in the fourth channel (alpha).
        """
        pass

    def plug_in_normalize(self, image: Gimp.Image=None, drawable: Gimp.Drawable=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Stretch brightness values to cover the full range.
        
        This plug-in performs almost the same operation as the 'contrast
        autostretch' plug-in, except that it won't allow the color
        channels to normalize independently. This is actually what most
        people probably want instead of contrast-autostretch; use c-a
        only if you wish to remove an undesirable color-tint from a
        source image which is supposed to contain pure-white and
        pure-black.
        
        Parameters:
        
        * image - Input image (unused).
        
        * drawable - Input drawable.
        """
        pass

    def plug_in_nova(self, image: Gimp.Image=None, drawable: Gimp.Drawable=None, xcenter: int=None, ycenter: int=None, color: Gimp.RGB=None, radius: int=None, nspoke: int=None, randomhue: int=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Add a starburst to the image.
        
        This plug-in produces an effect like a supernova burst. The amount of
        the light effect is approximately in proportion to 1/r, where r
        is the distance from the center of the star.
        
        Parameters:
        
        * image - Input image (unused).
        
        * drawable - Input drawable.
        
        * xcenter (default: 0) - X coordinates of the center of supernova.
        
        * ycenter (default: 0) - Y coordinates of the center of supernova.
        
        * color - Color of supernova.
        
        * radius (default: 1) - Radius of supernova.
        
        * nspoke (default: 1) - Number of spokes.
        
        * randomhue (default: 0) - Random hue.
        """
        pass

    def plug_in_oilify(self, image: Gimp.Image=None, drawable: Gimp.Drawable=None, mask_size: int=None, mode: int=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Smear colors to simulate an oil painting.
        
        This function performs the well-known oil-paint effect on the specified
        drawable.
        
        Parameters:
        
        * image - Input image (unused).
        
        * drawable - Input drawable.
        
        * mask_size (default: 1) - Oil paint mask size.
        
        * mode (default: 0) - Algorithm { RGB (0), INTENSITY (1) }.
        """
        pass

    def plug_in_oilify_enhanced(self, image: Gimp.Image=None, drawable: Gimp.Drawable=None, mode: int=None, mask_size: int=None, mask_size_map: Gimp.Drawable=None, exponent: int=None, exponent_map: Gimp.Drawable=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Smear colors to simulate an oil painting.
        
        This function performs the well-known oil-paint effect on the specified
        drawable.
        
        Parameters:
        
        * image - Input image (unused).
        
        * drawable - Input drawable.
        
        * mode (default: 0) - Algorithm { RGB (0), INTENSITY (1) }.
        
        * mask_size (default: 1) - Oil paint mask size.
        
        * mask_size_map - Mask size control map.
        
        * exponent (default: 1) - Oil paint exponent.
        
        * exponent_map - Exponent control map.
        """
        pass

    def plug_in_pagecurl(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, colors: str=None, edge: str=None, orientation: str=None, shade: bool=None, opacity: float=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE) -> Gimp.Layer:
        """Curl up one of the image corners.
        
        Image types: RGB*, GRAY*
        Menu label: _Pagecurl...
        Menu path: <Image>/Filters/Distorts
        
        This plug-in creates a pagecurl-effect.
        
        Parameters:
        
        * image - The input image.
        
        * num_drawables (default: 1) - Number of input drawables.
        
        * drawables - The input drawables.
        
        * colors -
        
        * edge - Corner which is curled.
        
        * orientation -
        
        * shade (default: True) - Shade the region under the curl.
        
        * opacity (default: 0.0) - Opacity.
        
        Returns:
        
        * curl_layer - The new layer with the curl.
        """
        pass

    def plug_in_palettemap(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Recolor the image using colors from the active palette.
        
        Image types: RGB*, GRAY*
        Menu label: _Palette Map
        Menu path: <Image>/Colors/Map
        
        This plug-in maps the contents of the specified drawable with the active
        palette. It calculates luminosity of each pixel and replaces the
        pixel by the palette sample at the corresponding index. A
        complete black pixel becomes the lowest palette entry, and
        complete white becomes the highest. Works on both Grayscale and
        RGB image with/without alpha channel.
        
        Parameters:
        
        * image - The input image.
        
        * num_drawables (default: 1) - Number of input drawables.
        
        * drawables - The input drawables.
        """
        pass

    def plug_in_papertile(self, image: Gimp.Image=None, drawable: Gimp.Drawable=None, tile_size: int=None, move_max: float=None, fractional_type: int=None, wrap_around: bool=None, centering: bool=None, background_type: int=None, background_color: Gegl.Color=None, background_alpha: int=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Cut image into paper tiles, and slide them.
        
        This plug-in cuts an image into paper tiles and slides each paper tile.
        
        Parameters:
        
        * image - Input image (unused).
        
        * drawable - Input drawable.
        
        * tile_size (default: 0) - Tile size (pixels).
        
        * move_max (default: 0.0) - Max move rate (%).
        
        * fractional_type (default: 0) - Fractional type { BACKGROUND (0),
          IGNORE (1), FORCE (2) }.
        
        * wrap_around (default: False) - Wrap around.
        
        * centering (default: False) - Centering.
        
        * background_type (default: 0) - Background type { TRANSPARENT (0),
          INVERTED (1), IMAGE (2), FG (3), BG (4), COLOR (5) }.
        
        * background_color - Background color (for background-type == 5).
        
        * background_alpha (default: 0) - Background alpha (unused).
        """
        pass

    def plug_in_photocopy(self, image: Gimp.Image=None, drawable: Gimp.Drawable=None, mask_radius: float=None, sharpness: float=None, pct_black: float=None, pct_white: float=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Simulate color distortion produced by a copy machine.
        
        Propagates dark values in an image based on each pixel's relative
        darkness to a neighboring average. The idea behind this filter
        is to give the look of a photocopied version of the image, with
        toner transferred based on the relative darkness of a particular
        region. This is achieved by darkening areas of the image which
        are measured to be darker than a neighborhood average and
        setting other pixels to white. In this way, sufficiently large
        shifts in intensity are darkened to black. The rate at which
        they are darkened to black is determined by the second pct_black
        parameter. The mask_radius parameter controls the size of the
        pixel neighborhood over which the average intensity is computed
        and then compared to each pixel in the neighborhood to decide
        whether or not to darken it to black. Large values for
        mask_radius result in very thick black areas bordering the
        regions of white and much less detail for black areas everywhere
        including inside regions of color. Small values result in less
        toner overall and more detail everywhere. Small values for the
        pct_black make the blend from the white regions to the black
        border lines smoother and the toner regions themselves thinner
        and less noticeable; larger values achieve the opposite effect.
        
        Parameters:
        
        * image - Input image (unused).
        
        * drawable - Input drawable.
        
        * mask_radius (default: 3.0) - Photocopy mask radius (radius of pixel
          neighborhood).
        
        * sharpness (default: 0.0) - Sharpness (detail level).
        
        * pct_black (default: 0.0) - Percentage of darkened pixels to set to
          black.
        
        * pct_white (default: 0.0) - Percentage of non-darkened pixels left
          white.
        """
        pass

    def plug_in_pixelize(self, image: Gimp.Image=None, drawable: Gimp.Drawable=None, pixel_width: int=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Simplify image into an array of solid-colored squares.
        
        Pixelize the contents of the specified drawable with specified
        pixelizing width.
        
        Parameters:
        
        * image - Input image (unused).
        
        * drawable - Input drawable.
        
        * pixel_width (default: 1) - Pixel width (the decrease in resolution).
        """
        pass

    def plug_in_pixelize2(self, image: Gimp.Image=None, drawable: Gimp.Drawable=None, pixel_width: int=None, pixel_height: int=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Simplify image into an array of solid-colored rectangles.
        
        Pixelize the contents of the specified drawable with specified
        pixelizing width and height.
        
        Parameters:
        
        * image - Input image (unused).
        
        * drawable - Input drawable.
        
        * pixel_width (default: 1) - Pixel width (the decrease in horizontal
          resolution).
        
        * pixel_height (default: 1) - Pixel height (the decrease in vertical
          resolution).
        """
        pass

    def plug_in_plasma(self, image: Gimp.Image=None, drawable: Gimp.Drawable=None, seed: int=None, turbulence: float=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Create a random plasma texture.
        
        This plug-in produces plasma fractal images.
        
        Parameters:
        
        * image - Input image (unused).
        
        * drawable - Input drawable.
        
        * seed (default: -1) - Random seed.
        
        * turbulence (default: 0.0) - The value of the turbulence.
        """
        pass

    def plug_in_plug_in_details(self, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Display information about plug-ins.
        
        Menu label: _Plug-In Browser
        Menu path: <Image>/Help/[Programming]
        
        Allows one to browse the plug-in menus system. You can search for
        plug-in names, sort by name or menu location and you can view a
        tree representation of the plug-in menus. Can also be of help to
        find where new plug-ins have installed themselves in the menus.
        """
        pass

    def plug_in_polar_coords(self, image: Gimp.Image=None, drawable: Gimp.Drawable=None, circle: float=None, angle: float=None, backwards: bool=None, inverse: bool=None, polrec: bool=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Convert image to or from polar coordinates.
        
        Remaps and image from rectangular coordinates to polar coordinates or
        vice versa.
        
        Parameters:
        
        * image - Input image (unused).
        
        * drawable - Input drawable.
        
        * circle (default: 0.0) - Circle depth in %.
        
        * angle (default: 0.0) - Offset angle.
        
        * backwards (default: False) - Map backwards.
        
        * inverse (default: False) - Map from top.
        
        * polrec (default: False) - Polar to rectangular.
        """
        pass

    def plug_in_qbist(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Generate a huge variety of abstract patterns.
        
        Image types: RGB*
        Menu label: _Qbist...
        Menu path: <Image>/Filters/Render/Pattern
        
        This Plug-in is based on an article by Jörn Loviscach (appeared in c't
        10/95, page 326). It generates modern art pictures from a random
        genetic formula.
        
        Parameters:
        
        * image - The input image.
        
        * num_drawables (default: 1) - Number of input drawables.
        
        * drawables - The input drawables.
        """
        pass

    def plug_in_randomize_hurl(self, image: Gimp.Image=None, drawable: Gimp.Drawable=None, rndm_pct: float=None, rndm_rcount: float=None, randomize: bool=None, seed: int=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Completely randomize a fraction of pixels.
        
        This plug-in "hurls" randomly-valued pixels onto the selection or image.
        You may select the percentage of pixels to modify and the number
        of times to repeat the process.
        
        Parameters:
        
        * image - Input image (unused).
        
        * drawable - Input drawable.
        
        * rndm_pct (default: 0.0) - Randomization percentage.
        
        * rndm_rcount (default: 1.0) - Repeat count.
        
        * randomize (default: False) - Use random seed.
        
        * seed (default: 0) - Seed value (used only if randomize is FALSE).
        """
        pass

    def plug_in_randomize_pick(self, image: Gimp.Image=None, drawable: Gimp.Drawable=None, rndm_pct: float=None, rndm_rcount: float=None, randomize: bool=None, seed: int=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Randomly interchange some pixels with neighbors.
        
        This plug-in replaces a pixel with a random adjacent pixel. You may
        select the percentage of pixels to modify and the number of
        times to repeat the process.
        
        Parameters:
        
        * image - Input image (unused).
        
        * drawable - Input drawable.
        
        * rndm_pct (default: 1.0) - Randomization percentage.
        
        * rndm_rcount (default: 1.0) - Repeat count.
        
        * randomize (default: False) - Use random seed.
        
        * seed (default: 0) - Seed value (used only if randomize is FALSE).
        """
        pass

    def plug_in_randomize_slur(self, image: Gimp.Image=None, drawable: Gimp.Drawable=None, rndm_pct: float=None, rndm_rcount: float=None, randomize: bool=None, seed: int=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Randomly slide some pixels downward (similar to melting.
        
        This plug-in "slurs" (melts like a bunch of icicles) an image. You may
        select the percentage of pixels to modify and the number of
        times to repeat the process.
        
        Parameters:
        
        * image - Input image (unused).
        
        * drawable - Input drawable.
        
        * rndm_pct (default: 1.0) - Randomization percentage.
        
        * rndm_rcount (default: 1.0) - Repeat count.
        
        * randomize (default: False) - Use random seed.
        
        * seed (default: 0) - Seed value (used only if randomize is FALSE).
        """
        pass

    def plug_in_recompose(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Recompose an image that was previously decomposed.
        
        Image types: GRAY*
        Menu label: R_ecompose
        Menu path: <Image>/Colors/Components
        
        This function recombines the grayscale layers produced by Decompose into
        a single RGB or RGBA layer, and replaces the originally
        decomposed layer with the result.
        
        Parameters:
        
        * image - The input image.
        
        * num_drawables (default: 1) - Number of input drawables.
        
        * drawables - The input drawables.
        """
        pass

    def plug_in_red_eye_removal(self, image: Gimp.Image=None, drawable: Gimp.Drawable=None, threshold: int=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Remove the red eye effect caused by camera flashes.
        
        This procedure removes the red eye effect caused by camera flashes by
        using a percentage based red color threshold. Make a selection
        containing the eyes, and apply the filter while adjusting the
        threshold to accurately remove the red eyes.
        
        Parameters:
        
        * image - Input image (unused).
        
        * drawable - Input drawable.
        
        * threshold (default: 0) - Red eye threshold in percent.
        """
        pass

    def plug_in_retinex(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, scale: int=None, nscales: int=None, scales_mode: int=None, cvar: float=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Enhance contrast using the Retinex method.
        
        Image types: RGB*
        Menu label: Retine_x...
        Menu path: <Image>/Colors/Tone Mapping
        
        The Retinex Image Enhancement Algorithm is an automatic image
        enhancement method that enhances a digital image in terms of
        dynamic range compression, color independence from the spectral
        distribution of the scene illuminant, and color/lightness
        rendition.
        
        Parameters:
        
        * image - The input image.
        
        * num_drawables (default: 1) - Number of input drawables.
        
        * drawables - The input drawables.
        
        * scale (default: 240) - Biggest scale value.
        
        * nscales (default: 3) - Number of scales.
        
        * scales_mode (default: 0) - Retinex distribution through scales {
          Uniform (0), Low (1), High (2) }.
        
        * cvar (default: 1.2) - Variance value.
        """
        pass

    def plug_in_rgb_noise(self, image: Gimp.Image=None, drawable: Gimp.Drawable=None, independent: bool=None, correlated: bool=None, noise_1: float=None, noise_2: float=None, noise_3: float=None, noise_4: float=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Distort colors by random amounts.
        
        Add normally distributed (zero mean) random values to image channels.
        Noise may be additive (uncorrelated) or multiplicative
        (correlated - also known as speckle noise). For color images
        color channels may be treated together or independently.
        
        Parameters:
        
        * image - Input image (unused).
        
        * drawable - Input drawable.
        
        * independent (default: False) - Noise in channels independent.
        
        * correlated (default: False) - Noise correlated (i.e. multiplicative
          not additive).
        
        * noise_1 (default: 0.0) - Noise in the first channel (red, gray).
        
        * noise_2 (default: 0.0) - Noise in the second channel (green,
          gray_alpha).
        
        * noise_3 (default: 0.0) - Noise in the third channel (blue).
        
        * noise_4 (default: 0.0) - Noise in the fourth channel (alpha).
        """
        pass

    def plug_in_ripple(self, image: Gimp.Image=None, drawable: Gimp.Drawable=None, period: float=None, amplitude: float=None, orientation: int=None, edges: int=None, waveform: int=None, antialias: bool=None, tile: bool=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Displace pixels in a ripple pattern.
        
        Ripples the pixels of the specified drawable. Each row or column will be
        displaced a certain number of pixels coinciding with the given
        wave form.
        
        Parameters:
        
        * image - Input image (unused).
        
        * drawable - Input drawable.
        
        * period (default: 200.0) - Period: number of pixels for one wave to
          complete.
        
        * amplitude (default: 25.0) - Amplitude: maximum displacement of wave.
        
        * orientation (default: 0) - Orientation { ORIENTATION-HORIZONTAL (0),
          ORIENTATION-VERTICAL (1) }.
        
        * edges (default: 0) - Edges { SMEAR (0), WRAP (1), BLANK (2) }.
        
        * waveform (default: 0) - Waveform { SAWTOOTH (0), SINE (1) }.
        
        * antialias (default: False) - Antialias { TRUE, FALSE }.
        
        * tile (default: False) - Tileable { TRUE, FALSE }.
        """
        pass

    def plug_in_rotate(self, image: Gimp.Image=None, drawable: Gimp.Drawable=None, angle: int=None, everything: bool=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Rotates a layer or the whole image by 90, 180 or 270 degrees.
        
        This plug-in does rotate the active layer or the whole image clockwise
        by multiples of 90 degrees. When the whole image is chosen, the
        image is resized if necessary.
        
        Parameters:
        
        * image - Input image (unused).
        
        * drawable - Input drawable.
        
        * angle (default: 1) - Angle { 90 (1), 180 (2), 270 (3) } degrees.
        
        * everything (default: False) - Rotate the whole image.
        """
        pass

    def plug_in_sample_colorize(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, sample_drawable: Gimp.Drawable=None, hold_inten: bool=None, orig_inten: bool=None, rnd_subcolors: bool=None, guess_missing: bool=None, in_low: int=None, in_high: int=None, gamma: float=None, out_low: int=None, out_high: int=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Colorize image using a sample image as a guide.
        
        Image types: RGB*, GRAY*
        Menu label: _Sample Colorize...
        Menu path: <Image>/Colors/Map
        
        This plug-in colorizes the contents of the specified (gray) layer with
        the help of a
        
        sample (color) layer. It analyzes all colors in the sample layer. The
        sample colors are sorted by brightness (== intentisty) and
        amount and stored in a sample colortable (where brightness is
        the index) The pixels of the destination layer are remapped with
        the help of the sample colortable. If use_subcolors is TRUE, the
        remapping process uses all sample colors of the corresponding
        brightness-intensity and distributes the subcolors according to
        their amount in the sample (If the sample has 5 green, 3 yellow,
        and 1 red pixel of the
        
        intensity value 105, the destination pixels at intensity value 105 are
        randomly painted in green, yellow and red in a relation of 5:3:1
        If use_subcolors is FALSE only one sample color per intensity is
        used. (green will be used in this example) The brightness
        intensity value is transformed at the remapping process
        according to the levels: out_lo, out_hi, in_lo, in_high and
        gamma The in_low / in_high levels specify an initial mapping of
        the intensity. The gamma value determines how intensities are
        interpolated between the in_lo and in_high levels. A gamma value
        of 1.0 results in linear interpolation. Higher gamma values
        results in more high-level intensities Lower gamma values
        results in more low-level intensities The out_low/out_high
        levels constrain the resulting intensity index The intensity
        index is used to pick the corresponding color in the sample
        colortable. If hold_inten is FALSE the picked color is used 1:1
        as resulting remap_color. If hold_inten is TRUE The brightness
        of the picked color is adjusted back to the original intensity
        value (only hue and saturation are taken from the picked sample
        color) (or to the input level, if orig_inten is set FALSE) Works
        on both Grayscale and RGB image with/without alpha channel. (the
        image with the dst_drawable is converted to RGB if necessary)
        The sample_drawable should be of type RGB or RGBA.
        
        Parameters:
        
        * image - The input image.
        
        * num_drawables (default: 1) - Number of input drawables.
        
        * drawables - The input drawables.
        
        * sample_drawable - Sample drawable (should be of Type RGB or RGBA).
        
        * hold_inten (default: True) - Hold brightness intensity levels.
        
        * orig_inten (default: True) - TRUE: hold brightness of original
          intensity levels, FALSE: Hold Intensity of input levels.
        
        * rnd_subcolors (default: False) - TRUE: Use all subcolors of same
          intensity, FALSE: Use only one color per intensity.
        
        * guess_missing (default: True) - TRUE: guess samplecolors for the
          missing intensity values, FALSE: use only colors found in
          the sample.
        
        * in_low (default: 0) - Intensity of lowest input.
        
        * in_high (default: 255) - Intensity of highest input.
        
        * gamma (default: 1.0) - Gamma adjustment factor, 1.0 is linear.
        
        * out_low (default: 0) - Lowest sample color intensity.
        
        * out_high (default: 255) - Highest sample color intensity.
        """
        pass

    def plug_in_screenshot(self, shoot_type: int=None, x1: int=None, y1: int=None, x2: int=None, y2: int=None, include_pointer: bool=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE) -> Gimp.Image:
        """Create an image from an area of the screen.
        
        Menu label: _Screenshot...
        Menu path: <Image>/File/Create
        
        The plug-in takes screenshots of an interactively selected window or of
        the desktop, either the whole desktop or an interactively
        selected region. When called non-interactively, it may grab the
        root window or use the window-id passed as a parameter.
        
        The last four parameters are optional and can be used to specify the
        corners of the region to be grabbed.On Mac OS X, when called
        non-interactively, the plug-inonly can take screenshots of the
        entire root window.Grabbing a window or a region is not
        supportednon-interactively. To grab a region or a
        particularwindow, you need to use the interactive mode.
        
        Parameters:
        
        * shoot_type (default: 0) - The shoot type { SHOOT-WINDOW (0),
          SHOOT-ROOT (1), SHOOT-REGION (2) }.
        
        * x1 (default: 0) - Region left x coord for SHOOT-WINDOW.
        
        * y1 (default: 0) - Region top y coord for SHOOT-WINDOW.
        
        * x2 (default: 0) - Region right x coord for SHOOT-WINDOW.
        
        * y2 (default: 0) - Region bottom y coord for SHOOT-WINDOW.
        
        * include_pointer (default: False) - Your pointing device's cursor
          will be part of the image.
        
        Returns:
        
        * image - Output image.
        """
        pass

    def plug_in_script_fu_console(self, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Interactive console for Script-Fu development.
        
        Menu label: Script-Fu _Console
        Menu path: <Image>/Filters/Development/Script-Fu
        
        Provides an interface which allows interactive scheme development.
        """
        pass

    def plug_in_script_fu_eval(self, script: str=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Evaluate scheme code.
        
        Evaluate the code under the scheme interpreter (primarily for batch
        mode).
        
        Parameters:
        
        * script - Batch commands in the target language, which will be run by
          the interpreter.
        """
        pass

    def plug_in_script_fu_server(self, ip: str=None, port: int=None, logfile: str=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Server for remote Script-Fu operation.
        
        Menu label: _Start Server...
        Menu path: <Image>/Filters/Development/Script-Fu
        
        Provides a server for remote script-fu operation. NOTE that for security
        reasons this procedure's API was changed in an incompatible way
        since GIMP 2.8.12. You now have to pass the IP to listen on as
        first parameter. Calling this procedure with the old API will
        fail on purpose.
        
        Parameters:
        
        * ip - The IP on which to listen for requests.
        
        * port (default: 0) - The port on which to listen for requests.
        
        * logfile - The file to log activity to.
        """
        pass

    def plug_in_script_fu_text_console(self, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Provides a text console mode for script-fu development.
        
        Provides an interface which allows interactive scheme development.
        """
        pass

    def plug_in_sel_gauss(self, image: Gimp.Image=None, drawable: Gimp.Drawable=None, radius: float=None, max_delta: int=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Blur neighboring pixels, but only in low-contrast areas.
        
        This filter functions similar to the regular gaussian blur filter except
        that neighbouring pixels that differ more than the given
        maxdelta parameter will not be blended with. This way with the
        correct parameters, an image can be smoothed out without losing
        details. However, this filter can be rather slow.
        
        Parameters:
        
        * image - Input image (unused).
        
        * drawable - Input drawable.
        
        * radius (default: 0.0) - Radius of gaussian blur (in pixels).
        
        * max_delta (default: 0) - Maximum delta.
        """
        pass

    def plug_in_sel2path(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, align_threshold: float=None, corner_always_threshold: float=None, corner_surround: int=None, corner_threshold: float=None, error_threshold: float=None, filter_alternative_surround: int=None, filter_epsilon: float=None, filter_iteration_count: int=None, filter_percent: float=None, filter_secondary_surround: int=None, filter_surround: int=None, keep_knees: bool=None, line_reversion_threshold: float=None, line_threshold: float=None, reparametrize_improvement: float=None, reparametrize_threshold: float=None, subdivide_search: float=None, subdivide_surround: int=None, subdivide_threshold: float=None, tangent_surround: int=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Converts a selection to a path.
        
        Image types: *
        
        Converts a selection to a path.
        
        Parameters:
        
        * image - The input image.
        
        * num_drawables (default: 1) - Number of input drawables.
        
        * drawables - The input drawables.
        
        * align_threshold (default: 0.5) - If two endpoints are closer than
          this, they are made to be equal.
        
        * corner_always_threshold (default: 60.0) - If the angle defined by a
          point and its predecessors and successors is smaller than
          this, it's a corner, even if it's within 'corner_surround'
          pixels of a point with a smaller angle.
        
        * corner_surround (default: 4) - Number of points to consider when
          determining if a point is a corner or not.
        
        * corner_threshold (default: 100.0) - If a point, its predecessors,
          and its successors define an angle smaller than this, it's a
          corner.
        
        * error_threshold (default: 0.4) - Amount of error at which a fitted
          spline is unacceptable. If any pixel is further away than
          this from the fitted curve, we try again.
        
        * filter_alternative_surround (default: 1) - A second number of
          adjacent points to consider when filtering.
        
        * filter_epsilon (default: 10.0) - If the angles between the vectors
          produced by filter_surround and filter_alternative_surround
          points differ by more than this, use the one from
          filter_alternative_surround.
        
        * filter_iteration_count (default: 4) - Number of times to smooth
          original data points.  Increasing this number dramatically
          --- to 50 or so --- can produce vastly better results. But
          if any points that 'should' be corners aren't found, the
          curve goes to hell around that point.
        
        * filter_percent (default: 0.33) - To produce the new point, use the
          old point plus this times the neighbors.
        
        * filter_secondary_surround (default: 3) - Number of adjacent points
          to consider if 'filter_surround' points defines a straight
          line.
        
        * filter_surround (default: 2) - Number of adjacent points to consider
          when filtering.
        
        * keep_knees (default: False) - Says whether or not to remove 'knee'
          points after finding the outline.
        
        * line_reversion_threshold (default: 0.01) - If a spline is closer to
          a straight line than this, it remains a straight line, even
          if it would otherwise be changed back to a curve. This is
          weighted by the square of the curve length, to make shorter
          curves more likely to be reverted.
        
        * line_threshold (default: 0.5) - How many pixels (on the average) a
          spline can diverge from the line determined by its endpoints
          before it is changed to a straight line.
        
        * reparametrize_improvement (default: 0.01) - If reparameterization
          doesn't improve the fit by this much percent, stop doing it.
          Amount of error at which it is pointless to reparameterize.
        
        * reparametrize_threshold (default: 1.0) - Amount of error at which it
          is pointless to reparameterize.  This happens, for example,
          when we are trying to fit the outline of the outside of an
          'O' with a single spline. The initial fit is not good enough
          for the Newton-Raphson iteration to improve it.  It may be
          that it would be better to detect the cases where we didn't
          find any corners.
        
        * subdivide_search (default: 0.1) - Percentage of the curve away from
          the worst point to look for a better place to subdivide.
        
        * subdivide_surround (default: 4) - Number of points to consider when
          deciding whether a given point is a better place to
          subdivide.
        
        * subdivide_threshold (default: 0.03) - How many pixels a point can
          diverge from a straight line and still be considered a
          better place to subdivide.
        
        * tangent_surround (default: 3) - Number of points to look at on
          either side of a point when computing the approximation to
          the tangent at that point.
        """
        pass

    def plug_in_semiflatten(self, image: Gimp.Image=None, drawable: Gimp.Drawable=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Replace partial transparency with the current background color.
        
        This plug-in flattens pixels in an RGBA image that aren't completely
        transparent against the current GIMP background color.
        
        Parameters:
        
        * image - Input image (unused).
        
        * drawable - Input drawable.
        """
        pass

    def plug_in_shift(self, image: Gimp.Image=None, drawable: Gimp.Drawable=None, shift_amount: int=None, orientation: int=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Shift each row or column of pixels by a random amount.
        
        Shifts the pixels of the specified drawable. Each row or column will be
        displaced a random value of pixels.
        
        Parameters:
        
        * image - Input image (unused).
        
        * drawable - Input drawable.
        
        * shift_amount (default: 0) - Shift amount.
        
        * orientation (default: 0) - Orientation { ORIENTATION-VERTICAL (0),
          ORIENTATION-HORIZONTAL (1) }.
        """
        pass

    def plug_in_sinus(self, image: Gimp.Image=None, drawable: Gimp.Drawable=None, xscale: float=None, yscale: float=None, complex: float=None, seed: int=None, tiling: bool=None, perturb: bool=None, colors: int=None, col1: Gegl.Color=None, col2: Gegl.Color=None, alpha1: float=None, alpha2: float=None, blend: int=None, blend_power: float=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Generate complex sinusoidal textures.
        
        FIXME: sinus help.
        
        Parameters:
        
        * image - Input image (unused).
        
        * drawable - Input drawable.
        
        * xscale (default: 0.0) - Scale value for x axis.
        
        * yscale (default: 0.0) - Scale value for y axis.
        
        * complex (default: 0.0) - Complexity factor.
        
        * seed (default: 0) - Seed value for random number generator.
        
        * tiling (default: False) - If set, the pattern generated will tile.
        
        * perturb (default: False) - If set, the pattern is a little more
          distorted...
        
        * colors (default: 0) - where to take the colors (0=B&W, 1=fg/bg,
          2=col1/col2).
        
        * col1 - fist color (sometimes unused).
        
        * col2 - second color (sometimes unused).
        
        * alpha1 (default: 0.0) - alpha for the first color (used if the
          drawable has an alpha channel).
        
        * alpha2 (default: 0.0) - alpha for the second color (used if the
          drawable has an alpha channel).
        
        * blend (default: 0) - 0=linear, 1=bilinear, 2=sinusoidal.
        
        * blend_power (default: 0.0) - Power used to stretch the blend.
        """
        pass

    def plug_in_small_tiles(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, num_tiles: int=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Tile image into smaller versions of the original.
        
        Image types: RGB*, GRAY*
        Menu label: _Small Tiles...
        Menu path: <Image>/Filters/Map
        
        More here later.
        
        Parameters:
        
        * image - The input image.
        
        * num_drawables (default: 1) - Number of input drawables.
        
        * drawables - The input drawables.
        
        * num_tiles (default: 2) - Number of tiles to make.
        """
        pass

    def plug_in_smooth_palette(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, width: int=None, height: int=None, n_tries: int=None, show_image: bool=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE) -> Tuple[Gimp.Image, Gimp.Layer]:
        """Derive a smooth color palette from the image.
        
        Image types: RGB*
        Menu label: Smoo_th Palette...
        Menu path: <Image>/Colors/Info
        
        Help!.
        
        Parameters:
        
        * image - The input image.
        
        * num_drawables (default: 1) - Number of input drawables.
        
        * drawables - The input drawables.
        
        * width (default: 256) - Width.
        
        * height (default: 64) - Height.
        
        * n_tries (default: 50) - Search depth.
        
        * show_image (default: True) - Show image.
        
        Returns:
        
        * new_image - Output image.
        
        * new_layer - Output layer.
        """
        pass

    def plug_in_sobel(self, image: Gimp.Image=None, drawable: Gimp.Drawable=None, horizontal: bool=None, vertical: bool=None, keep_sign: bool=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Specialized direction-dependent edge detection.
        
        This plug-in calculates the gradient with a sobel operator. The user can
        specify which direction to use. When both directions are used,
        the result is the RMS of the two gradients; if only one
        direction is used, the result either the absolute value of the
        gradient, or 127 + gradient (if the 'keep sign' switch is on).
        This way, information about the direction of the gradient is
        preserved. Resulting images are not autoscaled.".
        
        Parameters:
        
        * image - Input image (unused).
        
        * drawable - Input drawable.
        
        * horizontal (default: False) - Sobel in horizontal direction.
        
        * vertical (default: False) - Sobel in vertical direction.
        
        * keep_sign (default: False) - Keep sign of result (one direction
          only).
        """
        pass

    def plug_in_softglow(self, image: Gimp.Image=None, drawable: Gimp.Drawable=None, glow_radius: float=None, brightness: float=None, sharpness: float=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Simulate glow by making highlights intense and fuzzy.
        
        Gives an image a softglow effect by intensifying the highlights in the
        image. This is done by screening a modified version of the
        drawable with itself. The modified version is desaturated and
        then a sigmoidal transfer function is applied to force the
        distribution of intensities into very small and very large only.
        This desaturated version is then blurred to give it a fuzzy
        'vaseline-on-the-lens' effect. The glow radius parameter
        controls the sharpness of the glow effect. The brightness
        parameter controls the degree of intensification applied to
        image highlights. The sharpness parameter controls how defined
        or alternatively, diffuse, the glow effect should be.
        
        Parameters:
        
        * image - Input image (unused).
        
        * drawable - Input drawable.
        
        * glow_radius (default: 0.0) - Glow radius in pixels.
        
        * brightness (default: 0.0) - Glow brightness.
        
        * sharpness (default: 0.0) - Glow sharpness.
        """
        pass

    def plug_in_solid_noise(self, image: Gimp.Image=None, drawable: Gimp.Drawable=None, tileable: bool=None, turbulent: bool=None, seed: int=None, detail: int=None, xsize: float=None, ysize: float=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Create a random cloud-like texture.
        
        Generates 2D textures using Perlin's classic solid noise function.
        
        Parameters:
        
        * image - Input image (unused).
        
        * drawable - Input drawable.
        
        * tileable (default: False) - Create a tileable output.
        
        * turbulent (default: False) - Make a turbulent noise.
        
        * seed (default: 0) - Random seed.
        
        * detail (default: 0) - Detail level.
        
        * xsize (default: 0.0) - Horizontal texture size.
        
        * ysize (default: 0.0) - Vertical texture size.
        """
        pass

    def plug_in_sparkle(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, lum_threshold: float=None, flare_inten: float=None, spike_len: int=None, spike_points: int=None, spike_angle: int=None, density: float=None, transparency: float=None, random_hue: float=None, random_saturation: float=None, preserve_luminosity: bool=None, inverse: bool=None, border: bool=None, color_type: int=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Turn bright spots into starry sparkles.
        
        Image types: RGB*, GRAY*
        Menu label: _Sparkle...
        Menu path: <Image>/Filters/Light and Shadow/[Light]
        
        Uses a percentage based luminosity threshold to find candidate pixels
        for adding some sparkles (spikes).
        
        Parameters:
        
        * image - The input image.
        
        * num_drawables (default: 1) - Number of input drawables.
        
        * drawables - The input drawables.
        
        * lum_threshold (default: 0.01) - Adjust the luminosity threshold.
        
        * flare_inten (default: 0.5) - Adjust the flare intensity.
        
        * spike_len (default: 20) - Adjust the spike length (in pixels).
        
        * spike_points (default: 4) - Adjust the number of spikes.
        
        * spike_angle (default: 15) - Adjust the spike angle (-1 causes a
          random angle to be chosen).
        
        * density (default: 1.0) - Adjust the spike density.
        
        * transparency (default: 0.0) - Adjust the opacity of the spikes.
        
        * random_hue (default: 0.0) - Adjust how much the hue should be
          changed randomly.
        
        * random_saturation (default: 0.0) - Adjust how much the saturation
          should be changed randomly.
        
        * preserve_luminosity (default: False) - Should the luminosity be
          preserved?.
        
        * inverse (default: False) - Should the effect be inversed?.
        
        * border (default: False) - Draw a border of spikes around the image.
        
        * color_type (default: 0) - Color of sparkles: { NATURAL (0),
          FOREGROUND (1), BACKGROUND (2) }.
        """
        pass

    def plug_in_spheredesigner(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Create an image of a textured sphere.
        
        Image types: RGB*, GRAY*
        Menu label: Sphere _Designer...
        Menu path: <Image>/Filters/Render
        
        This plug-in can be used to create textured and/or bumpmapped spheres,
        and uses a small lightweight raytracer to perform the task with
        good quality.
        
        Parameters:
        
        * image - The input image.
        
        * num_drawables (default: 1) - Number of input drawables.
        
        * drawables - The input drawables.
        """
        pass

    def plug_in_spread(self, image: Gimp.Image=None, drawable: Gimp.Drawable=None, spread_amount_x: float=None, spread_amount_y: float=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Move pixels around randomly.
        
        Spreads the pixels of the specified drawable. Pixels are randomly moved
        to another location whose distance varies from the original by
        the horizontal and vertical spread amounts.
        
        Parameters:
        
        * image - Input image (unused).
        
        * drawable - Input drawable.
        
        * spread_amount_x (default: 0.0) - Horizontal spread amount.
        
        * spread_amount_y (default: 0.0) - Vertical spread amount.
        """
        pass

    def plug_in_spyrogimp(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, curve_type: int=None, shape: int=None, sides: int=None, morph: float=None, fixed_teeth: int=None, moving_teeth: int=None, hole_percent: float=None, margin: int=None, equal_w_h: bool=None, pattern_rotation: float=None, shape_rotation: float=None, tool: int=None, long_gradient: bool=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Draw spyrographs using current tool settings and selection.
        
        Image types: *
        Menu label: Spyrogimp...
        Menu path: <Image>/Filters/Render
        
        Uses current tool settings to draw Spyrograph patterns. The size and
        location of the pattern is based on the current selection.
        
        Parameters:
        
        * image - The input image.
        
        * num_drawables (default: 1) - Number of input drawables.
        
        * drawables - The input drawables.
        
        * curve_type (default: 0) - The curve type { Spyrograph (0),
          Epitrochoid (1), Sine (2), Lissajous(3) }.
        
        * shape (default: 0) - Shape of fixed gear.
        
        * sides (default: 3) - Number of sides of fixed gear (3 or greater).
          Only used by some shapes.
        
        * morph (default: 0.0) - Morph shape of fixed gear, between 0 and 1.
          Only used by some shapes.
        
        * fixed_teeth (default: 96) - Number of teeth for fixed gear.
        
        * moving_teeth (default: 36) - Number of teeth for moving gear.
        
        * hole_percent (default: 100.0) - Location of hole in moving gear in
          percent, where 100 means that the hole is at the edge of the
          gear, and 0 means the hole is at the center.
        
        * margin (default: 0) - Margin from selection, in pixels.
        
        * equal_w_h (default: False) - Make height and width equal.
        
        * pattern_rotation (default: 0.0) - Pattern rotation, in degrees.
        
        * shape_rotation (default: 0.0) - Shape rotation of fixed gear, in
          degrees.
        
        * tool (default: 1) - Tool to use for drawing the pattern.
        
        * long_gradient (default: False) - Whether to apply a long gradient to
          match the length of the pattern. Only applicable to some of
          the tools.
        """
        pass

    def plug_in_threshold_alpha(self, image: Gimp.Image=None, drawable: Gimp.Drawable=None, threshold: int=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Make transparency all-or-nothing.
        
        Make transparency all-or-nothing.
        
        Parameters:
        
        * image - Input image (unused).
        
        * drawable - Input drawable.
        
        * threshold (default: 0) - Threshold.
        """
        pass

    def plug_in_tile(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, new_width: int=None, new_height: int=None, new_image: bool=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE) -> Tuple[Gimp.Image, Gimp.Layer]:
        """Create an array of copies of the image.
        
        Image types: *
        Menu label: _Tile...
        Menu path: <Image>/Filters/Map
        
        This function creates a new image with a single layer sized to the
        specified 'new_width' and 'new_height' parameters. The specified
        drawable is tiled into this layer.
        
        The new layer will have the same type as the specified drawable and the
        new image will have a corresponding base type.
        
        Parameters:
        
        * image - The input image.
        
        * num_drawables (default: 1) - Number of input drawables.
        
        * drawables - The input drawables.
        
        * new_width (default: 1) - New (tiled) image width.
        
        * new_height (default: 1) - New (tiled) image height.
        
        * new_image (default: True) - Create a new image.
        
        Returns:
        
        * new_image - Output image (NULL if new-image == FALSE).
        
        * new_layer - Output layer (NULL if new-image == FALSE).
        """
        pass

    def plug_in_unit_editor(self, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Create or alter units used in GIMP.
        
        Menu label: U_nits
        Menu path: <Image>/Edit/[Preferences]
        
        The GIMP unit editor.
        """
        pass

    def plug_in_unsharp_mask(self, image: Gimp.Image=None, drawable: Gimp.Drawable=None, radius: float=None, amount: float=None, threshold: int=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """The most widely useful method for sharpening an image.
        
        The unsharp mask is a sharpening filter that works by comparing using
        the difference of the image and a blurred version of the image.
        It is commonly used on photographic images, and is provides a
        much more pleasing result than the standard sharpen filter.
        
        Parameters:
        
        * image - Input image (unused).
        
        * drawable - Input drawable.
        
        * radius (default: 0.0) - Radius of gaussian blur.
        
        * amount (default: 0.0) - Strength of effect.
        
        * threshold (default: 0) - Threshold.
        """
        pass

    def plug_in_video(self, image: Gimp.Image=None, drawable: Gimp.Drawable=None, pattern_number: int=None, additive: bool=None, rotated: bool=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Simulate distortion produced by a fuzzy or low-res monitor.
        
        This function simulates the degradation of being on an old low-dotpitch
        RGB video monitor to the specified drawable.
        
        Parameters:
        
        * image - Input image (unused).
        
        * drawable - Input drawable.
        
        * pattern_number (default: 0) - Type of RGB pattern to use.
        
        * additive (default: False) - Whether the function adds the result to
          the original image.
        
        * rotated (default: False) - Whether to rotate the RGB pattern by
          ninety degrees.
        """
        pass

    def plug_in_vinvert(self, image: Gimp.Image=None, drawable: Gimp.Drawable=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Invert the brightness of each pixel.
        
        This function takes an indexed/RGB image and inverts its 'value' in HSV
        space. The upshot of this is that the color and saturation at
        any given point remains the same, but its brightness is
        effectively inverted. Quite strange. Sometimes produces
        unpleasant color artifacts on images from lossy sources (ie.
        JPEG).
        
        Parameters:
        
        * image - Input image (unused).
        
        * drawable - Input drawable.
        """
        pass

    def plug_in_vpropagate(self, image: Gimp.Image=None, drawable: Gimp.Drawable=None, propagate_mode: int=None, propagating_channel: int=None, propagating_rate: float=None, direction_mask: int=None, lower_limit: int=None, upper_limit: int=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Propagate certain colors to neighboring pixels.
        
        Propagate values of the layer.
        
        Parameters:
        
        * image - Input image (unused).
        
        * drawable - Input drawable.
        
        * propagate_mode (default: 0) - Propagate mode { 0:white, 1:black,
          2:middle value 3:foreground to peak, 4:foreground,
          5:background, 6:opaque, 7:transparent }.
        
        * propagating_channel (default: 0) - Channels which values are
          propagated.
        
        * propagating_rate (default: 0.0) - Propagating rate.
        
        * direction_mask (default: 0) - Direction mask.
        
        * lower_limit (default: 0) - Lower limit.
        
        * upper_limit (default: 0) - Upper limit.
        """
        pass

    def plug_in_warp(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, amount: float=None, warp_map: Gimp.Drawable=None, iter: int=None, dither: float=None, angle: float=None, wrap_type: int=None, mag_map: Gimp.Drawable=None, mag_use: bool=None, substeps: int=None, grad_map: Gimp.Drawable=None, grad_scale: float=None, vector_map: Gimp.Drawable=None, vector_scale: float=None, vector_angle: float=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Twist or smear image in many different ways.
        
        Image types: RGB*, GRAY*
        Menu label: _Warp...
        Menu path: <Image>/Filters/Map
        
        Smears an image along vector paths calculated as the gradient of a
        separate control matrix. The effect can look like brushstrokes
        of acrylic or watercolor paint, in some cases.
        
        Parameters:
        
        * image - The input image.
        
        * num_drawables (default: 1) - Number of input drawables.
        
        * drawables - The input drawables.
        
        * amount (default: 10.0) - Pixel displacement multiplier.
        
        * warp_map - Displacement control map.
        
        * iter (default: 5) - Iteration count.
        
        * dither (default: 0.0) - Random dither amount.
        
        * angle (default: 90.0) - Angle of gradient vector rotation.
        
        * wrap_type (default: 0) - Edge behavior: { WRAP (0), SMEAR (1), BLACK
          (2), COLOR (3) }.
        
        * mag_map - Magnitude control map.
        
        * mag_use (default: False) - Use magnitude map.
        
        * substeps (default: 1) - Substeps between image updates.
        
        * grad_map - Gradient control map.
        
        * grad_scale (default: 0.0) - Scaling factor for gradient map (0=don't
          use).
        
        * vector_map - Fixed vector control map.
        
        * vector_scale (default: 0.0) - Scaling factor for fixed vector map
          (0=don't use).
        
        * vector_angle (default: 0.0) - Angle for fixed vector map.
        """
        pass

    def plug_in_wavelet_decompose(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, scales: int=None, create_group: bool=None, create_masks: bool=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Wavelet decompose.
        
        Image types: RGB*, GRAY*
        Menu label: _Wavelet-decompose...
        Menu path: <Image>/Filters/Enhance
        
        Compute and render wavelet scales.
        
        Parameters:
        
        * image - The input image.
        
        * num_drawables (default: 1) - Number of input drawables.
        
        * drawables - The input drawables.
        
        * scales (default: 5) - Number of scales.
        
        * create_group (default: True) - Create a layer group to store the
          decomposition.
        
        * create_masks (default: False) - Add a layer mask to each scales
          layer.
        """
        pass

    def plug_in_waves(self, image: Gimp.Image=None, drawable: Gimp.Drawable=None, amplitude: float=None, phase: float=None, wavelength: float=None, type: bool=None, reflective: bool=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Distort the image with waves.
        
        Distort the image with waves.
        
        Parameters:
        
        * image - Input image (unused).
        
        * drawable - Input drawable.
        
        * amplitude (default: 0.0) - The Amplitude of the Waves.
        
        * phase (default: -360.0) - The Phase of the Waves.
        
        * wavelength (default: 0.1) - The Wavelength of the Waves.
        
        * type (default: False) - Type of waves: { 0 = smeared, 1 = black }.
        
        * reflective (default: False) - Use Reflection (not implemented).
        """
        pass

    def plug_in_web_browser(self, url: str=None):
        """Open an URL in the user specified web browser.
        
        Opens the given URL in the user specified web browser.
        
        Parameters:
        
        * url (default: https://www.gimp.org/) - URL to open.
        """
        pass

    def plug_in_whirl_pinch(self, image: Gimp.Image=None, drawable: Gimp.Drawable=None, whirl: float=None, pinch: float=None, radius: float=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Distort an image by whirling and pinching.
        
        Distorts the image by whirling and pinching, which are two common
        center-based, circular distortions. Whirling is like projecting
        the image onto the surface of water in a toilet and flushing.
        Pinching is similar to projecting the image onto an elastic
        surface and pressing or pulling on the center of the surface.
        
        Parameters:
        
        * image - Input image (unused).
        
        * drawable - Input drawable.
        
        * whirl (default: -720.0) - Whirl angle (degrees).
        
        * pinch (default: -1.0) - Pinch amount.
        
        * radius (default: 0.0) - Radius (1.0 is the largest circle that fits
          in the image, and 2.0 goes all the way to the corners).
        """
        pass

    def plug_in_wind(self, image: Gimp.Image=None, drawable: Gimp.Drawable=None, threshold: int=None, direction: int=None, strength: int=None, algorithm: int=None, edge: int=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Smear image to give windblown effect.
        
        Renders a wind effect.
        
        Parameters:
        
        * image - Input image (unused).
        
        * drawable - Input drawable.
        
        * threshold (default: 0) - Controls where blending will be done.
        
        * direction (default: 0) - Wind direction { 0:left, 1:right, 2:top,
          3:bottom }.
        
        * strength (default: 1) - Controls the extent of the blending.
        
        * algorithm (default: 0) - Algorithm { WIND (0), BLAST (1) }.
        
        * edge (default: 0) - Affected edge { BOTH (0), LEADING (1), TRAILING
          (2) }.
        """
        pass

    def plug_in_zealouscrop(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Autocrop unused space from edges and middle.
        
        Image types: *
        Menu label: _Zealous Crop
        Menu path: <Image>/Image/[Crop]
        
        Parameters:
        
        * image - The input image.
        
        * num_drawables (default: 1) - Number of input drawables.
        
        * drawables - The input drawables.
        """
        pass

    def python_fu_console(self, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Interactive GIMP Python interpreter.
        
        Menu label: Python _Console
        Menu path: <Image>/Filters/Development/Python-Fu
        
        Type in commands and see results.
        """
        pass

    def python_fu_eval(self, script: str=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Evaluate Python code.
        
        Evaluate python code under the python interpreter (primarily for batch
        mode).
        
        Parameters:
        
        * script - Batch commands in the target language, which will be run by
          the interpreter.
        """
        pass

    def python_fu_foggify(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, name: str=None, color: Gimp.RGB=None, turbulence: float=None, opacity: float=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Add a layer of fog.
        
        Image types: RGB*, GRAY*
        Menu label: _Fog...
        Menu path: <Image>/Filters/Decor
        
        Adds a layer of fog to the image.
        
        Parameters:
        
        * image - The input image.
        
        * num_drawables (default: 1) - Number of input drawables.
        
        * drawables - The input drawables.
        
        * name (default: Clouds) - Layer name.
        
        * color - Fog color.
        
        * turbulence (default: 1.0) - Turbulence.
        
        * opacity (default: 100.0) - Opacity.
        """
        pass

    def python_fu_palette_offset(self, palette: Gimp.Palette=None, amount: int=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE) -> Gimp.Palette:
        """Offset the colors in a palette.
        
        Menu label: _Offset Palette...
        Menu path: <Palettes>
        
        Offset the colors in the palette. Offsets and returns the given palette
        when it is editable, otherwise copies the given palette and
        returns it.
        
        Parameters:
        
        * palette - Palette.
        
        * amount (default: 1) - Offset.
        
        Returns:
        
        * new_palette - The newly created palette when read-only, otherwise
          the input palette.
        """
        pass

    def python_fu_palette_sort(self, palette: Gimp.Palette=None, selections: int=None, slice_expr: str=None, channel1: int=None, ascending1: bool=None, channel2: int=None, ascending2: bool=None, quantize: float=None, pchannel: int=None, pquantize: float=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE) -> Gimp.Palette:
        """Sort the colors in a palette.
        
        Menu label: _Sort Palette...
        Menu path: <Palettes>
        
        Sorts a palette, or part of a palette. Sorts the given palette when it
        is editable, otherwise creates a new sorted palette. The default
        is a 1D sort, but you can also sort over two color channels or
        create a 2D sorted palette with sorted rows. You can optionally
        install colormath (https://pypi.python.org/pypi/colormath/1.0.8)
        to GIMP's Python to get even more channels to choose from.
        
        Parameters:
        
        * palette - Palette.
        
        * selections (default: 0) - ['All', 'Slice / Array', 'Autoslice
          (fg->bg)', 'Partitioned'].
        
        * slice_expr -      Format is 'start:nrows,length' . All items are
          optional.      The empty string selects all items, as does
          ':'     ':4,' makes a 4-row selection out of all colors
          (length auto-determined)     ':4' also.     ':1,4' selects
          the first 4 colors     ':,4' selects rows of 4 colors (nrows
          auto-determined)     ':3,4' selects 3 rows of 4 colors
          '4:' selects a single row of all colors after 4, inclusive.
          '3:,4' selects rows of 4 colors, starting at 3 (nrows
          auto-determined)     '2:3,4' selects 3 rows of 4 colors (12
          colors total), beginning at index 2.     '4' is illegal
          (ambiguous) .
        
        * channel1 (default: 3) - Channel to sort: ('Red', 'Green', 'Blue',
          'Luma (Y)', 'Hue', 'Saturation', 'Value', 'Saturation
          (HSL)', 'Lightness (HSL)', 'Index', 'Random').
        
        * ascending1 (default: True) - Ascending.
        
        * channel2 (default: 5) - Secondary Channel to sort: ('Red', 'Green',
          'Blue', 'Luma (Y)', 'Hue', 'Saturation', 'Value',
          'Saturation (HSL)', 'Lightness (HSL)', 'Index', 'Random').
        
        * ascending2 (default: True) - Ascending.
        
        * quantize (default: 0.0) - Quantization.
        
        * pchannel (default: 3) - Partitioning channel: ('Red', 'Green',
          'Blue', 'Luma (Y)', 'Hue', 'Saturation', 'Value',
          'Saturation (HSL)', 'Lightness (HSL)', 'Index', 'Random').
        
        * pquantize (default: 0.0) - Partition quantization.
        
        Returns:
        
        * new_palette - Palette.
        """
        pass

    def python_fu_palette_to_gradient(self, palette: Gimp.Palette=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE) -> Gimp.Gradient:
        """Create a gradient using colors from the palette.
        
        Menu label: Palette to _Gradient
        Menu path: <Palettes>
        
        Create a new gradient using colors from the palette.
        
        Parameters:
        
        * palette - Palette or None for the currently selected palette.
        
        Returns:
        
        * new_gradient - Read-write integer property.
        """
        pass

    def python_fu_palette_to_gradient_repeating(self, palette: Gimp.Palette=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE) -> Gimp.Gradient:
        """Create a repeating gradient using colors from the palette.
        
        Menu label: Palette to _Repeating Gradient
        Menu path: <Palettes>
        
        Create a new repeating gradient using colors from the palette.
        
        Parameters:
        
        * palette - Palette or None for the currently selected palette.
        
        Returns:
        
        * new_gradient - Read-write integer property.
        """
        pass

    def python_fu_project_browser(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Prism Functions.
        
        Menu label: Project Browser
        Menu path: <Image>/Prism
        
        Prism Functions.
        
        Parameters:
        
        * image - The input image.
        
        * num_drawables (default: 1) - Number of input drawables.
        
        * drawables - The input drawables.
        """
        pass

    def python_fu_save_ver_with_comment(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Prism Functions.
        
        Menu label: Save Ver with Comment
        Menu path: <Image>/Prism
        
        Prism Functions.
        
        Parameters:
        
        * image - The input image.
        
        * num_drawables (default: 1) - Number of input drawables.
        
        * drawables - The input drawables.
        """
        pass

    def python_fu_save_version(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Prism Functions.
        
        Menu label: Save Version
        Menu path: <Image>/Prism
        
        Prism Functions.
        
        Parameters:
        
        * image - The input image.
        
        * num_drawables (default: 1) - Number of input drawables.
        
        * drawables - The input drawables.
        """
        pass

    def python_fu_state_manager(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Prism Functions.
        
        Menu label: State Manager
        Menu path: <Image>/Prism
        
        Prism Functions.
        
        Parameters:
        
        * image - The input image.
        
        * num_drawables (default: 1) - Number of input drawables.
        
        * drawables - The input drawables.
        """
        pass

    def script_fu_add_bevel(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, adjustment: int=None, toggle: bool=None, toggle_2: bool=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Add a beveled border to an image.
        
        Image types: RGB*
        Menu label: Add B_evel...
        Menu path: <Image>/Filters/Decor
        
        Parameters:
        
        * image - The input image.
        
        * num_drawables (default: 1) - Number of input drawables.
        
        * drawables - The input drawables.
        
        * adjustment (default: 5) - _Thickness.
        
        * toggle (default: True) - _Work on copy.
        
        * toggle_2 (default: False) - _Keep bump layer.
        """
        pass

    def script_fu_addborder(self, otherImage: Gimp.Image=None, drawable: Gimp.Drawable=None, adjustment: int=None, adjustment_2: int=None, color: Gimp.RGB=None, adjustment_3: int=None, toggle: bool=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Add a border around an image.
        
        Image types: *
        Menu label: Add _Border...
        Menu path: <Image>/Filters/Decor
        
        Parameters:
        
        * otherImage - Input image.
        
        * drawable - Input drawable.
        
        * adjustment (default: 12) - Border X size.
        
        * adjustment_2 (default: 12) - Border Y size.
        
        * color - Border color.
        
        * adjustment_3 (default: 25) - Delta value on color.
        
        * toggle (default: True) - Allow resizing.
        """
        pass

    def script_fu_blend_anim(self, otherImage: Gimp.Image=None, drawable: Gimp.Drawable=None, adjustment: int=None, adjustment_2: int=None, toggle: bool=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Create intermediate layers to blend two or more layers over a
        background as an animation.
        
        Image types: RGB* GRAY*
        Menu label: _Blend...
        Menu path: <Image>/Filters/Animation
        
        Parameters:
        
        * otherImage - Image.
        
        * drawable - Drawable.
        
        * adjustment (default: 3) - Intermediate frames.
        
        * adjustment_2 (default: 0) - Max. blur radius.
        
        * toggle (default: True) - Looped.
        """
        pass

    def script_fu_burn_in_anim(self, otherImage: Gimp.Image=None, drawable: Gimp.Drawable=None, color: Gimp.RGB=None, toggle: bool=None, value: str=None, value_2: str=None, value_3: str=None, toggle_2: bool=None, toggle_3: bool=None, value_4: str=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Create intermediate layers to produce an animated 'burn-in'
        transition between two layers.
        
        Image types: RGBA GRAYA INDEXEDA
        Menu label: B_urn-In...
        Menu path: <Image>/Filters/Animation
        
        Parameters:
        
        * otherImage - The image.
        
        * drawable - Layer to animate.
        
        * color - Glow color.
        
        * toggle (default: False) - Fadeout.
        
        * value (default: 100) - Fadeout width.
        
        * value_2 (default: 7) - Corona width.
        
        * value_3 (default: 50) - After glow.
        
        * toggle_2 (default: True) - Add glowing.
        
        * toggle_3 (default: False) - Prepare for GIF.
        
        * value_4 (default: 50) - Speed (pixels/frame).
        """
        pass

    def script_fu_carve_it(self, otherImage: Gimp.Image=None, drawable: Gimp.Drawable=None, drawable_2: Gimp.Drawable=None, toggle: bool=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Use the specified drawable as a stencil to carve from the specified
        image.
        
        Image types: GRAY
        Menu label: Stencil C_arve...
        Menu path: <Image>/Filters/Decor
        
        Parameters:
        
        * otherImage - Mask image.
        
        * drawable - Mask drawable.
        
        * drawable_2 - Image to carve.
        
        * toggle (default: True) - Carve white areas.
        """
        pass

    def script_fu_circuit(self, otherImage: Gimp.Image=None, drawable: Gimp.Drawable=None, adjustment: int=None, adjustment_2: int=None, toggle: bool=None, toggle_2: bool=None, toggle_3: bool=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Fill the selected region (or alpha) with traces like those on a
        circuit board.
        
        Image types: RGB* GRAY*
        Menu label: _Circuit...
        Menu path: <Image>/Filters/Render
        
        Parameters:
        
        * otherImage - Image.
        
        * drawable - Drawable.
        
        * adjustment (default: 17) - Oilify mask size.
        
        * adjustment_2 (default: 3) - Circuit seed.
        
        * toggle (default: False) - No background (only for separate layer).
        
        * toggle_2 (default: True) - Keep selection.
        
        * toggle_3 (default: True) - Separate layer.
        """
        pass

    def script_fu_clothify(self, otherImage: Gimp.Image=None, drawable: Gimp.Drawable=None, adjustment: int=None, adjustment_2: int=None, adjustment_3: float=None, adjustment_4: float=None, adjustment_5: int=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Add a cloth-like texture to the selected region (or alpha).
        
        Image types: RGB* GRAY*
        Menu label: _Clothify...
        Menu path: <Image>/Filters/Artistic
        
        Parameters:
        
        * otherImage - Input image.
        
        * drawable - Input drawable.
        
        * adjustment (default: 9) - Blur X.
        
        * adjustment_2 (default: 9) - Blur Y.
        
        * adjustment_3 (default: 135.0) - Azimuth.
        
        * adjustment_4 (default: 45.0) - Elevation.
        
        * adjustment_5 (default: 3) - Depth.
        """
        pass

    def script_fu_clothify_v3(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, adjustment: int=None, adjustment_2: int=None, adjustment_3: float=None, adjustment_4: float=None, adjustment_5: int=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Add a cloth-like texture to the selected region (or alpha).
        
        Image types: RGB* GRAY*
        Menu label: _Clothify v3...
        Menu path: <Image>/Filters/Artistic
        
        Parameters:
        
        * image - The input image.
        
        * num_drawables (default: 1) - Number of input drawables.
        
        * drawables - The input drawables.
        
        * adjustment (default: 9) - Blur X.
        
        * adjustment_2 (default: 9) - Blur Y.
        
        * adjustment_3 (default: 135.0) - Azimuth.
        
        * adjustment_4 (default: 45.0) - Elevation.
        
        * adjustment_5 (default: 3) - Depth.
        """
        pass

    def script_fu_coffee_stain(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, adjustment: int=None, toggle: bool=None, gradient: Gimp.Gradient=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Add layers of stain or blotch marks.
        
        Image types: RGB*
        Menu label: _Stain...
        Menu path: <Image>/Filters/Decor
        
        Parameters:
        
        * image - The input image.
        
        * num_drawables (default: 1) - Number of input drawables.
        
        * drawables - The input drawables.
        
        * adjustment (default: 3) - Number of stains to add.
        
        * toggle (default: True) - Darken only.
        
        * gradient - Gradient to color stains.
        """
        pass

    def script_fu_contactsheet(self, dirname: Gio.File=None, option: int=None, font: Gimp.Font=None, font_2: Gimp.Font=None, color: Gimp.RGB=None, color_2: Gimp.RGB=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Create a series of images containing thumbnail sized versions of all
        of the images in a specified directory.
        
        Menu label: _Contact Sheet...
        Menu path: <Image>/Filters/Combine
        
        Parameters:
        
        * dirname - Images Directory.
        
        * option (default: 0) - Sheet size.
        
        * font - Title font.
        
        * font_2 - Legend font.
        
        * color - Text color.
        
        * color_2 - Background color.
        """
        pass

    def script_fu_difference_clouds(self, otherImage: Gimp.Image=None, drawable: Gimp.Drawable=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Solid noise applied with Difference layer mode.
        
        Image types: RGB* GRAY*
        Menu label: _Difference Clouds
        Menu path: <Image>/Filters/Render/Noise
        
        Parameters:
        
        * otherImage - Image.
        
        * drawable - Drawable.
        """
        pass

    def script_fu_distress_selection(self, otherImage: Gimp.Image=None, drawable: Gimp.Drawable=None, adjustment: int=None, adjustment_2: int=None, adjustment_3: int=None, adjustment_4: int=None, toggle: bool=None, toggle_2: bool=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Distress the selection.
        
        Image types: RGB*,GRAY*
        Menu label: _Distort...
        Menu path: <Image>/Select/[Modify]
        
        Parameters:
        
        * otherImage - The image.
        
        * drawable - The layer.
        
        * adjustment (default: 127) - _Threshold (bigger 1<-->254 smaller).
        
        * adjustment_2 (default: 8) - _Spread.
        
        * adjustment_3 (default: 4) - _Granularity (1 is low).
        
        * adjustment_4 (default: 2) - S_mooth.
        
        * toggle (default: True) - Smooth hor_izontally.
        
        * toggle_2 (default: True) - Smooth _vertically.
        """
        pass

    def script_fu_drop_shadow(self, otherImage: Gimp.Image=None, drawable: Gimp.Drawable=None, adjustment: int=None, adjustment_2: int=None, adjustment_3: int=None, color: Gimp.RGB=None, adjustment_4: int=None, toggle: bool=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Add a drop shadow to the selected region (or alpha).
        
        Image types: RGB* GRAY*
        Menu label: _Drop Shadow (legacy)...
        Menu path: <Image>/Filters/Light and Shadow/[Shadow]
        
        Parameters:
        
        * otherImage - Image.
        
        * drawable - Drawable.
        
        * adjustment (default: 4) - Offset X.
        
        * adjustment_2 (default: 4) - Offset Y.
        
        * adjustment_3 (default: 15) - Blur radius.
        
        * color - Color.
        
        * adjustment_4 (default: 60) - Opacity.
        
        * toggle (default: True) - Allow resizing.
        """
        pass

    def script_fu_font_map(self, string: str=None, toggle: bool=None, toggle_2: bool=None, string_2: str=None, adjustment: int=None, adjustment_2: int=None, option: int=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Create an image filled with previews of fonts matching a fontname
        filter.
        
        Menu label: Render _Font Map...
        Menu path: <Fonts>
        
        Parameters:
        
        * string (default: How quickly daft jumping zebras vex.) - _Text.
        
        * toggle (default: False) - Use font _name as text.
        
        * toggle_2 (default: True) - _Labels.
        
        * string_2 (default: Sans) - _Filter (regexp).
        
        * adjustment (default: 32) - Font _size (pixels).
        
        * adjustment_2 (default: 10) - _Border (pixels).
        
        * option (default: 0) - _Color scheme.
        """
        pass

    def script_fu_fuzzy_border(self, otherImage: Gimp.Image=None, drawable: Gimp.Drawable=None, color: Gimp.RGB=None, adjustment: int=None, toggle: bool=None, adjustment_2: float=None, toggle_2: bool=None, adjustment_3: int=None, toggle_3: bool=None, toggle_4: bool=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Add a jagged, fuzzy border to an image.
        
        Image types: RGB* GRAY*
        Menu label: _Fuzzy Border...
        Menu path: <Image>/Filters/Decor
        
        Parameters:
        
        * otherImage - The image.
        
        * drawable - The layer.
        
        * color - Color.
        
        * adjustment (default: 16) - Border size.
        
        * toggle (default: True) - Blur border.
        
        * adjustment_2 (default: 4.0) - Granularity (1 is Low).
        
        * toggle_2 (default: False) - Add shadow.
        
        * adjustment_3 (default: 100) - Shadow weight (%).
        
        * toggle_3 (default: True) - Work on copy.
        
        * toggle_4 (default: True) - Flatten image.
        """
        pass

    def script_fu_gradient_example(self, adjustment: int=None, adjustment_2: int=None, toggle: bool=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Create an image filled with an example of the current gradient.
        
        Menu label: Custom _Gradient...
        Menu path: <Gradients>
        
        Parameters:
        
        * adjustment (default: 400) - Width.
        
        * adjustment_2 (default: 30) - Height.
        
        * toggle (default: False) - Gradient reverse.
        """
        pass

    def script_fu_guide_new(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, option: int=None, adjustment: int=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Add a guide at the orientation and position specified (in pixels).
        
        Image types: *
        Menu label: New _Guide...
        Menu path: <Image>/Image/Guides
        
        Parameters:
        
        * image - The input image.
        
        * num_drawables (default: 1) - Number of input drawables.
        
        * drawables - The input drawables.
        
        * option (default: 0) - _Direction.
        
        * adjustment (default: 0) - _Position.
        """
        pass

    def script_fu_guide_new_percent(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, option: int=None, adjustment: float=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Add a guide at the position specified as a percentage of the image
        size.
        
        Image types: *
        Menu label: New Guide (by _Percent)...
        Menu path: <Image>/Image/Guides
        
        Parameters:
        
        * image - The input image.
        
        * num_drawables (default: 1) - Number of input drawables.
        
        * drawables - The input drawables.
        
        * option (default: 0) - _Direction.
        
        * adjustment (default: 50.0) - _Position (in %).
        """
        pass

    def script_fu_guides_from_selection(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Create four guides around the bounding box of the current selection.
        
        Image types: *
        Menu label: New Guides from _Selection
        Menu path: <Image>/Image/Guides
        
        Parameters:
        
        * image - The input image.
        
        * num_drawables (default: 1) - Number of input drawables.
        
        * drawables - The input drawables.
        """
        pass

    def script_fu_guides_remove(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Remove all horizontal and vertical guides.
        
        Image types: *
        Menu label: _Remove all Guides
        Menu path: <Image>/Image/Guides
        
        Parameters:
        
        * image - The input image.
        
        * num_drawables (default: 1) - Number of input drawables.
        
        * drawables - The input drawables.
        """
        pass

    def script_fu_lava(self, otherImage: Gimp.Image=None, drawable: Gimp.Drawable=None, adjustment: int=None, adjustment_2: int=None, adjustment_3: int=None, gradient: Gimp.Gradient=None, toggle: bool=None, toggle_2: bool=None, toggle_3: bool=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Fill the current selection with lava.
        
        Image types: RGB* GRAY*
        Menu label: _Lava...
        Menu path: <Image>/Filters/Render
        
        Parameters:
        
        * otherImage - Image.
        
        * drawable - Drawable.
        
        * adjustment (default: 10) - Seed.
        
        * adjustment_2 (default: 10) - Size.
        
        * adjustment_3 (default: 7) - Roughness.
        
        * gradient - Gradient.
        
        * toggle (default: True) - Keep selection.
        
        * toggle_2 (default: True) - Separate layer.
        
        * toggle_3 (default: False) - Use current gradient.
        """
        pass

    def script_fu_line_nova(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, adjustment: int=None, adjustment_2: float=None, adjustment_3: int=None, adjustment_4: int=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Fill a layer with rays emanating outward from its center using the
        foreground color.
        
        Image types: *
        Menu label: Line _Nova...
        Menu path: <Image>/Filters/Render
        
        Parameters:
        
        * image - The input image.
        
        * num_drawables (default: 1) - Number of input drawables.
        
        * drawables - The input drawables.
        
        * adjustment (default: 200) - _Number of lines.
        
        * adjustment_2 (default: 1.0) - S_harpness (degrees).
        
        * adjustment_3 (default: 100) - O_ffset radius.
        
        * adjustment_4 (default: 30) - Ran_domness.
        """
        pass

    def script_fu_make_brush_elliptical(self, string: str=None, adjustment: int=None, adjustment_2: int=None, adjustment_3: float=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Create an elliptical brush.
        
        Menu label: _Elliptical...
        Menu path: <Brushes>
        
        Parameters:
        
        * string (default: Ellipse) - Name.
        
        * adjustment (default: 20) - Width.
        
        * adjustment_2 (default: 20) - Height.
        
        * adjustment_3 (default: 25.0) - Spacing.
        """
        pass

    def script_fu_make_brush_elliptical_feathered(self, string: str=None, adjustment: int=None, adjustment_2: int=None, adjustment_3: int=None, adjustment_4: float=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Create an elliptical brush with feathered edges.
        
        Menu label: Elli_ptical, Feathered...
        Menu path: <Brushes>
        
        Parameters:
        
        * string (default: Ellipse) - Name.
        
        * adjustment (default: 20) - Width.
        
        * adjustment_2 (default: 20) - Height.
        
        * adjustment_3 (default: 4) - Feathering.
        
        * adjustment_4 (default: 25.0) - Spacing.
        """
        pass

    def script_fu_make_brush_rectangular(self, string: str=None, adjustment: int=None, adjustment_2: int=None, adjustment_3: float=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Create a rectangular brush.
        
        Menu label: _Rectangular...
        Menu path: <Brushes>
        
        Parameters:
        
        * string (default: Rectangle) - Name.
        
        * adjustment (default: 20) - Width.
        
        * adjustment_2 (default: 20) - Height.
        
        * adjustment_3 (default: 25.0) - Spacing.
        """
        pass

    def script_fu_make_brush_rectangular_feathered(self, string: str=None, adjustment: int=None, adjustment_2: int=None, adjustment_3: int=None, adjustment_4: float=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Create a rectangular brush with feathered edges.
        
        Menu label: Re_ctangular, Feathered...
        Menu path: <Brushes>
        
        Parameters:
        
        * string (default: Rectangle) - Name.
        
        * adjustment (default: 20) - Width.
        
        * adjustment_2 (default: 20) - Height.
        
        * adjustment_3 (default: 4) - Feathering.
        
        * adjustment_4 (default: 25.0) - Spacing.
        """
        pass

    def script_fu_old_photo(self, otherImage: Gimp.Image=None, drawable: Gimp.Drawable=None, toggle: bool=None, adjustment: int=None, toggle_2: bool=None, toggle_3: bool=None, toggle_4: bool=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Make an image look like an old photo.
        
        Image types: RGB* GRAY*
        Menu label: _Old Photo...
        Menu path: <Image>/Filters/Decor
        
        Parameters:
        
        * otherImage - The image.
        
        * drawable - The layer.
        
        * toggle (default: True) - Defocus.
        
        * adjustment (default: 20) - Border size.
        
        * toggle_2 (default: True) - Sepia.
        
        * toggle_3 (default: False) - Mottle.
        
        * toggle_4 (default: True) - Work on copy.
        """
        pass

    def script_fu_paste_as_brush(self, string: str=None, string_2: str=None, adjustment: float=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Paste the clipboard contents into a new brush.
        
        Menu label: Paste as New _Brush...
        Menu path: <Image>/Edit/Paste as
        
        Parameters:
        
        * string (default: My Brush) - _Brush name.
        
        * string_2 (default: mybrush) - _File name.
        
        * adjustment (default: 25.0) - _Spacing.
        """
        pass

    def script_fu_paste_as_pattern(self, string: str=None, string_2: str=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Paste the clipboard contents into a new pattern.
        
        Menu label: Paste as New _Pattern...
        Menu path: <Image>/Edit/Paste as
        
        Parameters:
        
        * string (default: My Pattern) - _Pattern name.
        
        * string_2 (default: mypattern) - _File name.
        """
        pass

    def script_fu_perspective_shadow(self, otherImage: Gimp.Image=None, drawable: Gimp.Drawable=None, adjustment: float=None, adjustment_2: float=None, adjustment_3: float=None, adjustment_4: int=None, color: Gimp.RGB=None, adjustment_5: int=None, enum: Gimp.InterpolationType=None, toggle: bool=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Add a perspective shadow to the selected region (or alpha).
        
        Image types: RGB* GRAY*
        Menu label: _Perspective...
        Menu path: <Image>/Filters/Light and Shadow/[Shadow]
        
        Parameters:
        
        * otherImage - Image.
        
        * drawable - Drawable.
        
        * adjustment (default: 45.0) - Angle.
        
        * adjustment_2 (default: 5.0) - Relative distance of horizon.
        
        * adjustment_3 (default: 1.0) - Relative length of shadow.
        
        * adjustment_4 (default: 3) - Blur radius.
        
        * color - Color.
        
        * adjustment_5 (default: 80) - Opacity.
        
        * enum (default: <enum GIMP_INTERPOLATION_LINEAR of type
          Gimp.InterpolationType>) - Interpolation.
        
        * toggle (default: False) - Allow resizing.
        """
        pass

    def script_fu_refresh(self, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Re-read all available Script-Fu scripts.
        
        Menu label: _Refresh Scripts
        Menu path: <Image>/Filters/Development/Script-Fu
        
        Re-read all available Script-Fu scripts.
        """
        pass

    def script_fu_reverse_layers(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Reverse the order of layers in the image.
        
        Image types: *
        Menu label: Reverse Layer _Order
        Menu path: <Image>/Layer/Stack
        
        Parameters:
        
        * image - The input image.
        
        * num_drawables (default: 1) - Number of input drawables.
        
        * drawables - The input drawables.
        """
        pass

    def script_fu_ripply_anim(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, adjustment: float=None, adjustment_2: int=None, option: int=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Create a multi-layer image by adding a ripple effect to the current
        layer.
        
        Image types: RGB* GRAY*
        Menu label: _Rippling...
        Menu path: <Image>/Filters/Animation
        
        Parameters:
        
        * image - The input image.
        
        * num_drawables (default: 1) - Number of input drawables.
        
        * drawables - The input drawables.
        
        * adjustment (default: 3.0) - Ri_ppling strength.
        
        * adjustment_2 (default: 15) - _Number of frames.
        
        * option (default: 0) - Edge _behavior.
        """
        pass

    def script_fu_round_corners(self, otherImage: Gimp.Image=None, drawable: Gimp.Drawable=None, adjustment: int=None, toggle: bool=None, adjustment_2: int=None, adjustment_3: int=None, adjustment_4: int=None, toggle_2: bool=None, toggle_3: bool=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Round the corners of an image and optionally add a drop-shadow and
        background.
        
        Image types: RGB* GRAY*
        Menu label: _Round Corners...
        Menu path: <Image>/Filters/Decor
        
        Parameters:
        
        * otherImage - Image.
        
        * drawable - Drawable.
        
        * adjustment (default: 15) - Edge radius.
        
        * toggle (default: True) - Add drop-shadow.
        
        * adjustment_2 (default: 8) - Shadow X offset.
        
        * adjustment_3 (default: 8) - Shadow Y offset.
        
        * adjustment_4 (default: 15) - Blur radius.
        
        * toggle_2 (default: True) - Add background.
        
        * toggle_3 (default: True) - Work on copy.
        """
        pass

    def script_fu_selection_round(self, otherImage: Gimp.Image=None, drawable: Gimp.Drawable=None, adjustment: float=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """This procedure is deprecated! Use
        'script-fu-selection-rounded-rectangle' instead.
        
        Image types: *
        
        Parameters:
        
        * otherImage - Image.
        
        * drawable - Drawable.
        
        * adjustment (default: 1.0) - Relative radius.
        """
        pass

    def script_fu_selection_rounded_rectangle(self, otherImage: Gimp.Image=None, drawable: Gimp.Drawable=None, adjustment: int=None, toggle: bool=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Round the corners of the current selection.
        
        Image types: *
        Menu label: Rounded R_ectangle...
        Menu path: <Image>/Select/[Modify]
        
        Parameters:
        
        * otherImage - Image.
        
        * drawable - Drawable.
        
        * adjustment (default: 50) - R_adius (%).
        
        * toggle (default: False) - Co_ncave.
        """
        pass

    def script_fu_set_cmap(self, otherImage: Gimp.Image=None, drawable: Gimp.Drawable=None, palette: Gimp.Palette=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Change the colormap of an image to the colors in a specified palette.
        
        Image types: INDEXED*
        Menu label: Se_t Colormap...
        Menu path: <Image>/Colors/Map/[Colormap]
        
        Parameters:
        
        * otherImage - Image.
        
        * drawable - Drawable.
        
        * palette - Palette.
        """
        pass

    def script_fu_slide(self, otherImage: Gimp.Image=None, drawable: Gimp.Drawable=None, string: str=None, string_2: str=None, font: Gimp.Font=None, color: Gimp.RGB=None, toggle: bool=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Add a slide-film like frame, sprocket holes, and labels to an image.
        
        Image types: RGB GRAY
        Menu label: _Slide...
        Menu path: <Image>/Filters/Decor
        
        Parameters:
        
        * otherImage - Image.
        
        * drawable - Drawable.
        
        * string (default: GIMP) - Text.
        
        * string_2 (default: 32) - Number.
        
        * font - Font.
        
        * color - Font color.
        
        * toggle (default: True) - Work on copy.
        """
        pass

    def script_fu_sota_chrome_it(self, otherImage: Gimp.Image=None, drawable: Gimp.Drawable=None, adjustment: int=None, adjustment_2: int=None, adjustment_3: float=None, filename: Gio.File=None, color: Gimp.RGB=None, color_2: Gimp.RGB=None, toggle: bool=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Add a chrome effect to the selected region (or alpha) using a
        specified (grayscale) stencil.
        
        Image types: GRAY
        Menu label: Stencil C_hrome...
        Menu path: <Image>/Filters/Decor
        
        Parameters:
        
        * otherImage - Chrome image.
        
        * drawable - Chrome mask.
        
        * adjustment (default: -80) - Chrome saturation.
        
        * adjustment_2 (default: -47) - Chrome lightness.
        
        * adjustment_3 (default: 0.75) - Chrome factor.
        
        * filename - Environment map.
        
        * color - Highlight balance.
        
        * color_2 - Chrome balance.
        
        * toggle (default: True) - Chrome white areas.
        """
        pass

    def script_fu_spinning_globe(self, otherImage: Gimp.Image=None, drawable: Gimp.Drawable=None, adjustment: int=None, toggle: bool=None, toggle_2: bool=None, adjustment_2: int=None, toggle_3: bool=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Create an animation by mapping the current image onto a spinning
        sphere.
        
        Image types: RGB* GRAY*
        Menu label: _Spinning Globe...
        Menu path: <Image>/Filters/Animation
        
        Parameters:
        
        * otherImage - The Image.
        
        * drawable - The Layer.
        
        * adjustment (default: 10) - Frames.
        
        * toggle (default: False) - Turn from left to right.
        
        * toggle_2 (default: True) - Transparent background.
        
        * adjustment_2 (default: 63) - Index to n colors (0 = remain RGB).
        
        * toggle_3 (default: True) - Work on copy.
        """
        pass

    def script_fu_test_sphere(self, adjustment: int=None, adjustment_2: float=None, toggle: bool=None, color: Gimp.RGB=None, color_2: Gimp.RGB=None, brush: Gimp.Brush=None, string: str=None, text: str=None, pattern: Gimp.Pattern=None, gradient: Gimp.Gradient=None, toggle_2: bool=None, font: Gimp.Font=None, adjustment_3: int=None, palette: Gimp.Palette=None, filename: Gio.File=None, option: int=None, enum: Gimp.InterpolationType=None, dirname: Gio.File=None, otherImage: Gimp.Image=None, layer: Gimp.Layer=None, channel: Gimp.Channel=None, drawable: Gimp.Drawable=None, vectors: Gimp.Vectors=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Simple script to test and show the usage of the new Script-Fu API
        extensions.
        
        Menu label: _Sphere...
        Menu path: <Image>/Filters/Development/Script-Fu/Test
        
        Parameters:
        
        * adjustment (default: 100) - Radius (in pixels).
        
        * adjustment_2 (default: 45.0) - Lighting (degrees).
        
        * toggle (default: True) - Shadow.
        
        * color - Background color.
        
        * color_2 - Sphere color.
        
        * brush - Brush.
        
        * string (default: Tiny-Fu rocks!) - Text.
        
        * text (default: Hello, World!) - Multi-line text.
        
        * pattern - Pattern.
        
        * gradient - Gradient.
        
        * toggle_2 (default: False) - Gradient reverse.
        
        * font - Font.
        
        * adjustment_3 (default: 50) - Font size (pixels).
        
        * palette - Palette.
        
        * filename - Environment map.
        
        * option (default: 0) - Orientation.
        
        * enum (default: <enum GIMP_INTERPOLATION_LINEAR of type
          Gimp.InterpolationType>) - Interpolation.
        
        * dirname - Output directory.
        
        * otherImage - Image.
        
        * layer - Layer.
        
        * channel - Channel.
        
        * drawable - Drawable.
        
        * vectors - Vectors.
        """
        pass

    def script_fu_tile_blur(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, adjustment: int=None, toggle: bool=None, toggle_2: bool=None, option: int=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Blur the edges of an image so the result tiles seamlessly.
        
        Image types: RGB*
        Menu label: _Tileable Blur...
        Menu path: <Image>/Filters/Blur
        
        Parameters:
        
        * image - The input image.
        
        * num_drawables (default: 1) - Number of input drawables.
        
        * drawables - The input drawables.
        
        * adjustment (default: 5) - Ra_dius.
        
        * toggle (default: True) - Blur _vertically.
        
        * toggle_2 (default: True) - Blur _horizontally.
        
        * option (default: 0) - Blur _type.
        """
        pass

    def script_fu_unsharp_mask(self, otherImage: Gimp.Image=None, drawable: Gimp.Drawable=None, adjustment: int=None, adjustment_2: int=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Make a new image from the current layer by applying the unsharp mask
        method.
        
        Menu label: Unsharp Mask...
        
        Parameters:
        
        * otherImage - Image.
        
        * drawable - Drawable to apply.
        
        * adjustment (default: 5) - Mask size.
        
        * adjustment_2 (default: 50) - Mask opacity.
        """
        pass

    def script_fu_waves_anim(self, otherImage: Gimp.Image=None, drawable: Gimp.Drawable=None, adjustment: float=None, adjustment_2: float=None, adjustment_3: int=None, toggle: bool=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Create a multi-layer image with an effect like a stone was thrown
        into the current image.
        
        Image types: RGB* GRAY*
        Menu label: _Waves...
        Menu path: <Image>/Filters/Animation
        
        Parameters:
        
        * otherImage - Image.
        
        * drawable - Drawable.
        
        * adjustment (default: 10.0) - Amplitude.
        
        * adjustment_2 (default: 10.0) - Wavelength.
        
        * adjustment_3 (default: 6) - Number of frames.
        
        * toggle (default: False) - Invert direction.
        """
        pass

    def script_fu_weave(self, otherImage: Gimp.Image=None, drawable: Gimp.Drawable=None, adjustment: float=None, adjustment_2: float=None, adjustment_3: float=None, adjustment_4: float=None, adjustment_5: float=None, adjustment_6: float=None, adjustment_7: float=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Create a new layer filled with a weave effect to be used as an
        overlay or bump map.
        
        Image types: RGB* GRAY*
        Menu label: _Weave...
        Menu path: <Image>/Filters/Artistic
        
        Parameters:
        
        * otherImage - Image to Weave.
        
        * drawable - Drawable to Weave.
        
        * adjustment (default: 30.0) - Ribbon width.
        
        * adjustment_2 (default: 10.0) - Ribbon spacing.
        
        * adjustment_3 (default: 75.0) - Shadow darkness.
        
        * adjustment_4 (default: 75.0) - Shadow depth.
        
        * adjustment_5 (default: 200.0) - Thread length.
        
        * adjustment_6 (default: 50.0) - Thread density.
        
        * adjustment_7 (default: 100.0) - Thread intensity.
        """
        pass

    def script_fu_xach_effect(self, otherImage: Gimp.Image=None, drawable: Gimp.Drawable=None, adjustment: int=None, adjustment_2: int=None, color: Gimp.RGB=None, adjustment_3: int=None, color_2: Gimp.RGB=None, adjustment_4: int=None, adjustment_5: int=None, adjustment_6: int=None, adjustment_7: int=None, toggle: bool=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE):
        """Add a subtle translucent 3D effect to the selected region (or alpha).
        
        Image types: RGB* GRAY*
        Menu label: _Xach-Effect...
        Menu path: <Image>/Filters/Light and Shadow/[Shadow]
        
        Parameters:
        
        * otherImage - Image.
        
        * drawable - Drawable.
        
        * adjustment (default: -1) - Highlight X offset.
        
        * adjustment_2 (default: -1) - Highlight Y offset.
        
        * color - Highlight color.
        
        * adjustment_3 (default: 66) - Highlight opacity.
        
        * color_2 - Drop shadow color.
        
        * adjustment_4 (default: 100) - Drop shadow opacity.
        
        * adjustment_5 (default: 12) - Drop shadow blur radius.
        
        * adjustment_6 (default: 5) - Drop shadow X offset.
        
        * adjustment_7 (default: 5) - Drop shadow Y offset.
        
        * toggle (default: True) - Keep selection.
        """
        pass

    def twain_acquire(self, image: Gimp.Image=None, num_drawables: int=None, drawables: Gimp.ObjectArray=None, run_mode: Gimp.RunMode=Gimp.RunMode.NONINTERACTIVE) -> Tuple[int, Gimp.ObjectArray]:
        """Capture an image from a TWAIN datasource.
        
        Image types: *
        Menu label: _Scanner/Camera...
        Menu path: <Image>/File/Create
        
        This plug-in will capture an image from a TWAIN datasource.
        
        Parameters:
        
        * image - The input image.
        
        * num_drawables (default: 1) - Number of input drawables.
        
        * drawables - The input drawables.
        
        Returns:
        
        * image_count (default: 0) - Number of acquired images.
        
        * images - Array of acquired images.
        """
        pass

class PyPDBProcedure:

    def __init__(self, pdb_wrapper, proc_name):
        pass

    @property
    def name(self):
        pass

    @property
    def proc(self):
        pass

    @property
    def has_run_mode(self):
        pass

    def __call__(self, *args, run_mode=Gimp.RunMode.NONINTERACTIVE, **kwargs):
        pass

    def _get_has_run_mode(self):
        pass

    def _create_config(self, run_mode, *proc_args, **proc_kwargs):
        pass

class PDBProcedureError(Exception):

    def __init__(self, message, status):
        pass

    def __str__(self):
        pass
pdb = _PyPDB()