"""Module for library managers factory, use it as entry-point to library managers."""

from mc_plugin_helper.config import Library
from mc_plugin_helper.library_manager.spigot import SpigotLibraryManager


class LibraryManagerFactory:
    """Fabric for Library Managers."""

    @staticmethod
    def create_library_manager(library: Library) -> SpigotLibraryManager:
        """Create object with library manager.

        Args:
            library: Protocol for which create file manager.

        Raises:
            TypeError: Wrong protocol provided.

        Returns:
            Object of file manager.
        """
        if library == Library.SPIGOT:
            return SpigotLibraryManager()
        else:
            # because there are another libraries, planning do it in future
            raise TypeError("Got wrong library")
